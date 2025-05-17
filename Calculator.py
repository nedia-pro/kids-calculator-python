import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import pygame

# تهيئة الصوت
pygame.mixer.init()

# الرسائل التشجيعية
messages = ["Great job!", "Awesome!", "You rock!", "Keep going!", "Well done!"]

# تشغيل الصوت
def play_sound():
    try:
        pygame.mixer.music.load("cheer.wav")
        pygame.mixer.music.play()
    except:
        print("Sound file not found or error playing it.")

# تنفيذ العملية الحسابية
def calculate(operator):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2

        result_label.config(text=f"Result: {result:.2f}")
        feedback_label.config(text=random.choice(messages))
        show_star()
        play_sound()

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# عرض صورة النجمة
def show_star():
    star_label.config(image=star_img)
    star_label.image = star_img

# واجهة المستخدم
window = tk.Tk()
window.title("Fun Kids Calculator")
window.geometry("450x400")
window.configure(bg='#FFF8DC')

# صورة نجمة
star_img = ImageTk.PhotoImage(Image.open("star.png").resize((60, 60)))
star_label = tk.Label(window, bg='#FFF8DC')
star_label.pack(pady=10)

title = tk.Label(window, text="🌟 Fun Calculator 🌟", font=("Arial", 22, "bold"), bg='#FFF8DC', fg="#FF6F61")
title.pack(pady=5)

entry1 = tk.Entry(window, font=("Arial", 16), width=10, justify='center')
entry1.pack(pady=5)

entry2 = tk.Entry(window, font=("Arial", 16), width=10, justify='center')
entry2.pack(pady=5)

button_frame = tk.Frame(window, bg='#FFF8DC')
button_frame.pack(pady=10)

for symbol in ['+', '-', '*', '/']:
    tk.Button(button_frame, text=symbol, font=("Arial", 16), width=5, bg='#AEDFF7',
              command=lambda s=symbol: calculate(s)).pack(side='left', padx=5)

result_label = tk.Label(window, text="Result: ", font=("Arial", 18), bg='#FFF8DC', fg='#333')
result_label.pack(pady=10)

feedback_label = tk.Label(window, text="", font=("Arial", 16, "italic"), fg='green', bg='#FFF8DC')
feedback_label.pack()

window.mainloop()
