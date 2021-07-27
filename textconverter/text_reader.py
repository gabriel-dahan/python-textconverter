from io import TextIOWrapper
from gtts import gTTS
from playsound import playsound

import multiprocessing
from typing import Union
import random
import os

def random_name(length: int):
    abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    name = ''.join(random.sample(abc, length))
    return name

class TextConverter(object):

    def __init__(self, text: Union[str, TextIOWrapper]):
        if isinstance(text, TextIOWrapper):
            text = text.read()
        self.text = text.replace('\n', ' ')

    def toaudiofile(self, out_file: str, lang: str = 'en', slow: bool = False):
        sp = gTTS(self.text, lang = lang, slow = slow)
        sp.save(out_file)
    
    def speech(self, lang: str = 'en', slow: bool = False):
        file_name = random_name(10) + '.mp3'
        self.toaudiofile(file_name, lang, slow)
        p = multiprocessing.Process(target = playsound, args = (file_name,))
        p.start()
        input(f'\nReading {file_name}...\nPress any key to stop playback ')
        p.terminate()
        print('\nDeleting file...\n')
        os.remove(file_name)

if __name__ == '__main__':
    tc = TextConverter(open('example.txt'))
    tc.speech('en')