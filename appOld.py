from flask import Flask, request, jsonify
import cv2
import numpy as np
import os

app = Flask(__name__)
image_dir = '/Users/sridhararunachalam/Desktop/MiniProject/test_images'

def dhash(image, hash_size=8):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize image to hash_size x hash_size
    resized = cv2.resize(gray, (hash_size + 1, hash_size))

    # Compute difference between adjacent pixels in each row
    diff = resized[:, 1:] > resized[:, :-1]

    # Convert difference matrix to binary hash code
    return np.packbits(diff.flatten())

def get_image_path(id):
    # Construct path to image file using the image ID
    return os.path.join(image_dir, f'{id}.jpg')

def find_similar_images(hash_code):
    # Iterate over all image files in the image directory
    similar_images = []
    for filename in os.listdir(image_dir):
        if not filename.endswith('.jpg'):
            continue

        # Load the image and compute its hash code
        image = cv2.imread(os.path.join(image_dir, filename))
        image_hash = dhash(image)

        # Compare hash codes and add to similar_images list if similar
        if np.count_nonzero(hash_code != image_hash) < 5:
            id = os.path.splitext(filename)[0]
            similar_images.append({
                'id': id,
                'path': get_image_path(id),
                'dhash': list(np.unpackbits(bytearray(image_hash)))
            })

    return similar_images

@app.route('/', methods=['GET', 'POST'])
def handle_image_upload():
    # Get the uploaded image file and save it to a temporary location
    file = request.files['file']
    file.save('temp_image.jpg')

    # Load the image and generate a hash code
    image = cv2.imread('temp_image.jpg')
    hash_code = dhash(image)

    # Find similar images and return them as a JSON response
    similar_images = find_similar_images(hash_code)
    return jsonify(similar_images)

if __name__ == '__main__':
    app.run(debug=True)