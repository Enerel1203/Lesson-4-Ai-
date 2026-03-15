import random
from colorama import init, Fore, Style

init(autoreset=True)

choices = ["rock", "paper", "scissors"]

player_history = []

def get_player_move():
    while True:
        move = input(Fore.GREEN + "Choose rock, paper, or scissors: ").lower()
        if move in choices:
            return move
        else:
            print(Fore.RED + "Invalid choice! Please try again.")

def ai_move():
    if len(player_history) < 2:
        return random.choice(choices)

    most_common = max(set(player_history), key=player_history.count)

    if most_common == "rock":
        return "paper"
    elif most_common == "paper":
        return "scissors"
    else:
        return "rock"

def determine_winner(player, ai):
    if player == ai:
        return "tie"
    
    if (player == "rock" and ai == "scissors") or \
       (player == "paper" and ai == "rock") or \
       (player == "scissors" and ai == "paper"):
        return "player"
    
    return "ai"

def display_result(player, ai, result, name):
    print(Fore.YELLOW + f"\n{name} chose: {player}")
    print(Fore.CYAN + f"AI chose: {ai}")

    if result == "player":
        print(Fore.GREEN + "You win this round!")
    elif result == "ai":
        print(Fore.RED + "AI wins this round!")
    else:
        print(Fore.MAGENTA + "It's a tie!")

def play_game():
    print(Fore.BLUE + "=== Rock Paper Scissors vs AI ===")
    name = input(Fore.GREEN + "Enter your name: ")

    player_score = 0
    ai_score = 0

    while True:
        player = get_player_move()
        player_history.append(player)

        ai = ai_move()

        result = determine_winner(player, ai)

        display_result(player, ai, result, name)

        if result == "player":
            player_score += 1
        elif result == "ai":
            ai_score += 1

        print(Fore.WHITE + f"\nScore -> {name}: {player_score} | AI: {ai_score}")

        again = input(Fore.GREEN + "\nPlay again? (yes/no): ").lower()

        if again != "yes":
            print(Fore.BLUE + "\nThanks for playing!")
            break

if __name__ == "__main__":
    play_game()