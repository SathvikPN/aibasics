import itertools
import random
import copy


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells: set, count: int):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        # raise NotImplementedError
        # {A, B, C} = 3 ==> 3 mines in cells ==> all are mines for sure
        if len(self.cells) == self.count:
            return self.cells
        return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        # raise NotImplementedError
        # {D, E} = 0 ==> 0 mines in set ==> all these cells are safe
        if self.count == 0:
            return self.cells
        return set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        # raise NotImplementedError
        # if cell not in sentence, no action/update required 
        # {A,B,C} = 2 be sentence 
        # if B marked as mine, sentence would be {A,C} = 1
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        # raise NotImplementedError
        # if cell not in sentence, no action/update required 
        # {A,B,C} = 2 be sentence 
        # if A marked as safe, sentence would be {B,C} = 2
        if cell in self.cells:
            self.cells.remove(cell)


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge: list[Sentence] = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # raise NotImplementedError
        # 1) mark the cell as a move that has been made
        self.moves_made.add(cell)

        # 2) mark the cell as safe
        self.mark_safe(cell)

        # 3) add a new sentence to the AI's knowledge base
        # based on the value of `cell` and `count`
        # KB += [set(unvisited neighbours) with count]
        unvisited_cells = set()
        ycell, xcell = cell[0], cell[1]
        for y in range(ycell-1, ycell+1+1):
            for x in range(xcell-1, xcell+1+1):
                if (0 <= y < self.height) and (0 <= x < self.width):
                    # exclude reference cell itself 
                    if (y,x) == cell:
                        continue
                    
                    # Note 1 =========================================================
                    # skip cells that are already inferred safe from knowledge
                    if (y,x) in self.safes:
                        continue
                    # skip cells that are already inferred mines from knowledge
                    if (y,x) in self.mines:
                        count -= 1
                        continue


                    if (y,x) not in self.moves_made:
                        unvisited_cells.add((y,x))

        self.knowledge.append(Sentence(unvisited_cells, count))

        # 4) mark any additional cells as safe or as mines
        # if it can be concluded based on the AI's knowledge base
        # 5) add any new sentences to the AI's knowledge base
        # if they can be inferred from existing knowledge
        
        knowledge_changed = True
        while knowledge_changed:
            knowledge_changed = False
            
            # Check for known safes and known mines in all sentences
            safes = set()
            mines = set()
            for sentence in self.knowledge:
                safes |= sentence.known_safes()
                mines |= sentence.known_mines()
                
            # Mark them globally (this mutates the sentences automatically)
            if safes or mines:
                knowledge_changed = True
                for safe in safes:
                    self.mark_safe(safe)
                for mine in mines:
                    self.mark_mine(mine)
                    
            # Clean up empty sentences that have served their purpose
            empty = Sentence(set(), 0)
            self.knowledge = [s for s in self.knowledge if s != empty]
            
            # Infer new sentences via subsets
            for sentenceA in self.knowledge:
                for sentenceB in self.knowledge:
                    if sentenceA == sentenceB:
                        continue
                        
                    if sentenceA.cells.issubset(sentenceB.cells):
                        inferred = Sentence(
                            sentenceB.cells - sentenceA.cells,
                            sentenceB.count - sentenceA.count
                        )
                        # Only append if it's new and has valid data
                        if inferred not in self.knowledge and len(inferred.cells) > 0:
                            self.knowledge.append(inferred)
                            knowledge_changed = True


    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        # raise NotImplementedError
        for cell in self.safes:
            if cell not in self.moves_made:
                return cell
        return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        choices = []
        for y in range(self.height):
            for x in range(self.width):
                if (y, x) not in self.moves_made and (y, x) not in self.mines:
                    choices.append((y, x))
        
        if choices:
            return random.choice(choices)
        return None
