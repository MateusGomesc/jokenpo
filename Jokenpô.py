from os import system
from random import choice
import pygame

# Cabeçalho
print('*** JOKENPÔ ***\n')
usuario = str(input('Digite seu nickname jogador: '))
system("cls")

# Recebe escolha do usuario
escolha_user = str(input(f'Digite sua escolha {usuario}: '))

# Recebe escolha do computador
opçoes = ['Pedra', 'Papel', 'Tesoura']
escolha_pc = choice(opçoes)

# Condições
if escolha_user.lower() == 'pedra' and escolha_pc.lower() == 'pedra':
    print('\n\033[33mEMPATE!\033[m')
    print(f'Sua escolha: {escolha_user}')
    print(f'Escolha do computador: {escolha_pc}')

elif escolha_user.lower() == 'papel' and escolha_pc.lower() == 'papel':
    print('\n\033[33mEMPATE!\033[m')
    print(f'Sua escolha: {escolha_user}')
    print(f'Escolha do computador: {escolha_pc}')    

elif escolha_user.lower() == 'tesoura' and escolha_pc.lower() == 'tesoura':
    print('\n\033[33mEMPATE!\033[m')
    print(f'Sua escolha: {escolha_user}')
    print(f'Escolha do computador: {escolha_pc}')    

elif escolha_user.lower() == 'pedra' and escolha_pc.lower() == 'papel':
    print('\n\033[31mVOCÊ PERDEU!\033[m')
    print(f'Sua escolha: {escolha_user}')
    print(f'Escolha do computador: {escolha_pc}')    

elif escolha_user.lower() == 'pedra' and escolha_pc.lower() == 'tesoura':
    print('\n\033[32mVOCÊ GANHOU!\033[m')
    print(f'Sua escolha: {escolha_user}')
    print(f'Escolha do computador: {escolha_pc}')
    pygame.init()
    pygame.mixer.music.load('jokenpo.mp3')
    pygame.mixer.music.play(loops=0,start=0.0)
    input()
    pygame.event.wait()        

elif escolha_user.lower() == 'papel' and escolha_pc.lower() == 'pedra':
    print('\n\033[32mVOCÊ GANHOU!\033[m')
    print(f'Sua escolha: {escolha_user}')
    print(f'Escolha do computador: {escolha_pc}')  
    pygame.init()
    pygame.mixer.music.load('jokenpo.mp3')
    pygame.mixer.music.play(loops=0,start=0.0)
    input()
    pygame.event.wait()      

elif escolha_user.lower() == 'papel' and escolha_pc.lower() == 'tesoura':
    print('\n\033[31mVOCÊ PERDEU!\033[m')
    print(f'Sua escolha: {escolha_user}')
    print(f'Escolha do computador: {escolha_pc}')    

elif escolha_user.lower() == 'tesoura' and escolha_pc.lower() == 'pedra':
    print('\n\033[31mVOCÊ PERDEU!\033[m')
    print(f'Sua escolha: {escolha_user}')
    print(f'Escolha do computador: {escolha_pc}')    

elif escolha_user.lower() == 'tesoura' and escolha_pc.lower() == 'papel':
    print('\n\033[32mVOCÊ GANHOU!\033[m')
    print(f'Sua escolha: {escolha_user}')
    print(f'Escolha do computador: {escolha_pc}') 
    pygame.init()
    pygame.mixer.music.load('jokenpo.mp3')
    pygame.mixer.music.play(loops=0,start=0.0)
    input()
    pygame.event.wait()       