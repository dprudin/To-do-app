FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Reads lines from a file and returns a list of strings"""
    with open(filepath, 'r') as file:
        readfile = file.readlines()
    return readfile


def write_to_file(todos, filepath=FILEPATH):
    """ Writes lines of text to a file from a list argument"""
    with open(filepath, 'w') as file:
        file.writelines(todos)


def print_list():
    """ Prints out the contents of a local file"""
    readfile = get_todos()
    todos = [x.strip("\n") for x in readfile]
    for index, item in enumerate(todos):
        print(f"{index + 1}. {item}")


# Using .index() method to return the index
# def print_list():
#     for item in todos:
#         print(str(todos.index(item) + 1) + ". " + item)

# Another way to display the list using enumerate

if __name__ == "__main__":
    """ if the program is run from this file, then the below code will be execute"""
    print("functions module is running")