import cv2
import matplotlib.pyplot as plt

def apply_gaussian_blur(image_path, ksize):
    image = cv2.imread(image_path)
    blurred = cv2.GaussianBlur(image, (ksize, ksize), 0)
    return blurred

image_path = 'path_to_your_image.jpg'
ksize = 15  # Kernel size (must be odd)

blurred_image = apply_gaussian_blur(image_path, ksize)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Gaussian Blurred Image')
plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
plt.show()
