import re
import sys
import logging

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
    except FileNotFoundError:       # Throw error if .ppp file doesn't exist
        end_on_error(f'''The file "{file_name}" doesn't exist''')
    else:
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

def parse_assignment(line, line_index):
    space_index = line.index(" ")
    before_space = line[:space_index]
    after_space = line[space_index + 1:]

    if not(before_space.startswith("[") and before_space.endswith("]")):
        end_on_error(
            f"Assignment target '{before_space}' is not a memory adress",
            line, line_index
        )

    logging.debug(f"target={before_space}, assign {after_space}")

    adress = parse_expression(before_space[1:-1], line, line_index)
    value_to_assign = parse_expression(after_space, line, line_index)
    #logging.debug(f"{memory_adress=}, {value_to_assign=}")
    return adress, value_to_assign

def parse_expression(expr, line, line_index):
    if not(expr.startswith("(") and expr.endswith(")")):
        end_on_error(
            f"Expression '{expr} is not a valid expression. Expressions need `"
            f"to be surrounded by parentheses.",
            line, line_index
        )

    expr_content = expr[1:-1]
    if re.match("^[+-]*$", expr_content):
        binary_string = expr[1:-1]
        binary_string = re.sub("\+", "1", binary_string)
        binary_string = re.sub("\-", "0", binary_string)

        value = int(binary_string, base=2)
    else:
        logging.ERROR("no support yet for compound expressions")
        sys.exit(1)

    return value

logging.basicConfig(level=logging.DEBUG)

memory = [0] * (2**16)
code_lines = load_from_file()
code_lines = clean_input(code_lines)
logging.debug(code_lines)

# TODO size checks
for line_index, this_line in enumerate(code_lines):
    if this_line is None:
        continue
    elif " " in this_line:
        address_to_assign, value_to_assign = parse_assignment(
            this_line, line_index
        )
        memory[address_to_assign] = value_to_assign
    else:
        logging.info(f"skipped line {this_line} for now (not assignment)")

for i, val in enumerate(memory):
    if not val:
        break
    logging.debug(f"{i=}, {val=}")
