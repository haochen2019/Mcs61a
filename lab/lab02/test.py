from lab02 import *
def add1(x):
     return x + 1
def times2(x):
    return x * 2
def add3(x):
    return x + 3
my_cycle = cycle(add1, times2, add3)
identity = my_cycle(0)
identity(5)

add_one_then_double = my_cycle(2)
add_one_then_double(1)

do_all_functions = my_cycle(3)
do_all_functions(2)

do_more_than_a_cycle = my_cycle(4)
do_more_than_a_cycle(2)

do_two_cycles = my_cycle(6)
do_two_cycles(1)