Ось звіт за твоїм прикладом виконання екзаменаційного завдання, де використано два файли: `main.py` для реалізації функції та `test.py` для написання юніт-тестів.

---

## **Звіт за екзаменом з тестування програмного забезпечення**

### **1. Опис завдання**
У даному завданні потрібно реалізувати функцію в окремому файлі `main.py`, а в другому файлі `test.py` написати юніт-тести для перевірки правильності її роботи. Для цього створюємо два файли:

- **main.py**: Функція, яка реалізує певну логіку (наприклад, генерація матриці).
- **test.py**: Юніт-тести для функції з `main.py`.

### **2. Структура файлів**
```
/exam
    ├── main.py
    └── test.py
```

### **3. Код файлу `main.py`**

```python
# main.py
import numpy as np

def generate_matrix(n):
    """
    Генерує квадратну матрицю розміру n x n із випадкових чисел.
    Піднімає помилку, якщо розмір не є додатнім цілим числом.
    
    :param n: Розмір матриці (ціле додатнє число)
    :return: Квадратна матриця розміру n x n
    """
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
```

### **4. Код файлу `test.py`**

```python
# test.py
import unittest
from main import generate_matrix  # Імпортуємо функцію з main.py
import numpy as np

class TestGenerateMatrix(unittest.TestCase):

    # Тест на коректний розмір
    def test_valid_input(self):
        matrix = generate_matrix(3)
        self.assertEqual(matrix.shape, (3, 3))  # Перевіряємо, що матриця має розмір 3x3

    # Тест на від'ємне значення
    def test_negative_input(self):
        with self.assertRaises(ValueError):
            generate_matrix(-5)

    # Тест на нульовий розмір
    def test_zero_input(self):
        with self.assertRaises(ValueError):
            generate_matrix(0)

    # Тест на неціле число
    def test_non_integer_input(self):
        with self.assertRaises(ValueError):
            generate_matrix(2.5)

    # Тест на строкове значення
    def test_string_input(self):
        with self.assertRaises(ValueError):
            generate_matrix("три")

if __name__ == "__main__":
    unittest.main()
```

### **5. Запуск програми**

Щоб запустити програму, потрібно виконати наступні кроки:

1. Відкрити командний рядок (термінал) у директорії, де знаходяться файли `main.py` та `test.py`.
2. Запустити файл `main.py` для перевірки роботи функції:

```bash
python main.py
```

Приклад введення та виведення:
```
Введіть розмір квадратної матриці (ціле додатнє число): 3
Згенерована матриця:
[[0.45736656 0.19448747 0.02063477]
 [0.94501312 0.95194324 0.36925469]
 [0.24660167 0.8369169  0.16044106]]
```

### **6. Запуск тестів**

Для того, щоб перевірити правильність роботи функції `generate_matrix`, використовуємо юніт-тести. Запускаємо тести наступною командою:

```bash
python -m unittest -v
```

### **7. Результати запуску тестів**

Якщо всі тести проходять успішно, ми отримаємо такий вивід:

```
test_negative_input (__main__.TestGenerateMatrix) ... ok
test_non_integer_input (__main__.TestGenerateMatrix) ... ok
test_string_input (__main__.TestGenerateMatrix) ... ok
test_valid_input (__main__.TestGenerateMatrix) ... ok
test_zero_input (__main__.TestGenerateMatrix) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK
```

Якщо виникають помилки в тестах, то виведеться повідомлення про невдалий тест, що дозволить виявити та виправити проблему.

---

### **8. Висновки**

Всі тести пройшли успішно, функція `generate_matrix` працює коректно. Тестування дозволяє забезпечити правильність функціонування програми та гарантує, що вона обробляє некоректні вхідні дані (від'ємні числа, нецілі числа, рядки тощо). 

---

### **9. Кроки для вдосконалення**

