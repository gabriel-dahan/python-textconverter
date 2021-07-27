# TextConverter

### Install and Import the module :

Installing the module :
```bash
~ git clone https://github.com/gabriel-dahan/textconverter/
~ cd textconverter/

# Linux / MacOS
~ python3 -m pip install -U .

# Windows 
~ py -3 -m pip install -U .
```
_Consider using the `--user` parameter if you're not a root/admin user._

Importing the module :
```python
from textconverter import TextConverter
```
### Create a MP3 file from a text.
```python
tc = TextConverter('Some text...')
# or
tc = TextConverter(open('somefile.txt'))

tc.toaudiofile('speech.mp3')
# If the text is in another language (than english), you must specify the lang as a parameter : 
tc.toaudiofile('speech.mp3', lang = 'fr') # For example
```
### Automaticy read the text.
```python
tc = TextConverter('...')

tc.speech()
# or
tc.speech(lang = '...')
```