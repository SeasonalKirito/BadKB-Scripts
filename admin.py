import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    print("The program is running with administrative privileges.")
else:
    print("The program is not running with administrative privileges.")