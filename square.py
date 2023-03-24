import sys

def square(x):
    return x * x

if __name__ == "__main__":
    input_number = int(sys.argv[1])
    result = square(input_number)
    print(f"The square of {input_number} is {result}")

