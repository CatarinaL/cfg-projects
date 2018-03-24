def print_by_times(times, text):
    #all indented is in function
    print "\nRepeat '{0}' {1} times: ".format(text, times)
    print (text + " ") * int(times)

def squareNumber(number):
    result = int(number) ** 2
    return result

print "Write something: "
text = raw_input()
print "How many times do you want to print?"
times = raw_input()

print_by_times(times, text)

print "What number do you want to square?"
number = raw_input()
result = squareNumber(number)
print result
