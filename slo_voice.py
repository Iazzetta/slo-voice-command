import speech_recognition as sr
import pyautogui as pag
import time
import warnings
import os

while True:

    r = sr.Recognizer()

    with sr.Microphone() as source:
        os.system('cls' if os.name=='nt' else 'clear')
        print 'SLO Voice Command ~ by Quadruped/Guilherme'
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language = "pt-br", show_all=False)
        print text

        if text.lower() == 'chidori':
            print 'Doing Chidori...'
            pag.press("3")
            pag.press("9")
            pag.press("8")

        elif text.lower() == 'fogo':
            print 'Doing Fire Breath...'
            pag.press("5")
            pag.press("8")
            pag.press("7")
            pag.press("4")

        elif text.lower() == 'vento':
            print 'Doing Wind Bullet'
            pag.press("2")
            pag.press("1")
            pag.press("0")
            pag.press("9")

        time.sleep(1)

    except LookupError as e:
        print("Could not understand audio: %s" % str(e))
    except sr.UnknownValueError:
        print("Slo could not understand audio")
    except sr.RequestError as e:
        print("Slo error; {0}".format(e))
