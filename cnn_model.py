import tensorflow as tf # type: ignore
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Conv2D, Flatten, Dense, MaxPooling2D, Dropout # type: ignore

def build_cnn_model(input_shape, num_classes):
    """
    Build and return a Convolutional Neural Network (CNN) for maze-solving.

    Parameters:
        input_shape (tuple): The shape of the input data (height, width, channels).
        num_classes (int): The number of output classes.

    Returns:
        model (tf.keras.Model): Compiled CNN model.
    """
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.25),

        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.25),

        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])

    model.compile(optimizer='adam', 
                  loss='categorical_crossentropy', 
                  metrics=['accuracy'])
    return model

if __name__ == "__main__":
    
    input_shape = (28, 28, 1)  # input shape for maze representation
    num_classes = 2  # Binary classification (e.g., solved/unsolved)

    cnn_model = build_cnn_model(input_shape, num_classes)
    cnn_model.summary()