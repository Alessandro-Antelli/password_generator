import password_tools
import validators 

def show_analysis(pwd):
    """Formats and prints the complete password analysis."""
    comp = password_tools.analyze_composition(pwd)
    score = password_tools.calculate_score(pwd)
    label, advice = password_tools.describe_score(score)
    
    bar = "#" * (score // 2)
    
    print("-" * 30)
    print(f"PASSWORD: {pwd}")
    print("-" * 30)
    for key, value in comp.items():
        print(f"{key.capitalize():<12}: {value}")
    print("-" * 30)
    print(f"STRENGTH: {label}")
    print(f"[{bar:<50}] {score}/100")
    print(f"ADVICE: {advice}\n")

def menu_generate():
    print("\n--- PASSWORD CONFIGURATION ---")
    L = validators.read_int("Length (8-64): ", minimum=8, maximum=64) 
    u = validators.read_confirm("Include uppercase?") 
    d = validators.read_confirm("Include digits?") 
    s = validators.read_confirm("Include symbols?") 
    o = validators.read_confirm("Include spaces?") 

    while True:
        pwd = password_tools.generate_password(L, u, d, s, o)
        show_analysis(pwd)
        if not validators.read_confirm("Regenerate with same parameters?"): 
            break

def menu_evaluate():
    print("\n--- PASSWORD EVALUATION ---")
    pwd = validators.read_string("Enter the password to test: ") 
    show_analysis(pwd)

def main():
    while True:
        print("\n=== PASSWORD GENERATOR ===")
        print("1. Generate a password")
        print("2. Evaluate an existing password")
        print("0. Exit") 
        
        choice = validators.read_choice("Choice: ", ["0", "1", "2"]) 
        
        if choice == "1":
            menu_generate()
        elif choice == "2":
            menu_evaluate()
        else:
            print("Goodbye and thanks for all the fish!")
            print("""
                                  __
                               _.-~  )
                    _..--~~~~,'   ,-/     _
                 .-'. . . .'   ,-','    ,' )
               ,'. . . _   ,--~,-'__..-'  ,'
             ,'. . .  (@)' ---~~~~      ,'
            /. . . . '~~             ,-'
           /. . . . .             ,-'
           ...""")
            break

if __name__ == "__main__":
    main()