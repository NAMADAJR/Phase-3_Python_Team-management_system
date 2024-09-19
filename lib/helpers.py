from models.player import Player
from models.coach import Coach

def add_coach(name, experience):
    """Add a new coach to the database."""
    return Coach.create(name, experience)

def add_player(name, position, coach_id):
    """Add a new player to the database, linked to a specific coach."""
    return Player.create(name, position, coach_id)

def get_coach_by_id(coach_id):
    """Retrieve a coach by their ID."""
    return Coach.find_by_id(coach_id)

def get_player_by_id(player_id):
    """Retrieve a player by their ID."""
    return Player.find_by_id(player_id)

def get_players_by_coach(coach_id):
    """Retrieve all players associated with a specific coach."""
    return Player.players_by_coach(coach_id)

def update_coach(coach_id, name=None, experience=None):
    """Update coach information."""
    coach = get_coach_by_id(coach_id)
    if coach:
        if name:
            coach.name = name
        if experience is not None:
            coach.experience = experience
        coach.update()
        return coach
    return None

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

def delete_coach(coach_id):
    """Delete a coach from the database."""
    coach = get_coach_by_id(coach_id)
    if coach:
        coach.delete()
        return True
    return False

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

