def check_even_odd():
    try:
        number_str = input("Enter a number: ")
        number = int(number_str)
        if number % 2 == 0:
            print(f"The number {number} is Even.")
        else:
            print(f"The number {number} is Odd.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

check_even_odd()
