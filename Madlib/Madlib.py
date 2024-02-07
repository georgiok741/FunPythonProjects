import random

def madlib_function(madlib):
    counter = madlib.count("(^")
    string_ = ""
    for i in range(counter):
        opener = madlib.find("(^") 
        closer = madlib.find("^)")
        if opener < closer:
            cut = madlib[opener+2:closer]
            inp_ = input("Enter comma-separated choices for "+ cut +": ")
            inp_split = inp_.split(",")
            inp_stripped = []
            for item in inp_split:
                stripped_ = item.strip()
                inp_stripped.append(stripped_)
            inp_chosen = random.choice(inp_stripped)
            string_ = string_ + madlib[:opener] + inp_chosen
            madlib = madlib[closer+2:]
    print(string_ + madlib)

def main():
    madlib = input("Enter madlib: ")

    spaces = int(input("Enter number of blank lines to hide the madlib: "))
    for i in range(spaces):
        print("")

    madlib_function(madlib)

main()
        
