import hashlib
import scipy 
import matplotlib.pyplot as plt
import time
import numpy as np
from PIL import Image
import os
import imagehash

imgs = "./static"
files_list = os.listdir(imgs)
# print(len(files_list))

def is_jpg(file_path):
    try:
        im = Image.open(file_path)
        return im.format == "JPEG"
    except IOError:
        return False

path = "/Users/sridhararunachalam/Desktop/MiniProject/static/"

def dHashing(file):
    original = imagehash.dhash(Image.open(path+file))
    duplicates = []
    hash_keys = dict()
    for index, filename in enumerate(os.listdir('./static')):  #listdir('.') = current directory
    # print(filename)
    # if os.path.isfile(filename):
    #     print(filename)
    # with open(path+filename, 'rb') as f:
        if is_jpg(path+filename):
            filehash = imagehash.dhash(Image.open(path+filename))
        # print(filehash)
        if filehash not in hash_keys: 
            hash_keys[filehash] = index
        else:
            duplicates.append((index,hash_keys[filehash]))

# print(hash_keys)


# for i in range(len(files_list)):
    hash_value = []
    for key, value in hash_keys.items():
    # print(key, value)
        hash_value.append(key)

    n = len(hash_keys)
    # print(n)
    diff_list = []
    for i in range(n):
        img = i
        diff = original - hash_value[i]
        if(diff < 10):
            diff_list.append(hash_keys.get(hash_value[img]))
    print(diff_list)
    return(diff_list)
  
    # print(str(hash_value[0]))
    # img1 = i
    # for j in range(i+1, n):
    #     img2 = j
    #     diff = hash_value[i] - hash_value[j]
    #     idx1=0
    #     idx2=0
    #         if(diff < 10):
    #         # print(diff)
    #         # print("Image1:", img1, "Image2:", img2)
    #             idx1, idx2 = hash_keys.get(hash_value[img1]), hash_keys.get(hash_value[img2])
    #             diff_list.append( [idx1,idx2])
    #     # diff_list += (hash_value[i] - hash_value[j])
    # print(diff_list)



# print(hash_keys.get(hash_value[4]), hash_keys.get(hash_value[9]))

# a = plt.imread(path+files_list[5])
# plt.imshow(a)

# b = plt.imread(path+files_list[11])
# plt.imshow(b)

# print(hash_value[7], hash_value[9])

# plt.subplot(121)
# plt.imshow(a)
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(b)
# plt.xticks([]), plt.yticks([])
# plt.show()

# print(diff_list)

# print(duplicates)
# print(files_list)
# # a = plt.imread(path+"autumn-copy.jpg")
# # print(a.shape)
# # plt.imshow(a)
# # plt.show()
# for file_indexes in duplicates[:30]:
#     try:
#         print(files_list[file_indexes[1]])
#         a = plt.imread(path+files_list[file_indexes[1]])
#         plt.imshow(a)
#         b = plt.imread(path+files_list[file_indexes[0]])
#         plt.subplot(121)
#         plt.imshow(a)
#         plt.title(file_indexes[1]), plt.xticks([]), plt.yticks([])
#         plt.subplot(122),plt.imshow(b)
#         plt.title(str(file_indexes[0]) + ' duplicate'), plt.xticks([]), plt.yticks([])
#         plt.show()
    
#     except OSError as e:
#         continue
