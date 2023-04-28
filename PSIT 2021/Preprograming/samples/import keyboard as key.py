import keyboard as key
import time as t
import random as r
key.wait('a')
# key.write("In parts of Alaska, it's illegal feed alcohol to a moose. You're subject to fines and/or ")
# t.sleep(5)
# key.write("imprisonment for making \"ugly faces\" at dogs in Oklahoma. In Utah, birds ")
# t.sleep(5)
# key.write("have the right of way on all highways. Christmas was once illegal in England. In Turkey")
# t.sleep(5)
# key.write(", in the sixteenth and seventeenth centuries, anyone caught drinking coffee was put ")
# t.sleep(5)
# key.write("to death. It is illegal to hunt camels In the state of Arizona.")
x = 'In parts of Alaska, it\'s illegal feed alcohol to a moose. You\'re subject to fines and/or imprisonment for making "ugly faces" at dogs in Oklahoma. In Utah, birds have the right of way on all highways. Christmas was once illegal in England. In Turkey, in the sixteenth and seventeenth centuries, anyone caught drinking coffee was put to death. It is illegal to hunt camels In the state of Arizona.'
for i in range(len(x)):
    key.write(x[i])
    t.sleep(r.uniform(0.1, 0.3))