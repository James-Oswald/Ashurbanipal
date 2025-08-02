
act = 3
chapters = 22
character = "Ludmila Zahradnik"

# Generate a folder called chapters_templates
# delete all contents in in if it exists
# create files in the folder named aNcM.tex where N is the act number and M is the chapter number
# populate each file with the following chapter header "\chapter{C}" where C is the character name

import os

def create_chapter_files(act, chapters, character):
    folder_name = "chapters_templates"
    
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    else:
        # Clear the folder if it exists
        for filename in os.listdir(folder_name):
            file_path = os.path.join(folder_name, filename)
            if os.path.isfile(file_path):
                os.unlink(file_path)

    # Create chapter files
    for chapter in range(1, chapters + 1):
        file_name = f"a{act}c{chapter}.tex"
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, 'w') as f:
            f.write(f"\\chapter{{{character}}}\n")

# Call the function to create chapter files
create_chapter_files(act, chapters, character)