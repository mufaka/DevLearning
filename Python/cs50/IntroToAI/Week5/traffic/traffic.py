import cv2
import numpy as np
import glob
import os
import sys
import tensorflow as tf

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    # sub_dir is the label
    category_dirs = [x[0] for x in os.walk(data_dir)]
    images = []
    labels = []

    for i, category_dir in enumerate(category_dirs):
        # NOTE: os.walk will return the root dir in the first index
        if i > 0:
            # the category is the path name relative to the data directory
            # print(f"Loading images from {category_dir}")
            category = int(os.path.relpath(category_dir, data_dir))

            # use glob to list files; seems easier than os.listfiles or os.walk
            files = glob.glob(f"{category_dir}{os.path.sep}*")

            for file in files:
                img = cv2.imread(file)
                resized_img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
                images.append(resized_img)
                labels.append(category)

    return images, labels


def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    # model = get_mnist_model()
    model = get_modified_model()

    # Train neural network
    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model

def get_mnist_model():
    model = tf.keras.models.Sequential([

        # Convolutional layer. Learn 32 filters using a 3x3 kernel
        tf.keras.layers.Conv2D(
            32, (3, 3), activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
        ),

        # Max-pooling layer, using 2x2 pool size
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

        # Flatten units
        tf.keras.layers.Flatten(),

        # Add a hidden layer with dropout
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dropout(0.5),

        # Add an output layer with output units for all 10 digits
        tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
    ])

    return model 

def get_modified_model():
    model = tf.keras.models.Sequential([

        # Convolutional layer - set kernels to be divisible by shape
        # https://stackoverflow.com/a/48243703/72992 for determining filter size
        # eg: filters should be greater than  3 * 3 * 3 (kernel, 3 channels) 
        tf.keras.layers.Conv2D(
            28, (3, 3), activation="sigmoid", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
        ),

        # Pool the layer, just using example demonstrated in lecture
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

        # Flatten the output for the dense layers
        tf.keras.layers.Flatten(),

        # Add a hidden layer with dropout
        # How to size hidden layer? 900 pixels in image but we've
        # convoluted that using 2 x 2 windows, so 225 data points. use half
        # that number for units? Rounding up to 128 because that is the first power
        # of 2 above the half-way point. There is no rule for this, just a gut feeling it
        # would be more uniform than 114.
        tf.keras.layers.Dense(128, activation="sigmoid"),

        # dropout helps avoid overfitting
        tf.keras.layers.Dropout(0.5),

        # Output layer. Softmax provides probability distribution
        tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
    ])

    return model 

if __name__ == "__main__":
    main()
