from function import*

Hello_World()

while True:
    try:
        arr = []
        for i in input("PLease, enter a list of number: ").split():
            arr.append(int(i))
        break
    except ValueError:
        print("ERROR, you didn't enter a number!!!")

parity(arr)


