import cv2
import matplotlib.pyplot as plt

def flip_image(image_path, flip_code):
    image = cv2.imread(image_path)
    flipped = cv2.flip(image, flip_code)
    return flipped

image_path = 'path_to_your_image.jpg'
flip_code = 1  # 0: vertical, 1: horizontal, -1: both

flipped_image = flip_image(image_path, flip_code)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Flipped Image')
plt.imshow(cv2.cvtColor(flipped_image, cv2.COLOR_BGR2RGB))
plt.show()
