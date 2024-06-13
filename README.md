# AUTHOR 
Mark K. kimathi
---

## Introduction

Take a look at the directory structure:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    |------expense_tracker
        ├──__pycache__
        ├──__init__.py
        ├──db.py
        ├──models.py
        ├──utils.py
    ├── models
    │   ├── __init__.py
    │   └── model_1.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```

## Generating Your Environment

You might have noticed in the file structure- there's already a Pipfile!

Install any additional dependencies you know you'll need for your project by
adding them to the `Pipfile`. Then run the commands:

```console
pipenv install
pipenv shell
```

---

## Generating Your CLI

A CLI is, simply put, an interactive script and prompts the user and performs
operations based on user input.

The project template has a sample CLI in `lib/main.py` 
to run the project on the CLI  use 'python lib/main.py'
## Menu Options
1. Create User: Prompts for username, email, and password to create a new user.
2. Delete User: Prompts for a username to delete the corresponding user.
3. Display All Users: Shows a list of all users.
4. Find User by Username: Prompts for a username to find and display the user details.
5. Create Expense: Prompts for username, amount, category, and description to create a new expense.
6. Delete Expense: Prompts for an expense ID to delete the corresponding expense.
7. Display All Expenses: Shows a list of all expenses.
8. Find Expense by ID: Prompts for an expense ID to find and display the expense details.
9. List Expenses for User: Prompts for a username to list all expenses associated with that user.
10. Exit: Exits the application.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for review.

## License
This project is licensed under the MIT License.

## Contact
For any questions or issues, please contact [kithiamark@gmail.com].