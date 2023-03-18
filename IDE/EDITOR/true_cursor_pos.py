from ctypes import windll, wintypes, byref

def cursor():
    cursor = wintypes.POINT()
    windll.user32.GetCursorPos(byref(cursor))
    return (cursor.x, cursor.y)
