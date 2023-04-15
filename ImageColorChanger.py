# %%
import cv2
import matplotlib.pyplot as plt
import PIL
import numpy as np
import os

# %%
base_dir = '/home/disha/abhi/IITH-Data-Science/Data_Science_Notes/Deep-Learning/CS5480_images/'
for dirs in os.listdir(base_dir):
    full_path = os.path.join(base_dir,dirs)
    p_img= PIL.Image.open(full_path)
    img = np.asarray(p_img)
    temp_img = img.copy() #np.ones_like(img,dtype=np.uint8)
    temp_img[:,:,0] = 223 #219 #230 # 181 #230
    temp_img[:,:,1] = 237 #233 #237 # 230 #237
    temp_img[:,:,2] = 246 #242 #253 # 245 #253
    added = cv2.addWeighted(img,0.5,temp_img,0.5,0)
    new_image = PIL.Image.fromarray(added)
    new_image.save(full_path)

# %%
base_dir = '/home/disha/abhi/IITH-Data-Science/Data_Science_Notes/Machine-Learning/CS5590_images/'
for dirs in os.listdir(base_dir):
    full_path = os.path.join(base_dir,dirs)
    p_img= PIL.Image.open(full_path)
    img = np.asarray(p_img)
    temp_img = img.copy() #np.ones_like(img,dtype=np.uint8)
    temp_img[:,:,0] = 223 #219 #230 # 181 #230
    temp_img[:,:,1] = 237 #233 #237 # 230 #237
    temp_img[:,:,2] = 246 #242 #253 # 245 #253
    added = cv2.addWeighted(img,0.5,temp_img,0.5,0)
    new_image = PIL.Image.fromarray(added)
    new_image.save(full_path)

# %%
base_dir = '/home/disha/abhi/IITH-Data-Science/Data_Science_Notes/Mathematics/CS6660_images/'
for dirs in os.listdir(base_dir):
    full_path = os.path.join(base_dir,dirs)
    p_img= PIL.Image.open(full_path)
    img = np.asarray(p_img)
    temp_img = img.copy() #np.ones_like(img,dtype=np.uint8)
    temp_img[:,:,0] = 223 #219 #230 # 181 #230
    temp_img[:,:,1] = 237 #233 #237 # 230 #237
    temp_img[:,:,2] = 246 #242 #253 # 245 #253
    added = cv2.addWeighted(img,0.5,temp_img,0.5,0)
    new_image = PIL.Image.fromarray(added)
    new_image.save(full_path)


