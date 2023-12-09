def main():
    """
    LEARNING

        Supervised Learning
            given a data set of input-output pairs, learn
            a function to map inputs to outputs

            Classification
                map input to discrete category
                human labeled training data

                eg: predict rain
                f(humidity, pressure) = category (rain / no rain) <- real, unknow function

                h(humidity, pressure) = category (hypothesis function)

                Nearest-Neighbor Classification
                    given an input, chooses the class of the nearest data point to that input

                    eg: if you have plotted known data (tagged) a new plot is classified by
                        an existing plot that is the closest to it

                    ??? could you use a vector database to do NNC?

                K-Nearest Neighbor Classification
                    take multiple neighbors (K) and find most common

                    - could be slower

                Linear Regression
                    find a line that separates data in a plot

                    - may not be a line that perfectly represents a classification
                
                    x1 = Humidity
                    x2 = Pressure

                    h(x1, x2) = Rain if W0 + w1x1 + w2x2 gte 0 otherwise No Rain

                        Weight Vector w: (w0, w1, w2)
                        Input Vector x: (1, x1, x2)

                        Dot Product of two vectors means multiply values (w1x1) and add (w1x1 + w2x2, etc)

                        w . x: w0 + w1x1 + w2x2

                        Hypothesis parametized by weights:
                            hw(x) = 1 if w. x gte 0, else 0

                    Perceptron Learning Rule
                        Given a data point (x, y), update each weight according to:
                            wi = wi + a(y - hw(X))) * xi

                            wi = wi + a(actual value - estimate) * xi (a is learning rate)

                    Output
                        Threshold value defines classification a or b, but doesn't show strength/confidence of prediction
                    
                        Logistic Function provides a softer threshold, possible output values are anything between 0 and 1 inclusive (percentage confidence)

                Support Vector Machines
                    maximum margin separator
                        maximizes distance between groups of points


                Choice of strategy depends on data set and testing

            Regression
                learning a function mapping an input point to a continuous value

                    f(advertising budget)
                        f(1200) = 5800
                        f(2800) = 13400
                        f(1800) = 8400

                    h(advertising)

                    find a line that approximates relationship (not separates points)

            How to evaluate function? 

                Evaluating Hypothesis
                    Optimization Problem

                    Loss Function
                        expresses how poorly the hypothesis performs

                        Classification
                            0 / 1 loss function
                                L(actual, predicted) = 0 if actual otherwise 1
                                    goal is to minimize

                        Regression
                            How close to the actual value?

                            L1 loss function
                                L(actual, predicted) = absolute value of actual - predicted; sum across all data points

                            L2 loss function
                                L(actual, predicted) = (actual - predicted) squared
                                    - penalizes more harshly the worse the prediction is

                    Overfitting
                        model fits too closely to a particular data set and may fail to generalize uknown. basically, it's
                        memorization of known data that may not be useful to unknown data.

                        Regularization    
                            cost(h) = loss(h)
                                - this might result in overfitting

                            cost(h) = loss(h) + (Lambda * complexity(h)) (how complicated does the line look; prefer simpler boundary decisions)
                                - need to come up with some balance of cost and complexity

                            penalize the more complex

                        Holdout cross-validation
                            splitting data into a training set and test set
                                train on training set, test on test set

                        
                        k-fold cross-validation
                            split into k different sets and experiment k times
                                eg: split into 10 sets
                                        train on 9 and evaluate on another
                                            repeate with different sets
                                                average the total cost

            scikit-learn
        
        Reinforcement Learning
            Learning from experience
                agent is rewarded or penalized (numerical values)
                    based on that it learns what actions to take in the future


            Agent works in an environment
                Agent gets a state
                    Action
                        Gets new state
                        Gets reward (positive good, negative bad)

            Markov Decision Process
                model for decision-making, representing states, actions, and their rewards

                - set of states
                - set of actions
                - transition model P(s'|s, a)
                - reward function R(s, a, s')

            Q-Learning
                method for learning a function Q(s, a),
                estimate of the value of performing action a in state s
                    how much reward will agent get for doing action a in state s

                - start with Q(s,a) = 0 for all s, a
                - when we have taken an action and receive a reward:
                    - estimate the value of Q(s,a) based on current reward
                        and expected future rewards.
                    - update Q(s,a) to take into account old estimate as was
                        as the new estimate

                    Q(s,a) <-- Q(s, a) = alpha(new value estimate - old value estimate)
                        Alpha of 1 uses only new information
                        How do we get estimates? 

                        Q(s,a) <-- Q(s, a) = alpha(new value estimate - Q(s, a))
                            new value estimate is current reward + future reward estimate

                            future reward estimate is max Q(s', a') (for all possible actions from current state, what is the max reward)
                                optionally another parameter for discounting future rewards
                    
                        Greedy Decision-Making
                            - when in state s, choose action a with highest Q(s, a)
                            - downside is that it might not find the best way

                        Explore vs Exploit
                            Explore other actions even though known reward
                                epsilon-greedy

                                    set epsilon equal to how oftwen we want to move randomly
                                    with prob 1 - epsilon, choose estimated best move
                                    with prob e, choose random move

                Nim
                    piles of objects (1, 3, 5, 7)
                        player removes 1 or more from a row

                    loser takes last object

            Function Approximation
                approximating Q(s,a), often by a functioni
                combining various features, rather than storing
                one value for every state-action pair

                useful when there are a large number of states
                    - possibly approximate based on similar states
        
        Unsupervised Learning
            No labels on data
                clustering
                    organize a set of objects in distinct clusters
                        - genetics
                        - image segmentation
                        - market research
                        - medical imaging
                        - social network analysis

                    k-means clustering
                        divide in k different clusters
                            cluster the data by repeatedly assigning points
                            to clusters and updating those clusters centers
                                

    """


if __name__ == "__main__":
    main()