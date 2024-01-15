AIRBNB PROJECT - THE CONSOLE
INTRODUCTION
The first part of the project that aims at creating a fully working website.
The project clones the airbnb.com website.
The Console creates a command interpreter
to manipulate data without a visual interface.
It is just like Shell. It is perfect for development and debugging.
The Console will:
	create your data model
	manage(create, update, destroy, etc) objects via a console
	/ command interpreter
	store and persist objects to a file(JSON file)

The first piece is to manipulate a powerful storage system.
This storage engine will give us an abstraction between “My object” and
“How they are stored and persisted”.
This means: from your console code(the command interpreter itself) and from
the front-end and RestAPI you will build later,
you won’t have to pay attention(take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage
easily without updating all of your codebase.

OVERVIEW
The user 

# Overview

Welcome to the Airbnb Console Project! This command-line interface (CLI) application is designed to provide users with a streamlined and efficient way to manage Airbnb property listings, reservations, and related tasks. Whether you're a property owner, manager, or Airbnb enthusiast, this console project offers a convenient interface to interact with Airbnb data.

   ```
   git clone https://github.com/yvonnegichovi/AirBnB_clone.git
   ```

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies:
   ```
   cd Airbnb_clone
   npm install
   ```

3. **Run the Command**: Launch the Airbnb Console by running the following command:
   ```
   ./console.py
   ```

4. **Explore Commands**: Familiarize yourself with the available commands by typing `help` in the console.
   ```
   ./console.py
   (hbnb) help quit
   ```

## Contributing

We welcome contributions from the community! If you have ideas for improvements, new features, or bug fixes, please submit an issue or a pull request.

Happy hosting with Airbnb Console Project! 🏡✨
