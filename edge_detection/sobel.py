import cv2
import matplotlib.pyplot as plt

def sobel_edge_detection(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    sobel = cv2.magnitude(sobelx, sobely)
    return sobel

image_path = 'path_to_your_image.jpg'

sobel_edges = sobel_edge_detection(image_path)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.imread(image_path, cv2.IMREAD_GRAYSCALE), cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Sobel Edge Detection')
plt.imshow(sobel_edges, cmap='gray')
plt.show()
