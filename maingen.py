


volume = "V1"

# this script generates a main.tex file that \include's all
# the .tex files in the content folder, in the correct order
# and adding an \part{actN} before each act, where N is the act number

import os
import re
from pathlib import Path
from datetime import datetime
from glob import glob

def main():
    content_path = Path("content")
    main_tex_path = Path("main.tex")

    # Get all .tex files in the content folder
    tex_files = sorted(glob(str(content_path / "*.tex")))

    # Create the main.tex file
    with open(main_tex_path, "w", encoding="utf-8") as main_tex:
        main_tex.write(f"% Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        main_tex.write("\\documentclass{book}\n")
        main_tex.write("\\usepackage[utf8]{inputenc}\n")
        main_tex.write("\\begin{document}\n")

        for tex_file in tex_files:
            act_match = re.search(r'act(\d+)', tex_file)
            if act_match:
                act_number = act_match.group(1)
                main_tex.write(f"\\part{{Act {act_number}}}\n")
            main_tex.write(f"\\input{{{tex_file}}}\n")

        main_tex.write("\\end{document}\n")