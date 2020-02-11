def celsius_to_farenheit(c):
    f = c*9/5 + 32
    msg_1 = " degrees celcius is "
    msg_2 = " degrees farenheit."
    return str(c) + msg_1 + str(f) + msg_2

user_input = input("Enter temp in C: ")

farenheit = celsius_to_farenheit(float(user_input))

print(farenheit)
if float(user_input) > 30:
    print("Drink lots of water!")