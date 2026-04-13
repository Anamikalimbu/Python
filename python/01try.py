def divide_numbers():
    try:
        print("=== Division Program ===")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        result = a / b

    except ValueError:
        print("Error: Please enter only numbers!")

    except ZeroDivisionError:
        print("Error: You cannot divide by zero!")

    except Exception as e:
        print("Unexpected Error:", e)

    else:
        # Runs only when no error occurs
        print(f"Result = {result}")

    finally:
        # Runs always
        print("Program Finished.")


divide_numbers()
