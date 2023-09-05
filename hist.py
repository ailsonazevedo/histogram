import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

from utils import generate_histogram_img


# img = cv.imread("beijaflor.jpg")

# img_parque = cv.imread("parque.jpg")

# img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# img_gray = convert_to_gray(img_parque)

# img_gray = cv.resize(img_gray, (500, 350))
# # plt.imshow(img)
# # cv.imshow("Imagem", img)
# cv.imshow("Parque em preto e branco", img_gray)
# cv.imshow("Parque Colorido", img_parque)
# # plt.show()


# # histograma RGB
# plt.hist(img_parque.ravel(),256,[0,256]) 


# plt.show()
# cv.waitKey(0)

url = "img/parque.jpg"
generate_histogram_img(url, "Parque")