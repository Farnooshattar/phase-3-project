import re
import time
import ipdb
from datetime import datetime
from prettycli import red
from simple_term_menu import TerminalMenu
from models import User
from models import Event

# from plyer import notification


class Cli():

    def __init__(self):
        current_user = None

    def start(self):
        self.clear_screen(44)
        # title = "hi"
        # message = "how are you?"
        # notification.notify(
        #     title=title, message=message, app_icon=None, app_name=None, timeout=10, toast=False)
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
                # if (Event.show_first_event(self.id)):
                # ipdb.set_trace()

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
        self.id = user.id
        print(f"Hello, {user.email} 👋")
        self.show_user_options()

    def show_user_options(self):
        options = ["My Events", "New Event",
                   "Edit Event", "Missed Events", "Delete Event", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        # print(options[menu_entry_index])
        if options[menu_entry_index] == "My Events":
            event = Event.find_events_by(self.id)
            if event:
                print(event)
                self.show_user_options()
            else:
                print("you have no events yet, please add events")
                self.show_user_options()
        if options[menu_entry_index] == "New Event":
            title = input("Please enter a title for your event:")
            description = input("Please enter a description for your event:")
            date = input(
                "Please enter a date and time for your event (YYYY-MM-DD HH:MM:SS):")
            try:
                date_time = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                print("Invalid date format. Please use the format: YYYY-MM-DD HH:MM:SS")
                self.show_user_options()
            else:
                Event.add_new_event(self.id, title, description, date_time)
                print("Event added successfully!")
                self.show_user_options()

        if options[menu_entry_index] == "Missed Events":
            missed_events = Event.find_missed_events(self.id)
            if missed_events:
                for event in missed_events:
                    print(event)
            else:
                print("No missed events found.")
            self.show_user_options()

        if options[menu_entry_index] == "Edit Event":
            self.edit_event()

        if options[menu_entry_index] == "Delete Event":
            self.delete_event()

        if options[menu_entry_index] == "Exit":
            self.exit()

    def edit_event(self):
        event_id = int(
            input("Please enter the ID of the event you want to edit: "))
        event = Event.show_first_event(self.id)
        if event:
            title = input("Please enter a new title for the event: ")
            description = input(
                "Please enter a new description for the event: ")
            date = input(
                "Please enter a new date and time for the event (YYYY-MM-DD HH:MM:SS): ")
            try:
                date_time = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                print("Invalid date format. Please use the format: YYYY-MM-DD HH:MM:SS")
            else:
                updated_event = Event.edit_event(
                    event_id, title, description, date_time)
                if updated_event:
                    print("Event updated successfully!")
                else:
                    print("Event not found.")
        else:
            print("No events found.")
        self.show_user_options()

    def delete_event(self):
        event_id = int(
            input("Please enter the ID of the event you want to delete: "))
        event = Event.show_first_event(self.id)
        if event:
            confirm = input(
                f"Are you sure you want to delete event {event_id}? (yes/no): ")
            if confirm.lower() == "yes":
                deleted = Event.delete_event(event_id)
                if deleted:
                    print("Event deleted successfully!")
                else:
                    print("Event not found.")
            else:
                print("Event deletion canceled.")
        else:
            print("No events found.")
        self.show_user_options()

    def exit(self):
        print("Bye!")


app = Cli()
app.start()
