import webbrowser, sys

sys.argv

# check if the command line arguments were passed

if len(sys.argv) > 1:
    location = ' '.join(sys.argv[1:])
else:
    location = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('www.google.com/maps/place/' + location)

