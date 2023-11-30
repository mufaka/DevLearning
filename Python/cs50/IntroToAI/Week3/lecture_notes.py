"""
Week 3 - Optimization    
    Choosing the best option from a set of options

    Algorithms to solve a broad range of problems

        Local Search
            - Maintain a single node and search by moving to neighboring node
                - not a pathfinding algorithm
                - all we care about is what the solution is; find the solution
                    2 types of buildings
                        House
                        Hospital

                            Find a way to place 2 hospitals on map while minimizing distance to every house
                                - Manhattan distance (rows and columns away)
                                - Cost is total distance of all, goal is to minimize

                state-space landscape
                    - list of costs 
                    - find a global maximum (objective function - how good is this state)
                    - find a global minimum (cost function - cost is time / money / distance / etc)

            Current State
                - move to a neighbor state
                    - hill climbing is simplist
                        left or right - pick highest one (for objective function)
                            - once current state is higher than both neighbors, algorithm is done

                function Hill-Climb(problem)
                    current = initial state of the problem (possibly picked randomly)

                    repeat:
                        neighbor = highest valued neighbor of current

                        if neighbor not better than current:
                            return current
                        else
                            current = neighbor

                    Limitation is that it might not find the optimal result because it's blocked by neighbor
                        - parabolic issue -- same as issue with optimizing neural networks (SGD to solve?)
                        - could have a flat local maximum where you would be stuck (more than 3 in a row)
                        - shoulder - flat local maximum but 3

                        Variations of Hill-Climbing
                            steepest-ascent - choose highest value neighbor (described above)
                            stochastic - choose randomly from higher valued neighbors
                            first-choice - choose first highest neighbor (how is this different from first?)

                            All have same potential risk
                            random-restart - conduct hill climbing multiple times

                            local beam search - choose k highest valued neighbors and perform multiples

                    look at hospitals.py in src for examples

                    The root problem with these is that they will never take a step to a worse position so
                    we can't be guaranteed a global min or max

            Simulated Annealing
                start with more random moves and gradually reduce the amount (temperature)

                function Simulated-Annealing(problem, max) -> max times to run annealing
                    current = initial state of problem

                    for t = 1 to max:
                        T = temperature(t) <-- some algorithm to 'cool down'
                        neighbor = random neighbor of current (could be better or worse)

                        Delta E = how much better neighbor is

                        if Delta E is > 0: (better)
                            current = neighbor
                        else:
                            # pick whether or not we'll accept worse neighbor
                            # based on Delta E and T
                                with probability e to the power of delta E / T set current = neighbor

                    return current


            Traveling Salesman Problem
                Find the best route that ends where it started (minimize total distance)
                    NP Complete Problem -> no known efficient way to solve, use approximation instead (like local search)

        Linear Programming
            optimize for some mathematical function
            real number values (decimals)

            - minimize a cost function c1x1 + c2x2 + ... + cnxn 
            - with constraints of form a1x1 + a2x2 + ... + anxn lte b
            - with bounds for each variable li lte xi lte ui

                Example:
                    - two machines x1 and x2
                        x1 is 50/hour
                        x2 is 80/hour
                        goal is to minimize cost
                    - constraints
                        x1 is 5 units of labor per hour
                        x2 is 2 units of labor per hour
                        Total of 20 units of labor to spend
                    - bounds
                        x1 produces 10 units / hour
                        x2 produces 12 units / hour
                        company needs 90 units of output
                    
                Cost Function = 50x1 + 80x2
                    x1 is hours x1 run
                    x2 is hours x2 run

                Constraint = 5x1 + 2x2 lte 20

                Constraint (bounds) = 10x1 + 12x2 gte 90 <--- linear programming usually deals with lte; you can multiply by -1 to achieve that
                                      (-10x1) + (-12x2) lte -90


                    Algorithms to solve these types of problems:
                        - Simplex
                        - Interior-Point

                    look at production.py for an example using scypy

                    result = scipy.optimize.linprog(
                        [50, 80],  # Cost function: 50x_1 + 80x_2
                        A_ub=[[5, 2], [-10, -12]],  # Coefficients for inequalities
                        b_ub=[20, -90],  # Constraints for inequalities: 20 and -90
                    )

            Idea is to look for ways to reduce a problem down to something that we can solve

            Constraint Satisfaction Problem
                Set of variables (x1, x2, ... xn)
                Set of domains for each variable {D1, D2, ..., Dn}
                Set of constraints C


                Student     Classes
                1           A B C
                2           B D E
                3           C E F
                4           E F G

                Exam Slots
                    Monday
                    Tuesday
                    Wednesday

                Try to schedule where each student doesn't take more than 1 exam on a day.

                Exam Slots
                    Monday      A E 
                    Tuesday     B F
                    Wednesday   C G D     

                How to formulate for an algorithm?    

                    Each course is a node.
                        If there is a constraint between two, create an edge between them.
                        This is the constraint graph

                    Variables
                        A B C D E F G
                    
                    Domain
                        Monday Tuesday Wednesday

                    Constraints (derived by student in course)
                        A ne B, A ne C, B ne C, etc ... all the edges for the nodes

            Hard Contstraints
                Must be satisfied in a correct solution

            Soft Constraints
                Express a notion of which solutions are preferred over others
                    
            Unary Constraint
                Constraint that only involves one variable (eg: A can't be on Monday)

            Binary Constraint
                Two variables (used above, A ne B)

        Node Consistency
            All values in a variables domain satisfy unary constraint.

        Arc Consistency
            Satisfy binary constraints. Arc is synonomous with edge.

            Solve as a search problem:

            # csp = constraint satisfaction problem
            function Revise(csp, X, Y):
                revised = false
                for x in X.domain:
                    if no y in Y.domain satisfies constraint for (X,Y):
                        delete x from X.domain
                        revised = true
                
                return revised

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

            This is "massively inefficient" ... so why cover this?

            Use Backtracking Search instead

            function Backtrack(assignment, csp):
                if assignment complete:
                    return assignment
                
                var = Select-Unassigned-Var(assignment, csp)
                for value in Domain-Values(var, assignment, csp):
                    if value consistent with assignment:
                        add {var = value} to assignment
                        result = Backtrack(assignment, csp) <-- recursive
                        if result ≠ failure:
                            return result
                        remove {var = value} from assignment
                
                return failure

            Even better is Maintaining Arc-Consistency backtrack algorithm that
            also uses inference.

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

            Even this can be improved with heuristics:

            Minimum Remaining Values (MRV) is one such heuristic. The idea here is that if a variable’s domain was 
            constricted by inference, and now it has only one value left (or even if it’s two values), then by making 
            his assignment we will reduce the number of backtracks we might need to do later. That is, we will have to 
            make this assignment sooner or later, since it’s inferred from enforcing arc-consistency. If this assignment 
            brings to failure, it is better to find out about it as soon as possible and not backtrack later.            

            The Degree heuristic relies on the degrees of variables, where a degree is how many arcs connect a variable 
            to other variables. By choosing the variable with the highest degree, with one assignment, we constrain multiple 
            other variables, speeding the algorithm’s process.

            Least Constraining Values heuristic, where we select the value that will constrain the least other variables. 
            The idea here is that, while in the degree heuristic we wanted to use the variable that is more likely to 
            constrain other variables, here we want this variable to place the least constraints on other variables. That is, 
            we want to locate what could be the largest potential source of trouble (the variable with the highest degree), 
            and then render it the least troublesome that we can (assign the least constraining value to it).            

"""

def main():
    ...




if __name__ == "__main__":
    main()