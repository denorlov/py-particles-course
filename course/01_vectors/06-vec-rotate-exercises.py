# Реализуйте функцию, которая будет поворачивать вектор на N градусов.
# Проверьте, что ваш метод разворота вектора совпадает с реализацией Vector2.rotate()

import random

from pygame.math import Vector2

v1 = Vector2(0, 1).rotate(random.uniform(0, 360))
print(v1)