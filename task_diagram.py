import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_points = 100
x = np.random.rand(num_points)
y = np.random.rand(num_points)

# Построение диаграммы рассеяния
plt.scatter(x, y, color='blue', alpha=0.7)
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()