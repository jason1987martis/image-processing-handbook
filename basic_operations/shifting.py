import cv2
import numpy as np
import matplotlib.pyplot as plt

def translate_image(image_path, x, y):
    image = cv2.imread(image_path)
    (h, w) = image.shape[:2]
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (w, h))
    return shifted

image_path = 'path_to_your_image.jpg'
x, y = 50, 50  # Translation along x and y axis

shifted_image = translate_image(image_path, x, y)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Shifted Image')
plt.imshow(cv2.cvtColor(shifted_image, cv2.COLOR_BGR2RGB))
plt.show()
