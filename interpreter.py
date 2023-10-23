import re
import sys

def end_on_error(error_description, line=None, line_pos=None):
    """Ends program on error"""
    if line:
        print(
            f"Error in line {line_pos}: '{line.strip()}'\n{error_description}"
        )
    else:
        print(f"Error: {error_description}")

    sys.exit(1)

def load_from_file():
    try:                    # Get name of .ppp file from command line argument
        file_name = sys.argv[1]
        if not file_name.endswith(".ppp"):
            end_on_error(f'''"{file_name}" is not a .ppp file''')
    except IndexError:
        end_on_error(
            "Please give the .ppp source file to interpret as a"
            "command line argument"
        )
    try:
        with open(file_name, 'r') as f:
            lines = f.readlines()
            # enumerated_lines = enumerate(lines)
    except FileNotFoundError:       # Throw error if .ppp file doesn't exist
        end_on_error(f'''The file "{file_name}" doesn't exist''')
    else:
        # return enumerated_lines
        return lines

def clean_input(lines):
    cleaned_lines = []
    for line in lines:
        clean_line = line

        # remove line ending and other trailing whitespace
        clean_line = clean_line.rstrip()

        # all symbols that plus++ uses, if none of these are used as a first
        # character, the line is assumed to be a comment
        line_is_code = re.match("[+{}()[\]\-]", line[0])
        if line_is_code is None:
            clean_line = None

        cleaned_lines.append(clean_line)

    return cleaned_lines


memory = [0] * (2**16)
code_lines = load_from_file()
code_lines = clean_input(code_lines)
print(code_lines)
