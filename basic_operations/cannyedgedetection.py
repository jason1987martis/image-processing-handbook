import cv2
import matplotlib.pyplot as plt

def canny_edge_detection(image_path, threshold1, threshold2):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(image, threshold1, threshold2)
    return edges

image_path = 'path_to_your_image.jpg'
threshold1 = 100
threshold2 = 200

edges = canny_edge_detection(image_path, threshold1, threshold2)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.imread(image_path, cv2.IMREAD_GRAYSCALE), cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Canny Edge Detection')
plt.imshow(edges, cmap='gray')
plt.show()
