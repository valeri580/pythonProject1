import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.hist(data, bins=30, edgecolor='black', alpha=0.7)
plt.title('Гистограмма нормально распределённых случайных данных')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(True)
plt.show()