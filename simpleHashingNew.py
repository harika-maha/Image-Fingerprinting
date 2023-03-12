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
print(len(files_list))

duplicates = []
hash_keys = dict()
path = "/Users/sridhararunachalam/Desktop/MiniProject/static/"
for index, filename in  enumerate(os.listdir('./static')):  #listdir('.') = current directory
    # print(filename)
    # if os.path.isfile(filename):
    #     print(filename)
    with open(path+filename, 'rb') as f:
        filehash = hashlib.md5(f.read()).hexdigest()
    if filehash not in hash_keys: 
        hash_keys[filehash] = index
    else:
        duplicates.append((index,hash_keys[filehash]))

print(duplicates)
print(files_list)
# a = plt.imread(path+"autumn-copy.jpg")
# print(a.shape)
# plt.imshow(a)
# plt.show()
for file_indexes in duplicates[:30]:
    try:
        print(files_list[file_indexes[1]])
        a = plt.imread(path+files_list[file_indexes[1]])
        plt.imshow(a)
        b = plt.imread(path+files_list[file_indexes[0]])
        plt.subplot(121)
        plt.imshow(a)
        plt.title(file_indexes[1]), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(b)
        plt.title(str(file_indexes[0]) + ' duplicate'), plt.xticks([]), plt.yticks([])
        plt.show()
    
    except OSError as e:
        continue
