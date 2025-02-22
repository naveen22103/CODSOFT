import random
import string
import qrcode
import pyperclip
from termcolor import colored

def display_banner():
    banner = """
    =====================================
        Welcome to SecurePass 3000!     
        Advanced Password Generator     
    =====================================
    """
    print(colored(banner, 'cyan', attrs=['bold']))

def get_user_input():
    print("\nChoose the password complexity level:")
    print("1. Basic (Lowercase only)")
    print("2. Strong (Lowercase, Uppercase, Numbers, Special Characters)")
    print("3. Custom (Choose your own settings)")
    
    choice = int(input(colored("Enter your choice (1-3): ", 'yellow')))
    length = int(input(colored("Enter the desired password length: ", 'yellow')))
    return choice, length

def generate_password(choice, length):
    if choice == 1:
        # Basic: Lowercase only
        characters = string.ascii_lowercase
    elif choice == 2:
        # Strong: Lowercase, Uppercase, Numbers, Special Characters
        characters = string.ascii_letters + string.digits + string.punctuation
    elif choice == 3:
        # Custom settings
        use_lower = input(colored("Include lowercase letters? (y/n): ", 'yellow')).lower() == 'y'
        use_upper = input(colored("Include uppercase letters? (y/n): ", 'yellow')).lower() == 'y'
        use_digits = input(colored("Include numbers? (y/n): ", 'yellow')).lower() == 'y'
        use_special = input(colored("Include special characters? (y/n): ", 'yellow')).lower() == 'y'
        
        characters = ""
        if use_lower:
            characters += string.ascii_lowercase
        if use_upper:
            characters += string.ascii_uppercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation
        
        if not characters:
            return "Error: No character set selected!"
    else:
        return "Invalid choice!"
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def evaluate_strength(password):
    if len(password) < 6:
        return "Weak"
    elif len(password) < 10:
        return "Medium"
    else:
        return "Strong"

def save_to_file(password):
    with open("generated_passwords.txt", "a") as file:
        file.write(password + "\n")
    print(colored("Password saved to 'generated_passwords.txt'.", 'green'))

def generate_qr_code(password):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(password)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save("password_qr.png")
    print(colored("QR Code saved as 'password_qr.png'.", 'green'))

def main():
    display_banner()
    choice, length = get_user_input()
    password = generate_password(choice, length)

    if "Error" in password or "Invalid" in password:
        print(colored(password, 'red'))
    else:
        print(colored(f"\nGenerated Password: {password}", 'green'))
        
        # Evaluate and display password strength
        strength = evaluate_strength(password)
        print(colored(f"Password Strength: {strength}", 'blue', attrs=['bold']))
        
        # Copy to clipboard
        pyperclip.copy(password)
        print(colored("Password copied to clipboard!", 'green'))
        
        # Additional options
        save = input(colored("\nDo you want to save this password to a file? (y/n): ", 'yellow')).lower()
        if save == 'y':
            save_to_file(password)
        
        qr = input(colored("Do you want to generate a QR code for this password? (y/n): ", 'yellow')).lower()
        if qr == 'y':
            generate_qr_code(password)
    
    print(colored("\nThank you for using SecurePass 3000!", 'cyan', attrs=['bold']))

if __name__ == "__main__":
    main()
