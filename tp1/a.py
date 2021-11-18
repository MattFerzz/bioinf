import time

string = "hello world"
for char in string:
    print(char, end='', flush=True)
    time.sleep(.25)