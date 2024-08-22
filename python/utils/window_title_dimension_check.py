import pygetwindow as gw
from pygetwindow import Win32Window as win
import win32gui

def get_window_region_by_title(title):
    try:
        window = gw.getWindowsWithTitle(title)[0]
        left, top, right, bottom = window.left, window.top, window.right, window.bottom
        width = right - left
        height = bottom - top
        return {
            "left": left,
            "top": top,
            "right": right,
            "bottom": bottom,
            "width": width,
            "height": height
        }
    except IndexError:
        return None

def activateWindow(win_title):
    currentWindowObjs = gw.getWindowsWithTitle(win_title)
    print(currentWindowObjs)
    if len(currentWindowObjs) > 0:
        currentWindowObjs[0].activate()
    else:
        raise 'Windows not available for given title'



# Replace 'Untitled - Notepad' with the title of the window you want to get the region for
window_title = 'Slack Properties'
# # region = get_window_region_by_title(window_title)
activateWindow(window_title)

# if region:
#     print(f"Window Region: {region}")
# else:
#     print("Window not found.")
