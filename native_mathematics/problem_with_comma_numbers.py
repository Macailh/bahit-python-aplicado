def float_addition_accuracy():
    # Define two floating-point numbers with limited decimal precision
    a = 0.1
    b = 0.2
    
    # Perform addition
    result = a + b
    
    # Print the result
    print("Result of adding 0.1 and 0.2:", result)

def float_representation_issue():
    # Define a floating-point number with problematic representation
    c = 0.1
    
    # Print the representation of c with higher precision
    print("Representation of 0.1 with higher precision:", "{:.25f}".format(c))

if __name__ == "__main__":
    print("Illustrating the problem of floating-point numbers in computers:")

    # Demonstrate the accuracy issue in floating-point addition
    print("\n1. Floating-point addition accuracy:")
    float_addition_accuracy()

    # Demonstrate the representation issue of floating-point numbers
    print("\n2. Floating-point representation issue:")
    float_representation_issue()
