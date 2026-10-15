
import random


# Tool 1: Calculate the result of a basic arithmetic operation.
def calculator():
    print("\n--- Simple Calculator ---")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    operation = input("Choose an operation (+, -, *, /): ")

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("Sorry, you cannot divide by zero.")
            return
        result = first_number / second_number
    else:
        print(f"Sorry, '{operation}' is not a valid operation.")
        return

    print(f"The answer is: {result}")


# Tool 2: Add, view, and remove tasks from a changeable list.
def todo_manager():
    tasks = []

    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter your task: ").strip()

            if task:
                tasks.append(task)
                print(f"Task added: {task}")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(
                        input("Enter the task number to remove: ")
                    )

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Removed task: {removed_task}")
                    else:
                        print("That task number does not exist.")

                except ValueError:
                    print("Please enter a valid whole number.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print(f"'{choice}' is not a valid choice. Try again.")


# Tool 3: Let the user guess a secret number using a loop.
def guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("\n--- Number Guessing Game ---")
    print("I have chosen a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if guess < 1 or guess > 10:
            print("Choose a number between 1 and 10.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(
                f"Congratulations! You guessed {secret_number} "
                f"in {attempts} attempt(s)."
            )
            break


# Main program: Display the menu until the user chooses to quit.
def main():
    print("Welcome to My Personal Mini-Toolkit!")

    while True:
        print("\nPlease choose a tool:")
        print("1. Simple Calculator")
        print("2. To-Do List Manager")
        print("3. Number Guessing Game")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            calculator()
        elif choice == "2":
            todo_manager()
        elif choice == "3":
            guessing_game()
        elif choice == "4":
            print("Thank you for using My Personal Mini-Toolkit!")
            print("Goodbye! Have a wonderful day.")
            break
        else:
            print(f"Sorry, '{choice}' is not on the menu. Please try again.")


if __name__ == "__main__":
    main()
