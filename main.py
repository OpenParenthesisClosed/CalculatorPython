def number_choice():
    som_type= input("Wil je opsommen, aftrekken, keren of delen?")
    if som_type == 'opsommen':
        x = input("Type a number")
        y= input("Type a number")
        sum= int(x)+int(y)

        print("The answer is: ")
        print(sum)

number_choice()