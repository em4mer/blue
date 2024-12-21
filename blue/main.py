import time
import sys
import pygame
import os
import platform

# Clear the terminal screen
def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

clear_terminal()

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

pygame.mixer.init()

music_file = 'blue/blue.mp3'

pygame.mixer.music.load(music_file)

pygame.mixer.music.play()

lyrics = """
I'll imagine we fell in love
I'll nap under moonlight skies with you
I think I'll picture us, you with the waves
The ocean's colors on your face
I'll leave my heart with your air
So let me fly with you
Will you be forever with me?
"""

phrases = [
    "I'll imagine we fell in love",
    "I'll nap under moonlight skies with you",
    "I think I'll picture us, you with the waves",
    "The ocean's colors on your face",
    "I'll leave my heart with your air",
    "So let me fly with you",
    "Will you be forever with me? 💖"
]

default_speed = 0.067
default_word_delay = 0.2

def print_word(word, speed):
    if word.lower() in ["imagine", "picture", "moonlight"]:
        speed = max(0, speed - 0.2)
    if word.endswith("..."):
        main_word = word[:-3]
        for char in main_word:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        for dot in "...":
            sys.stdout.write(dot)
            sys.stdout.flush()
            time.sleep(3.0 / 3)
        return
    for char in word:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    if word.lower() == "fly":
        time.sleep(0.87)
    if word.lower() == "forever":
        time.sleep(0.97)
    if word.lower() == "you":
        time.sleep(0.17)

for i, phrase in enumerate(phrases):
    words = phrase.split()
    for word in words:
        print_word(word, default_speed)
        sys.stdout.write(' ')
        sys.stdout.flush()
        time.sleep(default_word_delay)
    print()

    if phrase == "I'll imagine we fell in love":
        time.sleep(0.1)
    if phrase == "I'll nap under moonlight skies with you":
        time.sleep(0.5)
    if phrase == "I'll leave my heart with your air":
        time.sleep(0.4)
    if phrase in ["I think I'll picture us, you with the waves", "Will you be forever with me?"]:
        time.sleep(0.2)
    if phrase == "The ocean's colors on your face":
        time.sleep(0.4)
    if phrase == "I'll leave my heart with your air":
        time.sleep(0.7)
    if phrase == "So let me fly with you":
        time.sleep(0.7)
    if phrase == "Will you be forever with me? 💖":
        time.sleep(0.9)
    if phrase == "by G for J":
        time.sleep(0.5)
    if i == 2:
        time.sleep(0.3)

while pygame.mixer.music.get_busy():
    time.sleep(0.1)

print()
