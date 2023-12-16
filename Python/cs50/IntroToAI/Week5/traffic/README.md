## Traffic Approach

Initially, I used the handwriting sample as a basis as that seemed to be a similar problem. Only changes to the Conv2D shape and number of output units were changed. This performed very poorly.

'''
333/333 - 1s - loss: 3.5064 - accuracy: 0.0558 - 968ms/epoch - 3ms/step
'''

This led to looking at documentation and guidance for some of the parameters of the network. I wanted to keep the same approach as the MNIST solution but better parameterize the model to fit the problem. For the convolution the amount of filters and activation were changed. With the MNIST model, it accounted for grayscale images and a single channel whereas this one is RGB (3 channels). It seemed that there would be too much variance in values for a ReLu to work well and a sigmoid would help normalize that better.

'''
tf.keras.layers.Conv2D(
    28, (3, 3), activation="sigmoid", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
),
'''

This resulted in a worse outcome with accuracy in the epochs being no higher than 0.1533 albeit slowly getting better. The testing actually performed better however:

'''
333/333 - 1s - loss: 2.1589 - accuracy: 0.3342 - 1s/epoch - 3ms/step
'''

But this is indicative of luck rather than a good model. I decided to look at the dense layer and how to size the units for that. I figured that I would start with roughly half the amount of units compared to the convolution size of 225. I also wanted to keep the activation function consistent with the convolution layer.

'''
tf.keras.layers.Dense(114, activation="sigmoid"),
'''

This resulted in a HUGE improvement.

'''
333/333 - 1s - loss: 0.0737 - accuracy: 0.9832 - 1s/epoch - 3ms/step
'''

In trying to make the result better, I added another hidden layer thinking that it would give more opportunity for the network to distinguish between images but it led to a slightly worse outcome.

'''
333/333 - 1s - loss: 0.0971 - accuracy: 0.9758 - 1s/epoch - 3ms/step
'''

It turns out that there isn't an agreement on how to size the hidden layers or how many there should be. This seems to be a problem to solve with testing and built up intuition rather than being a black and white science.
https://www.baeldung.com/cs/neural-networks-hidden-layers-criteria
https://stats.stackexchange.com/questions/350718/confused-in-selecting-the-number-of-hidden-layers-and-neurons-in-an-mlp-for-a-bi


Furthermore, it was learned that there are many variables from convolution filters, activation functions, drop-out, and the amount of hidden layers and units that come into play when modeling a Neural Network. There is a lot to learn but there should be a lot of examples of similar problems that can be used as a good starting point. Understanding how the attributes changing changes the results helps in coming up with solutions quicker. 
