import cv2
import numpy as np

def COCOdata(img_dir):
    image = cv2.imread(img_dir)
    image = image.astype(np.float32)
    resized_img = image/255.0
    return resized_img