import numpy as np
import matplotlib.pyplot as plt
import cv2

# считать изображение
im = cv2.imread('images\hydrangeas_01.jpg')
# считать яркость точки из RGB каналов и сжать в одноразмерный массив
vals = np.apply_along_axis((lambda a: 0.299*a[0] + 0.5876*a[1] + 0.114*a[2]), 2, im).flatten()

# получение оттенков серого
i = 0
def get_gray():
    global i
    i += 1
    return vals[i - 1]
im = np.uint8([[[get_gray()] * 3 for y in x] for x in im])

vals = np.apply_along_axis((lambda a: 0.299*a[0] + 0.5876*a[1] + 0.114*a[2]), 2, im).flatten()
counts, bars = np.histogram(vals, range(257))
# отрисовать гистограмму на промежутке от 0 до 255
plt.bar(bars[:-1] - 0.5, counts, width=1)
plt.xlim([-0.5, 255.5])
plt.xlabel('Яркость точки')
plt.ylabel('Количество повторений')
plt.show()

cv2.imshow('image', im)
cv2.waitKey()
cv2.destroyAllWindows()