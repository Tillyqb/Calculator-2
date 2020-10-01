"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

def calculator(input_string):
    """Reads a keyboard input string that is space delimited 
       and prints the result of the called function.
    """


    hell = 'warm'
    while not hell == 'frozen':
        string_as_list = input_string.split(' ')
        if string_as_list[0] == 'q':
            hell = "frozen"
        elif string_as_list[0] == 'pow':
            print(power(float(string_as_list[1]), float(string_as_list[2])))
            input_string = input('???')
        elif string_as_list[0] == '+':
            print(add(float(string_as_list[1]), float(string_as_list[2])))
            input_string = input('???')
        elif string_as_list[0] == '-':
            print(subtract(float(string_as_list[1]), float(string_as_list[2])))
            input_string = input('???')
        elif string_as_list[0] == '/':
            print(divide(float(string_as_list[1]), float(string_as_list[2])))
            input_string = input('???')  
        elif string_as_list[0] == 'square':
            print(square(float(string_as_list[1])))
            input_string = input('???') 
        elif string_as_list[0] == 'cube':
            print(cube(float(string_as_list[1])))
            input_string = input('???')  
        elif string_as_list[0] == 'mod':
            print(mod(float(string_as_list[1]), float(string_as_list[2])))
            input_string = input('???')
        elif string_as_list[0] == '*':
            print(multiply(float(string_as_list[1]), float(string_as_list[2])))
            input_string = input('???')
        else:
            input_string = input('Please provide relevant arguments.')

input_string = input('???')
calculator(input_string)
