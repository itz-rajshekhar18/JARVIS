import pyautogui as gui

def scroll_up():
    gui.press('up',presses=5)

def scroll_down():
    gui.press('down',presses=5)
    
def scroll_to_top():
    gui.hotkey('home')

def scroll_to_down():
    gui.hotkey('end')
    
def perform_scroll_action(text):
    if "scroll up" in text or "upar scroll karo" in text:
        scroll_up()
    elif "scroll down" in text or "niche scroll karo" in text:
        scroll_down()
    elif "scroll to top" in text or "upar jao" in text:
        scroll_to_top()
    elif "scroll to down" in text or "niche jao" in text:
        scroll_to_down()