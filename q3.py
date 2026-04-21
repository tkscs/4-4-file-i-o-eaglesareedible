import string
# Read "romeo_and_juliet.txt" (The full text of Shakespeare's Romeo and Juliet)
file = open("romeo_and_juliet.txt", "r")
with open("romeo_and_juliet.txt", "r") as f:
    text = f.read()

# Count how many times the word "Juliet" appears
count = 0
x = file.read().split(" ")
for i in x:
    if "Juliet" in i:
        count +=1
print(count)
