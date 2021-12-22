import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('D:\Downloads\ex21.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(1)
x = input('digite algo para encerrar...')
