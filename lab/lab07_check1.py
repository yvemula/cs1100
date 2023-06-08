# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:12:41 2022

@author: Yathin Vemula
"""

def parse_line(inputs):
    inputs_tup=inputs.split('/')
    digits=inputs_tup[-3:]
    del inputs_tup[-3:]
    digits=(' '.join(map(str,digits)))
    digits=digits.split(' ')
    check=''.join(map(str,digits))
    inputs_tup=('/'.join(inputs_tup))
    if check.isdigit():
        final_tup=(int(digits[0]), int(digits[1]), int(digits[2]), inputs_tup)
        print(final_tup)
        return final_tup
    else:
        return None

parse_line("Here is some random text, like 5/4=3./12/3/4")
print(parse_line("Here is some random text, like 5/4=3./12/3/4as"))
print(parse_line("Here is some random text, like 5/4=3./12/412/a/3/4"))
print(parse_line(" Here is some spaces 12/32/4"))
parse_line(" Again some spaces\n/12/12/12")