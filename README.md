 # Filmify
 ### AUTHOR
 Allan Too
 ## Explanation
 This is a program that is meant to be used in the film industry to track the relationships of films and those who contributed in making them as well as showing the reelationships between them.It is a CLI application that allows users to add,view and remove from the database thus promoting smooth handling of the film data.
### LOGICAL FUNCTIONING 
The programm has a database called Films.db in which the data is stored.It has four tables with the movies table having a one to many with the others as it has foreighn keys from all the other tables.When a user interacts with the program,they are given four options,either to add,list,delete or clear the database.When a user selects add they are given a series of prompts and if their inputs meet the conditions the inputs are updated to the database.When a user selects delete they can specify what exactly what they want to delete and using a select by name method,the element is removed from the database.The clear input completely clears the database.Finally the list option provides the user with a list from the databse showing the relationships between data.
## GETTING STARTED
### PREREQUISITES
 >  Python 3.8 and above.
 >  pipenv
 >  sqlite3
 ### INSTALLATION
 -  Clone this repository
 -  install dependencies using pipenv install and run using pipenv shell
 -  run python3 app.py in the terminal
 ## FUNCTIONALITY
### COMMANDS
 1. ADD -adds to the data in the database using a series of propmpts to the user
 2. List-Provides the user with a lsit of the data in the database showing the relationships between them.The user can choose what they want to be listen making it easier for them
 3. Delete-Provides the user with the ability to choose what to delete as the user can specify what exactly it is they want removed from the database by use of the select by name method
 4. Clear-Provides the user with the ability to clear the whole database in the event of they want to start afresh.
 5. Exit-This is the input that allows the user to leave the loop.
### License
This project is licensed under the MIT License. See the LICENSE.md file for details.
### Acknowledgments
Filmify was supported by resources and documentation from Python SQLite3 Documentation and Pipenv Documentation.
###  Contacts
For inquiries and support,kindly contact the author ,Allan Too at allankipr6@gmail.com
