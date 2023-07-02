from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' #Не выводит водные слова из Pygame

from pygame import mixer
import brave,explorer,calc,WINWORD,calend,notepad #Импортирование файлов для взаимодействия с приложениями
import hello,how_are_you,jokes #Импортирования файлов для общения
import youtube,twitch,вк #Импортирование файлов для открытия сайтов
import random
import psutil
import os
import speech_recognition as sr
import webbrowser
import pygame
import time
import all_input_commands

 #Функции для закрытия/открытия программ

def close_progs(prog1):
    print(1)
    mixer.Sound(random.choice(brave.output1)).play()
    for process in (process for process in psutil.process_iter() if process.name()==prog1):                                                                                                            
        process.kill()

def open_progs(prog):
    print(1)
    mixer.Sound(random.choice(brave.output)).play()  
    os.startfile(prog)
    

c=0   
c2=0
c3=0
eror=''

mixer.init()                       
r = sr.Recognizer()    

#Главная функция

def record_volume():
    global c,c2,c3
    global eror
    prog=0
    with sr.Microphone() as source:
        r.pause_threshold = 0.5  
        r.adjust_for_ambient_noise(source, duration=0.5) 
        if c2==0 :
            
            try:
                audio = r.listen(source)
 
            except:
                record_volume()

            try:
                

                query = r.recognize_google(audio, language = 'ru-RU')
                text = query.lower()

                    
                
                while 'привет' and 'софия' not in text and c!=1:
                    record_volume()

  
                if c3==0:
                    text='привет'
                    c3=2
                c=1
                
                if c==1 :
                    music='off'
                    print(text) 


                    if text=='топ':
                        text='стоп'
                    
                    if text in all_input_commands.input_comands:
                        music='on'
                    else:
                        parts = text.split(' ')
                        print(len(parts))
                        if  parts[0] in all_input_commands.input_comands and parts[1] in all_input_commands.progs and len(parts)<4 and len(parts)>1:
                            print('kk')
                            music='on'
                        elif len(parts)==1:
                            if parts[0] in all_input_commands.progs:

                                music='on'
                        else:
                            record_volume()
                    
                    if music=='on':
                        mixer.Sound('9.mp3').play()
                        time.sleep(0.5)
                        

                    

                    if text in hello.input_commands:                        
                        mixer.Sound(random.choice(hello.output)).play()

                    elif text in how_are_you.input_commands:
                        mixer.Sound(random.choice(how_are_you.output)).play()  
                                           
                    #Открытие разных программ

                    elif  text in brave.input_commands:
                        prog='brave.exe'
                    elif text in calc.input_commands:
                        prog='calc.exe'
                    elif text in notepad.input_commands:
                        prog='notepad.exe'
                    elif text in WINWORD.input_commands:
                        prog='WINWORD.exe'
                    elif text in explorer.input_commands:
                        prog='explorer.exe'
                    elif text in calend.input_commands:
                        mixer.Sound(random.choice(brave.output)).play()
                        webbrowser.open_new('https://time.is/ru/calendar')
                        
                        
                    #Закрытие разных программ

                    elif text in brave.input_commands1:                                             
                        prog1='brave.exe'  
                    elif text in explorer.input_commands1:                       
                        prog1='explorer.exe'
                    elif text in WINWORD.input_commands1:                       
                        prog1='WINWORD.EXE'
                    elif text in calc.input_c:                       
                        prog1='CalculatorApp.exe'
                    elif text in notepad.input_commands1:                       
                        prog1='Notepad.exe'
                    

                    #Открытие сайтов


                    if text in youtube.input_commands:
                        webbrowser.open_new('https://www.youtube.com/')
                        mixer.Sound(random.choice(brave.output)).play()
                    elif text in twitch.input_commands:
                        webbrowser.open_new('https://www.twitch.tv/')
                        mixer.Sound(random.choice(brave.output)).play()
                    elif text in вк.input_commands:
                        webbrowser.open_new('https://vk.com/feed')
                        mixer.Sound(random.choice(brave.output)).play()

                    
                    #Шутки
                    
                    elif text in jokes.input_commands:
                        joke='g'
                        while joke[-1]!='0':
                            joke=random.choice(jokes.output)
                            if joke[-1]=='0':
                                mixer.Sound(joke[:-1]).play()
                                break
                            
                    
                        time_sleep=4       
                        jokes.output[jokes.output.index(joke)]=joke[:-1]+'1'
                        joke=joke[:-1]+'1'
                        if joke[:-1]=='7j.mp3' or  joke[:-1]=='8j.mp3':
                            time_sleep=7
 
                        print(joke)
                        for i in jokes.output:
                            if i!=joke:
                                if i[-1]=='1' or i[-1]=='2' :       
                                    jokes.output[jokes.output.index(i)]=i[:-1]+str(int(i[-1])+1)
                                if i[-1]=='3':
                                    jokes.output[jokes.output.index(i)]=i[:-1]+'0'
                        while pygame.mixer.music.get_busy()!=False:
                            time.sleep(time_sleep)
                            

                    elif text=='стоп':
                        c=0
                        record_volume()
                    else:
                        eror+='e'
                        if 'eeeee' in eror:
                            c=0
                       

                    eror=''
                    c=1
                    c2=1

                    if prog!=0:
                        open_progs(prog)
                        prog=0
                        
                        
                    elif prog1!=0:
                        close_progs(prog1)
                        prog1=0
                        
                    record_volume()

                      
            except:               
                eror+='e'
                if 'eeeee' in eror:
                    c=0
         
                record_volume()
        elif c2==1:
            c2=0
    
        elif c2==2:
            c2=1

        record_volume()

record_volume()
       








































