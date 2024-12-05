import tkinter as tk
from tkinter import Canvas
import pygame
import keyboard
import time
import threading
import os
import sys

# إعداد مكتبة pygame للصوت
pygame.mixer.init()

# إنشاء نافذة Tkinter
root = tk.Tk()
root.title("برنامج التحدث بواجهة رسومية")
root.attributes('-fullscreen', True)  # جعل النافذة ملء الشاشة

# إعداد الواجهة الرسومية (العيون والفم)
canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg='black')
canvas.pack()

# تكبير حجم العيون والفم بما يتناسب مع الشاشة
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# إضافة العيون (دائرتين بيضاويتين)
left_eye = canvas.create_oval(screen_width * 0.25 - 50, screen_height * 0.2 - 50, screen_width * 0.25 + 50, screen_height * 0.2 + 50, fill='white')
right_eye = canvas.create_oval(screen_width * 0.75 - 50, screen_height * 0.2 - 50, screen_width * 0.75 + 50, screen_height * 0.2 + 50, fill='white')

# إضافة الفم (خط مستقيم يمكن تحريكه ليبدو كأنه يتحدث)
mouth = canvas.create_line(screen_width * 0.3, screen_height * 0.6, screen_width * 0.7, screen_height * 0.6, fill='red', width=10)

# دالة لتحريك الفم

def move_mouth(is_open):
    if is_open:
        canvas.coords(mouth, screen_width * 0.3, screen_height * 0.6, screen_width * 0.7, screen_height * 0.65)  # فتح الفم
    else:
        canvas.coords(mouth, screen_width * 0.3, screen_height * 0.6, screen_width * 0.7, screen_height * 0.6)  # غلق الفم
    root.update()

# دالة لتشغيل الصوت وتحريك الفم

def play_audio_with_mouth(audio_file):
    try:
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            move_mouth(True)
            time.sleep(0.1)
            move_mouth(False)
            time.sleep(0.1)
    except pygame.error as e:
        print(f"خطأ في تشغيل الملف الصوتي: {e}")

# دالة للتعامل مع ضغطات لوحة المفاتيح

def listen_for_keys():
    while True:
        if keyboard.is_pressed('q'):
            root.quit()  # إغلاق البرنامج عند الضغط على زر Q
            break
        elif keyboard.is_pressed('1'):
            threading.Thread(target=play_audio_with_mouth, args=('1.mp3',)).start()
        elif keyboard.is_pressed('2'):
            threading.Thread(target=play_audio_with_mouth, args=('2.mp3',)).start()
        elif keyboard.is_pressed('3'):
            threading.Thread(target=play_audio_with_mouth, args=('3.mp3',)).start()
        elif keyboard.is_pressed('4'):
            threading.Thread(target=play_audio_with_mouth, args=('4.mp3',)).start()
        elif keyboard.is_pressed('5'):
            threading.Thread(target=play_audio_with_mouth, args=('5.mp3',)).start()
        elif keyboard.is_pressed('6'):
            threading.Thread(target=play_audio_with_mouth, args=('6.mp3',)).start()
        elif keyboard.is_pressed('7'):
            threading.Thread(target=play_audio_with_mouth, args=('7.mp3',)).start()
        elif keyboard.is_pressed('8'):
            threading.Thread(target=play_audio_with_mouth, args=('8.mp3',)).start()
        elif keyboard.is_pressed('9'):
            threading.Thread(target=play_audio_with_mouth, args=('9.mp3',)).start()
        elif keyboard.is_pressed('a'):
            threading.Thread(target=play_audio_with_mouth, args=('A.mp3',)).start()
        elif keyboard.is_pressed('b'):
            threading.Thread(target=play_audio_with_mouth, args=('B.mp3',)).start()
        elif keyboard.is_pressed('c'):
            threading.Thread(target=play_audio_with_mouth, args=('C.mp3',)).start()
        elif keyboard.is_pressed('d'):
            threading.Thread(target=play_audio_with_mouth, args=('D.mp3',)).start()
        elif keyboard.is_pressed('e'):
            threading.Thread(target=play_audio_with_mouth, args=('E.mp3',)).start()
        elif keyboard.is_pressed('f'):
            threading.Thread(target=play_audio_with_mouth, args=('F.mp3',)).start()
        elif keyboard.is_pressed('g'):
            threading.Thread(target=play_audio_with_mouth, args=('G.mp3',)).start()
        elif keyboard.is_pressed('h'):
            threading.Thread(target=play_audio_with_mouth, args=('H.mp3',)).start()
        elif keyboard.is_pressed('i'):
            threading.Thread(target=play_audio_with_mouth, args=('I.mp3',)).start()
        elif keyboard.is_pressed('j'):
            threading.Thread(target=play_audio_with_mouth, args=('J.mp3',)).start()
        elif keyboard.is_pressed('k'):
            threading.Thread(target=play_audio_with_mouth, args=('K.mp3',)).start()
        elif keyboard.is_pressed('l'):
            threading.Thread(target=play_audio_with_mouth, args=('L.mp3',)).start()
        elif keyboard.is_pressed('m'):
            threading.Thread(target=play_audio_with_mouth, args=('M.mp3',)).start()
        elif keyboard.is_pressed('n'):
            threading.Thread(target=play_audio_with_mouth, args=('N.mp3',)).start()
        elif keyboard.is_pressed('o'):
            threading.Thread(target=play_audio_with_mouth, args=('O.mp3',)).start()
        elif keyboard.is_pressed('p'):
            threading.Thread(target=play_audio_with_mouth, args=('P.mp3',)).start()
        elif keyboard.is_pressed('q'):
            threading.Thread(target=play_audio_with_mouth, args=('Q.mp3',)).start()
        elif keyboard.is_pressed('r'):
            threading.Thread(target=play_audio_with_mouth, args=('R.mp3',)).start()
        elif keyboard.is_pressed('s'):
            threading.Thread(target=play_audio_with_mouth, args=('S.mp3',)).start()
        elif keyboard.is_pressed('t'):
            threading.Thread(target=play_audio_with_mouth, args=('T.mp3',)).start()
        elif keyboard.is_pressed('u'):
            threading.Thread(target=play_audio_with_mouth, args=('U.mp3',)).start()
        elif keyboard.is_pressed('v'):
            threading.Thread(target=play_audio_with_mouth, args=('V.mp3',)).start()
        elif keyboard.is_pressed('w'):
            threading.Thread(target=play_audio_with_mouth, args=('W.mp3',)).start()
        elif keyboard.is_pressed('x'):
            threading.Thread(target=play_audio_with_mouth, args=('X.mp3',)).start()
        elif keyboard.is_pressed('y'):
            threading.Thread(target=play_audio_with_mouth, args=('Y.mp3',)).start()
        elif keyboard.is_pressed('z'):
            threading.Thread(target=play_audio_with_mouth, args=('Z.mp3',)).start()
        time.sleep(0.1)

# تشغيل الاستماع لضغطات المفاتيح في خيط منفصل
threading.Thread(target=listen_for_keys, daemon=True).start()

# تشغيل الواجهة الرسومية
root.mainloop()
