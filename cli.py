import re
import time
from prettycli import red
from simple_term_menu import TerminalMenu
from models import User
from models import Event


class Cli():

    def __init__(self):
        current_user = None

    def start(self):
        self.clear_screen(44)
        options = ["Login", "SignUp", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Login":
            self.handle_login()
        elif options[menu_entry_index] == "Exit":
            self.exit()
        else:
            self.handle_signup()

    def clear_screen(self, lines):
        print("\n" * lines)

    def handle_login(self):
        email = input("Please enter your email:\n\n")
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, email):
            # print("Find a user by email")
            user = User.find_by(email)
            if user:
                self.current_user = user
                self.id = user.id
                print(f"Hello, {user.email} 👋")
                self.show_user_options()
            else:
                print("user not found, please signup")
                time.sleep(3)
                self.start()
        else:
            print(red("Invalid email. Please try again!"))
            time.sleep(3)
            self.start()

    def handle_signup(self):
        email = input("Please add a new email to sign up")
        user = User.Add_user_by(email)
        self.current_user = user
        print(f"Hello, {user.email} 👋")
        self.show_user_options()

    def show_user_options(self):
        options = ["My Events", "New Event", "Edit My Info", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        # print(options[menu_entry_index])
        if options[menu_entry_index] == "My Events":
            Event.find_events_by(self.id)

    def exit(self):
        print("Bye!")


app = Cli()
app.start()
