from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # TODO

    # Game Rule: Either one character, not both ======================
    # Either knight or knave
    Or(AKnight, AKnave), 
    # But cannot be both
    Not(And(AKnight, AKnave)), 

    # Game Rule: Knight always Truth, Knave always Lies =================
    # Knight always tells the truth
    # if AKnight, then sentence should be true
    # Implication(AKnight, And(AKnight, AKnave)), 

    # Knive always tells the lie
    # if AKnave, then sentence should be false
    # Implication(AKnave, Not(And(AKnight, AKnave))), 

    # Both implications can be merged as biconditional 
    # A is Knight IF-and-ONLY-IF sentence is True
    Biconditional(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
    # Game Rule: Either one character, not both ======================
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)), 
    Not(And(BKnight, BKnave)),

    # Puzzle Modelling =========================
    # 1. A says "We are both knaves."
    # A is knight IF-and-ONLY-IF A statement is true 
    Biconditional(AKnight, And(AKnave, BKnave)),

    # 2. B says nothing.
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
    # Game Rule: Either one character, not both ======================
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)), 
    Not(And(BKnight, BKnave)),

    # Puzzle Modelling =========================
    # 1. A says "We are the same kind."
    Biconditional(AKnight, Or(
        And(AKnight, BKnight),
        And(AKnave, BKnave),
    )),

    # 2. B says "We are of different kinds."
    Biconditional(BKnight, Or(
        And(AKnight, BKnave),
        And(AKnave, BKnight),
    ))

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
    # Game Rule: Either one character, not both ======================
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)), 
    Not(And(BKnight, BKnave)),

    # Puzzle Modelling =========================
    # 1. A says either "I am a knight." or "I am a knave.", but you don't know which.
    # A either knight or knave seems like repeating game rule without any new info.
    # But what is true and what was said are two different pieces of data.
    # From game rule, character either knight or knave is always true (tautology)
    # A said it, recording saying of A in formal logic statement lets to infer A said truth
    Biconditional(AKnight, Or(AKnight, AKnave)),

    # 2. B says "A said 'I am a knave'."
    # B is Knight IFF it said truth i.e. if A was Knight
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),

    # 3. B says "C is a knave."
    # B is Knight IFF it said truth i.e. if  C was Knave
    Biconditional(BKnight, CKnave),

    # 4. C says "A is a knight."    
    # C is Knight IFF it said truth i.e. A was Knight
    Biconditional(CKnight, AKnight),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
