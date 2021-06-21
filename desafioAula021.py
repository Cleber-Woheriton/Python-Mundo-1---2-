# Faça um programa que abra e reproduza um áudio MP3
#import pygame

#pygame.init()
#pygame.mixer.music.load('remix.mp3')
#pygame.mixer.music.play(loops=0, start=0.0)
#input()
#pygame.event.wait()
#while(pygame.mixer.music.get_busy()): pass
from pydub import AudioSegment
from pydub.playback import play

musica = input('remix.mp3'), AudioSegment.from_mp3(musica)
#musica = AudioSegment.from_mp3(musica)
play(musica)
