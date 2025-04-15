art = """
+----------------------------------------------------------------------------------------------------------+
|                                                                                                          |
|   ,----..               ,--,                             ,--,                  ___                       |
|  /   /   \            ,--.'|                           ,--.'|                ,--.'|_                     |
| |   :     :           |  | :                      ,--, |  | :                |  | :,'   ,---.    __  ,-. |
| .   |  ;. /           :  : '                    ,'_ /| :  : '                :  : ' :  '   ,'\ ,' ,'/ /| |
| .   ; /--`   ,--.--.  |  ' |      ,---.    .--. |  | : |  ' |     ,--.--.  .;__,'  /  /   /   |'  | |' | |
| ;   | ;     /       \ '  | |     /     \ ,'_ /| :  . | '  | |    /       \ |  |   |  .   ; ,. :|  |   ,' |
| |   : |    .--.  .-. ||  | :    /    / ' |  ' | |  . . |  | :   .--.  .-. |:__,'| :  '   | |: :'  :  /   |
| .   | '___  \__\/: . .'  : |__ .    ' /  |  | ' |  | | '  : |__  \__\/: . .  '  : |__'   | .; :|  | '    |
| '   ; : .'| ," .--.; ||  | '.'|'   ; :__ :  | : ;  ; | |  | '.'| ," .--.; |  |  | '.'|   :    |;  : |    |
| '   | '/  :/  /  ,.  |;  :    ;'   | '.'|'  :  `--'   \;  :    ;/  /  ,.  |  ;  :    ;\   \  / |  , ;    |
| |   :    /;  :   .'   \  ,   / |   :    ::  ,      .-./|  ,   /;  :   .'   \ |  ,   /  `----'   ---'     |
|  \   \ .' |  ,     .-./---`-'   \   \  /  `--`----'     ---`-' |  ,     .-./  ---`-'                     |
|   `---`    `--`---'              `----'                         `--`---'                                 |
|                                                                                                          |
+----------------------------------------------------------------------------------------------------------+

"""

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2


operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}

addition = operations["+"]
multiply = operations["*"]
subtraction = operations["-"]
division = operations["/"]



def calculate():
    print(art)
    acumulate = True
    num1 = float(input("Enter the first number: "))

    while acumulate:
        op = input("Pick an operation: \n+\n-\n*\n/\n\n")
        num2 = float(input("Enter next number: "))
        result = 0
        if op == "+":
            result = addition(num1,num2)
        elif op == "-":
            result = subtraction(num1,num2)
        elif op == "*":
            result = multiply(num1,num2)
        elif op == "/":
            result = division(num1,num2)
        else:
            print("Invalid Input")

        print(f"Result: {num1} {op} {num2} = {result}")

        retry = input(f"Type 'yes' to continue further calculation with {result} or Type 'no' to restart: ").lower()

        if retry == "yes":
            num1 = result
        elif retry == "no":
            acumulate = False
            print("\n"*20)
            calculate()

calculate()







