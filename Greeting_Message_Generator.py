def generate_greeting(first_name, last_name):
    greeting_message = f"Hello {first_name} {last_name}! You just developed into python."
    return greeting_message

def main():
    # Prompt user for input
    first_name = input("Enter your first name (up to 10 characters): ")
    last_name = input("Enter your last name (up to 10 characters): ")

    # Check input constraints
    if len(first_name) > 10 or len(last_name) > 10:
        print("Error: First and last names must be 10 characters or less.")
    else:
        # Generate and display greeting message
        message = generate_greeting(first_name, last_name)
        print(message)

if __name__ == "__main__":
    main()
