import re

text = """Giraffes have arroused the curiosity of __PLURAL_NOUN__
since the earliest times. The giraffe is the tallest of all living
 __PLURAL_NOUN__, but scientists are unable to explain 
how it got its long __BODYPART__.
The giraffe's tremendous height, 
which might reach __NUMBER__ 
__PLURAL_NOUN__, comes from it's legs and __BODYPART__.
"""


def mad_libs(mls):
    """
    :param mls: String wiht parts the
    user should fill out surrounded by
    double underscores in all caps.
    Underscores cannot be inside the hint,
    e.g. no hint_hint_ only __hint__.
    """

    hints = re.findall("__.*?__", mls)

    if hints is not None:
        for word in hints:
            response = "Enter a {}: ".format(word)
            new = input(response)
            mls = mls.replace(word, new, 1)
        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("Invalid mls.")

mad_libs(text)
