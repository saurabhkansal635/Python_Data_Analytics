import re

BACK_SLASH = re.compile("\\\\")

BACK_SLASH.sub('^', "523846348\\/")


def match_numeric_data(input_string):
    numeric_pattern = re.compile(r'^\d+$ | ^\d+\.\d+$ | ^(\d+,)+(\d+)$ | ^(\d+,)+\.(\d+,)$')
    a = numeric_pattern.match(str(input_string))

    if a is not None:
        return a.string
    else:
        return False


match_numeric_data('12/22/2019')
match_numeric_data('63842789')


match_numeric_data('12.222019')

re.match(r'^(\d+)(,\d*)(\.\d+?$)', '806308,50')
re.match(r'^\d+$|^\d*\.\d+$|^(\d+,)+(\d+)$|^(\d+,)*\.(\d+)$', '.945')

a = re.match('(^\d{1,2}[/.-]\d{1,2}[/.-]\d{2,4}$)', '2/22/5449')

# a = re.match('^\d{1,2}$', '333')

if a is not None:
    print(a.string)
else:
    print("Not found")