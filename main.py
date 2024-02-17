# TODO: Create a letter using starting_letter.txt
PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as invited_names_file:
    lines = invited_names_file.read()
    names = lines.splitlines()

with open("Input/Letters/starting_letter.txt") as starting_letter_file:
    starting_letter = starting_letter_file.read()

# for each name in invited_names.txt
for name in names:
    # Replace the [name] placeholder with the actual name.
    updated_letter = starting_letter.replace(PLACEHOLDER, name)
    # Save the letters in the folder "ReadyToSend".
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(updated_letter)
