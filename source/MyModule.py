print "Welcome to my calculator!"

running = True

while running:

    print "Please Make a selection:"
    print "1. Add"
    print "2. Subtract"
    print "3. Multiply"
    print "4. Divide"
    print "0. Exit"

    choice = int(raw_input())
    
    if choice == 0: running = False
    elif choice > 4:
        print "Please choose one of the available functions."
    else:
        print "Enter two values:"
        
        a = float(raw_input("A: "))
        b = float(raw_input("B: "))
        
        c = 0.0
        
        if choice == 1:
            c = a + b
        elif choice == 2:
            c = a - b
        elif choice == 3:
            c = a * b
        elif choice == 4:
            c = a / b
            
        print "The answer is " + str(c)
    
    print