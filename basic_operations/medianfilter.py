import cv2
import matplotlib.pyplot as plt

def apply_median_filter(image_path, ksize):
    image = cv2.imread(image_path)
    filtered = cv2.medianBlur(image, ksize)
    return filtered

image_path = 'path_to_your_image.jpg'
ksize = 5  # Kernel size (must be odd)

filtered_image = apply_median_filter(image_path, ksize)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Median Filtered Image')
plt.imshow(cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB))
plt.show()
