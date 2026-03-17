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

from `maze`:
- heapq.heappush(self.frontier, (f, self.counter, node))  
python maintains the heap invariant by **comparing the elements of the tuple sequentially, from left to right.**  
- 1. The Primary Key: `f` (Total Cost = `g + h`)  
- If `Tuple_A[0] < Tuple_B[0]`, `Tuple_A` wins and bubbles closer to the top of the heap grabbing the lowest `f` cost first.  
- 2. The Tie-Breaker: `self.counter` (Insertion Order)   
- Since `Tuple_A[0] == Tuple_B[0]`, python moves to index `1` of the tuple to break the tie.  
- Index `1` is `self.counter`, an integer that solely tracks the order elements were added.  
- Because `self.counter` strictly increases every time we add a node, it guarantees that **no two items will ever have the same counter value.**  
- If `Tuple_A[1] < Tuple_B[1]`, `Tuple_A` wins (meaning it was added to the queue *before* B). This effectively ensures **FIFO (First-In, First-Out)** behavior among nodes with identical costs.  
- 3. The Prevented Crash: Node object
Why do we even need the counter? Why not just `heapq.heappush(self.frontier, (f, node))`?  
Index `1` would be the custom Node object without `__lt__` (less than) method!  
comparison error `TypeError: '<' not supported between instances of 'Node' and 'Node'`.
- python is famously lazy with tuple comparison; as soon as it finds a definitive difference at index 0 or index 1, it immediately stops comparing and never even glances at the un-comparable Node



`2.5 x 10^6` 
``` 
$x^2$

number^{ax+b}

```

x<sup>sup</sup> 