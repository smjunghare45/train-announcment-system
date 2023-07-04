import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS
from playsound import playsound
import numpy as np

import time
import pygame


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)


def play_22221_audio():
    playsound(
        r'C:\\Users\\91859\\Desktop\\semi_final\\22221.mp3')


def play_12243_audio():
    playsound(r'C:\\Users\\91859\\Desktop\\semi_final\\12243.mp3')


def play_16557_audio():
    playsound(r'C:\\Users\\91859\\Desktop\\semi_final\\16557.mp3')


def play_12297_audio():
    playsound(r'C:\\Users\\91859\\Desktop\\semi_final\\12297.mp3')


def play_82501_audio():
    playsound(r'C:\\Users\\91859\\Desktop\\semi_final\\82501.mp3')


def play_12067_audio():
    playsound(r'C:\\Users\\91859\\Desktop\\semi_final\\12067.mp3')


def play_22423_audio():
    playsound(r'C:\\Users\\91859\\Desktop\\semi_final\\22423.mp3')


def play_22447_audio():
    playsound(r'C:\\Users\\91859\\Desktop\\semi_final\\22447.mp3')


def play_12983_audio():
    playsound(r'C:\\Users\\91859\\Desktop\\semi_final\\12983.mp3')


def play_12169_audio():
    playsound(r'C:\\Users\\91859\\Desktop\\semi_final\\12169.mp3')


def play_12275_audio():
    playsound(r'C:\\Users\\91859\\Desktop\\semi_final\\12275.mp3')


def play_12249_audio():
    playsound(r'C:\\Users\\91859\\Desktop\\semi_final\\12249.mp3')


def play_22701_audio():
    playsound(r'C:\\Users\\91859\\Desktop\\semi_final\\22701.mp3')


def play_15906_audio():
    playsound(r'C:\\Users\\91859\\Desktop\\semi_final\\15906.mp3')


def play_22921_audio():
    playsound(r'C:\\Users\\91859\\Desktop\\semi_final\\22921.mp3')


def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined


def generateBody():
    audio = AudioSegment.from_mp3('train.mp3')

    # 1-Generate kripya dhyan dijiye
    start = 16300
    finish = 19200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")

    # 2-is from city

    # 3-Generate se chalkar
    start = 21400
    finish = 22200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    # 4-is via-city

    # 5-Generate ke raaste
    start = 19900
    finish = 20660
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # 6-is to-city

    # 7-Generate ko jaani vali
    start = 23100
    finish = 24000
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 8- is train no and name

    # 9-Generate  platform
    start = 28900
    finish = 29920
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")

    # 10-is platform no

    # 11-Generate par aa chuki hai
    start = 30400
    finish = 32270
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")


def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2-Generate from-city
        textToSpeech(item['from'], '2_hindi.mp3')
        # 4-Generate via-city
        textToSpeech(item['via'], '4_hindi.mp3')
        # 6-Generate to-city
        textToSpeech(item['to'], '6_hindi.mp3')
        # 8-Generate train no and name
        textToSpeech(item['train_no'] + " "+item['train_name'], '8_hindi.mp3')
        # 10=Generate platform number
        textToSpeech(item['platform'], '10_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1, 12)]

        announcement = mergeAudios(audios)
        announcement.export(
            f"hin_announce_{item['train_no']}_{index+1}.mp3", format="mp3")

# English


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)


def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined


def generateBody():
    audio = AudioSegment.from_mp3('train.mp3')

    # 1-May I have your attention please
    start = 0000
    finish = 3800
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_english.mp3", format="mp3")

    # 2-Train no and name

    # 3-From
    start = 8780
    finish = 9230
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_english.mp3", format="mp3")

    # 4-is from-city

    # 5-via
    start = 10300
    finish = 10750
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_english.mp3", format="mp3")

    # 6-is via-city

    # 7-to
    start = 11290
    finish = 11760
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_english.mp3", format="mp3")

    # 8- is to-city

    # 9-Has arrived at platform no.
    start = 12500
    finish = 14570
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_english.mp3", format="mp3")

    # 10-is platform no


def generateAnnounce(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2-Train no and name
        textToSpeech(item['train_no'] + " " +
                     item['train_name'], '2_english.mp3')
        # 4-is from-city
        textToSpeech(item['from'], '4_english.mp3')
        # 6-is via-city
        textToSpeech(item['via'], '6_english.mp3')
        # 8- is to-city
        textToSpeech(item['to'], '8_english.mp3')
        # 10-is platform no
        textToSpeech(item['platform'], '10_english.mp3')

        audios = [f"{i}_english.mp3" for i in range(1, 11)]

        announcement = mergeAudios(audios)
        announcement.export(
            f"eng_announce_{item['train_no']}_{index+1}.mp3", format="mp3")


# def display_board():
#     pygame.init()


# # define the RGB value
# # for white colour
# black = (0, 0, 0)

# # assigning values to X and Y variable
# X = 1550
# Y = 800

# # create the display surface object
# # of specific dimension..e(X, Y).
# display_surface = pygame.display.set_mode((X, Y))

# # set the pygame window name
# pygame.display.set_caption('Image')

# # create a surface object, image is drawn on it.
# image = pygame.image.load(
#     r'C:\Users\Aryan\Desktop\Learning Skills\python\Train_announcement_python\displayboard.png')

# # infinite loop
# while True:

#     # completely fill the surface object
#     # with white colour
#     display_surface.fill(black)

#     # copying the image surface object
#     # to the display surface object at
#     # (0, 0) coordinate.
#     display_surface.blit(image, (0, 0))

#     # iterate over the list of Event objects
#     # that was returned by pygame.event.get() method.
#     for event in pygame.event.get():

#         # if event object type is QUIT
#         # then quitting the pygame
#         # and program both.
#         if event.type == pygame.QUIT:

#             # deactivates the pygame library
#             pygame.quit()

#             # quit the program.
#             quit()

#         # Draws the surface object to the screen.
#         pygame.display.update()


if __name__ == "__main__":
    print("                <--------------------------------------------Welcome to Mini project ------------------------------------------------>")
    generateBody()
    print("                                           Travel Safe And Happy Journey                       ")
    localtime = time.asctime(time.localtime(time.time()))
    print(
        f"                          \t\t\t{localtime}                                         ")
    generateAnnouncement("announce_hindi.xlsx")
pygame.init()
black = (0, 0, 0)
Set_Width = 1550
Set_Height = 800
display_surface = pygame.display.set_mode((Set_Width, Set_Height))
pygame.display.set_caption('Image')
image = pygame.image.load(
    r'C:\Users\91859\Desktop\semi_final\displayboard.png')
while True:
    display_surface.fill(black)
    display_surface.blit(image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
        play_22221_audio()
        play_12243_audio()
        play_16557_audio()
        play_12297_audio()
        play_82501_audio()
        play_12067_audio()
        play_22423_audio()
        play_22447_audio()
        play_12983_audio()
        play_12169_audio()
        play_12275_audio()
        play_12249_audio()
        play_22701_audio()
        play_15906_audio()
        play_22921_audio()
