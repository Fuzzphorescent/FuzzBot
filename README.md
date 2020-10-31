# FuzzBot 
*Simple Discord bot with miscellaneous functions*

## Features
#### Ping Pong:
+ Returns `pongi` when the message `pingi` is sent in a channel.
+ Returns accurate results for `iphone 12 price`.

#### Forward and Reverse Reaction Roles:
+ Allows a role to be added, and another removed when a specified reaction is made to a designated message.
+ Performs the opposite operation when the reaction is removed.

## Cloning and Execution
+ Clone the repository: git clone https://github.com/Fuzzphorescent/FuzzBot.git
+ `cd FuzzBot`
+ Create a virtual environment: `virtualenv -p python3 venv`
+ Activate the virtual environment: `source venv/bin/activate`
+ `cp src/config.py.example src/config.py`
+ Modify config.py with your bot token, desired message ID, etc. 
+ Run the bot: `python src/FuzzBot.py`