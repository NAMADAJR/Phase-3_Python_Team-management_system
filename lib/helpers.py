from models.player import Player
from models.coach import Coach

def add_player(name, position, coach_id):
    """Add a new player to the database, linked to a specific coach."""
    return Player.create(name, position, coach_id)


def get_player_by_id(player_id):
    """Retrieve a player by their ID."""
    return Player.find_by_id(player_id)


def list_players_by_coach(coach_id):
    """Retrieve all players associated with a specific coach."""
    return Player.players_by_coach(coach_id)

def get_players_by_coach():
    """Prompt user to select a coach and display all players associated with the selected coach."""
    
    # List available coaches
    coaches = list_all_coaches()
    if not coaches:
        print("No coaches available.")
        return
    
    print("Available Coaches:")
    for coach in coaches:
        print(f"{coach.id}: {coach.name} (Experience: {coach.experience})")

    # Get the coach ID input
    coach_id = int(input("Enter the coach ID to view associated players: "))
    
    # Retrieve and display players associated with the selected coach
    players = list_players_by_coach(coach_id)
    if players:
        print(f"\nPlayers under Coach {coach_id}:")
        for player in players:
            print(f"{player.id}: {player.name} - {player.position}")
    else:
        print(f"No players found for Coach ID: {coach_id}")


def update_player(player_id, name=None, position=None, coach_id=None):
    """Update player information."""
    player = get_player_by_id(player_id)
    if player:
        if name:
            player.name = name
        if position:
            player.position = position
        if coach_id:
            player.coach_id = coach_id
        player.update()
        return player
    return None


def delete_player(player_id):
    """Delete a player from the database."""
    player = get_player_by_id(player_id)
    if player:
        player.delete()
        return True
    return False

def list_all_coaches():
    """List all coaches in the database."""
    return Coach.get_all()

def list_all_players():
    """List all players in the database."""
    return Player.get_all()

def handle_add_player():
    name = input("Enter player name: ")
    
    # Display position options
    print("Select a position:")
    positions = ["Goalkeeper", "Defender", "Midfielder", "Forward"]
    for idx, position in enumerate(positions, start=1):
        print(f"{idx}. {position}")
    
    position_choice = int(input("Enter the number of the chosen position: "))
    position = positions[position_choice - 1] if 1 <= position_choice <= len(positions) else None
    
    if not position:
        print("Invalid position selection.")
        return
    
    # List available coaches
    coaches = list_all_coaches()
    if not coaches:
        print("No coaches available. Please add a coach first.")
        return

    print("Available Coaches:")
    for coach in coaches:
        print(f"{coach.id}: {coach.name} (Experience: {coach.experience})")
    
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


def handle_delete_player():
    player_id = int(input("Enter player ID to delete: "))
    if delete_player(player_id):
        print("Player deleted successfully.")
    else:
        print("Player not found.")


def exit_program():
    print("Exiting the program. Goodbye!")
    exit()