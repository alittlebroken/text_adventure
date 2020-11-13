# pokehmapton.py A Text adventure game engine
# Paul Lockyer 11th November 2020
# plockyer@googlemail.com

# Imports
from map import Map

class Pokehampton:

    def __init__(self, game_title):
        '''Initiator method for an instance of this class'''

        # Sets the title of the game
        self.title = game_title
        # The main loop for the game
        self.main_loop = True
        # The game loop
        self.game_loop = False
        # Store any messages to be displayed
        self.messages = []
        # Create an instance of the map
        self.world_map = Map()

        # Set the intro for the game
        self.intro = """
        You are Tarvin Blastinton, a mediocre paranormal investigator.
        
        You have heard the rumours of the supposed haunted village of Pokehampton and its strange
        occurrences and disappearances.
        
        You just know that if you could prove just one paranormal occurrence within the village then
        you will no longer be the laughing stock of the paranormal community.
        
        The train you are on slowly comes to a stop at the villages only station. You grab your pack
        from the overhead compartment and step down onto the platform. You pull your coat collar tight to keep
        the nights chilly air at bay and make you way out of the station into the misty car park lot.
        
        This village will be your ruin or your salvation.
        """

    def _show_screen(self):
        '''Shows the main game screen in the terminal'''

        # Show the title screen
        self._show_title()

        # Display any messages
        self._show_messages()

    def _show_help(self):
        '''Show the help screen to the player'''

        self._add_message('The commands that can be run are as follows: ')
        self._add_message('>\tquit')
        self._add_message('>\thelp')

    def _print_header(self, caption):
        '''Prints out a common menu or title screen header'''
        print()
        print("*" * (len(caption) + 4))
        print("  {}  ".format(caption))
        print("*" * (len(caption) + 4))
        print()


    def _show_title(self):
        '''Show the game title'''

        # output the title
        self._print_header(self.title)


    def _main_menu(self):
        '''Display the games main menu'''
        self._print_header('Main Menu')
        print("[N]ew game")
        print("[Q]uit")
        print()

        # Ask the player what they wish to do and then process there response
        choice = input("What would you like to do: ").lower()
        if choice == 'n':
            self.game_loop = True
        else:
            self.main_loop = False


    def _show_messages(self):
        '''Display any messages gathered whilst playing'''

        if self.messages is not None:
            idx = 0
            for idx in range(len(self.messages)):
                print(self.messages[idx])
            self.messages.clear()


    def _add_message(self, message):
        '''Add a message to the internal message list'''
        self.messages.append(message)


    def _show_cli(self):
        '''Show the cli prompt and return back the command chosen by the player'''
        return input(">_: ")


    def _process_cli(self, command):
        '''Processes a command entered on the cli by the player'''
        if command.lower() == "quit":
            self.game_loop = False
        elif command.lower() == "help":
            self._show_help()
        else:
            self._add_message("That command has not been recognised")


    def run(self):
        '''Runs the game'''

        while self.main_loop:

            self._show_title()
            self._main_menu()

            # Display the games introduction
            print(self.intro)

            while self.game_loop:

                self._show_screen()

                # TODO: Display location information
                # TODO: Display fight information
                # TODO: Display help message

                # Get any commands inputted by the player
                cmd = self._show_cli()
                # Now process those commands
                self._process_cli(cmd)


        print("Thanks for playing.")







