print('===== DESAFIO 21 =====')
# Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# METODO 1: IMPORTANTO O PYGAME
'''import pygame
print('NOW PLAYING: The Office Opening Theme')
pygame.init()  # este módulo precisa ser iniciado pela função init()
pygame.mixer.music.load('ex021.mp3')  # carregando o arquivo mp3
pygame.mixer.music.play()  # para executar a música
input()
pygame.event.wait()'''

# METODO 2: IMPORTANDO O PLAYSOUND
from playsound import playsound

print('NOW PLAYING: The Office Opening Theme')
playsound('ex021.mp3')
