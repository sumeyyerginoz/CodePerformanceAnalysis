import cv2
import time 

start=time.time()

camera = cv2.VideoCapture(0)

red,frame = camera.read()

cv2.flip(frame,1)

camera.release()

cv2.destroyAllWindows()
fınısh=time.time()

print(fınısh-start)


