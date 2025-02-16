

from openai import OpenAI
import os 
API_KEY_BUILD_NVDIA = os.environ.get("API_KEY_BUILD_NVDIA")

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = API_KEY_BUILD_NVDIA
)
#similar to python function that we send to the model, it is the prompt 
voltage_task = "In a human neuron if you decrease the conductance in the dendrite by 0.01s then what happens to the voltage, will it increase or decrease? " # give me a very short answer just as a number that is either minus one for decrease and plus one for increase.
new_task = voltage_task + "return the result as a plus one or minues one but as a python function"

completion = client.chat.completions.create(
  model="meta/llama-3.3-70b-instruct",
  messages=[{"role":"user","content": new_task }],
  temperature=0.05,
  top_p=0.7,
  max_tokens=4096,
  stream=True
)

code_string_zero = []
for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")
    code_string_zero.append(chunk.choices[0].delta.content)
print(str(code_string_zero))

"".join([code_string_zero])
print(code_string_zero)



print("----------\n")
print("----------\n")


code_string = \
"""
def effect_on_voltage(conductance_decrease):
    if conductance_decrease > 0:
        return -1  # Voltage decreases
    else:
        return 1  # Voltage increases (if conductance increases)

conductance_decrease = 0.01
effect = effect_on_voltage(conductance_decrease)
print("Effect on voltage:", effect)

"""


exec(code_string)



"""
code_string = "def effect_on_voltage(conductance_decrease):" \
    +"if conductance_decrease > 0:"\
    +"return -1  # Voltage decreases"\
    +"else:"\
    +"return 1  # Voltage increases (if conductance increases)"\


    +"conductance_decrease = 0.01"\
    +"effect = effect_on_voltage(conductance_decrease)"
"""






"""

from openai import OpenAI


client = OpenAI()
print("Created client")

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"systems", "content":"You are a biophysics assistant"},
        {"role": "user", "content:": "your task is, if we add 0.01amperes of current to a Calcium channel in dendrite membrane what is the resulting voltage change? answer just a number. if you dont know answer 0. "}


    ]
)

print(completion.choices[0].message)
"""
