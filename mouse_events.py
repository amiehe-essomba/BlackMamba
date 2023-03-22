from pynput.mouse import Listener


def on_move(x, y):
    print(x, y)
    return False


def on_click(x, y, button, pressed):
    print(x, y, button, pressed)
    return False


def on_scroll(x, y, dx, dy):
    print(x, y, dx, dy)
    return False


with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()