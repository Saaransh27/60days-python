#from functions import get_todos , write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_reaction = input("select your function as add, edit, complete, show or exit : ")
    user_reaction = user_reaction.strip()

    if user_reaction.startswith("add"):
        todo = user_reaction[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_reaction.startswith("show"):
        todos = functions.get_todos()

        for index, items in enumerate(todos):
            items = items.strip("\n")
            items = items.title()
            row = f"{index + 1}.{items}"
            print(row)
    elif user_reaction.startswith("edit"):
        try:
            number = int(user_reaction[5:]) - 1

            todos = functions.get_todos()

            todo_new = input("enter new todo : ")
            todos[number] = todo_new + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is invalid.")
            continue

    elif user_reaction.startswith("complete"):
        try:
            number = int(user_reaction[9:])

            todos = functions.get_todos()

            todo_to_remove = todos[number-1].strip("\n")
            todos.pop(number-1)

            functions.write_todos(todos)

            print(f"{todo_to_remove.title()} has been removed form the list")
        except IndexError:
            print("The entered index value does not exist.")
            continue
        except ValueError:
            print("The entered value is invalid.")
    elif user_reaction.startswith("exit"):
        with open('todos.txt' , 'w') as file:
            clean = ()
            file.writelines(clean)

        break
    else:
        print("command not available")

print("bye!")