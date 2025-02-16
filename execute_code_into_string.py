a = -2
b = +2
x = 9

code_string = f"""
def effect_on_voltage(conductance_decrease):
    if conductance_decrease > 0:
        return {a}  # Voltage decreases
    else:
        return {b}  # Voltage increases (if conductance increases)

conductance_decrease = 0.01
effect = effect_on_voltage(conductance_decrease)
print("Effect on voltage:", effect)

"""
"""
def top_k():
    k = x
    for i in range(0,k):
        print(i)
"""
"""

list_of_strings = ['hello', 'goodbye','good day']
for string in list_of_strings:
    my_top_k_program = def top_k():\n    k=2\n    print(k)\ntop_k()
    exec(my_top_k_program)
"""



my_top_k_program = f"""
def top_k():
    k = {x}
    print("{{}}")
    for i in range(0,k):
        print(i)
top_k()
"""

list_of_strings = ['hello', 'goodbye','good day']
for string in list_of_strings:
    my_top_k_program2 = my_top_k_program.format(string)
    try:
        exec(my_top_k_program2)
    except Exception as e:
        print("This is my Exception: " + str(e))
        









#top_k()

#rint(code_string)
