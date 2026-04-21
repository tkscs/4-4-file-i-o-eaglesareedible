# Read and print the contents of the file "q1.txt"

file = open("q1.txt", "r")
with open("q1.txt", "r") as f:
        text = f.read()
print(file.read())