from pynput.mouse import Button, Controller
from python_imagesearch.imagesearch import imagesearch

def cursor():
    mouse = Controller()
    position = imagesearch('C:\\Users\\mlf05\\Desktop\\answermezoom\\typemessage.png')
    temp =[1]*2
    for i,pos in zip(range(2),position):
        temp[i] = pos + 25
    newpos = (temp[0],temp[1])
    mouse.position=(newpos)
    mouse.press(Button.left)
    mouse.release(Button.left)



