def enter_number():
    number_input = raw_input("Enter a number between 1 and 10: ")
    number = int(number_input) #convert to int

    if number > 10:
        print "Nope, too high!"

    elif number <= 0: #careful with the elifs.. not too many
        print "Too low!"

    else:
        print "Good choice."

while True:
    enter_number()
    continue_input = raw_input("Enter 'y' to continue: ")
    if continue_input.strip() != 'y':
        break

print "Goodbye!"
