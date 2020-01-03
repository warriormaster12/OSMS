import pygame

pygame.mixer.pre_init(44100, -16, 2, 2048) 
pygame.mixer.init()
pygame.init()


def value_HighC(): 
    sound = pygame.mixer.Sound('Instruments/Music_Notes/C1.wav') 
    sound.play() 

def value_B():
    sound = pygame.mixer.Sound('Instruments/Music_Notes/B.wav') 
    sound.play() 

def value_As(): 
    sound = pygame.mixer.Sound('Instruments/Music_Notes/Bb.wav') 
    sound.play() 

def value_A():
    sound = pygame.mixer.Sound('Instruments/Music_Notes/A.wav') 
    sound.play() 

def value_Gs(): 
    sound = pygame.mixer.Sound('Instruments/Music_Notes/G_s.wav') 
    sound.play() 

def value_G():
    sound = pygame.mixer.Sound('Instruments/Music_Notes/G.wav') 
    sound.play() 

def value_Fs(): 
    sound = pygame.mixer.Sound('Instruments/Music_Notes/F_s.wav') 
    sound.play() 

def value_F():
    sound = pygame.mixer.Sound('Instruments/Music_Notes/F.wav') 
    sound.play() 

def value_E(): 
    sound = pygame.mixer.Sound('Instruments/Music_Notes/E.wav') 
    sound.play() 

def value_Ds():
    sound = pygame.mixer.Sound('Instruments/Music_Notes/D_s.wav') 
    sound.play() 

def value_D(): 
    sound = pygame.mixer.Sound('Instruments/Music_Notes/D.wav') 
    sound.play() 

def value_Cs():
    sound = pygame.mixer.Sound('Instruments/Music_Notes/C_s.wav') 
    sound.play() 

def value_LowC():
    sound = pygame.mixer.Sound('Instruments/Music_Notes/C.wav') 
    sound.play() 
