try:
    # Code that might raise an exception
    x = int(input("Enter a number: "))
    y = 10 / x
    print("Result:", y)

except ZeroDivisionError:
    print("Error: Division by zero!")
#For the Test purpose
except ValueError:
    print("Error: Invalid input. Please enter a number.")
#I will add this to experimental branchgi

except Exception as e:  # Catch all other exceptions
    print(f"An unexpected error occurred: {e}")

else:
    # Code to be executed if no exceptions occurred
    print("Calculation successful!")

finally:
    # Code that always executes, regardless of exceptions
    print("This block always executes.")