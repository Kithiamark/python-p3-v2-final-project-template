import click
from expense_tracker.db import init_db, SessionLocal
from expense_tracker.models import User, Expense
from expense_tracker.utils import hash_password

def display_menu():
    click.echo("\nExpense Tracker Menu:")
    options = [
        "Create User", "Delete User", "Display All Users",
        "Find User by Username", "Create Expense", "Delete Expense",
        "Display All Expenses", "Find Expense by ID", "List Expenses for User",
        "Exit"
    ]
    for i, option in enumerate(options, 1):
        click.echo(f"{i}. {option}")
    return click.prompt("Enter your choice", type=int, default=1)

def create_user(db):
    username = click.prompt("Enter username")
    email = click.prompt("Enter email")
    password = click.prompt("Enter password", hide_input=True)
    hashed_password = hash_password(password)
    user = User(username=username, email=email, password_hash=hashed_password)
    user.create(db)
    click.echo(f'User {username} created.')

def delete_user(db):
    username = click.prompt("Enter username to delete")
    user = User.find_by_username(db, username)
    if user:
        user.delete(db)
        click.echo(f'User {username} deleted.')
    else:
        click.echo(f'User {username} not found.')

def display_all(db, model):
    for instance in model.get_all(db):
        click.echo(instance)

def find_by_username(db, model):
    username = click.prompt("Enter username to find")
    user = model.find_by_username(db, username)
    click.echo(user if user else f'User {username} not found.')

def create_expense(db):
    username = click.prompt("Enter username for expense")
    user = User.find_by_username(db, username)
    if user:
        amount = click.prompt("Enter amount", type=float)
        category = click.prompt("Enter category")
        description = click.prompt("Enter description (optional)", default="")
        expense = Expense(user_id=user.user_id, amount=amount, category=category, description=description)
        expense.create(db)
        click.echo(f'Expense added for user {username}.')
    else:
        click.echo(f'User {username} not found.')

def delete_expense(db):
    expense_id = click.prompt("Enter expense ID to delete", type=int)
    expense = Expense.find_by_id(db, expense_id)
    if expense:
        expense.delete(db)
        click.echo(f'Expense {expense_id} deleted.')
    else:
        click.echo(f'Expense {expense_id} not found.')

def find_by_id(db, model):
    instance_id = click.prompt(f"Enter {model.__name__.lower()} ID to find", type=int)
    instance = model.find_by_id(db, instance_id)
    click.echo(instance if instance else f'{model.__name__} {instance_id} not found.')

def list_expenses_for_user(db):
    username = click.prompt("Enter username to list expenses")
    user = User.find_by_username(db, username)
    if user:
        for expense in user.expenses:
            click.echo(f'[{expense.expense_date}] {expense.category}: {expense.amount} ({expense.description})')
    else:
        click.echo(f'User {username} not found.')

@click.command()
def cli():
    """Expense Tracker CLI"""
    init_db()
    db = SessionLocal()
    actions = {
        1: lambda: create_user(db),
        2: lambda: delete_user(db),
        3: lambda: display_all(db, User),
        4: lambda: find_by_username(db, User),
        5: lambda: create_expense(db),
        6: lambda: delete_expense(db),
        7: lambda: display_all(db, Expense),
        8: lambda: find_by_id(db, Expense),
        9: lambda: list_expenses_for_user(db),
        10: lambda: click.echo("Goodbye!")
    }
    try:
        while True:
            choice = display_menu()
            if choice == 10:
                break
            actions.get(choice, lambda: click.echo("Invalid choice"))()
    except Exception as e:
        click.echo(f"An error occurred: {e}")
    finally:
        db.close()

if __name__ == '__main__':
    cli()
