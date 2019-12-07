import sys
import pyautogui as pyauto
import screeninfo
from infi.systray import SysTrayIcon


class Screen:
    def create(self, key, n, x, y, w, h):
        self.key = key
        self.n = n
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def from_monitor(self, key, mon):
        self.key = key
        self.x = mon.x
        self.y = mon.y
        self.w = mon.width
        self.h = mon.height
        self.n = int(mon.name[-1:])

def main():
    print("caca")

    key_combo = ""

    curr_screen = 1
    screens = []

    monitors = screeninfo.get_monitors()
    for i in range(len(monitors)):
        screen = Screen()
        screen.from_monitor(sys.argv[i+1], monitors[i])
        screens.append(screen)

    for i in range(len(sys.argv) - len(monitors) - 1):
        key_combo += "'" + sys.argv[len(monitors)+i+1] + "',"

    print(key_combo)

    #Checking for the screen the maouse is at at the beginning
    mouse_pos = pyauto.position()
    for screen in screens:
        if bounds(mouse_pos.x, mouse_pos.y, screen.x, screen.y, screen.w, screen.h):
            curr_screen = screen.n
            to_exec = "press_combo(" + key_combo + "'" + screen.key + "')"
            print(to_exec)
            exec(to_exec)

    while True:
        mouse_pos = pyauto.position()
        for screen in screens:
            if bounds(mouse_pos.x, mouse_pos.y, screen.x, screen.y, screen.w, screen.h):
                if screen.n != curr_screen:
                    print("swaped screens")
                    curr_screen = screen.n
                    to_exec = "press_combo(" + key_combo + "'" + screen.key + "')"
                    exec(to_exec)
            

#def on_mouse_move(x, y):


def press_combo(*keys):
    for key in keys:
        pyauto.keyDown(key)
    
    for key in keys:
        pyauto.keyUp(key)

def bounds(mx, my, x, y, w, h):
    return mx > x and mx < x+w and my > y and my < y+h

menu_options = ((None, None, main),)
systray = SysTrayIcon("", "PyOBSwitching", menu_options)
systray.start()
main()