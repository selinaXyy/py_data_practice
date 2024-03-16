PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()

with open("./Input/Names/invited_names.txt") as names: #default mode is "r" (read)
    for line in names: #each line in the file
        name = line.strip()
        new_letter = letter.replace(PLACEHOLDER, name) #replaces the placeholder with actually name
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as final_letter: #creates directory if does not exist
            final_letter.write(new_letter) #writes content