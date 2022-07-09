def number_choice():
    som_type= input("Wil je opsommen, aftrekken, keren of delen?")
    if som_type == 'opsommen':
        x = input("Type a number")
        y= input("Type a number")
        sum= int(x)+int(y)

        print("The answer is: ")
        print(sum)

    if som_type == 'aftrekken':
        x = input("Type a number")
        y = input("Type a number")
        sub= int(x)-int(y)

        print("The answer is: ")
        print(sub)

    if som_type == 'keren':
        x = input("Type a number")
        y = input("Type a number")
        mul= int(x)*int(y)

        print("The answer is: ")
        print(mul)

    if som_type == 'delen':
        x = input("Type a number")
        y = input("Type a number")
        dev= int(x)/int(y)

        print("The answer is: ")
        print(dev)

number_choice()