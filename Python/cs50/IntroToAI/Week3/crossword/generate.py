import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
        constraints; in this case, the length of the word.)

        Given the length and the domain, remove any word from the domain that isn't the unary 
        constraint of length
        """
        for var in self.domains.keys():
            # filter out words that don't match the variables length
            self.domains[var] = set(filter(lambda x: len(x) == var.length, self.domains[var]))

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        
        print(self.domains[x])
        print(self.domains[y])

        x {'START', 'DEPTH', 'GRAPH', 'INFER', 'BAYES', 'ALPHA', 'FALSE', 'PRUNE', 'TRUTH', 'LOGIC'}
        y {'MINIMAX', 'NETWORK', 'BREADTH', 'RESOLVE', 'INITIAL'}        
        """

        # To make x arc consistent with y, you’ll want to remove any value from the domain of x that 
        # does not have a corresponding possible value in the domain of y.
        # so, if any word in x domain has a letter that can't be used in the intersection of y 
        # then it should be removed from x

        # get the overlap positions
        x_o, y_o = self.crossword.overlaps[(x, y)]

        # assume no revisions as default
        revised = False

        # keep an array of words to remove from x domain
        removed_words = []

        # loop through both domains and check the nth letter of each
        for x_word in self.domains[x]:
            # need to check every word in y before decision!
            matched = False
            for y_word in self.domains[y]:
                if x_word[x_o] == y_word[y_o]:
                    matched = True

            if not matched:
                if x_word not in removed_words:
                    removed_words.append(x_word)
                    revised = True

        # print(f"x_o = {x_o}, y_o = {y_o}")
        # print(self.domains[x])
        # print(self.domains[y])

        # remove the words from x domain
        for removed_word in removed_words:
            # print(f"removing word {removed_word}")
            self.domains[x].remove(removed_word)

        # TODO: what if x domain is now empty? maybe check before removing?

        return revised


    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.

        function AC-3(csp):
            queue = all arcs in csp
            while queue non-empty:
                (X, Y) = Dequeue(queue)
                if Revise(csp, X, Y):
                    if size of X.domain == 0:
                        return false
                    
                    for each Z in X.neighbors - {Y}:
                        Enqueue(queue, (Z,X))
            return true

        NOTE: self.crossword.overlaps is a set of arcs
              (Variable(1, 7, 'down', 7), Variable(4, 4, 'across', 5)): (3, 3),
        """

        # arcs are tuples of (x, y) where x and y are variables
        # queue = all arcs in csp
        queue = []

        if arcs == None:
            #for key in self.crossword.overlaps:
                #if self.crossword.overlaps[key] != None:
                    #queue.append(key)
            # need to check domains instead of overlaps...
            for x in self.domains:
                for y in self.crossword.neighbors(x):
                    queue.append((x, y))
        else:
            queue = arcs

        # while queue non-empty:
        while len(queue) > 0:
            # (X, Y) = Dequeue(queue)
            (x, y) = queue.pop()
            
            # if Revise(csp, X, Y):
            if self.revise(x, y):
                # if size of X.domain == 0:
                if len(self.domains[x]) == 0:
                    # return false
                    return False

                # for each Z in X.neighbors - {Y}:
                for z in self.crossword.neighbors(x):
                    if z != y:
                        queue.append((x, z))

        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        # An assignment is a dictionary where the keys are Variable objects and the values 
        #   are strings representing the words those variables will take on.
        # An assignment is complete if every crossword variable is assigned to a value 
        #   (regardless of what that value is).
        # print(f"Assignment Complete? Assignments: {len(assignment.keys())}, Variables: {len(self.crossword.variables)}")
        return len(assignment.keys()) == len(self.crossword.variables)

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        # An assignment is consistent if it satisfies all of the constraints of the problem: 
        # that is to say, all values are distinct, every value is the correct length, and 
        # there are no conflicts between neighboring variables.

        # is the same word used more than once in the assignment?
        # dupe_check = set(filter(lambda x: len(x) > 1, assignment.values())) <-- this didn't work
        # print(len(dupe_check))
        
        dupe_check = []

        # loop through the assignment and check for consistency
        for var in assignment.keys():

            if assignment[var] not in dupe_check:
                dupe_check.append(assignment[var])
            else:
                return False 

            # is the assignment the correct length?
            if var.length != len(assignment[var]):
                return False 
            
            # are there any neighbors we can check?
            for neighbor_var in self.crossword.neighbors(var):
                if neighbor_var in assignment.keys():
                    # get the overlap positions
                    x_o, y_o = self.crossword.overlaps[(var, neighbor_var)]
                    # the characters should match
                    if assignment[var][x_o] != assignment[neighbor_var][y_o]:
                        return False
        
        return True 
            

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        # if assigning var to a particular value results in eliminating n possible 
        # choices for neighboring variables, you should order your results in ascending order of n.

        # least-constraining values dictionary
        lc_values = {}

        # find words in the neighbors
        for word in self.domains[var]:
            lc_values[word] = 0

            for neighbor_var in self.crossword.neighbors[var]:
                if neighbor_var not in assignment.keys():
                    if word in self.domains[neighbor_var]:
                        # TODO: need to also check intersection
                        lc_values[word] = lc_values[word] + 1

        # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value?answertab=scoredesc#tab-top
        # This was also covered in IntroToPython Week 6
        return sorted(lc_values, key=lc_values.get)

    # nested class for keeping track of variable stats
    # used by select_unassigned_variable below
    class VarStat():

        def __init__(obj, var):
            obj._var = var
            obj._neighbor_count = 0
            obj._word_count = 0


        @property
        def var(self):
            return self._var


        @property
        def neighbor_count(self):
            return self._neighbor_count


        @neighbor_count.setter
        def neighbor_count(self, count):
            self._neighbor_count = count


        @property
        def word_count(self):
            return self._word_count
        

        @word_count.setter
        def word_count(self, count):
            self._word_count = count


    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """

        # Your function should return a Variable object. You should return the 
        # variable with the fewest number of remaining values in its domain. 
        # If there is a tie between variables, you should choose among whichever 
        # among those variables has the largest degree (has the most neighbors). 
        # If there is a tie in both cases, you may choose arbitrarily among tied variables.
        best_var_stat = None

        for var in self.crossword.variables:
            if var not in assignment.keys():
                var_stat = CrosswordCreator.VarStat(var)
                var_stat.word_count = len(self.domains[var])
                var_stat.neighbor_count = len(self.crossword.neighbors(var))

                if best_var_stat == None:
                    best_var_stat = var_stat
                else:
                    if var_stat.word_count < best_var_stat.word_count:
                        best_var_stat = var_stat
                    elif (var_stat.word_count == best_var_stat.word_count 
                            and var_stat.neighbor_count > best_var_stat.neighbor_count
                    ):
                        best_var_stat = var_stat 
    
        return best_var_stat.var

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.

        function Backtrack(assignment, csp):
            if assignment complete:
                return assignment
        
            var = Select-Unassigned-Var(assignment, csp)
                for value in Domain-Values(var, assignment, csp):
                    if value consistent with assignment:
                        add {var = value} to assignment
                        inferences = Inference(assignment, csp)
                        if inferences ≠ failure:
                            add inferences to assignment
                        result = Backtrack(assignment, csp)
                        if result ≠ failure:
                            return result
                        remove {var = value} and inferences from assignment
            return failure

        """
        if self.assignment_complete(assignment):
            return assignment
        
        unassigned = self.select_unassigned_variable(assignment)

        if unassigned:
            for word in self.domains[unassigned]:
                # if we assign this word to the unassigned var, is it consistent?
                assignment[unassigned] = word

                if self.consistent(assignment):
                    # skipping inference
                    # recursively add more
                    result = self.backtrack(assignment)

                    if result != None:
                        return result 
                
                assignment.pop(unassigned)

        return None

def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
