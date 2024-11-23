def main():
    
    # read input
    gate = input("choose a gate (either: 1 or 2): ")
    
    # input validation
    if gate not in ["1", "2"]:
        print("your choice should be either 1 or 2")
        return

    # next step
    if gate == "1":
        box = input("choose a box: ")
        if box in ["a", "A"]:
            print("you win!")
            return
    
    print("yo lose :(")

main()
        
