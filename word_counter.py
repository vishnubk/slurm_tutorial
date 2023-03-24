import sys

def word_count(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)

if __name__ == "__main__":
    file_path = sys.argv[1]
    print("Total words in the file:", word_count(file_path))

