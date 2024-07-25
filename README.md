Code Overview

generate_letters.py
This script reads names from invited_names.txt and replaces the [name] placeholder in starting_letter.txt with each name. The personalized letters are then saved to the ./Output/ReadyToSend/ directory.

Steps:

Read Names: Opens invited_names.txt and reads each name.
Read Template: For each name, opens starting_letter.txt and reads the template letter.
Replace Placeholder: Replaces the [name] placeholder in the template with the current name.
Write Letter: Saves the personalized letter to ./Output/ReadyToSend/ with the filename format letter_for_[name].txt.

Example

If invited_names.txt contains:
Alice
Bob
Charlie

And starting_letter.txt contains:

Dear [name],

You are invited to our event!

Best regards,
Event Organizer


The script will generate:

letter_for_Alice.txt
letter_for_Bob.txt
letter_for_Charlie.txt
Each file will have [name] replaced with the respective name.

