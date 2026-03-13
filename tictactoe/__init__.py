from .tictactoe import *

# this init file and imports resolved pylance error of not able reach tictactoe.py methods in runner.py

# Because the directory didn't have an init.py file, 
# Pylance treated the directory as a Namespace Package. 
# A namespace package is just a container for other sub-modules; it doesn't "own" the contents of the files inside it.

# Pylance thought ttt referred to the folder tictactoe/, not the file tictactoe.py 
# Since the folder itself doesn't have an attribute named initial_state, it threw the Pylance(reportAttributeAccessIssue) error.

# adding init.py and imports in there to the tictactoe/ folder, 
# you transformed it from a generic folder into a Regular Python Package.
# 1. "promoted" the contents of tictactoe.py up to the package level
# 2. told Python (and Pylance) that "whenever someone imports the tictactoe package, they should automatically get everything imported at init.py 