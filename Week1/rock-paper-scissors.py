# # mon fichier : rock-paper-scissors.py
from game import Game

def get_user_menu_choice():
    print("\n--- Main Menu ---")
    print("1. Play a new game")
    print("2. Show scores")
    print("3. Quit")
    choice = input("Enter your choice (1/2/3): ").strip()
    if choice == "1":
        return "play"
    elif choice == "2":
        return "show"
    elif choice == "3":
        return "quit"
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return None

def print_results(results):
    print("\n--- Game Summary ---")
    print(f"Wins: {results.get('win', 0)}")
    print(f"Losses: {results.get('loss', 0)}")
    print(f"Draws: {results.get('draw', 0)}")
    print("Thanks for playing!")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    
    while True:
        choice = get_user_menu_choice()
        if choice == "play":
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == "show":
            print_results(results)
        elif choice == "quit":
            print_results(results)
            break

if __name__ == "__main__":
    main()
