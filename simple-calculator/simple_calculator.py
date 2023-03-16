# </> -- > Developed by: @Henrique-Coder (https://github.com/Henrique-Coder) </>

from os import system as cmd


def app_title():
    cmd('cls || clear')
    print('\n# </> -- > Simple Calculator </>\n')


def calculation(num1, num2, mode):
    if mode == '1':
        return str(num1 + num2)
    elif mode == '2':
        return str(num1 - num2)
    elif mode == '3':
        return str(num1 * num2)
    elif mode == '4':
        return str(num1 / num2)
    else:
        return False


while True:
    app_title()
    while True:
        try:
            num1 = float(input('Enter the first number: '))
            break

        except ValueError:
            input('\n[!] Invalid Input! Only numbers are allowed. Press ENTER to try again.')

    while True:
        app_title()
        try:
            print(f'Enter the first number: {num1}')
            num2 = float(input(f'Enter the second number: '))
            break

        except ValueError:
            input('\n[!] Invalid Input! Only numbers are allowed. Press ENTER to try again.')

    while True:
        app_title()
        print(f'Calculation: {num1} [?] {num2} = ?')
        print('Operations: [1] Addition, [2] Subtraction, [3] Multiplication, [4] Division')
        op_choice = input('Choice: ')

        if op_choice in ['1', '2', '3', '4']:
            break

        else:
            input('\n[!] Invalid operation! Press ENTER to try again.')

    result = calculation(num1, num2, op_choice)

    if not result:
        app_title()
        input('[!] Invalid operation! Press ENTER to try again.')

    else:
        app_title()
        print(
            f'Calculation: '
            f'{num1} {"+" if op_choice == "1" else "-" if op_choice == "2" else "*" if op_choice == "3" else "/"} {num2} = {result}')

    final_choice = input('\n[#] Press ENTER to restart the calculator or type anything to exit: ')
    if final_choice:
        break
