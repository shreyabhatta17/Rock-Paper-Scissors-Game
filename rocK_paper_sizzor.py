import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
def play_game():
    options = ["rock", "paper", "scissors"]
    
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit.")
    
    while True:
        # User input
        user_choice = input("\nYour choice: ").lower()
        
        if user_choice == "exit":
            print("Thanks for playing! Goodbye!")
            break
        
        if user_choice not in options:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
       
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")
        
        
        result = determine_winner(user_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    play_game()
