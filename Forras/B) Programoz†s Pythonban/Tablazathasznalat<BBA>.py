from TableBBA import Table

t = Table(5, 6)

t.set_value(0, 0, "óra")
t.set_value(0, 1, "hétfő")
t.set_value(0, 2, "kedd")
t.set_value(0, 3, "szerda")
t.set_value(0, 4, "csütörtök")
t.set_value(0, 5, "péntek")

t.set_value(1, 0, "1")
t.set_value(1, 1, "prog.")
t.set_value(1, 2, "ikt.")
t.set_value(1, 3, "prog.")
t.set_value(1, 4, "angol")
t.set_value(1, 5, "prog.")

t.set_value(2, 0, "2")
t.set_value(2, 1, "prog.")
t.set_value(2, 2, "ikt.")
t.set_value(2, 3, "prog.")
t.set_value(2, 4, "angol")
t.set_value(2, 5, "prog.")

t.set_value(3, 0, "3")
t.set_value(3, 1, "prog.")
t.set_value(3, 2, "ikt.")
t.set_value(3, 3, "angol")
t.set_value(3, 4, "ikt.")
t.set_value(3, 5, "prog.")

t.set_value(4, 0, "4")
t.set_value(4, 1, "prog.")
t.set_value(4, 2, "angol")
t.set_value(4, 3, "ikt.")
t.set_value(4, 4, "ikt.")
t.set_value(4, 5, "prog.")

t.draw()
