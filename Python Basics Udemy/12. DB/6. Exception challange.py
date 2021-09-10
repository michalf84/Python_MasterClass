import sys

def getint():
    while True:
        try:
            number=int(input("please enter a number"))
            return number
        except ValueError:
            print("invalid number entered try again")
        except EOFError:
            sys.exit(1)
        finally:
            print("the finally clause always executes")
first_number=getint()
second_number=getint()

try:
    print("{} divided by {}".format(first_number,second_number))
except ZeroDivisionError:
    print("you can't divide by zero")
    sys.exit(2)

#the below always executes
else:
    print("division performed successfully")