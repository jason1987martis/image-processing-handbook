import cv2
import numpy as np
import matplotlib.pyplot as plt

def adjust_contrast(image_path, alpha):
    image = cv2.imread(image_path)
    adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=0)
    return adjusted

image_path = 'path_to_your_image.jpg'
alpha = 1.5  # Contrast control (1.0-3.0)

adjusted_image = adjust_contrast(image_path, alpha)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Contrast Adjusted Image')
plt.imshow(cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2RGB))
plt.show()
