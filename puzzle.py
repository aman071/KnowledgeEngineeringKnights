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
    Or(AKnave,AKnight),                                 #I know that A is a knave or a knight. Not both.
    
    Implication(AKnight, And(AKnave,AKnight)),          #If A is a knight, then A must be both a knave and a knight. Which is what A said.
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnave, AKnight),                                #I know only one of them can be true.
    Or(BKnave, BKnight),                                # I know only one of them can be true.
    
    Implication(AKnight, And(AKnave, BKnave)),          #If A is a knight, then it is true that both are knaves. We know this does not make sense.
    
    Implication(AKnave, Not(And(AKnave, BKnave)))       #If A is knave, then it is not possible that both are knaves, since a knave always lies.
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnave, AKnight),                                #I know only one of them can be true.
    Or(BKnave, BKnight),                                #I know only one of them can be true.

    Biconditional(AKnight, And(AKnight, BKnight)),      #I know that if both are of the same kind, can only be knights. Since knight never lies.
    Implication(AKnave, And(AKnave, BKnight)),          #If A is knave, both are of different kinds. Which means B is a knight.
 
    Biconditional(BKnave, And(BKnave, AKnave)),         #I know if B is lying, then both are same. Which makes B a knave, hence A a knave.
    Implication(BKnight, And(AKnave, BKnight))          #If B is knight, both are different. A can only be a knave.
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnave, AKnight),                                #I know only one of them can be true.
    Or(BKnave, BKnight),                                #I know only one of them can be true.
    Or(CKnave, CKnight),                                # I know only one of them can be true.

    Or(And(BKnight, AKnave), And(BKnave, AKnight)),     #Either B is telling truth, making A a knave. Or B lies, making A a knight.

    Biconditional(BKnight, AKnave),                     #A is a knave iff B is a knight.
    
    Biconditional(BKnight, CKnave),                     #C is a knave iff B is a knight.
    
    And(BKnight, And(AKnave, CKnave)),                  #If B is a knight, then A and C are knaves.
    
    Biconditional(CKnight, AKnight)                     #A is a knight iff C is a knight.

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
