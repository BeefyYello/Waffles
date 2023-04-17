Good work getting the repository up to GitHub.

Today we're going to work on a tiny piece of the system: a function that handles reporting a victory message. Right now I've set it to a sample message ("You brought the turtle home safely.").

I'll do my best to minimize the amount of stuff that requires a terminal, but a little bit will indeed be required: it's the best way to run pytest, a system for testing your code, and it's also the best way to make sure that certain software is installed. Please don't hesitate to ask me if you have any trouble at all with this; for me it has been by far the most frustrating part of many of my software projects.

This chunk of work is:

1. Run pytest in the Waffles/ directory. You might need to do the following steps: (a) Make sure pip is installed. You can do this by running "python -m ensurepip --upgrade" in your terminal in the Waffles/ directory. (b) Install Pytest. The instructions are here: https://docs.pytest.org/en/7.1.x/getting-started.html
1. Ensure that the test *fails*.
1. Modify the function in main.py so that it returns something else (anything else). You can think a bit about what you want the victory condition of your game to be; it can be anything.
1. Run pytest again; now the test should *pass*.
1. Push your changes to GitHub (please feel free to use GitHub Desktop or any other software to help with this, and also feel free to ask for help).
