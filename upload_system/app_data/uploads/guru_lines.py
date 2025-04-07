
def count_lines(file_name):
    with open(file_name, "r") as file:
        line_count = 0
        for line in file:
            if line != "\n":
                line_count += 1
        return line_count

