
from pynput.keyboard import Key, Controller

control = Controller()
def keyboard(h):
    j = h.lower()

    if "control" in j:
        control.press(Key.control)
        control.release(Key.control)
    elif "windows" in j:
        control.press(Key.cmd)
        control.release(Key.cmd)
    elif " altgr" in j:
        control.press(Key.alt_gr)
        control.release(Key.alt_gr)
    elif "enter" in j:
        control.press(Key.enter)
        control.release(Key.enter)
    elif "tab" in j:
        control.press(Key.tab)
        control.release(Key.tab)
    elif "space" in j:
        control.press(Key.space)
        control.release(Key.space)
    elif "alt" in j:
        control.press(Key.alt)
        control.release(Key.alt)
    elif "backspace" in j:
        control.press(Key.backspace)
        control.release(Key.backspace)
    elif "shift" in j:
        control.press(Key.shift)
        control.release(Key.shift)
    elif "caps lock" in j:
        control.press(Key.caps_lock)
        control.release(Key.caps_lock)
    elif "delete" in j:
        control.press(Key.delete)
        control.release(Key.delete)
    elif "down arrow" in j:
        control.press(Key.down)
        control.release(Key.down)
    elif "up arrow" in j:
        control.press(Key.up)
        control.release(Key.up)
    elif "end" in j:
        control.press(Key.end)
        control.release(Key.end)
    elif "home" in j:
        control.press(Key.home)
        control.release(Key.home)
    elif "escape" in j:
        control.press(Key.esc)
        control.release(Key.esc)
    elif "insert" in j:
        control.press(Key.insert)
        control.release(Key.insert)
    elif "left arrow" in j:
        control.press(Key.left)
        control.release(Key.left)
    elif "right arrow" in j:
        control.press(Key.right)
        control.release(Key.right)
    elif "menu" in j:
        control.press(Key.menu)
        control.release(Key.menu)
    elif "num lock" in j:
        control.press(Key.num_lock)
        control.release(Key.num_lock)
    elif "page down" in j:
        control.press(Key.page_down)
        control.release(Key.page_down)
    elif "page up" in j:
        control.press(Key.page_up)
        control.release(Key.page_up)
    elif "pause key" in j:
        control.press(Key.pause)
        control.release(Key.pause)
    elif "print screen" in j:
        control.press(Key.print_screen)
        control.release(Key.print_screen)
    elif "scroll lock" in j:
        control.press(Key.scroll_lock)
        control.release(Key.scroll_lock)
    elif "f1" in j:
        control.press(Key.f1)
        control.release(Key.f1)
    elif "f2" in j:
        control.press(Key.f2)
        control.release(Key.f2)
    elif "f3" in j:
        control.press(Key.f3)
        control.release(Key.f3)
    elif "f4" in j:
        control.press(Key.f4)
        control.release(Key.f4)
    elif "f5" in j:
        control.press(Key.f5)
        control.release(Key.f5)
    elif "f6" in j:
        control.press(Key.f6)
        control.release(Key.f6)
    elif "f7" in j:
        control.press(Key.f7)
        control.release(Key.f7)
    elif "f8" in j:
        control.press(Key.f8)
        control.release(Key.f8)
    elif "f9" in j:
        control.press(Key.f9)
        control.release(Key.f9)
    elif "f10" in j:
        control.press(Key.f10)
        control.release(Key.f10)
    elif "f11" in j:
        control.press(Key.f11)
        control.release(Key.f11)
    elif "f12" in j:
        control.press(Key.f12)
        control.release(Key.f12)
    elif "left control" in j:
        control.press(Key.control_l)
        control.release(Key.control_l)
    elif "right control" in j:
        control.press(Key.control_r)
        control.release(Key.control_r)
    elif "left alt" in j:
        control.press(Key.alt_l)
        control.release(Key.alt_l)
    elif "right alt" in j:
        control.press(Key.alt_r)
        control.release(Key.alt_r)
    elif "left windows" in j:
        control.press(Key.cmd_l)
        control.release(Key.cmd_l)
    elif "right windows" in j:
        control.press(Key.cmd_r)
        control.release(Key.cmd_r)
    elif "left shift" in j:
        control.press(Key.shift_l)
        control.release(Key.shift_l)
    elif "right shift" in j:
        control.press(Key.shift_r)
        control.release(Key.shift_r)
    else:
        print("i think you are wrong.")
        print(j)

