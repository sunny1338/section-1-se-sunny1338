import webbrowser, sys 

VIDEO_LINK = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def input_math():
    while True:
        user_input = input("1 times 1 = ? ")
        if int(user_input) == 1: 
            open_video()
            break
        elif user_input == "exit":
            sys.exit()
        else:
            print("Wrong! Try again.")
            open_video()

def open_video():
    global VIDEO_LINK
    webbrowser.open(VIDEO_LINK)
    return

input_math()
