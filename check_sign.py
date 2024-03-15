from tensorflow.keras.preprocessing.image import load_img, img_to_array
from skimage.metrics import structural_similarity
import matplotlib.pyplot as plt
import numpy as np


def ssim(A, B):
    return structural_similarity(A, B, data_range=A.max() - A.min())

def check_sign(db_sign_path, cheque_sign_path):
    
    mode = "rgb"
    db_sign = load_img(db_sign_path,color_mode=mode, target_size=(150,150))
    cheque_sign = load_img(cheque_sign_path,color_mode=mode, target_size=(150,150))

    A_array = img_to_array(db_sign)
    B_array = img_to_array(cheque_sign)

    ssimValue = ssim(A_array.flatten(),B_array.flatten())

    print(ssimValue)

