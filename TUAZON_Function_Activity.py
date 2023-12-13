while True:
    print()
    print("COMPUTER PROGRAMMING 1 - LABORATORY ACTIVITY\nCREATED BY : NICOLE SHANE P. TUAZON\n")
    def calculate_sum_or_multiply():
        # Get input from the user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))

        # Calculate the sum
        total_sum = num1 + num2 + num3

        # Check if the numbers are the same
        if num1 == num2 == num3:
            result = num1 * num2 * num3
        else:
            result = total_sum

        # Display the result
        print(f"Result is {result}")

    # Call the function to execute the program
    calculate_sum_or_multiply()


