import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_dilation(image_path, kernel_size):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    dilated = cv2.dilate(image, kernel, iterations=1)
    return dilated

image_path = 'path_to_your_image.jpg'
kernel_size = 5

dilated_image = apply_dilation(image_path, kernel_size)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.imread(image_path, cv2.IMREAD_GRAYSCALE), cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Dilated Image')
plt.imshow(dilated_image, cmap='gray')
plt.show()
