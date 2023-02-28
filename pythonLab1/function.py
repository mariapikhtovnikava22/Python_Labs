def Hello_World():
    print("Hello World")

def parity ( ):
    while True:
        try:
            arr = []
            for i in input("PLease, enter a list of number: ").split():
                arr.append(int(i))
            break
        except ValueError:
            print("ERROR, you didn't enter a number!!!")

    new_list = list()

    for i in arr:
        if i % 2 == 0:
            new_list += [i]

    if (len(new_list) != 0):
        print(new_list)
    else:
        print("There are no even numbers in the list")

def mini_calculate ( ):

    while True:

        try:
            num1 = int(input("Enter a number 1: "))
            num2 = int(input("Enter a number 2: "))

            while True:
                try:
                    n = int(input(
                        "Enter the operation number that you want to apply to our numbers: \n 1) + \n 2) - \n 3) * \n 4) / \n"))
                    if ((n < 1) or (n > 4)):
                        raise Exception()
                    break
                except Exception as e:
                    print("Error!!!Enter the operation number")
            break

        except ValueError:
            print("ERROR, you didn't enter a number!!!")
        except Exception as e:
            print("Error!!!Enter the operation number")

    if (n == 1):
        print(f'{num1} + {num2} = {num1 + num2}')
    if (n == 2):
        if (num2 > num1):
            print(f'{num2} - {num1} = {num2 - num1}')
        else:
            print(f'{num1} - {num2} = {num1 - num2}')
    if (n == 3):
        print(f'{num1} * {num2} = {num1 * num2}')

    if (n == 4):
        try:
            print(f'{num1} / {num2} = {num1 / num2}')
        except ZeroDivisionError:
            print("ERROR!!! You can't divide by zero")







