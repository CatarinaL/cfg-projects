# -*- coding: utf-8 -*-
name = "bla"
print "bla {0}".format(name)

print "\nDe 1 a TRETA quão treta é isto?"
new_input = raw_input()
print "Nivel de treta: \t{0}".format(new_input)

def print_times(times, text):
    #all indented is in function
    print "\nrepeat '{0}' {1} times: ".format(text, times)
    print "repeat " + text + " " + str(times)

    a = {
        "abc": 10,
        "bcd": 23
    }
    

    #print(f"repeat {text} {times}")
    print (text + " ") * times

times = 3
text = "hello"
print_times(times, "boring")
print_times(4, text)
