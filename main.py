import cv2
import numpy as np

# Загрузка изображения
image = cv2.imread("1.jpg")

# Изменение размера изображения для уменьшения времени обработки
image = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)

# Обнаружение лиц
faces = cv2.face.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 255), 2)
    roi_gray = image[y:y + h, x:x + w]
    roi_color = image[y:y + h, x:x + w]

# Отображение результата
cv2.imshow("1.jpg", image)
cv2.waitKey(0)
