# main.py
import numpy as np

def generate_matrix(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Розмір матриці повинен бути цілим додатнім числом.")
    matrix = np.random.rand(n, n)
    return matrix

if __name__ == "__main__":
    try:
        user_input = input("Введіть розмір квадратної матриці (ціле додатнє число): ")
        n = int(user_input)
        result = generate_matrix(n)
        print("Згенерована матриця:")
        print(result)
    except ValueError as e:
        print(f"Помилка: {e}")
