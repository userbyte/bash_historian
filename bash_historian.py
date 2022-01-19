## bash_historian
## 1/19/2022
## Written by userbyte
## Description: Keeps track of the .bash_history file. Generates stats about most used commands, commonly misspelled commands, etc. Runs periodically to create over time statistics.

import os

currentuser = str(os.getlogin())
histfile = f"/home/{currentuser}/.bash_history"

# ILL FINISH THIS SOMETIME IN THE FUTURE MAYBE... LOL