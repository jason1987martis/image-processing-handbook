import cv2
import matplotlib.pyplot as plt

def invert_image(image_path):
    image = cv2.imread(image_path)
    inverted = cv2.bitwise_not(image)
    return inverted

image_path = 'path_to_your_image.jpg'

inverted_image = invert_image(image_path)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Inverted Image')
plt.imshow(cv2.cvtColor(inverted_image, cv2.COLOR_BGR2RGB))
plt.show()
