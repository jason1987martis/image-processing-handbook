import cv2
import numpy as np
import matplotlib.pyplot as plt

def adjust_brightness(image_path, beta):
    image = cv2.imread(image_path)
    adjusted = cv2.convertScaleAbs(image, alpha=1, beta=beta)
    return adjusted

image_path = 'path_to_your_image.jpg'
beta = 50  # Brightness control (0-100)

adjusted_image = adjust_brightness(image_path, beta)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Brightness Adjusted Image')
plt.imshow(cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2RGB))
plt.show()
