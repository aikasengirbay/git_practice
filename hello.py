"""This is a Terminal-based program that allows a user to create and edit a to-do list.

The stub of each function has been provided. Read the docstrings for what each 
function should do and complete the body of the functions below.

You can run the script in your Terminal at any time using the command:

    >>> python todo_list.py

"""

def add_to_list(my_list):
    """Takes user input and adds it as a new item to the end of the list."""
    new_todo_item = raw_input("Add new item: > ")
    new_todo_item  = new_todo_item.title()
    if new_todo_item in my_list:
    	print "This item already in ToDo list"
    else:
		my_list.append(new_todo_item)
    return my_list


def view_list(my_list):
    """Print each item in the list."""
    my_list = sorted(my_list)
    for items in my_list:
        print items



def edit_list(my_list):
    """Gives option to edit/delete items the list"""
    for items in my_list:
        print items
    delete_item = raw_input("which item number in the list you would like remove? ")
    delete_item = my_list.index(delete_item)
    # delete_item = int(delete_item)
 #    if delete_item in my_list:
	# 	my_list.pop(delete_item) 
	# else:
	# 	print "This item is not in ToDo list"
    print my_list



def display_main_menu(my_list):
    """Displays main options, takes in user input, and calls view or add function."""

    user_options = """Would you like to
    A. Add a new item
    B. View list
    C. Quit the program
    D. Edit the list
    >>> """
   

    while True:
        answer = raw_input(user_options)
        answer = answer.upper() 
        # Collect input and include your if/elif/else statements here.
        if answer == "A":
            add_to_list(my_list)  
        elif answer == "B":
            view_list(my_list)
        elif answer == "D":
            edit_list(my_list)
        elif answer == "C":
            break
        else:
        	print "That's not an option"

#-------------------------------------------------

my_list = ["The ToDo List:","Delete","Walk", "Drink", "Eat"]
display_main_menu(my_list)
