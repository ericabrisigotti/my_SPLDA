import ex_func

s_in = input()


if s_in.isdigit():
    print(my_func.number_to_letter(int(s_in)))
elif s_in.isupper():
    print(my_func.letter_to_number(s_in))
else:
    print("Invalid input")
