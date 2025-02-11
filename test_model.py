import numpy as np # type: ignore
from tensorflow.keras.utils import to_categorical # type: ignore
from cnn_model import build_cnn_model


def generate_dummy_data(num_samples, input_shape, num_classes):
    """
    Generate dummy data for testing the CNN model.

    Parameters:
        num_samples (int): Number of samples to generate.
        input_shape (tuple): Shape of each input sample.
        num_classes (int): Number of output classes.

    Returns:
        X (np.array): Input data.
        y (np.array): One-hot encoded labels.
    """
    X = np.random.random((num_samples, *input_shape))
    y = np.random.randint(0, num_classes, num_samples)
    y = to_categorical(y, num_classes)
    return X, y


def test_cnn_model():
    """
    Test the CNN model with dummy data.
    """
    # Define parameters
    input_shape = (28, 28, 1)
    num_classes = 2  # number of classes
    num_samples = 100  # Number of dummy samples

    # Generate dummy data
    X, y = generate_dummy_data(num_samples, input_shape, num_classes)

    # Build the model
    model = build_cnn_model(input_shape, num_classes)

    # Train the model on dummy data
    model.fit(X, y, epochs=5, batch_size=10, verbose=1)

    # Evaluate the model
    loss, accuracy = model.evaluate(X, y, verbose=0)
    print(f"Test Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}")


if __name__ == "__main__":
    test_cnn_model()
