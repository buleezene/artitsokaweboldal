class Table:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [["" for _ in range(cols)] for _ in range(rows)]

    def set_value(self, row, col, value):
        self.data[row][col] = value

    def draw(self):
        cell_width = 11

        def print_border():
            print("+" + "+".join("-" * cell_width for _ in range(self.cols)) + "+")

        print_border()
        for r in range(self.rows):
            row_text = "|"
            for c in range(self.cols):
                text = str(self.data[r][c])
                row_text += " " + text.ljust(cell_width - 1) + "|"
            print(row_text)
            print_border()


