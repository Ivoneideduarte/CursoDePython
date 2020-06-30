#Desafio 21
#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''
import pygame
pygame.init()
pygame.mixer.music.load('pareceQueOjogoVirou.mp3')
pygame.mixer.music.play()
pygame.event.wait()
'''

from pygame import mixer
mixer.init()
mixer.music.load('pareceQueOjogoVirou.mp3')
mixer.music.play()
input('Agora você escuta?')