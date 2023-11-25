def main():
    ...

'''
Uncertainty / Probability

    Possible events that could happen and the likelihood they will. 

Probability
    Possible Worlds (w: greek omega)
        Each world has a probability of occuring P(w) 

        Axioms
            0 <= P(w) <= 1 
                probability is between 0 and 1 inclusive. 0 is impossible, 1 is certain
            
            Σ = Sigma, summation
            ω = worlds
            ϵ = inclusive
            Ω = all possibilities

            Σ P(w) = 1
            ωϵΩ 
                If you sum up the worlds that are in set of all possible worlds, the value should be 1.
            

    2 6 sided dice probability of sum

        P(sum to 12) = 1/36: only a 6 and a 6
        P(sum to 7) = 6/36 = 1/6: 1/6, 6/1, 2/5, 5/2, 3/4, 4/3


Unconditional Probability
    degree of belief in a proposition in the absence of any other evidence

Conditional Probability
    degree of belief in a proposition given some evidence that has already been revealed.

    P(a | b) = a is what we are testing for, b is the evidence that we are certain about
        What is the probability of a given b?

    P(a | b) = P(a ^ b)  Probability that a and b are true divided by probability that b is true
               -------
                 P(b)

    2 six sided dice example. Rolling a 12

    
    P(sum 12 | one dice is 6) = P(sum 12 ^ 6) (1 / 36)
                               ---------
                                  P(6)   (1 / 6)

                                1 / 36 divided by 1 / 6 is 1 / 6


    P(a ^ b) = P(b)P(a | b)
    P(a ^ b) = P(a)P(b | a)

Random Variable

    a variable in probability theory with a domain of possible
    values it can take on

    Roll (random variable)
    {1,2,3,4,5,6}

    Weather (random variable)
    {sun, cloud, rain, wind, snow}


Probability Distribution

    Takes random variable and gives probability for each of the possible values of the random variable

    Random Variable Flight with possible values of { on-time, delayed, cancelled }
    on-time = .6
    delayed = .3
    cancelled = .1

    P(Flight) = <0.6, 0.3, 0.1> vector

Independence

    the knowledge that one event occurs does not affect the probability of the other event
        eg: first die roll of 6 doesn't change probability of second roll being a 6

    P(a ^ b) = P(a)P(b)

        P (sum 12 ^ 6) = P(sum 12)P(6)
        P(sum 12) = P(sum 12 ^ 6)
                    ------------
                        P(6)


Bayes' Rule (very important rule for inference and probability)

    We know these are true:
    P(a ^ b) = P(b)P(a | b)
    P(a ^ b) = P(a)P(b | a)

    So:
    P(a)P(b | a) = P(b)P(a | b)

    So: (Bayes' Rule)
    P(b | a) = P(b)P(a | b)
               -----------
                  P(a)

    eg:

        AM - Cloudy     PM - Rainy

        Given clouds in the morning, what is the probability of rain in the afternoon

        80% of rainy afternoons start with cloudy mornings                                                                                        
        40% of days have cloudy mornings
        10% of days have rainy afternoons

        a = rain
        b = clouds

        P(rain | clouds) = P(rain)P(clouds | rain)
                           -----------------------
                                P(clouds)

        P(rain | clouds) = (.8)(.1)
                           --------
                              .4

        P(rain | clouds) = .2


Joint Probability
    Multiple events simultaneously        


    C = cloud    C = Not cloud          R = rain       R = not rain
        .4           .6                     .1             .9

    If you have probabilites of both happening, you have joint probability:

                    R = rain       R = not rain
    C = cloud           .08            .32
    C = Not cloud       .02            .58

    P(C | R) = P(C, R)
               -------
                 P(R) <-- normalization constant α

    P(C | R) = αP(C, R)
    P(C | R) = α<.08, .02> <--- distribution doesn't sum to 1 so α needs to be a value that will normalize it

    α = 1 / (.08 + .02) = 10


Negation
    P(not a) = 1 - P(a)

Inclusion-Exclusion
    P(a or b) = P(a) + P(b) - P(A and b)

Marginalization
    P(a) = P(a, b) + P(a, not b) 

    P(X = Xi) = Σ P(X = Xi, Y = Yj)
                j

    j = all values y can take on


                    R = rain       R = not rain
    C = cloud           .08            .32
    C = Not cloud       .02            .58

    P(C = cloud)
    = P(C = cloud, R = rain) + P(C = cloud, R = not rain)
    = .08 + .32

Conditioning
    P(a) = P(a | b)P(b) + P(a | not b)P(not b)


Bayesian Network
    data structure that represents the dependencies among random variables

    directed graph 
        node represents random variable
        arrow from x to y means x is a parent of y
            P(X | Parents(X)) (cause to effect)


            Rain
            {none, light, heavy}  <--- no dependencies 0.7, 0.2, 0.1 
                |           |  
            Maintenance     |
            {yes, no}       |  <-- dependent on rain so conditional probability
                |           |                     R     yes   no
                    Train                         none  0.4   0.6
                    {on time, delayed}            light 0.2   0.8
                            |                     heavy 0.1   0.9
                        Appointment
                        {attend, missed}


            Train conditional probability
            R      M        on time      delayed
            none   yes      0.8          0.2
            none   no       0.9          0.1
            light  yes      0.6          0.4
            light  no       0.7          0.3
            heavy  yes      0.4          0.6
            heavy  no       0.5          0.5

            Appointment conditional probability
            T       attend      miss
            on time 0.9         0.1
            delayed 0.6         0.4


            P(light, no maintenance)
            P(light)P(no | light)

            P(light, no, delayed)
            P(light)P(no | light)P(delayed | light, no)

Inference in a probalistic setting

    Query X: variable for which to compute distribution
    Evidence variables E: observed variables for event e
    Hidden variables Y: non-evidence, non-query variables

    Goal: Calculate P(X | e)


    P(Appointment | light, no)

    Conditional probability is proportional to joint probability
    = alpha P(Appointment, light, no)

    = alpha [P(Appointment, light, no, on time)
            + P(Appointment, light, no, delayed)]

    !!! if you don't have evidence for on-time and delayed, you add the probabilities of each; marginalization
        In this case, one or the other is true so you can include both (shouldn't that distribution equal to, or normalized to, 1 anyways though? --> normalize against all probabilities (alpha) instead )

    P(X | e) = alpha P(X, e) = alpha Σ P(X, e, y)
                                     y

    X is query
    e is evidence
    y ranges over values of hidden variables
    alpha normalizes the result
    
** pomegranate is one of many Bayesian Network libraries for Python, but that one was used in the demo


Approximation Inference
    As the variables increase, use approximation

    Sample randomly from each node
        Rejection sampling is inefficient if the event is unlikely

        Likelihood Weighting
            Start by fixing values for evidence variables
            Sample non-evidence variabls using conditional probabilities
            Weight each sample by likelihood
                probability of all the evidence
            
            P(Rain = Light | train on time)

            Sample only where train on time
                Weight based on probability of other variables

Uncertainty over time

    Xt: Weather at time t (time steps)

    Markov Assumption
        The assumption that the current state depends on only a finite fixed number of previous states
            -- eg: Don't use 365 days of previous weather, use yesterdays, or two or three days instead

    Markov Chain
        A sequence of random variables where the distribution of each variable follows the Markov Assumption

        Transition Model
            Chain together state changes to predict future values

Sensor Models (emission probabilities)

    Hidden State        |   Observation
    robots position         robot's sensor data
    words spoken            audio waveforms
    user engagement         analytics
    weather                 umbrella

    Hidden Markov Model
        a Markov mode for a system with hidden states that generate some
        observed event

        Sensor Markov Assumption
        The assumption that the evidence variable depends only on the corresponding state

        Task                        Definition
        Filtering                   given observations from start until now, calculate distribution for current state
        Prediction                  given observations from start until now, calculate future state
        Smoothing                                                                      past state
        Most likely explanation                                                        most likely sequence of states


''' 


if __name__ == "__main__":
    main()