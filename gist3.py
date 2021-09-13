import numpy as np
import matplotlib.pyplot as plt
import cv2

# считать изображение
im = cv2.imread('images\hydrangeas_01.jpg')
brighter = int(input('Введите константу для увеличения яркости: '))

i = 0
# добавление яркости
def get_brighter(z):
    global brighter, i
    if 0 > z + brighter:
        i += 1
        return 0
    if z + brighter > 255:
        i += 1
        return 255
    return z + brighter

im = np.uint8([[[get_brighter(z) for z in y] for y in x] for x in im])
print(f'Не удалось добавить(уменьшить) яркость {i} раз!')

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