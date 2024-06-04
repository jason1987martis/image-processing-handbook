import cv2
import matplotlib.pyplot as plt

def rotate_image(image_path, angle):
    image = cv2.imread(image_path)
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center,angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

image_path = 'path_to_your_image.jpg'
angle = 45  # Angle in degrees

rotated_image = rotate_image(image_path, angle)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Rotated Image')
plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
plt.show()
