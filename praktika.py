import re
import tkinter as tk
from tkinter import messagebox


# Функция проверки пароля
def check_password_strength():
    password = password_entry.get()
    score = 0

    # Критерии надёжности пароля
    criteria = {
        "Длина не менее 8 символов": len(password) >= 8,
        "Наличие хотя бы одной цифры": bool(re.search(r'\d', password)),
        "Наличие хотя бы одной строчной буквы": bool(re.search(r'[a-z]', password)),
        "Наличие хотя бы одной заглавной буквы": bool(re.search(r'[A-Z]', password)),
        "Наличие хотя бы одного специального символа": bool(re.search(r'[!@#$%^&*(),.?\":{}|<>]', password))
    }

    # Проверяем каждый критерий и подсчитываем баллы
    result_text = "Результаты проверки:\n"
    for criterion, passed in criteria.items():
        if passed:
            result_text += f"✔ {criterion}\n"
            score += 1
        else:
            result_text += f"✘ {criterion}\n"

    # Оценка на основе баллов
    if score == 5:
        strength = "Очень надёжный"
        color = "green"
    elif score >= 3:
        strength = "Надёжный"
        color = "orange"
    elif score >= 1:
        strength = "Средней надёжности"
        color = "brown"
    else:
        strength = "Ненадёжный"
        color = "red"

    result_text += f"\nОценка надёжности пароля: {strength}"
    result_label.config(text=result_text, fg=color)


# Функция для переключения видимости пароля
def toggle_password_visibility():
    if password_entry.cget('show') == "*":
        password_entry.config(show="")
        toggle_button.config(text="Скрыть пароль")
    else:
        password_entry.config(show="*")
        toggle_button.config(text="Показать пароль")


# Настройка окна приложения
root = tk.Tk()
root.title("Проверка надёжности пароля")
root.geometry("400x400")
root.config(bg="white")

# Метка и поле для ввода пароля
password_label = tk.Label(root, text="Введите пароль:", font=("Arial", 12), bg="white")
password_label.pack(pady=(20, 5))

password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=30)
password_entry.pack(pady=5)

# Кнопка для переключения видимости пароля
toggle_button = tk.Button(root, text="Показать пароль", font=("Arial", 10), command=toggle_password_visibility,
                          bg="#2196F3", fg="white")
toggle_button.pack(pady=5)

# Кнопка для проверки пароля
check_button = tk.Button(root, text="Проверить", font=("Arial", 12), command=check_password_strength, bg="#4CAF50",
                         fg="white")
check_button.pack(pady=20)

# Метка для отображения результата
result_label = tk.Label(root, text="", font=("Arial", 12), bg="white", justify="left")
result_label.pack(pady=10)

# Запуск главного цикла приложения
root.mainloop()