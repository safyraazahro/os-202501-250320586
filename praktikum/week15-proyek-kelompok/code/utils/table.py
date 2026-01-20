def print_table(headers, rows):
    col_widths = [len(h) for h in headers]

    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    def line():
        print("+" + "+".join("-" * (w + 2) for w in col_widths) + "+")

    line()
    print("| " + " | ".join(headers[i].ljust(col_widths[i]) for i in range(len(headers))) + " |")
    line()

    for row in rows:
        print("| " + " | ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(row))) + " |")
    line()