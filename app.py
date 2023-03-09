# Import dependencies
from PIL import Image
import imagehash
import os
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, url_for

# similar = []
# hash_keys = dict()
# for index, filename in  enumerate(os.listdir('./test_images')):  #listdir('.') = current directory
#     # if os.path.isfile(filename):

#     HDBatmanHash = imagehash.phash(Image.open('/Users/sridhararunachalam/Desktop/MiniProject/test_images/'+filename))
#     # print(HDBatmanHash)
#     if (HDBatmanHash not in hash_keys):
#         hash_keys[HDBatmanHash] = index
#         for key, value in hash_keys.items():
#             # print(key)
#             if((key - HDBatmanHash<20) and (key - HDBatmanHash)!=0):
#                 similar.append([value, hash_keys[HDBatmanHash]])

# # print(similar)

# files_list = os.listdir('./test_images')
# for file_indexes in similar:
#     # print(file_indexes)
# #     # try:
#     print(files_list[file_indexes[0]])
#     print(files_list[file_indexes[1]])
#     a = plt.imread(str(files_list[file_indexes[0]]))
    # b = plt.imread(files_list[file_indexes[1]])        
    # plt.subplot(121),plt.imshow(a)
    # plt.title(file_indexes[1]), plt.xticks([]), plt.yticks([])
    # plt.subplot(122),plt.imshow(b)
    # plt.title(str(file_indexes[0]) + ' duplicate'), plt.xticks([]), plt.yticks([])
    # plt.show()
    
    # except OSError as e:
    #     continue

# for i in similar:
#     a = plt.imread(i[0])
#     b = plt.imread(i[1])
#     plt.subplot(121),plt.imshow(files_list(a)
#     plt.title(), plt.xticks([]), plt.yticks([])
#     plt.subplot(122),plt.imshow(files_list(b)
#     plt.title(str(file_indexes[0]) + ' duplicate'), plt.xticks([]), plt.yticks([])
#     plt.show()

# print(hash_keys)

app = Flask(__name__)
 
 
@app.route("/")
def index():
    return render_template("index.html")
 

@app.route('/form', methods=["GET","POST"])
def redirect():
    return render_template("redirect.html")

def dPhashing():
# Create the Hash Object of the first image
    HDBatmanPHash = imagehash.phash(Image.open('/Users/sridhararunachalam/Desktop/MiniProject/test_images/img1.jpg'))
    print('Batman HD Picture: ' + str(HDBatmanPHash))

    HDBatmanDHash = imagehash.dhash(Image.open('/Users/sridhararunachalam/Desktop/MiniProject/test_images/img1.jpg'))
    print('D-Hash: '+ str(HDBatmanDHash))

# Create the Hash Object of the second image
    SDBatmanPHash = imagehash.phash(Image.open('/Users/sridhararunachalam/Desktop/MiniProject/test_images/bluejacket.jpg'))
    print('Batman HD Picture: ' + str(SDBatmanPHash))

    SDBatmanDHash = imagehash.dhash(Image.open('/Users/sridhararunachalam/Desktop/MiniProject/test_images/bluejacket.jpg'))
    print('D-Hash: '+ str(SDBatmanDHash))


    print(HDBatmanPHash - SDBatmanPHash)
    print(HDBatmanDHash - SDBatmanDHash)
# Compare hashes to determine whether the pictures are the same or not
    if(HDBatmanPHash == SDBatmanPHash):
        print("The pictures are perceptually the same !")
    elif(HDBatmanPHash - SDBatmanPHash<20):
        print("The pictures are kinda similar :)" + str(HDBatmanPHash-SDBatmanPHash))
    else:
        print("The pictures are different, distance: " + str(HDBatmanPHash - SDBatmanPHash))

if __name__ == "__main__":
    app.run()