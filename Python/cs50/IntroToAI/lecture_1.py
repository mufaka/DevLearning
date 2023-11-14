"""
Knowledge
    Reason about information we know to solve problems.

Facts:
    If it didn't rain, Harry visited Hagrid today.
    Harry visted Hagrid or Dumbledore today, but not both.
    Harry visited Dumbledore today.

    Harry did not visit Hagrid today
    It rained today

knowledge-based agents
    agents that reason by operating on internal representations of knowledge
    
sentence
    an assertion about the world in a knowledge representation language

Propositional Logic
    Logic of propositions

    Symbols:
    P - It is raining
    Q - Harry visited Hagrid today
    R - Xxxx

Logical Connectives
    not (dash with line down on right)
    and ^
    or  V
    implication --->
    biconditional <---->

Truth Tables for logical connectives. See lecture notes, make sure to know the symbols and tables and have them accessible.

P           Not P
true        false
false       true

P       Q       P and Q
false   false   false
false   true    false
true    false   false
true    true    true

** logical &, both must be true to evaluate to true


P       Q       P or Q
false   false   false
false   true    true
true    false   true
true    true    true

** logical |, either one must be true to evaluate to true


Implication

P       Q       P --> Q (P implies Q)
false   false   true
false   true    true
true    false   false
true    true    true

** If P is true then Q is also true. 

** Only false case is P true, Q false. Why?
If P(it is raining), Implication(then Q(I will be indoors)). 
P true, Q true so P --> Q is true

If it is raining then I will be indoors, but I am not indoors means the original statement was not true.
P true, Q false so P --> Q is false

When P is false, the implication makes no claim at all so the evaluation of P --> Q is always true.

Biconditional can be read as if, and only if.

P       Q       P <--> Q
false   false   true
false   true    false
true    false   false
true    true    true

** Only true if P and Q are the same



Model
    assignment of a truth value to every propositional symbol (a "possible world")

    P: It is raining
    Q: It is a Tuesday

    {P = true, Q = false}

    If N variables then possible scenarios is 2^N (combinations)


Knowledge Base
    a set of sentences known by a knowledge-based agent. (sentence is defined above; an assertion about the world in a knowledge representation language)    

AI uses information in knowledge-base to draw conclusions about the rest of the world.    

The conclusions are Entailments
    In every model in which sentence α is true, sentence β is also true
    
    If α ⊨ β (α entails β), then in any world where α is true, β is true, too.
    (alpha entails beta)

    α = I know that is a Tuesday in January
    β = I know that it is January

    Ultimately, we want the AI to figure out the entailments; inference.

    If it didn't rain, Harry visited Hagrid today.
    Harry visted Hagrid or Dumbledore today, but not both.
    Harry visited Dumbledore today.

    Inferences:
    Harry did not visit Hagrid today
    It rained today

Inference
    The process of deriving new sentences from old ones.

    
Example:

    P: It is a Tuesday
    Q: It is raining
    R: Harry will go for a run

    KB:
        (P ^ not Q) --> R
        (P and not Q) implies R
        If it is Tuesday and it is not raining then Harry will go for a run.

        If we know P is true and Q is false, we know that R is true.

        
Does KB (Knowledge Base) |= (Entail) α (Alpha)
    Using only information in the knowledge base, can we conclude that α is true?

    
Model Checking (model is some assigment of symbols to truth values)
    To determine if KB |= α
        Enumerate all possible models
        If in every model where KB is true, α is true, then KB entails α otherwise KB does not entail α

Knowledge Engineering
    creating the propositional sentences for inference algorithm

    Code is in Week1 folder. logic.py creates an object model for above.
   
        
Model Checking is not efficient. As number of variables increases, other methods are needed.

Inference Rules (Modus Ponens)

        Premise
    -------------------
        Conclusion


    If it is raining, then Harry is inside.
    It is raining

        It is raining
    -----------------------
        Harry is inside

    
And Elimination

        Harry is friends with Ron and Hermione
    ------------------------------------------------
        Harry is friends with Ron


        alpha and beta
    --------------------------
        alpha

        alpha and beta
    --------------------------
        beta


Double Negation Elimination


    It is not true that Harry did not pass the test
    ----------------------------------------------
    Harry passed the test


        not(not alpha)
    ----------------------
        alpha

    
Implication Elimination

    Translate if/then statements to or statements:

    If it is raining, then harry is inside
    --------------------------------------
    it is not raining or Harry is inside


        alpha --> beta
    ---------------------
        not alpha or beta

Biconditional Elimination

    It is raining if and only if Harry is inside
    --------------------------------------------
    If it is raining, then Harry is inside,
    and if Harry is inside, then it is raining

        alpha <---> beta
    ---------------------------
        (alpha --> beta) and (beta --> alpha)    

        
De Morgan's law (turn and into an or)        

        It is not true that both Harry _and_ Ron
            passed the test
    -------------------------------------------
        Harry did not pass the test 
        _or_ Ron did not pass the test

    
        not(alpha and beta)
    ------------------------------------------
        not alpha or not beta
    

        It is not true that both Harry _or_ Ron
            passed the test
    -------------------------------------------
        Harry did not pass the test 
        _and_ Ron did not pass the test
        

        not(alpha or beta)
    ------------------------------------------
        not alpha and not beta
        

Distributive Property 

        (alpha and (beta or gamma))
    ------------------------------------------
       (alpha and beta) or (alpha and gamma)


        (alpha or (beta and gamma))
    ------------------------------------------
        (alpha or beta) and (alpha or gamma)
        

Theorom Proving (solving as a search problem)
    initial state: starting knowledge base
    actions: inference rules
    transition model: new knowledge base after inference
    goal test: check statement we're trying to prove
    path cost function: number of steps in proof


Resolution

        Complimentary Literals:
        (Ron is in the Great Hall) or (Hermione is in the library)

        Ron is not in the Great Hall
    -----------------------------------
        Hermione is in the library

    Unit Resolution Rule

    P or Q

    not P
    -----
      Q

      
    P or Q1 or Q2 or Q3 or Q4

            not P
    ------------------------
      Q1 or Q2 or Q3 or Q4

      
        (Ron is in the Great Hall) or (Hermione  is in the library)
        (Ron is not in the Great Hall) or (Harry is sleeping)
    --------------------------------------------------------------------
        (Hermione is in the library) or (Harry is sleeping)


        P or Q
        not P or R
    -----------------
        Q or R
    
Clause:
    a disjuntion (or) of literals (things connected with or)

    eg: P or Q or R        


Conjunctive Normal Form: (CNF)
    logical sentence that is a conjunction (and) of clauses

    (a or b or c) and (d or not e) and (f or g)

Conversion to CNF
    1. Eliminate biconditionals (if and only if statements)
        a. turn (a <--> b) into (a --> b) and (b --> a)
    2. Eliminate implications
        a. turn (a --> b) into not a or b
    3. Move not inwards using De Morgan's laws
        a. turn not(a and b) into not a or not b
    4. All that should remain is ands and ors
        a. use distributive law to distribute or wherever possible


    Example
        (P or Q) ---> R
        not(P or Q) or R                eliminate implication
        (not P and not Q) or R          De Morgan's Law
        (not P or R) and (not Q or R)   distributive law


Inference by Resolution
    To determine if KB |= a (knowledge base entails alpha)
        check if (KB not a) is a contradiction
            if so, KB|= a
            otherwise, no entailment

    To determine if KB |= a (knowledge base entails alpha)
        convert (KB and not a) to CNF
        keep checking to see if we can use resolution to produce a new clause (are there contradictory clauses like P and not P)
            if ever we produce the empty clause, we have a contradiction 
            otherwise, no entailment (can't add new clauses and no empty clause)


    Does (a or b) and (not b or c) and (not c) entail a
        (a or b) and (not b or c) and (not c) and (not a) <-- not entailment


First-Order Logic

    Constant Symbol         Predicate Symbol (true or false)
    ---------------         ----------------
    Minerva                 Person
    Pomona                  House
    Horace                  BelongsTo
    Gilderoy
    Gryffindor
    Hufflepuff
    Ravenclaw
    Slytherin

    Person(Minerva)                     Minerva is a person
    House(Gryffindor)                   Gryffindor is a house
    not House(Minerva)                  Minerva is not a house
    BelongsTo(Minerva, Gryffindor)      Minerva belongs to Gryffindor


Universal Quantification
    A should be upside down, means for all x
    Ax. BelongsTo(x, Gryffindor) --> not BelongsTo(x, Hufflepuff) 

        For all objects x
        If x belongs to Gryffindor, x does not belong to Hufflepuff

        Anyone in Gryffindor is not in Hufflepuff

Existential Quantification
    Some variables (at least one) are true.

    E should be backwards
    Ex. House(x) and BelongsTo(Minerva, x)

    There exists an object x such that x is a house and Minerva belongs to x
    (Minerva belongs to a house)

    
    Ax. Person(x) --> (Ey. House(y) and BelongsTo(x, y))

    For all x there is a person that belongs to at least one house.

"""


