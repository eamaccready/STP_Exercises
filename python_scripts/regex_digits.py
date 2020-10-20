import re

string = "Arizona 479, 501, 870. California 209, 213, 650"

nums = re.findall("\d", string)

print(nums)
