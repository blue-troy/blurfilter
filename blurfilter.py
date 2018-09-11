# -*-coding:utf-8-*-
import os
import shutil

import cv2


def get_blur_var(img_path):
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var()


def move_blur_img(img_path):
    if not img_path.startswith(blur_path):
        try:
            shutil.move(img_path, blur_path)
        except BaseException:
            print("文件移动异常\n", BaseException)


def handle_blur_dir(threshold):
    blur_path = DIR + "/blur" + str(threshold)
    if not os.path.exists(blur_path):
        os.mkdir(blur_path)
    return blur_path


def get_threshold():
    threshold_input = input("请输入模糊值, 或者一个图片路径作为模糊参照标准：")
    if os.path.exists(threshold_input):
        if is_image(threshold_input):
            return get_blur_var(threshold_input)
        else:
            print("图片地址错误")
    else:
        return int(threshold_input)


def is_image(img_path):
    return img_path.endswith(".jpg") or img_path.endswith(".png")


if __name__ == '__main__':

    DIR = input("请输入文件夹路径：")
    THRESHOLD = get_threshold()
    blur_path = handle_blur_dir(THRESHOLD)

    for (root, dirs, files) in os.walk(DIR):
        for file in files:
            img_path = os.path.join(root, file)
            if is_image(img_path):
                if get_blur_var(img_path) < THRESHOLD:
                    move_blur_img(img_path)
