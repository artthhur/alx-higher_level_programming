#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5

    from calculator_1 import sub, add, div, mul,

    add_results = add(a, b)
    sub_results = sub(a, b)
    mul_results = mul(a, b)
    div_results = div(a, b)

    print('{} + {} = {}'.format(a, b, add_results))
    print('{} - {} = {}'.format(a, b, sub_results))
    print('{} * {} = {}'.format(a, b, mul_results))
    print('{} / {} = {}'.format(a, b, div_results))
