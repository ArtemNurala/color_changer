import numpy as np
import matplotlib.pyplot as plt
import cv2

# считать изображение
im = cv2.imread('images\hydrangeas_01.jpg')
# считать яркость точки из RGB каналов и сжать в одноразмерный массив
vals = np.apply_along_axis((lambda a: 0.299*a[0] + 0.5876*a[1] + 0.114*a[2]), 2, im).flatten()
contraster = float(input('Введите константу для увеличения контрастности: '))

i, j = 0, 0
# добавление контрастности
def get_contraster(z):
    global contraster, i, j
    j += 1
    k = (int)(j / 3)
    new_value = contraster * (z - vals[k - 1]) + vals[k - 1]
    if new_value < 0:
        i += 1
        return 0
    if new_value > 255:
        i += 1
        return 255
    return new_value

im = np.uint8([[[get_contraster(z) for z in y] for y in x] for x in im])
vals = np.apply_along_axis((lambda a: 0.299*a[0] + 0.5876*a[1] + 0.114*a[2]), 2, im).flatten()
print(f'Не удалось добавить(уменьшить) контрастность {i} раз!')

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