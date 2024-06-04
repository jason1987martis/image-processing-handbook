import cv2
import matplotlib.pyplot as plt

def histogram_equalization(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    equalized = cv2.equalizeHist(image)
    return equalized

image_path = 'path_to_your_image.jpg'

equalized_image = histogram_equalization(image_path)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.imread(image_path, cv2.IMREAD_GRAYSCALE), cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Histogram Equalized Image')
plt.imshow(equalized_image, cmap='gray')
plt.show()
