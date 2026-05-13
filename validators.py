def read_string(prompt):
    """Reads a non-empty string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: The field cannot be empty.") 

def read_int(prompt, minimum=None, maximum=None):
    """Reads an integer and checks the range if specified."""
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Error: Minimum value is {minimum}.")
                continue
            if maximum is not None and value > maximum:
                print(f"Error: Maximum value is {maximum}.")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid integer.") 
            
def read_float(prompt, minimum=None, maximum=None):
    """Reads a float, accepting both comma or dot as a separator."""
    while True:
        try:
            user_input = input(prompt).replace(',', '.')
            value = float(user_input)
            if minimum is not None and value < minimum:
                print(f"Error: Minimum value is {minimum}.")
                continue
            if maximum is not None and value > maximum:
                print(f"Error: Maximum value is {maximum}.")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid decimal number.")

def read_confirm(prompt):
    """Reads y/n and returns True or False."""
    while True:
        choice = input(f"{prompt} [y/n]: ").lower().strip()
        if choice in ['y', 'yes']:
            return True
        if choice in ['n', 'no']:
            return False
        print("Error: Please answer with 'y' or 'n'.") 

def read_choice(prompt, valid_options):
    """Reads a choice from acceptable values."""
    options = [str(o).lower() for o in valid_options]
    while True:
        choice = input(prompt).lower().strip()
        if choice in options:
            return choice
        print(f"Error: Invalid choice. Select from: {', '.join(valid_options)}")