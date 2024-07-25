
PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt", mode="r") as f:
    for name in f:
        new_name = name.strip()

        with open("./Input/Letters/starting_letter.txt", mode="r") as letter_txt:
            letter = letter_txt.read()
            letter_with_name = letter.replace(PLACEHOLDER, new_name)

        with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as invite_letter:
            invite_letter.write(letter_with_name)
