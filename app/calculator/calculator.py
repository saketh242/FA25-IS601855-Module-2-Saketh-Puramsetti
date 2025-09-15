from app.operations.operations import addition, subtraction, multiplication, division

def calculator():
    
    "I am rewriting this myself, but following the same structure as module2 github repo"
    print("\nWelcome to the calculator!\n")
    
    while True:
        user_input = input("Enter operation (add, subtract, multiply, divide) followed by two numbers or exit to quit: ").strip().lower()
        
        if user_input == "exit":
            print("Thank you for using the calculator. Bye!\n")
            break
        
        input_params = user_input.split()
        if len(input_params) != 3 or input_params[0] not in ["add", "subtract", "multiply", "divide"]:
            print("Invalid input. Please enter an operation followed by two numbers.")
            continue
        
        try:
            operation, num1_str, num2_str = input_params[0], float(input_params[1]), float(input_params[2])
            if operation == "add":
                result = addition(num1_str, num2_str)
            elif operation == "subtract":
                result = subtraction(num1_str, num2_str)
            elif operation == "multiply":
                result = multiplication(num1_str, num2_str)
            elif operation == "divide":
                result = division(num1_str, num2_str)
            print(f"\nThe result is {result}\n")
        
        except ValueError:
            print("🫤  Enter not a valid number.\n")

        except ZeroDivisionError:
            print("🫠  You know we cannot divide by zero.\n")

        except Exception as e:  
            print("😭  Unexpected error:", e)
            print("\n")

if __name__ == "__main__":
    calculator()