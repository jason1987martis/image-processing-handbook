import cv2
import matplotlib.pyplot as plt

def crop_image(image_path, start_x, start_y, width, height):
    image = cv2.imread(image_path)
    cropped = image[start_y:start_y + height, start_x:start_x + width]
    return cropped

image_path = 'path_to_your_image.jpg'
start_x, start_y = 50, 50  # Starting point
width, height = 200, 200   # Width and height of the cropped area

cropped_image = crop_image(image_path, start_x, start_y, width, height)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Cropped Image')
plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
plt.show()
