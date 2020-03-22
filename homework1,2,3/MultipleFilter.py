import math
import cv2
import numpy as np
import os


def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
    return cv_img





kernerl_size = [3,5,7,11]
load_path = "GrayImages/NoiseImage"
save_path = "Result/NoiseImage"



imgs_list = os.listdir(load_path)

for img_name in imgs_list: # filter for each picture
    img = cv_imread(load_path + "/" + img_name)
    print(img_name)
    for size in kernerl_size:           
        
        # 均值滤波
        img_mean = cv2.blur(img, (size,size))
        cv2.imwrite(save_path + "/" + "Mean_" + str(size)+"_" + img_name , img_mean)

        # 高斯滤波
        img_Guassian = cv2.GaussianBlur(img,(size,size),5)
        cv2.imwrite(save_path + "/" + "Gausee_" + str(size)+"_" + img_name , img_Guassian)

        # 中值滤波
        img_median = cv2.medianBlur(img, size)
        cv2.imwrite(save_path + "/" + "Median_" + str(size)+"_" + img_name , img_median)

           
