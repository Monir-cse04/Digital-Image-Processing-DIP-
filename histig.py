import numpy as np
import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("fruits.png")


# Show images
cv2.imshow("Original img", img)

# Histogram
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.hist(img.ravel(), bins=50)
plt.title("Original Histogram")

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
