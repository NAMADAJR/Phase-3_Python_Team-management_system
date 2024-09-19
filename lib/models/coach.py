# lib/models/coach.py
from models.__init__ import CURSOR, CONN


class Coach:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, experience, id=None):
        self.id = id
        self.name = name
        self.experience = experience

    def __repr__(self):
        return f"<Coach {self.id}: {self.name}, {self.experience}>"

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
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, experience):
        if isinstance(experience, int) and experience >= 0:
            self._experience = experience
        else:
            raise ValueError(
                "Experience must be a non-negative integer"
            )

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Coach instances """
        sql = """
            CREATE TABLE IF NOT EXISTS coaches (
            id INTEGER PRIMARY KEY,
            name TEXT,
            experience INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Coach instances """
        sql = """
            DROP TABLE IF EXISTS coaches;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and experience values of the current Coach instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO coaches (name, experience)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.experience))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, experience):
        """ Initialize a new Coach instance and save the object to the database """
        coach = cls(name, experience)
        coach.save()
        return coach

    def update(self):
        """Update the table row corresponding to the current Coach instance."""
        sql = """
            UPDATE coaches
            SET name = ?, experience = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.experience, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Coach instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM coaches
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Coach object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        coach = cls.all.get(row[0])
        if coach:
            # ensure attributes match row values in case local instance was modified
            coach.name = row[1]
            coach.experience = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            coach = cls(row[1], row[2])
            coach.id = row[0]
            cls.all[coach.id] = coach
        return coach

    @classmethod
    def get_all(cls):
        """Return a list containing a Coach object per row in the table"""
        sql = """
            SELECT *
            FROM coaches
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Coach object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM coaches
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Coach object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM coaches
            WHERE name = ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
