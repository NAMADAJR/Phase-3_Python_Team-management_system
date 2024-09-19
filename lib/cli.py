# lib/cli.py

from helpers import (
    add_coach,
    add_player,
    get_coach_by_id,
    get_player_by_id,
    get_players_by_coach,
    update_coach,
    update_player,
    delete_coach,
    delete_player,
    list_all_coaches,
    list_all_players
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            handle_add_coach()
        elif choice == "2":
            handle_add_player()
        elif choice == "3":
            handle_list_coaches()
        elif choice == "4":
            handle_list_players()
        elif choice == "5":
            handle_update_coach()
        elif choice == "6":
            handle_update_player()
        elif choice == "7":
            handle_delete_coach()
        elif choice == "8":
            handle_delete_player()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add a coach")
    print("2. Add a player")
    print("3. List all coaches")
    print("4. List all players")
    print("5. Update a coach")
    print("6. Update a player")
    print("7. Delete a coach")
    print("8. Delete a player")


def handle_add_coach():
    name = input("Enter coach name: ")
    experience = int(input("Enter years of experience: "))
    coach = add_coach(name, experience)
    print(f"Added coach: {coach}")


def handle_add_player():
    name = input("Enter player name: ")
    position = input("Enter player position: ")
    coach_id = int(input("Enter coach ID: "))
    player = add_player(name, position, coach_id)
    print(f"Added player: {player}")


def handle_list_coaches():
    coaches = list_all_coaches()
    print("List of Coaches:")
    for coach in coaches:
        print(coach)


def handle_list_players():
    players = list_all_players()
    print("List of Players:")
    for player in players:
        print(player)


def handle_update_coach():
    coach_id = int(input("Enter coach ID to update: "))
    name = input("Enter new name (leave blank to keep current): ")
    experience = input("Enter new experience (leave blank to keep current): ")
    experience = int(experience) if experience else None
    updated_coach = update_coach(coach_id, name if name else None, experience)
    if updated_coach:
        print(f"Updated coach: {updated_coach}")
    else:
        print("Coach not found.")


def handle_update_player():
    player_id = int(input("Enter player ID to update: "))
    name = input("Enter new name (leave blank to keep current): ")
    position = input("Enter new position (leave blank to keep current): ")
    coach_id = input("Enter new coach ID (leave blank to keep current): ")
    coach_id = int(coach_id) if coach_id else None
    updated_player = update_player(player_id, name if name else None, position if position else None, coach_id)
    if updated_player:
        print(f"Updated player: {updated_player}")
    else:
        print("Player not found.")


def handle_delete_coach():
    coach_id = int(input("Enter coach ID to delete: "))
    if delete_coach(coach_id):
        print("Coach deleted successfully.")
    else:
        print("Coach not found.")


def handle_delete_player():
    player_id = int(input("Enter player ID to delete: "))
    if delete_player(player_id):
        print("Player deleted successfully.")
    else:
        print("Player not found.")


def exit_program():
    print("Exiting the program. Goodbye!")
    exit()


if __name__ == "__main__":
    main()