keyboard("Wind")





def holdkey(h):
    j = h.lower()

    if "control" in j:
        control.press(Key.control)
    elif "windows" in j:
        control.press(Key.cmd)
    elif " altgr" in j:
        control.press(Key.alt_gr)
    elif "enter" in j:
        control.press(Key.enter)
    elif "tab" in j:
        control.press(Key.tab)
    elif "space" in j:
        control.press(Key.space)
    elif "alt" in j:
        control.press(Key.alt)
    elif "backspace" in j:
        control.press(Key.backspace)
    elif "shift" in j:
        control.press(Key.shift)
    elif "caps lock" in j:
        control.press(Key.caps_lock)
    elif "delete" in j:
        control.press(Key.delete)
    elif "down arrow" in j:
        control.press(Key.down)
    elif "up arrow" in j:
        control.press(Key.up)
    elif "end" in j:
        control.press(Key.end)
    elif "home" in j:
        control.press(Key.home)
    elif "escape" in j:
        control.press(Key.esc)
    elif "insert" in j:
        control.press(Key.insert)
    elif "left arrow" in j:
        control.press(Key.left)
    elif "right arrow" in j:
        control.press(Key.right)
    elif "menu" in j:
        control.press(Key.menu)
    elif "num lock" in j:
        control.press(Key.num_lock)
    elif "page down" in j:
        control.press(Key.page_down)
    elif "page up" in j:
        control.press(Key.page_up)
    elif "pause key" in j:
        control.press(Key.pause)
    elif "print screen" in j:
        control.press(Key.print_screen)
    elif "scroll lock" in j:
        control.press(Key.scroll_lock)
    elif "f1" in j:
        control.press(Key.f1)
    elif "f2" in j:
        control.press(Key.f2)
    elif "f3" in j:
        control.press(Key.f3)
    elif "f4" in j:
        control.press(Key.f4)
    elif "f5" in j:
        control.press(Key.f5)
    elif "f6" in j:
        control.press(Key.f6)
    elif "f7" in j:
        control.press(Key.f7)
    elif "f8" in j:
        control.press(Key.f8)
    elif "f9" in j:
        control.press(Key.f9)
    elif "f10" in j:
        control.press(Key.f10)
    elif "f11" in j:
        control.press(Key.f11)
    elif "f12" in j:
        control.press(Key.f12)
    elif "left control" in j:
        control.press(Key.control_l)
    elif "right control" in j:
        control.press(Key.control_r)
    elif "left alt" in j:
        control.press(Key.alt_l)
    elif "right alt" in j:
        control.press(Key.alt_r)
    elif "left windows" in j:
        control.press(Key.cmd_l)
    elif "right windows" in j:
        control.press(Key.cmd_r)
    elif "left shift" in j:
        control.press(Key.shift_l)
    elif "right shift" in j:
        control.press(Key.shift_r)
    else:
        print("i think you are wrong.")
        print(j)




