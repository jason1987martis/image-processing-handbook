import cv2
import matplotlib.pyplot as plt

def resize_image(image_path, width, height):
    image = cv2.imread(image_path)
    resized = cv2.resize(image, (width, height))
    return resized

image_path = 'path_to_your_image.jpg'
width, height = 300, 300  # Desired width and height

resized_image = resize_image(image_path, width, height)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Resized Image')
plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
plt.show()
