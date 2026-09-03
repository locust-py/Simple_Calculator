def soma(n1, n2):
    resultado = n1 + n2
    print(resultado)

def subtracao(n1, n2):
    resultado = n1 - n2
    print(resultado)

def multiplicacao(n1, n2):
    resultado = n1 * n2
    print(resultado)

def divisao(n1, n2):
    resultado = n1 / n2
    print(resultado)

while True:
    try:
        num1 = input("Enter the first number (STOP) to exit: ").upper().strip()
        if num1 == "STOP":
            break
        num2 = input("Enter the second number (STOP) to exit: ").upper().strip()
        if num2 == "STOP":
            break

        num1 = int(num1)
        num2 = int(num2)

        ch = int(input("""Enter the choice
        1 - add
        2 - subtract
        3 - multiply
        4 - divide
        """))

        if ch == 1:
            soma(num1, num2)
        elif ch == 2:
            subtracao(num1, num2)
        elif ch == 3:
            multiplicacao(num1, num2)
        elif ch == 4:
            divisao(num1, num2)

    except ValueError:
        print("Enter a number")
    except ZeroDivisionError:
        print("You cannot divide by zero")

