# slo-voice-command
Voice command created in python to execute jutsu (combo) in Shinobi Life Online game.

## Installation

* Install Python: https://www.python.org/downloads/
* Install pip (to manage the dependencies): https://pip.pypa.io/en/stable/installing/
* Install PyAutoGui: http://pyautogui.readthedocs.io/en/latest/install.html
* After install pip, execute this command:

``pip install SpeechRecognition``

* After install python speech_recognition, install pyaudio (https://people.csail.mit.edu/hubert/pyaudio/):

```
(windows): 
    python -m pip install pyaudio
    
(mac osx):
    brew install portaudio 
    pip install pyaudio

(ubuntu/debian):
    sudo apt-get install python-pyaudio python3-pyaudio
```

* Finish! Run:
``python slo_voice.py``

## How to change language?

* Change "pt-br" to "en-us":
```
text = r.recognize_google(audio, language = "pt-br", show_all=False) to
text = r.recognize_google(audio, language = "en-us", show_all=False)
```

* Change the text expected for what you want:
```
(old) if text == 'Chidori':
(new) if text == 'thunder':

(old) if text == 'bola de fogo':
(new) if text == 'fire':


```

