
def bill():
    print("I am bill, please input your name")
    name = str(raw_input())
    print("Hi %s" % name)
    print("Now input a command")
    a = raw_input("Command line:")
    a = a.lower()
    if a == "":
        print("You inputed nothing")
        bill()
    if a == "help":
        print("The commands in my database are help, hello, do this * math problem, do this division math problem")
        bill()
    if a == "hello":
        print("Hello %s!" % name)
        bill()
    if a == "do this * math problem":
        print("Type no. 1")
        b = int(raw_input("Please type an integer"))
        print("Type no. 2")
        c = int(raw_input("Please type an integer"))
        print("Computing...")
        d = b * c
        print("The answer is %d" % d)
        bill()
    if a == "do this division math problem":
        print("Type no. 1")
        e = int(raw_input("Please type an integer"))
        print("Type no. 2")
        f = int(raw_input("Please type an integer"))
        print("Computing...")
        g = e * f
        print("The answer is %d" % g)
        bill()
    if a == "multiply my name":
        name * 100
        bill()
    if a == "open database":
        print("Openining database")
        bill_database()
    else:
        print("That command is not in my database")
        
def bill_database():
    
        
        
    print("Welcome to the bill Profile database, input your first name (Sorry, this command has been discontinued in the release version.")
    a = str(raw_input("Enter Here:"))
    a = a.lower()
    print("Information for %s" % a)
    a = a.lower()
   
        
    bill()


bill()