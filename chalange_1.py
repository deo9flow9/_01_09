import sys


def input_check(text_show):
    while True:
        try:
            return int(input(text_show))
        except ValueError:
            print("Try something else")
        except EOFError:
            print("Exit the program")
            sys.exit(1)
        finally:
            print("The finally clause always executes")

def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        sys.exit(2)
    finally:
        print("Division performed successfully")

while True:
    first_number = input_check("First number ")
    second_number = input_check("Second number ")
    print(division(first_number, second_number))