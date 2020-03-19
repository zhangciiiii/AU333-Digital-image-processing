import math
import cv2
import numpy as np
import os
def gausskernel(size, sigma=1.0):
    mid = int(size/2)
    gausskernel=np.zeros((size,size),np.float32)
    for i in range (size):
        for j in range (size):
            norm=math.pow(i-mid,2)+math.pow(j-mid,2)
            gausskernel[i,j]=math.exp(-norm/(2*math.pow(sigma,2)))   
    summay=np.sum(gausskernel)   
    kernel=gausskernel/summay  
    return kernel

def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
    return cv_img


'''
for size in [3,5,7,9,11,17]:
    print(gausskernel(size))
'''
kernerl_size = [3,5,7,9,11,17]
load_path = "GrayImages/GaussScale"
save_path = "Result/GaussScale"


imgs_list = os.listdir(load_path)
print(imgs_list)
for img_name in imgs_list: # filter for each picture
    print(img_name)
    img = cv_imread(load_path + "/" + img_name)
    cv2.imshow('pirate',img)
    for size in kernerl_size:           
        img = cv2.GaussianBlur(img,(size,size),0)
        cv2.imwrite(save_path + "/" + str(size)+"_" + img_name , img)


    
