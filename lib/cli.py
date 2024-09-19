from helpers import (
    exit_program,
    handle_add_player,
    handle_list_coaches,
    handle_list_players,
    handle_update_player,
    handle_delete_player,
    get_players_by_coach
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            handle_add_player()
        elif choice == "2":
            handle_list_players()
        elif choice == "3":
            handle_list_coaches()
        elif choice == "4":
            handle_update_player()
        elif choice == "5":
            handle_delete_player()
        elif choice == "6":
            get_players_by_coach()
        else:
            print("Invalid choice")


def menu():
    print("\nPlease select an option:")
    print("------------------------")
    print("0. Exit the program")
    print("1. Add a player")
    print("2. List all players")
    print("3. List all coaches")
    print("4. Update a player")
    print("5. Delete a player")
    print("6. Players under a coach")


if __name__ == "__main__":
    main()
