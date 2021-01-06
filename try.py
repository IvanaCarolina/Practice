#error exceptions

while True:
    try:
        age = int(input('whats your age ? '))
        10/age
    except ValueError:
        print('a number please')
    except ZeroDivisionError:
        print('a number higher than zero')
    else:
        print('Thanks')
        break
    finally:
        print('----Bye----')