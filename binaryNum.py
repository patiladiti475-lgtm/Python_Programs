def Binary(no):
    binary = ""

    while no > 0:
        rem = no % 2
        binary = str(rem) + binary
        no = no // 2

    print("Binary equivalent is:", binary)


num = int(input("Enter a number: "))
Binary(num)