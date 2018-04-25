import math
from auto_simpson import auto_simpson
from auto_trapezium import auto_trap
from Romberg import romberg

simpson=auto_simpson(1,9,math.sqrt)
print(simpson.cal())

trap=auto_trap(1,9,math.sqrt)
print(trap.cal())


rom=romberg(1,9,math.sqrt)
print(rom.cal())