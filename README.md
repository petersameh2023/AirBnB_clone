# 0x00. AirBnB clone - The console

## Group Project

This project is a console command interpreter for an AirBnB clone.

## Description

This project is the first step in developing a full web application. This project implements a command interpreter in Python, which allows users to interact with the AirBnB clone's objects via the console.

## our Team nemas:

* Peter Nageub
* Mohamed Maher

## Project Setup

1. Clone the repository: `git clone https://github.com/your-username/AirBnB_clone.git`
2. Navigate into the directory: `cd AirBnB_clone`
3. Run the command interpreter: `./console.py`

## Usage

### Commands

The command interpreter supports the following commands:

* **create**: Creates a new instance of a given class, saves it to the JSON file, and prints the ID.
* **show**: Prints the string representation of an instance based on the class name and ID.
* **destroy**: Deletes an instance based on the class name and ID.
* **all**: Prints the string representation of all instances, optionally filtered by class name.
* **update**: Updates an instance based on the class name and ID by adding or updating an attribute.
* **quit**: Exits the command interpreter.

### Examples

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) 


## Files

* `console.py`: The command interpreter program.
* `models/`: A package containing all model classes (e.g., `base_model.py`, `user.py`, `state.py`, etc.).
* `models/engine/`: A sub-package containing the storage engine (`file_storage.py`).
* `tests/`: A directory containing all unit tests for the project.

## Code Style

The code follows the PEP 8 style guide and is checked with `pycodestyle`.

## Authors

* Peter Nageub
* Mohamed Maher

