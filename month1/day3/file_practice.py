import json

notes = [
    "Learn Python",
    "Learn Git",
    "Learn JSON"
]

# convert notes to text file name notes.txt
with open("notes.txt", "w") as file:
    for note in notes:
        file.write(note + "\n")

with open("notes.txt", "r") as file:
    content = file.read()
    print("Content of notes.txt:")
    print(content)