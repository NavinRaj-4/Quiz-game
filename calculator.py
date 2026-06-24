def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a/b

def modulus(a,b):
    if b==0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a%b



while True:
    print("\nCalculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5.Modulus division")
    print("6. Exit")
    
    
        
    try:
        choice=int(input("Enter your choice: "))

        if choice==6:
            print("Exited")
            break
        
        a=int(input("Enter a vlaue 'a': "))
        b=int(input("Enter a vlaue 'b': "))

        match choice:
    
            case 1:
                print("Result: ",add(a,b))
            case 2:
                print("Result: ",sub(a,b))
            case 3:
                print("Result: ",multiply(a,b))
            case 4:
                print("Result: ",divide(a,b))
            case 5:
                print("Result: ",modulus(a,b))
            case _:
                print("Invalid choice")
                continue
            
            
    
    except ValueError :
        print("Enter only numbers")

    except ZeroDivisionError as e:
            print(e)

    
    
    