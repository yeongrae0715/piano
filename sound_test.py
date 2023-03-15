import pygame
pygame.mixer.init(44100, -16, 2, 1024)
print('pygame init')
my_sound = pygame.mixer.Sound('Choir/C4.wav')
print('load audio file')
my_sound.set_volume(1.0)
print('set volume 1.0')
my_sound.play()
print('play sound')