import css.Variables as Variables

"""

"""

def right_box():
    right_box_width = Variables.get_variables("right-box-width")
    return f"""
            2width: {right_box_width};
            """


if __name__ == "__main__":
    print(right_box())