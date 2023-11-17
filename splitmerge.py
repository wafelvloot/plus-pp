import logging
import re
from dataclasses import dataclass

MAX_NUM_SIZE = 1 << 16
START_CHAR = "("
END_CHAR = ")"


@dataclass
class Cell:
    value: int
    action: str


def get_priority(action):
    match action:
        case "*":
            return 2
        case "+" | "-":
            return 1
        case ")":
            return 0
        case _:
            assert False


def cells_can_merge(left_cell, right_cell):
    return (get_priority(left_cell.action) >= get_priority(right_cell.action))


def merge_cells(left_cell, right_cell):
    match left_cell.action:
        case "*":
            left_cell.value *= right_cell.value
        case "+":
            left_cell.value += right_cell.value
        case "-":
            left_cell.value -= right_cell.value

    left_cell.value %= MAX_NUM_SIZE
    left_cell.action = right_cell.action
    return left_cell


def merge(list_to_merge, dest_cell, list_index, merge_one_only=False):
    while (list_index < len(list_to_merge)):
        next_cell = list_to_merge[list_index]
        list_index += 1

        while not cells_can_merge(dest_cell, next_cell):
            next_cell, list_index = merge(
                list_to_merge, next_cell, list_index, merge_one_only=True
            )


        merge_cells(dest_cell, next_cell)

        if merge_one_only:
            return dest_cell, list_index

        # list_index += 1

    return dest_cell, list_index


def merge_whole_expr(list_to_merge):
    expr_val_cell, _ = merge(list_to_merge, list_to_merge[0], 1)
    return expr_val_cell.value


def still_collecting(current_token_str, next_char):
    if current_token_str == "" and next_char == END_CHAR:
        return True

    if is_valid_action(next_char):
        return False

    if next_char == START_CHAR or next_char == END_CHAR:
        return False

    return True


def is_valid_action(char):
    return (char in ["+", "-", "*"])


def not_end_of_expr(expr_str, str_index):
    return str_index < len(expr_str) and expr_str[str_index] != END_CHAR


def update_action(expr_str, str_index, last_char):
    if str_index >= len(expr_str) or expr_str[str_index] == END_CHAR:
        return END_CHAR

    # TODO see below
    assert False


def calculate_expression(expr_str, start_index=0):
    list_to_merge = []
    current_token = ""
    str_index = start_index

    while not_end_of_expr(expr_str, str_index):
        this_char = expr_str[str_index]
        str_index += 1

        if still_collecting(current_token, this_char):
            current_token += this_char

            if not_end_of_expr(expr_str, str_index):
                continue

        # TODO get value after ( if applicable + update action
        this_token_val = int(current_token)
        action_char = (this_char if is_valid_action(this_char)
                       else update_action(expr_str, str_index, this_char))
        list_to_merge.append(Cell(this_token_val, action_char))
        current_token = ""

    return merge_whole_expr(list_to_merge)
