import pandas as pd 
import numpy as np 

# Number variable
x = 8

# String variable
y = 'laura'

# Lists
num = [1, 3, 5, 7]
names = ['jane', 'john', 'jim']

# Dictionary
colors = {
    'firstcolor': 'yellow',
    'secondcolor': 'blue',
    'thirdcolor': 'red',
    'numbers': [200, 300, 400, 500],
    'icecream': {
        'flavor': 'vanilla',
        'conetype': 'waffle',
        'quantity': 11,
        'toppings': 'sprinkles'
    }
}



colors['numbers'][:2]
colors['firstcolor'] + ' ' + colors['thirdcolor']
colors['icecream']['conetype']
colors.keys()
type(colors)

ages = [30, 40, 50, 60, 70]

for x in ages: 
    age_plus10 = x + 10
    print('original age: ', x)
    print('your age in 10 years is: ', age_plus10)