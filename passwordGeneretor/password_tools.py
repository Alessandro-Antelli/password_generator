import random
import string
import math

# --- CONFIGURATION CONSTANTS ---
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS    = string.digits
SYMBOLS   = "!@#£$&()[]|*+;:,.-_<>?^"
OTHERS    = " "  # Includes space

THRESHOLD_VERY_WEAK = 20
THRESHOLD_WEAK      = 40
THRESHOLD_MEDIUM    = 60
THRESHOLD_STRONG    = 80

def get_type(c):
    """Returns the synthetic category of the character."""
    if c in LOWERCASE: return "l"
    if c in UPPERCASE: return "U"
    if c in DIGITS:    return "D"
    if c in SYMBOLS:   return "S"
    if c in OTHERS:    return "O"
    return "X"

def analyze_composition(password):
    """Returns a dictionary with character type counts."""
    return {
        "length":    len(password),
        "lowercase": sum(1 for c in password if c in LOWERCASE),
        "uppercase": sum(1 for c in password if c in UPPERCASE),
        "digits":    sum(1 for c in password if c in DIGITS),
        "symbols":   sum(1 for c in password if c in SYMBOLS),
        "others":    sum(1 for c in password if c in OTHERS)
    }

def calculate_entropy(password):
    """Calculates mathematical entropy in bits."""
    comp = analyze_composition(password)
    pool_size = 0
    if comp["lowercase"] > 0: pool_size += len(LOWERCASE)
    if comp["uppercase"] > 0: pool_size += len(UPPERCASE)
    if comp["digits"]    > 0: pool_size += len(DIGITS)
    if comp["symbols"]   > 0: pool_size += len(SYMBOLS)
    if comp["others"]    > 0: pool_size += len(OTHERS)
    
    if pool_size == 0: return 0.0
    return len(password) * math.log2(pool_size)

def analyze_structural_pattern(password):
    """Identifies logical structure and returns the penalty."""
    blocks = []
    for c in password:
        t = get_type(c)
        # Group Uppercase and Lowercase as 'L' (Letters) for pattern analysis
        if t in ['l', 'U']:
            blocks.append('L')
        else:
            blocks.append(t)
    
    pattern = "".join(blocks)
    type_changes = sum(1 for i in range(1, len(pattern)) if pattern[i] != pattern[i-1])
    
    # Penalty calculation
    order_ratio = (1 - (type_changes / len(password))) * 20
    return round(order_ratio)

def calculate_score(password):
    """Calculates 0-100 score combining entropy and penalties."""
    entropy_bits = calculate_entropy(password)
    
    # Start with entropy (up to 110 to absorb penalties for a true 100)
    score = int(min(110, entropy_bits))
    score -= analyze_structural_pattern(password)
    
    # Consecutive identical character penalty
    repeats = sum(1 for i in range(1, len(password)) if password[i].lower() == password[i-1].lower())
    score -= (repeats * 5)
    
    return min(100, max(0, score))

def describe_score(score):
    """Returns text rating and advice based on score."""
    if score < THRESHOLD_VERY_WEAK:
        return ("EXTREMELY WEAK", "Increase length and use more character types.")
    elif score < THRESHOLD_WEAK:
        return ("VERY WEAK", "Add digits, uppercase letters, or symbols.")
    elif score < THRESHOLD_MEDIUM:
        return ("WEAK", "Use more variety; common patterns lower your score.")
    elif score < THRESHOLD_STRONG:
        return ("GOOD", "Secure password, but you could increase randomness.")
    else:
        return ("EXCELLENT", "Extremely robust and complex password.")

def generate_password(length, use_upper, use_digits, use_symbols, use_others):
    """Generates a password ensuring the selected categories are present."""
    pool = LOWERCASE
    guaranteed = [random.choice(LOWERCASE)]
    
    if use_upper:
        pool += UPPERCASE
        guaranteed.append(random.choice(UPPERCASE))
    if use_digits:
        pool += DIGITS
        guaranteed.append(random.choice(DIGITS))
    if use_symbols:
        pool += SYMBOLS
        guaranteed.append(random.choice(SYMBOLS))
    if use_others:
        pool += OTHERS
        guaranteed.append(random.choice(OTHERS))
    
    missing = length - len(guaranteed)
    remaining = [random.choice(pool) for _ in range(missing)]
    
    final_list = guaranteed + remaining
    random.shuffle(final_list)
    return "".join(final_list)