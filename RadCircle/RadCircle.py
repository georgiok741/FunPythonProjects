def print_circle():
    r = int(input("Enter positive integer radius (0 to quit):"))
    if r > 0:
        for row in range(-r, r + 1):
            for col in range(-r, r + 1):
                if row ** 2 + col ** 2 <= r ** 2:
                    print(" * ", end="")
                else:
                    print("   ", end="") 
            print("\n")
    else:
        print("Quitting program now...")

print_circle()

    

