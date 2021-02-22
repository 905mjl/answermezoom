'''
1. open zoom
 - use keyboard sim to input shortcut keys
2. see if chat window is open
 - take a screenshot of display (maybe able to determine where screenshot is saved)
 - locate image path
 - use python-imagesearch to see if isolated "file" image is present in screenshot
3. if not, open
 - keyboard sim
4. use keyboard simulator to type answer
'''

from pynput.keyboard import Key, Controller

keyboard = Controller()

shortcuts = {
    'open zoom': [Key.ctrl, Key.shift, Key.alt],
    'open chat': [Key.alt, 'h']
}


def press_many(keys):
    for key in keys:
        keyboard.press(key)

    for key in keys:
        keyboard.release(key)


def automate():
    press_many(shortcuts['open zoom'])
    press_many(shortcuts['open chat'])
