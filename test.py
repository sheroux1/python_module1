import my_module

# print(my_module.area_of_house(10,10))
# print(my_module.my_circle(10))

want_to_continue = True
while want_to_continue:
    print("There are three things I can help you with: ")
    print("1. Calculate square footage of a house. ")
    print("2. Calculate the circumference of a circle. ")
    print("3. Sing you a song. ")
    mathtivity = input("\tWhat would you like to do? type 1, 2, or 3, '('q' to quit')'")
    if mathtivity == '1':
        print("Great! I will need the width and length of the house. Also, the number of floors if it's more than 1.")
        width = input("What is the width of the house?")
        length = input("What is the length of the house?")
        floors = input("How many floors does this house have? ")
        # Put code to validate data type here
        clear_output()
        the_area = my_module.area_of_house(int(width), int(length), int(floors))
        print(f"The house if {the_area} square feet in size. Cool!\n\n ")
        continue
    elif mathtivity == '2':
        the_radius = input("Cool! I love geometry. I will need the radius of the circle: ")
        the_circumference = my_module.my_circle(float(the_radius))
        print(f"The circumference of that circle is {the_circumference}.")
        continue
    elif mathtivity == '3':
        print("\n\tThere once was a ship that put to sea, ")
        print("\tThe name of the ship was the Billy 'O Tea, '")
        print("\tThe winds blew hard, her bow dipped down, ")
        print("\tBelow my Bully boys Below, HURAH! \n")
        continue
    elif mathtivity.lower() == 'q':
        want_to_continue = False
        
clear_output()
print("Thanks for playing!")