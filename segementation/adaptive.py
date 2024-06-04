import cv2
import matplotlib.pyplot as plt

def adaptive_thresholding(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    adaptive_mean = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    adaptive_gaussian = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return adaptive_mean, adaptive_gaussian

image_path = 'path_to_your_image.jpg'

adaptive_mean, adaptive_gaussian = adaptive_thresholding(image_path)

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(cv2.imread(image_path, cv2.IMREAD_GRAYSCALE), cmap='gray')

plt.subplot(1, 3, 2)
plt.title('Adaptive Mean Thresholding')
plt.imshow(adaptive_mean, cmap='gray')

plt.subplot(1, 3, 3)
plt.title('Adaptive Gaussian Thresholding')
plt.imshow(adaptive_gaussian, cmap='gray')
plt.show()
