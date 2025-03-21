def calculateAbsolute():
    # Catches bad input and gets a number to calculate absolute value from the user
    try:
        in_num  = int(input("Enter a number: ")) # input from user
    except:
        print("Bad number")
        exit()

    # Calculates the absolute value of input number - 21
    absolue_difference = abs(in_num - 21)

    # If the input number is greater than 21, double it
    if in_num > 21:
        absolue_difference *= 2
    
    print(f"Result: {absolue_difference}")
    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
