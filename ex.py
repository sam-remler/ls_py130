def even(number):
    return number % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(even, numbers)
#print(even_numbers.__class__.__name__)
#print(list(even_numbers))     # [2, 4]


#----------------

def select ( callback, list):
    return [item for item in list if callback(item)]

def reject ( callback, list):
    return [item for item in list if not callback(item)]

def reduce(callback, iterable, starting_value):
    accum = starting_value
    for item in iterable:
        accum = callback(item, accum)

    return accum


numbers = (1, 2, 4, 8, 16)
total = lambda number, accum: accum + number
print(reduce(total, numbers, 0))        # 31

numbers = [10, 3, 5]
product = lambda number, accum: accum * number
print(reduce(product, numbers, 2))      # 300

colors = ['red', 'orange', 'yellow', 'green',
          'blue', 'indigo', 'violet']
rainbow = lambda color, accum: accum + color[0].upper()
print(reduce(rainbow, colors, ''))      # ROYGBIV

numbers = [3, 7, 2, 9, 5]
sumsquare = reduce(lambda number, accum: accum + number**2, numbers, 0)
print(sumsquare) # 1 + 4 + 9 = 14