#caso o pygame estiver em vermelho é porque é necessário instalar o pacote pygame
#para isso passe o mouse no pygame, clique na lâmpada vermelha e clique em install package pygame
import pygame
pygame.init()
#nada melhor do que uma música de super metroid :3
pygame.mixer.music.load('North.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
