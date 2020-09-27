import cv2
import numpy as np
import matplotlib.pyplot as plt

# import image
image = cv2.imread('DSC00134.JPG',0)
print(image.shape)
image = cv2.resize(image,(600,400))
# cv2.imshow('image',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.show()