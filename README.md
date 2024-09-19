# Football Management System


This is a simple football management system written in Python. The system allows for managing players and coaches, with functionality to add, update, and list players, as well as associate players with specific coaches. The system also supports displaying all players under a selected coach and assigning positions to players.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [License](#license)

## Features

- Add new players to the system with an option to choose a position.
- Players can be assigned to a coach from a list of available coaches.
- List all players and all coaches in the system.
- Update or delete player details.
- Display all players under a selected coach.
- Predefined positions include: Goalkeeper, Defender, Midfielder, and Forward.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.x
- SQLite3 (Python's standard library includes support for SQLite)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/football-management-system.git
   ```
   ```bash
   cd football-management-system
   ```

2. Install dependencies:
   ```bash
    pipenv install
   ``` 
3. Set up the database schema by running the setup.py script:
    ```bash
    python lib/insert_data.py
    ```
## Project Structure
The project is organized as follows:

```bash
lib/
│
├── models/
│   ├── player.py           
│   ├── coach.py            
│   └── __init__.py         
│
├── helpers.py             
├── cli.py                  
└── insert_data.py                
```
### Models
- `Player`: Represents a player with attributes like name, position, and coach.

- `Coach`: Represents a coach with attributes like name and experience.

CLI Interface: The cli.py file provides a command-line interface to interact with the system.

## Usage
To run the football management system, use the following command:
```bash
python lib/cli.py
```
This will launch the command-line interface where you can:
1. Add new players.
2. View a list of all players and coaches.
3. Update or delete players.
4. View players assigned to specific coaches.

Example Flow:
- Add a player to the system:
```bash
Choose a name.
Choose a position (Goalkeeper, Defender, Midfielder, Forward).
Assign the player to a coach.
```

- List all players and coaches:
```bash
View players with details such as their name, position, and coach.
```

- View players by coach:
```bash
Select a coach and display all players associated with that coach.
```

#### Menu Options:
```bash
Please select an option:
0. Exit the program
1. Add a player
2. List all players
3. List all coaches
4. Update a player
5. Delete a player
6. View players by coach
```

### Database Schema
The system uses SQLite for storing player and coach data. Below is an overview of the tables used:

```py
coach:
id: INTEGER PRIMARY KEY
name: TEXT
experience: INTEGER


player:
id: INTEGER PRIMARY KEY
name: TEXT
position: TEXT
coach_id: INTEGER (Foreign key referencing the coaches table)
```
## Contributing
Contributions are welcome! If you'd like to contribute to the project, feel free to submit a pull request or open an issue.

### Steps to contribute:
1. Fork the repository.
2. Create a new branch `git checkout -b feature-branch`.
3. Make your changes and commit them `git commit -m "Add new feature"`.
4. Push to the branch `git push origin feature-branch`.
5. Open a pull request.

## License
MIT License

Copyright (c) [2024] [Namada Junior]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.





