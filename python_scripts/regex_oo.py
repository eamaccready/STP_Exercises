import re

string = "The ghost that says boo haunts the loo."

words = re.findall("\woo", string)

print(words)
