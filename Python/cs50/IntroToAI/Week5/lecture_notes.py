def main():
    ...
    """
    Neural Networks

    Models computer learning based on human learning

        Neurons are connected to an receive electrical signals from other neurons
        Neurons process input signals and can be activated

    ANN - Artificial Neural Network
        Mathematical model for learning inspired by biological neural networks

        Model mathematical function from inputs to outputs based on the structure and parameters
        of the network

        Allows for learning the network's parameters based on data

    Units/Node/Neuron synonyms

        Unit connected to another unit (input / output)


        h(x1, x2) = rain or not rain
            w0 + w1x1 + w2x2
            w0 = bias
        
        Activation Functions

            step function
                g(x) = 1 if x gte 0, else 0

            logistic sigmoid (s shaped curve / probability)   

                g(x) = e to the power of x
                    -------------------
                        e to the power of x + 1

            ReLu
                g(x) = max(0, x) (if negative, zero otherwise value)

            g(w0 + w1x1 + w2x2) where g is the activation function

        
    Gradient Descent
        Algorithm for minimizing loss when training a neural network

        Which direction should we be moving the weights?

            Start with a random choice of weights

            Repeat:
                Calculate the gradient based on all data points:
                    Direction that will lead to decreasing loss
                
                Update weights according to the gradient (small / dynamic steps in that direction)

            What is the expensive part of the above? "all data points"

    Stochastic Gradient Descent

            Start with a random choice of weights

            Repeat:
                Calculate the gradient based on ONE data point:
                    Direction that will lead to decreasing loss
                
                Update weights according to the gradient (small / dynamic steps in that direction)

            Update all weights based on just one data point; less accurate estimate but much faster

    Mini-Batch Gradient Descent

            Start with a random choice of weights

            Repeat:
                Calculate the gradient based on small batch of data points:
                    Direction that will lead to decreasing loss
                
                Update weights according to the gradient (small / dynamic steps in that direction)

    Limitations - Perceptron
        Binary - only can predict things that are linearly separable


    Multilayer Neural Network
        ANN with input and output layers but one or more hidden layers

        Hidden layer allows for separate boundary decisions

            backpropagation
                start with random choice of weights

                repeat:
                    calculate error for output layer

                    for every layer, starting with output and moving inwards towards
                    the earliest hidden layer:

                        propagate error back one layer

                        update weights

    DNN - Deep Neural Networl
        NN with multiple hidden layers

        If too complex, it could lead to overfitting because it's memorizing rather than generalizing

    Dropout
        temporarily removing units - selected at random - from a neural network to prevent over-reliance on
        certain units

            helps generalize the solution

    TensorFlow - Google
        NN Library

        playground.tensorflow.org - visualize NN


    banknotes example
        import tensorflow as tf

            tf.keras.models.Sequential (keras is a separate API)
                - one layer after another

            Dense layer means all layers connected

            model = tf.keras.models.Sequential()
            model.add(tf.keras.layers.Dense(8, input_shape=(4,), activation="relu"))
            model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

            model.compile(
                optimizer="adam",
                loss="binary_crossentropy",
                metrics=["accuracy"]
            )

            model.fit(X_training, y_training, epochs=20) # trains the model on data and labels (20 times)

            model.evaluate(X_testing, Y_testing, verbose=2)

    computer vision
        CNN - Convolutional Neural Network
            neural networks that use convolution, usually for analyzing images

            1. Apply a number of image filters to image to get feature map
                a. Can train the neural network what the filters should be!
            2. Pooling
                a. max / average pooling. other methods as well
                b. point is to reduce the dimensions for fewer inputs
                    i. makes more resistant to shifts in pixels
            3. Flattening
                a. NN inputs

            NOTE: You could use multiple iterations of step 1 and 2 before flattening.
                  Useful if the resulting feature map is still very large
        

        MNIST - NN inputs lose shape of image

        Image Convolution
            applying a filter that adds each pixel value of an image to its neighbors,
            weighted according to a kernel matrix

            kernel matrix

            0 -1 0
            -1 5 -1
            0 -1 0

            10 20 30 40
            10 20 30 40
            20 30 40 50
            20 30 40 50

            If kernel is 3 x 3, start with first 3 x 3  in image
                multiply corresponding pixels and sum the result


                10 * 0      20 * -1     30 * 0
                10 * -1     20 * 5      30 * -1
                20 * 0      30 * -1     40 * 0

                = 10 

            Slide the 3 x 3 kernel over image. In above example the 3 x 3
            will fit into the 4 x 4 matrix 4 times

                "How many 3 x 3 squares can fit into image"

            NOTE: you can have a different stride length (or jump) for the kernel

            Resulting matrix = Feature Map

            10  20
            40  50


            The following Kernel helps detect differing pixels
            -1  -1  -1
            -1  8   -1
            -1  -1  -1

            eg: assume the following portion of an image

            20  20  20
            20  20  20
            20  20  20

            Applying the kernel results in zero. All the pixels are the same. 

            eg: differing

            20  20  20
            50  50  50
            50  50  50

            Applying the kernel results in 90

            Look at filter.py for example of this using PIL

        Pooling
            reducing the size of an input by sampling each region

            max-pooling
                pooling by choosing the maximum value in each region

            eg:

                30  40  80  90
                20  50  100 110
                0   10  20  30
                10  20  40  30

                2 x 2 max pool

                50  110
                20  40

    Look at handwriting.py for an MNIST solution using CNN with tensorflow
        mnist = tf.keras.datasets.mnist

        tf.keras.layers.Conv2D(
            # 32 different filters, 3 x 3 kernel, relu, 28 x 28 pixel image, 1 channel value (black and white). If rgb, channel would be 3
            32, (3, 3), activation="relu", input_shape=(28, 28, 1)
        )

        # look at 2 x 2 regions and extract max value
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2))

        # flatten into values for input layer
        tf.keras.layers.Flatten()

        # 128 units in hidden layer
        tf.keras.layers.Dense(128, activation="relu")

        # randomly dropout half of hidden layer
        tf.keras.layers.Dropout(0.5)

        # 10 units for output (0 - 9)
        # softmax activation function - turns output into probability distribution
        tf.keras.layers.Dense(10, activation="softmax")


    Feed Forward Neural Network
        Input - Network - Output

        Fixed input and output shape

    RNN - Recurrent Neural Network
        Input - Network - Output -> Input - Network - Output

        Allows network to store state

        Useful for sequential data

        CaptionBot - Microsoft
            - describes images

        One to many relationship between inputs and values

        Input - Network - Output (first word, output to self as input)
                Network - Output (second word, output to self as input)
                Network - Output ( ... )
                Network - Output ( ... )

        Video
            Input - Network
            Input - Network
            Input - Network
            Input - Network (cumulative input from sequence)
            Input - Network - Output
            Input - Network - Output
            Input - Network - Output

        Long Short Term Memory NN (LSTM)

    Adversarial Networks and other types


    """


if __name__ == "__main__":
    main()