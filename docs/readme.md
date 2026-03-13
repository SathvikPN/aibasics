```bash
(venv) degrees (main) % check50 --local ai50/projects/2024/x/degrees
```

general:
- plugin marketplaces in vscode/antigravity donot have verification process [xpost](https://x.com/SathvikPN/status/2032385113192063388?s=20)  
pylance propriatery of MS, not available at antigravity.  
switched back to vscode with verified publisher MS:  
pylance (py language server)
black formatter (py pep guided formatter)

from `degrees`:
- you cannot use a class name as a type hint inside that same class's definition unless you enclose it in quotes (e.g., 'Node') or use a special import.
local checks passed but online checks erred with unable to import Node.
- add spectial import for resolution. ``` from __future__ import annotations ```

from `tictactoe`:
- pylance fails to recognise initial_state(tictactoe.py) at runner.py  
reason: tictactoe folder without init.py is just a namespace package, holder for submodules  
fix: adding init.py (imports within), tictactoe folder is now python module. all init.py imports are available throughout module files.  

- test driven dev. grouped tests for each function.