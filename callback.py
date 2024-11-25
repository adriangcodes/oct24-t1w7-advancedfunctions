import time

def greet(name, cb):
    print(f'Hello, {name}!')
    # time.sleep(3)
    cb()

def say_bye():
    print('Bye!')

def shout():
    for i in range(5):
        print('GOODBYE!!!!!')

# Main
greet('Steve', say_bye)
greet('Mary', shout)
print('Continuing main...')
# More statements