def releasekey(h):
    j = h.lower()

    if "control" in j:
        control.release(Key.control)
    elif "windows" in j:
        control.release(Key.cmd)
    elif " altgr" in j:
        control.release(Key.alt_gr)
    elif "enter" in j:
        control.release(Key.enter)
    elif "tab" in j:
        control.release(Key.tab)
    elif "space" in j:
        control.release(Key.space)
    elif "alt" in j:
        control.release(Key.alt)
    elif "backspace" in j:
        control.release(Key.backspace)
    elif "shift" in j:
        control.release(Key.shift)
    elif "caps lock" in j:
        control.release(Key.caps_lock)
    elif "delete" in j:
        control.release(Key.delete)
    elif "down arrow" in j:
        control.release(Key.down)
    elif "up arrow" in j:
        control.release(Key.up)
    elif "end" in j:
        control.release(Key.end)
    elif "home" in j:
        control.release(Key.home)
    elif "escape" in j:
        control.release(Key.esc)
    elif "insert" in j:
        control.release(Key.insert)
    elif "left arrow" in j:
        control.release(Key.left)
    elif "right arrow" in j:
        control.release(Key.right)
    elif "menu" in j:
        control.release(Key.menu)
    elif "num lock" in j:
        control.release(Key.num_lock)
    elif "page down" in j:
        control.release(Key.page_down)
    elif "page up" in j:
        control.release(Key.page_up)
    elif "pause key" in j:
        control.release(Key.pause)
    elif "print screen" in j:
        control.release(Key.print_screen)
    elif "scroll lock" in j:
        control.release(Key.scroll_lock)
    elif "f1" in j:
        control.release(Key.f1)
    elif "f2" in j:
        control.release(Key.f2)
    elif "f3" in j:
        control.release(Key.f3)
    elif "f4" in j:
        control.release(Key.f4)
    elif "f5" in j:
        control.release(Key.f5)
    elif "f6" in j:
        control.release(Key.f6)
    elif "f7" in j:
        control.release(Key.f7)
    elif "f8" in j:
        control.release(Key.f8)
    elif "f9" in j:
        control.release(Key.f9)
    elif "f10" in j:
        control.release(Key.f10)
    elif "f11" in j:
        control.release(Key.f11)
    elif "f12" in j:
        control.release(Key.f12)
    elif "left control" in j:
        control.release(Key.control_l)
    elif "right control" in j:
        control.release(Key.control_r)
    elif "left alt" in j:
        control.release(Key.alt_l)
    elif "right alt" in j:
        control.release(Key.alt_r)
    elif "left windows" in j:
        control.release(Key.cmd_l)
    elif "right windows" in j:
        control.release(Key.cmd_r)
    elif "left shift" in j:
        control.release(Key.shift_l)
    elif "right shift" in j:
        control.release(Key.shift_r)
    elif "release them" in j:
        control.release(Key.control)
        control.release(Key.cmd)
        control.release(Key.alt_gr)
        control.release(Key.enter)
        control.release(Key.tab)
        control.release(Key.space)
        control.release(Key.alt)
        control.release(Key.backspace)
        control.release(Key.shift)
        control.release(Key.caps_lock)
        control.release(Key.delete)
        control.release(Key.down)
        control.release(Key.up)
        control.release(Key.end)
        control.release(Key.home)
        control.release(Key.esc)
        control.release(Key.insert)
        control.release(Key.left)
        control.release(Key.right)
        control.release(Key.menu)
        control.release(Key.num_lock)
        control.release(Key.page_down)
        control.release(Key.page_up)
        control.release(Key.pause)
        control.release(Key.print_screen)
        control.release(Key.scroll_lock)
        control.release(Key.f1)
        control.release(Key.f2)
        control.release(Key.f3)
        control.release(Key.f4)
        control.release(Key.f5)
        control.release(Key.f6)
        control.release(Key.f7)
        control.release(Key.f8)
        control.release(Key.f9)
        control.release(Key.f10)
        control.release(Key.f11)
        control.release(Key.f12)
        control.release(Key.control_l)
        control.release(Key.control_r)
        control.release(Key.alt_l)
        control.release(Key.alt_r)
        control.release(Key.cmd_l)
        control.release(Key.cmd_r)
        control.release(Key.shift_l)
        control.release(Key.shift_r)
    else:
        print("i think you are wrong.")
        print(j)


def shortcut(j):
    if "close" in j:
        control.press(Key.alt)
        control.press(Key.f4)
        control.release(Key.f4)
        control.release(Key.alt)
    elif "copy" in j:
        control.press(Key.control)
        control.press('c')
        control.release('c')
        control.release(Key.control)
    elif "paste" in j:
        control.press(Key.control)
        control.press('v')
        control.release('v')
        control.release(Key.control)
    elif "save" in j:
        control.press(Key.control)
        control.press('s')
        control.release('s')
        control.release(Key.control)
    elif "battery" in j:
        control.press(Key.insert)
        control.press(Key.shift)
        control.press('b')
        control.release('b')
        control.release(Key.shift)
        control.release(Key.insert)
