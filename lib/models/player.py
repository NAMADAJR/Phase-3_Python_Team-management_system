
# lib/models/player.py
from models.__init__ import CURSOR, CONN
from models.coach import Coach


class Player:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, position, coach_id, id=None):
        self.id = id
        self.name = name
        self.position = position
        self.coach_id = coach_id

    def __repr__(self):
        return (
            f"<Player {self.id}: {self.name}, {self.position}, " +
            f"Coach ID: {self.coach_id}>"
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        if isinstance(position, str) and len(position):
            self._position = position
        else:
            raise ValueError(
                "Position must be a non-empty string"
            )

    @property
    def coach_id(self):
        return self._coach_id

    @coach_id.setter
    def coach_id(self, coach_id):
        if type(coach_id) is int and Coach.find_by_id(coach_id):
            self._coach_id = coach_id
        else:
            raise ValueError(
                "coach_id must reference a coach in the database"
            )

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Player instances """
        sql = """
            CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            name TEXT,
            position TEXT,
            coach_id INTEGER,
            FOREIGN KEY (coach_id) REFERENCES coaches(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Player instances """
        sql = """
            DROP TABLE IF EXISTS players;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, position, and coach id values of the current Player object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO players (name, position, coach_id)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.position, self.coach_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Player instance."""
        sql = """
            UPDATE players
            SET name = ?, position = ?, coach_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.position, self.coach_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Player instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM players
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, name, position, coach_id):
        """ Initialize a new Player instance and save the object to the database """
        player = cls(name, position, coach_id)
        player.save()
        return player

    @classmethod
    def instance_from_db(cls, row):
        """Return a Player object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        player = cls.all.get(row[0])
        if player:
            # ensure attributes match row values in case local instance was modified
            player.name = row[1]
            player.position = row[2]
            player.coach_id = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            player = cls(row[1], row[2], row[3])
            player.id = row[0]
            cls.all[player.id] = player
        return player

    @classmethod
    def get_all(cls):
        """Return a list containing one Player object per table row"""
        sql = """
            SELECT *
            FROM players
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Player object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM players
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return Player object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM players
            WHERE name = ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def players_by_coach(cls, coach_id):
        """Return a list of Player objects associated with the specified coach"""
        sql = """
            SELECT *
            FROM players
            WHERE coach_id = ?
        """
        rows = CURSOR.execute(sql, (coach_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
