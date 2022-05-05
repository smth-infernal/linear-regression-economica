import numpy as np
import matplotlib.pyplot as plt
import data

# импортируем значения из файла
x = data.array_x
y = data.array_y


# Находим коэффициенты для вычисления регрессии
def estimate_coefficients(x, y):
    n = np.size(x)

    b_0 = ((np.sum(y)*np.sum(x*x)) - (np.sum(x)*np.sum(x*y))) / (n*np.sum(x*x) - (np.sum(x)**2))
    b_1 = ((n*np.sum(x*y)) - (np.sum(x)*np.sum(y))) / (n*np.sum(x*x) - (np.sum(x)**2))

    return(b_0, b_1)


# Функция для построения графика
def plot_regression_line(x, y, b):
    plt.scatter(x, y, color="m", marker="o")

# Поиск значения, на которое должен быть смещен график регрессии, а так же прогноз стоимости доллара 1.12
    y_pred = b[0] + b[1]*x
    y_pred_1 = b[0] + b[1]*31

    plt.plot(x, y_pred, color="g")

    plt.xlabel('Дни')
    plt.ylabel('Стоимость доллара')

    plt.show()
    print('Стоимость доллара 01.12: ', y_pred_1)


def main():
    b = estimate_coefficients(x, y)
    plot_regression_line(x, y, b)


if __name__ == "__main__":
    main()
