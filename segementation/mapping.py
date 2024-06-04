import cv2
import matplotlib.pyplot as plt

def apply_colormap(image_path, colormap):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    colored_image = cv2.applyColorMap(image, colormap)
    return colored_image

image_path = 'path_to_your_image.jpg'
colormap = cv2.COLORMAP_JET  # Choose from different colormaps like COLORMAP_JET, COLORMAP_HOT, etc.

colored_image = apply_colormap(image_path, colormap)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Grayscale Image')
plt.imshow(cv2.imread(image_path, cv2.IMREAD_GRAYSCALE), cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Colored Image')
plt.imshow(cv2.cvtColor(colored_image, cv2.COLOR_BGR2RGB))
plt.show()
