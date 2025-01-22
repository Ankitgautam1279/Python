import cv2

src = cv2.imread('face.png', cv2.IMREAD_UNCHANGED)

new_width = int(src.shape[1] * 20/100)
new_height = int(src.shape[0] * 20/100)

output = cv2.resize(src,(new_width, new_height))

cv2.imwrite('newImage.jpeg', output)

