import logging
import sys 

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', 
                    level=logging.DEBUG,
                    stream=sys.stdout)

def get_mouse_pos():
    mouse_pos = None 
    if sys.platform in ['linux', 'linux2']:pass 
    elif sys.platform == "windows":
        try: import win32api
        except ImportError: 
            logging.info("win32api not installed")
            win32api = None 
        if win32api is not None :
            x, y = win32api.GetCursorPos()
            mouse_pos = {"x":  x, "y":y}
        elif sys.platform == "Mac": pass 
        else:
            try: import tkinter as TK 
            except ImportError:
                logging.info("Tkinter is not installed")
                TK = None 
            
            if TK is not None:
                p = TK.Tk()
                x, y = p.winfo_pointerxy()
                mouse_pos = {"x":x, "y":y}
            print(f"sys.platform = {sys.platform} is unknown. please report.")
            print(sys.version)
        return mouse_pos 
    
        
            