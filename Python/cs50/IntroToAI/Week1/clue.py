import termcolor

from logic import *

# define the propositional symbols
mustard = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")

# one of these is the murderer
# mustard or plum or scarlet; mustard v plum v scarlet
characters = [mustard, plum, scarlet]

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")

# one of these is the location
# ballroom v kitchen v library
rooms = [ballroom, kitchen, library]

knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")

# one of these weapons was used
# knife v revolver v wrench
weapons = [knife, revolver, wrench]

# all of the above make up the symbols
symbols = characters + rooms + weapons

def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol): # do I know if this symbol is true?
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)): # do I know if this symbol is not true?
            print(f"{symbol}: MAYBE")

        # else, don't know whether symbol is true or false

# There must be a person, room, and weapon.
knowledge = And(
    Or(mustard, plum, scarlet), # either of these
    Or(ballroom, kitchen, library), # and either of these
    Or(knife, revolver, wrench) # and either of these
)

print(knowledge.formula())
# (ColMustard ∨  ProfPlum ∨  MsScarlet) ∧ (ballroom ∨  kitchen ∨  library) ∧ (knife ∨  revolver ∨  wrench)

# at this point we don't have any clues, just knowledge above
print("No clues, just knowledge")
check_knowledge(knowledge)
"""
ColMustard: MAYBE
ProfPlum: MAYBE
MsScarlet: MAYBE
ballroom: MAYBE
kitchen: MAYBE
library: MAYBE
knife: MAYBE
revolver: MAYBE
wrench: MAYBE
"""

# Initial cards (players cards)
knowledge.add(And(
    Not(mustard), Not(kitchen), Not(revolver)
))

print("And(Not(mustard), Not(kitchen), Not(revolver))")
print(knowledge.formula())
# (ColMustard ∨  ProfPlum ∨  MsScarlet) ∧ (ballroom ∨  kitchen ∨  library) ∧ (knife ∨  revolver ∨  wrench) ∧ ((¬ColMustard) ∧ (¬kitchen) ∧ (¬revolver))
#  ∧ ((¬ColMustard) ∧ (¬kitchen) ∧ (¬revolver)) and not ColMustard and not kitchen, and not revolver

check_knowledge(knowledge)
"""
Above statement eliminates ColMustard, kitchen, and revolver
ProfPlum: MAYBE
MsScarlet: MAYBE
ballroom: MAYBE
library: MAYBE
knife: MAYBE
wrench: MAYBE
"""

# Unknown card (someone guessed scarlet, library, wrench so you know it's not at least one of those)
knowledge.add(Or(
    Not(scarlet), Not(library), Not(wrench)
))

# Known cards
knowledge.add(Not(plum))

print("Not(plum)")
print(knowledge.formula())
# (ColMustard ∨  ProfPlum ∨  MsScarlet) ∧ (ballroom ∨  kitchen ∨  library) ∧ (knife ∨  revolver ∨  wrench) ∧ ((¬ColMustard) ∧ (¬kitchen) ∧ (¬revolver)) ∧ ((¬MsScarlet) ∨  (¬library) ∨  (¬wrench)) ∧ (¬ProfPlum)
check_knowledge(knowledge)
"""
MsScarlet: YES <-- we have Col Mustard and someone showed Prof Plum, so must be Ms Scarlet
ballroom: MAYBE
library: MAYBE
knife: MAYBE
wrench: MAYBE
"""

knowledge.add(Not(ballroom))
print("Not(ballroom)")
# (ColMustard ∨  ProfPlum ∨  MsScarlet) ∧ (ballroom ∨  kitchen ∨  library) ∧ (knife ∨  revolver ∨  wrench) ∧ ((¬ColMustard) ∧ (¬kitchen) ∧ (¬revolver)) ∧ ((¬MsScarlet) ∨  (¬library) ∨  (¬wrench)) ∧ (¬ProfPlum) ∧ (¬ballroom)
print(knowledge.formula())

check_knowledge(knowledge)
"""
MsScarlet: YES
library: YES <-- we have kitchen and someone showed ballroom, so must be library
knife: YES <-- we have revolver, but how did we eliminate wrench?
((¬MsScarlet) ∨  (¬library) ∨  (¬wrench)) <-- Not MsScarlet isn't true and Not library isn't true, so Not wrench must be true. If wrench is true, that leaves knife
"""
