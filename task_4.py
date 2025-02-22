import random
from termcolor import colored

# ASCII Art for Moves
ascii_art = {
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

# Display Welcome Message
def display_welcome():
    banner = """
    =====================================
      Welcome to Rock, Paper, Scissors!
    =====================================
    """
    print(colored(banner, 'cyan', attrs=['bold']))

# Display Menu
def display_menu():
    print("\nChoose a game mode:")
    print("1. Single Round")
    print("2. Best of 3")
    print("3. Best of 5")
    print("4. Exit")

# Get User Choice
def get_user_choice():
    print("\nChoose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = int(input(colored("Enter your choice (1-3): ", 'yellow')))
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    elif choice == 3:
        return "scissors"
    else:
        return None

# Get Computer Choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Determine Winner
def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

# Play a Single Round
def play_round():
    user_choice = get_user_choice()
    if not user_choice:
        print(colored("Invalid choice! Please select again.", 'red'))
        return None, None
    
    computer_choice = get_computer_choice()
    
    print("\nYour move:")
    print(colored(ascii_art[user_choice], 'green'))
    print("Computer's move:")
    print(colored(ascii_art[computer_choice], 'red'))
    
    winner = determine_winner(user_choice, computer_choice)
    if winner == "tie":
        print(colored("It's a tie!", 'blue'))
    elif winner == "user":
        print(colored("You win!", 'green', attrs=['bold']))
    else:
        print(colored("You lose!", 'red', attrs=['bold']))
    
    return winner, computer_choice

# Play Multiple Rounds
def play_game(mode):
    user_score = 0
    computer_score = 0
    rounds = 1 if mode == 1 else 3 if mode == 2 else 5

    for _ in range(rounds):
        print(colored(f"\nRound {_ + 1}/{rounds}", 'cyan', attrs=['bold']))
        winner, _ = play_round()
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        print(colored(f"Score: You {user_score} - {computer_score} Computer", 'yellow', attrs=['bold']))

    print(colored("\nFinal Scoreboard:", 'magenta', attrs=['bold']))
    print(colored(f"You: {user_score} | Computer: {computer_score}", 'green', attrs=['bold']))

    if user_score > computer_score:
        print(colored("Congratulations! You are the overall winner!", 'green', attrs=['bold']))
    elif user_score < computer_score:
        print(colored("Better luck next time. The computer wins!", 'red', attrs=['bold']))
    else:
        print(colored("It's a draw! Both performed equally well!", 'blue', attrs=['bold']))

# Main Function
def main():
    display_welcome()

    while True:
        display_menu()
        mode = int(input(colored("Enter your choice (1-4): ", 'yellow')))
        if mode == 4:
            print(colored("Thank you for playing Rock, Paper, Scissors!", 'cyan', attrs=['bold']))
            break
        elif mode in [1, 2, 3]:
            play_game(mode)
        else:
            print(colored("Invalid choice! Please select a valid option.", 'red'))

if __name__ == "__main__":
    main()
