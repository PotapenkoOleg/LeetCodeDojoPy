import collections
import heapq
import math

from heapq import * # type: ignore
from functools import cache

k = 42


def functions_scope():
    global k
    k += 1
    n = 5

    def decrement():
        nonlocal n
        global k
        k = 55
        n -= 1  # Modifies the outer n

    decrement()


functions_scope()


def walrus_operator():
    x = 0
    # The parentheses used to surround an assignment expression are always required
    lst = []
    while (x := x + 1) < 3:
        lst.append(x)


def ranges():
    """
    The range(i, j [, step]) function creates an object that represents a range of integers
    with values from i up to, but not including, j.
    If the starting value is omitted, it’s taken to be zero.
    """

    a = range(5)  # a = 0, 1, 2, 3, 4
    b = range(1, 8)  # b = 1, 2, 3, 4, 5, 6, 7
    c = range(0, 14, 3)  # c = 0, 3, 6, 9, 12
    d = range(8, 1, -1)  # d = 8, 7, 6, 5, 4, 3, 2
    print("ranges")


def consumer(x, y, z, lst=[]):
    lst.append(f'{x}-{y}-{z}')


def iterables():
    letters = list('Dave')  # letters = ['D', 'a', 'v', 'e']

    d = {'x': 1, 'y': 2, 'z': 3}
    consumer(**d)

    # [a, *s, b], (a, *s, b), {a, *s, b}
    # Expansion in a list, tuple, or set literals

    # Any iterable can be expanded when writing out list, tuple, and set literals.
    # This is also done using the star (*).
    items = [1, 2, 3]
    a = [10, *items, 11]  # a = [10, 1, 2, 3, 11]        (list)
    b = (*items, 10, *items)  # b = (1, 2, 3, 10, 1, 2, 3)  (tuple)
    c = {10, 11, *items}  # c = {1, 2, 3, 10, 11}        (set)

    v = 'hello' in 'hello world'

    items = [3, 4, 5]
    d = {}
    d['x'], d['y'], d['z'] = items

    items = [1, 2, 3, 4, 5]
    a, b, *extra = items  # a = 1, b = 2, extra = [3,4,5]
    *extra, a, b = items  # extra = [1,2,3], a = 4, b = 5
    a, *extra, b = items  # a = 1, extra = [2,3,4], b = 5

    datetime = ((5, 19, 2008), (10, 30, "am"))

    (month, *_), (hour, *_) = datetime
    print("iterables")


def sequences():
    """
    A sequence is an iterable container that has a size and allows items
    to be accessed by an integer index starting at 0.
    Examples include strings, lists, and tuples.
    """
    a = [3, 4, 5]
    b = [6, 7]
    c = a + b
    list_a = ['x', 'y'] + ['z', 'z', 'y']  # Result is ['x','y','z','z','y']

    # The s * n operator makes n copies of a sequence.
    # However, these are shallow copies that replicate elements by reference only.
    shallow_copy = c * 3

    a = 'Hello World'
    x = len(a)  # 11
    b = a[4]  # b = 'o'
    cc = a[-1]
    c = a[:5]  # c = 'Hello'
    d = a[6:]  # d = 'World'
    e = a[3:8]  # e = 'lo Wo'
    f = a[-5:]  # f = 'World'

    names = ['Dave', 'Paula', 'Thomas', 'Lewis']
    lb = names[0:2]
    lc = names[2:]
    names[1] = 'Becky'
    names[0:2] = ['Dave', 'Mark', 'Jeff']

    s = [(1, 2, 3), (4, 5, 6)]

    for x, y, z in s:
        p = f'{x}-{y}-{z}'

    s = [(1, 2), (3, 4, 5), (6, 7, 8, 9)]

    for x, y, *extra in s:
        p = f'{x}-{y}-{extra}'

    for *first, x, y in s:
        p = f'{first}-{x}-{y}'

    for x, *middle, y in s:
        p = f'{x}-{middle}-{y}'

    for i, x in enumerate(s):
        p = f'{i}-{x}'

    for i, x in enumerate(s, start=100):
        p = f'{i}-{x}'

    s = [(11, 12), (13, 14, 15), (16, 17, 18, 19)]
    t = [(1, 2), (3, 4, 5), (6, 7, 8, 9)]
    for x, y in zip(s, t):
        p = f'{x}-{y}'
    print("sequences")


def mutable_sequences():
    s = [11, 12, 13, 14, 15, 16, 17, 18, 19]
    # Deletes an element
    del s[-1]

    # Slice assignment
    s[0:2] = [5]

    # Deletes a slice
    del s[0:2]

    # Extended slice assignment
    s[0:6:2] = [6, 3, 2]

    # Deletes an extended slice
    del s[0:6:2]
    print("mutable_sequences")


def comprehensions():
    data = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'MSFT', 'shares': 50, 'price': 45.67},
        {'name': 'HPE', 'shares': 75, 'price': 34.51},
        {'name': 'CAT', 'shares': 60, 'price': 67.89},
        {'name': 'IBM', 'shares': 200, 'price': 95.25}
    ]

    # List comprehension
    list_comprehension = [s['name'] for s in data if s['shares'] > 50]

    # Set comprehension
    set_comprehension = {s['name'] for s in data if s['shares'] > 50}

    # Dictionary comprehension
    # If you specify key:value pairs, you’ll create a dictionary
    dictionary_comprehension = {s['name']: s['price'] for s in data if s['shares'] > 50}

    # Generator expression
    # A generator expression is an object that carries out the same computation as a
    # LIST COMPREHENSION but produces the result iteratively
    generator_expression = (s['name'] for s in data if s['shares'] > 50)
    sum1 = sum((s['shares'] for s in data if s['shares'] > 50))
    sum2 = sum(s['shares'] for s in data if s['shares'] > 50)  # Extra parenthesis removed
    print("comprehensions")


def map_filter_reduce():
    from functools import reduce
    nums = [1, 2, 3, 4, 5]
    map_result = list(map(lambda x: x * x, nums))
    filter_result = list(filter(lambda x: x > 2, nums))
    sum_result = reduce(lambda x, y: x + y, nums)
    product_result = reduce(lambda x, y: x * y, nums, 1)
    print("map_filter_reduce")


def pipes():
    # from toolz import pipe
    # nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # avg = pipe(
    #     nums,
    #     filter(lambda n: n % 2 == 0),
    #     map(lambda n: n * 10),
    #     map(lambda n: n + 5),
    #     lambda n: sum(n) / len(n)
    # )
    print("pipes")


def useful_funcs():
    s = [11, 12, 13, 14, 15, 16, 17, 18, 19]
    # abs(x)
    abs_res = abs(-5)

    # all(s)
    all_res = all(s)
    all_res2 = all(x > 0 for x in s)

    # any(s)
    res = any(s)
    res = any(x > 15 for x in s)

    # enumerate(iter, start=0)
    enumerate_res = dict(enumerate(s, start=100))

    # filter(function, iterable)

    # float([x])
    float_res1 = float('-inf')
    float_res2 = float('inf')
    positive_inf_1 = math.inf
    negative_inf_1 = -math.inf

    # int(x [,base])

    # len(s)
    len_res = len(s)

    # max(s [, args, ...], *, default=obj, key=func)
    max_res1 = max(1, 2, 3)
    max_res2 = max(s, key=lambda x: x ** 4, default=float('-inf'))

    # min(s [, args, ...], *, default=obj, key=func)
    min_res1 = min(1, 2, 3)
    min_res2 = min(s, key=lambda x: x ** 4, default=float('-inf'))

    # next(s [, default])

    # range([start,] stop [, step])

    # reversed(s) # Creates a reverse iterator for a sequence s
    reversed_res = reversed(s)

    # round(x [, n])
    # The round() function implements “banker’s rounding.”
    # If the value being rounded is equally close to two multiples,
    # it is rounded to the nearest even multiple (for example, 0.5 is rounded to 0.0, and 1.5 is rounded to 2.0)

    # floor()
    # returns the floor of x i.e., the largest integer not greater than x
    floor_res1 = math.floor(-23.11)  # -24.0
    floor_res2 = math.floor(300.16)  # 300.0
    floor_res3 = math.floor(300.72)  # 300.0

    # ceil()
    # returns a ceiling value of x i.e., the smallest integer greater than or equal to x
    ceil_res1 = math.ceil(-23.11)  # -23.0
    ceil_res2 = math.ceil(300.16)  # 301.0
    ceil_res3 = math.ceil(300.72)  # 301.0

    # sorted(iterable, *, key=keyfunc, reverse=reverseflag)
    nums = [1, 3, 2]
    nums.sort(reverse=True)

    # str([object])

    # sum(items [,initial])

    # tuple([items])

    # zip([s1 [, s2 [, ... ]]])

    print("useful_funcs")


def copy_and_deepcopy():
    a = [1, 2, [3, 4]]
    b = list(a)  # Create a shallow copy of a

    # Deep copy
    import copy
    a = [1, 2, [3, 4]]
    b = copy.deepcopy(a)

    a = [3, 4, 5]
    b = [a]
    c = 4 * b
    # c = shallow copy
    # [[3, 4, 5], [3, 4, 5], [3, 4, 5], [3, 4, 5]]
    a[0] = -7
    # c = changes visible in copy, because it references
    # [[-7, 4, 5], [-7, 4, 5], [-7, 4, 5], [-7, 4, 5]]

    # deep copy
    a = [3, 4, 5]
    c = [list(a) for _ in range(4)]  # list() makes a copy of a list
    print("copy_and_deepcopy")


def math_funcs():
    positive_inf = float("inf")
    negative_inf = float("-inf")

    positive_inf_1 = math.inf
    negative_inf_1 = -math.inf
    print("math")


def strings():
    """
    str([object]) Type representing a string
    If an object is supplied, a string representation of its value is created by calling its __str__() method.
    This is the same string that you see when you print the object.
    If no argument is given, an empty string is created
    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
    """
    s = "Hello"
    t = "cruel world"

    # Concatenates strings if t is a string
    w = s + t

    # Replicates a string if n is an integer
    w1 = s * 5

    # Returns element i of a string
    w3 = s[0]

    # Returns a slice
    w4 = s[3:5]

    # Returns an extended slice
    w5 = s[0:10:2]

    # Number of elements in s
    w6 = len(s)

    # Converts s to a string usable for a caseless comparison.
    w7 = s.casefold()

    # Counts occurrences of the specified substring sub.
    w8 = s.count("a", 0, len(s))

    # Finds the first occurrence of the specified substring sub.
    w9 = s.find("x", 0, 10)

    # Finds the first occurrence or error in the specified substring sub.
    w10 = s.index("e", 0, 10)

    # Checks whether all characters are alphanumeric.
    w11 = s.isalnum()

    # Checks whether all characters are alphabetic.
    w12 = s.isalpha()

    # Checks whether all characters are digits
    w13 = s.isdigit()

    # Checks whether all characters are lowercase
    w14 = s.islower()

    # Checks whether all characters are numeric
    w15 = s.isnumeric()

    # Checks whether all characters are whitespace.
    w16 = s.isspace()

    # Checks whether all characters are uppercase.
    w17 = s.isupper()

    # Joins a sequence of strings t using a delimiter s.
    w18 = s.join(t)

    # Converts to lowercase.
    w19 = s.lower()

    # Removes leading whitespace or characters supplied in chrs.
    w20 = s.lstrip("H")

    # Replaces a substring.
    w21 = s.replace("H", "h", 1)

    # Finds the last occurrence of a substring.
    w22 = s.rfind("Hell", 0, 10)

    # Splits a string using sep as a delimiter. maxsplit is the maximum number of splits to perform.
    w23 = s.split("l", 5)

    # Splits a string into a list of lines. If keepends is True, trailing newlines are preserved.
    w23 = s.splitlines(keepends=True)

    # Removes leading and trailing whitespace or characters supplied in chrs.
    w24 = s.strip("H")

    print("strings")


def tuples():
    """
    tuple([items]) Type representing a tuple
    If supplied, items is an iterable object that is used to populate the tuple.
    However, if an item is already a tuple, it’s returned unmodified.
    If no argument is given, an empty tuple is returned
    https://docs.python.org/3/library/stdtypes.html#tuples
    """
    s = ("x", "y", "z")
    b = ('a',)
    tuple_a = ()  # 0-tuple (empty tuple)
    tuple_b = ('',)  # 1-tuple (note the trailing comma)
    t = ()
    l = (11, 12, 13, 14, 15, 16, 17, 18, 19)

    # Concatenation if t is a list.
    t1 = t + b

    # Replication if n is an integer.
    t2 = s * 4

    # Returns element i of a s.
    t3 = s[2]

    # Returns a slice.
    t4 = s[0:1]

    # Returns an extended slice.
    t5 = l[1:7:2]

    # Number of elements in s.
    t6 = len(l)

    # Counts occurrences of x in s.
    t7 = s.count("x")

    # Returns the smallest i, where s[i] == x
    t8 = l.index(14, 0, 10)

    print("tuples")


def lists():
    """
    list([items]) Type representing a list
    Items may be any iterable object, the values of which are used to populate the list.
    If items is already a list, a shallow copy is made. If no argument is given, an empty list is returned.
    https://docs.python.org/3/library/stdtypes.html#lists
    """
    names = ['Dave', 'Paula', 'Thomas', 'Lewis']
    letters = list('Dave')  # letters = ['D', 'a', 'v', 'e']
    l0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]

    # Concatenation if t is a list
    l3 = l1 + l2

    # Replication if n is an integer
    l4 = l1 * 3

    # Returns element i of s
    x = l1[2]

    # Returns a slice.
    l5 = l0[2:5]

    # Returns an extended slice
    l6 = l0[2:9:3]

    # Item assignment
    l0[3] = 100

    # Slice assignment
    l0[0:3] = [10]

    # Extended slice assignment
    l0[0:5:2] = [100, 100, 100]

    # Item deletion
    del l0[0]

    # Slice deletion
    del l0[0:3]

    # Extended slice deletion
    del l0[0:100:2]

    # Number of elements in s.
    l7 = len(l0)

    # Appends a new element, x, to the end of s
    l0.append(9)

    # Appends a new list, t, to the end of s
    l0.extend(l1)

    # Counts occurrences of x
    l8 = l0.count(10)

    # Returns the smallest i, where s[i] == x
    l9 = l0.index(9, 2, 10)

    # Inserts x at index i
    l10 = l0.insert(42, 3)

    # Returns the element i and removes it from the list
    l11 = l0.pop(3)  # 3 = index

    # Searches for x and removes it from s
    l12 = l0.remove(9)  # 9 = value

    # Reverses items of s in place
    l0.reverse()

    # Sorts items of s in place. a key is a key function
    l0.sort(key=lambda k0: k0, reverse=True)


def sets():
    """
    set([items]) Type representing a set
    The items must be immutable.
    If an item contains other sets, those sets must be of type frozenset.
    If an item is omitted, an empty set is returned.
    https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
    """
    names = set()
    frozen_names = frozenset(['IBM', 'MSFT', 'AA'])
    names1 = {'IBM', 'MSFT', 'AA'}

    s = {1, 2, 3, 4, 5}
    t = {4, 5, 6, 7, 8, 9}
    
    # Check if Sets are equal
    eq = s == t

    # Union of s and t
    s1 = s & t

    # Intersection of s and t
    s2 = s - t

    # Set difference (items in s, not in t)
    s3 = s ^ t

    # Symmetric difference (items not in both s or t)
    s0 = s | t

    # Symmetric difference (items not in both s or t)
    s5 = {s for s in t}

    # The difference between remove() and discard() is that
    # discard() doesn't raise an exception if the item isn’t present.
    s6 = t.remove(9)
    s7 = t.discard(9)

    # Returns a number of items in s.
    s8 = len(s)

    # Adds item to s. Has no effect if the item is already in s
    s9 = s.add(9)

    # Removes all items from s
    s10 = names1.clear()

    # Makes a copy of s
    s11 = s.copy()

    # Set difference. Returns all the items in s, but not in t
    s12 = s.difference(t)

    # Removes all the items from s that are also in t
    s13 = s.difference_update(t)

    # Removes item from s. If an item is not a member of s, nothing happens
    s14 = s.discard(50)

    # Intersection. Returns all the items that are both in s and in t
    s15 = s.intersection(t)

    # Computes the intersection of s and t and leaves the result in s
    s16 = s.intersection_update(t)

    # Returns True if s and t have no items in common
    s17 = s.isdisjoint(t)

    # Returns True if s is a subset of t
    s18 = s.issubset(t)

    # Returns True if s is a superset of t
    s19 = s.issuperset(t)

    s = {1, 2, 3, 4, 5}

    # Returns an arbitrary set element and removes it from s
    s20 = s.pop()

    # Removes item from s. If an item is not a member, KeyError is raised
    s21 = s.remove(4)

    # Symmetric difference. Returns all the items that are in s or t, but not in both sets
    s22 = s.symmetric_difference(t)

    # Computes the symmetric difference of s and t and leaves the result in s
    s23 = s.symmetric_difference_update(t)

    # Union. Returns all items in s or t
    s24 = s.union(t)

    # Adds all the items in t to s. t may be another set, a sequence, or any object that supports iteration
    s25 = s.update(t)


def convert_to_key(arr):
    return tuple(arr)


def dictionaries():
    """
    Type representing a dictionary
    If no argument is given, an empty dictionary is returned
    If m is a mapping object (such as another dictionary),
    a new dictionary having the same keys and same values as m is returned
    For example, if m is a dictionary, dict(m) makes a shallow copy of it
    If m is not a mapping, it must support iteration in which a sequence
    of (key, value) pairs is produced
    These pairs are used to populate the dictionary
    dict() can also be called with keyword arguments
    For example, dict(foo=3, bar=7) creates the dictionary {'foo': 3, 'bar': 7 }
    https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
    """
    prices = {
        'ACME': 50,
        'GOOG': 92.34,
        'AAPL': 123.15,
        'IBM': 75,
        'MSFT': 102.25,
        'BNP': 40,
        'NVDA': 74.50,
        'GOOG1': 50,
        'WM': 124.75
    }

    d1 = prices.get('IBM1', 0.0)
    del prices['GOOG1']
    prices['IBM'] = 91.23
    # An example of a dictionary comprehension
    d2 = {s[0]: 0 for s in prices}
    # To obtain a list of dictionary keys, convert a dictionary to a list
    # The keys always appear in the same order
    # as the items were initially inserted into the dictionary
    d3 = list(prices)

    # Merges m and n into a single dictionary.
    foo = {"a": 1, "b": 2}
    bar = {"c": 3, "d": 4}
    baz = foo | bar

    # Returns the number of items in m.
    d4 = len(prices)

    # Returns the item of m with key k.
    d5 = prices['NVDA']

    # Sets m[k] to x.
    d6 = prices['NVDA'] = 600

    # Removes m[k] from m.
    del prices['BNP']

    # Returns True if k is a key in m.
    d7 = 'AAPL' in prices

    # Removes all items from m.
    foo.clear()

    # Makes a shallow copy of m.
    d8 = bar.copy()

    # Creates a new dictionary with keys from a sequence s and values all set to value.
    d9 = foo.fromkeys(range(5), 42)

    # Returns m[k] if found; otherwise, returns v.
    d10 = foo.get('42', 0)

    # Returns the keys
    d12 = prices.keys()

    # Returns the values.
    d17 = prices.values()

    # Returns (key, value) pairs.
    d11 = prices.items()

    # Returns m[k] if found and removes it from m; otherwise,
    # returns default if supplied or raises KeyError if not.
    d13 = prices.pop('WM', 50)

    # Removes a random (key, value) pair from m and returns it as a tuple.
    d14 = prices.popitem()

    # If a key is in the dictionary, return its value.
    # If not, insert a key with a value of default and return default. default defaults to None.
    d15 = prices.setdefault('WM', 100)

    # Adds all objects from b to m.
    d16 = prices.update(bar)

    # -----------------------------------------------

    # Declaration: a hash map is declared like any other variable. The syntax is {}
    hash_map = {}  # dict()
    # Set operations also work on the key-view and item-view objects of dictionaries.
    # For example, to find out which keys two dictionaries have in common, do this:

    # If you want to initialize it with some key value pairs, use the following syntax:
    hash_map = {1: 2, 5: 3, 7: 2}

    # Checking if a key exists: simply use the `in` keyword
    dd1 = 1 in hash_map  # True
    dd2 = 9 in hash_map  # False

    # Accessing a value given a key: use square brackets, similar to an array.
    dd3 = hash_map[5]  # 3

    # Adding or updating a key: use square brackets, similar to an array.
    # If the key already exists, the value will be updated
    dd4 = hash_map[5] = 6

    # If the key doesn't exist yet, the key value pair will be inserted
    hash_map[9] = 15

    # Deleting a key: use the del keyword. Key must exist or you will get an error.
    del hash_map[9]

    # Get size
    dd5 = len(hash_map)  # 3

    # Get keys: use .keys(). You can iterate over this using a for loop.
    keys = hash_map.keys()
    for key in keys:
        k = key

    # Get values: use .values(). You can iterate over this using a for loop.
    values = hash_map.values()
    for val in values:
        v = val
    pass


def default_dict_class():
    """
    https://docs.python.org/3/library/collections.html#collections.defaultdict
    """

    from collections import defaultdict

    # Using a list as the default_factory,
    # it is easy to group a sequence of key-value pairs into a dictionary of lists
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    d = defaultdict(list)
    for k, v in s:
        d[k].append(v)
    sorted(d.items())  # [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

    # Setting the default_factory to int makes the defaultdict useful for counting
    s = 'mississippi'
    d = defaultdict(int)
    for k1 in s:
        d[k1] += 1
    sorted(d.items())  # [('i', 4), ('m', 1), ('p', 2), ('s', 4)]

    #  A faster and more flexible way to create constant functions is to use a lambda function
    #  which can supply any constant value (not just zero)
    def constant_factory(value):
        return lambda: value

    d = defaultdict(constant_factory('<missing>'))
    d.update(name='John')

    # Setting the default_factory to set makes the defaultdict useful for building a dictionary of sets
    s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
    d = defaultdict(set)
    for k, v in s:
        d[k].add(v)
    sorted(d.items())  # [('blue', {2, 4}), ('red', {1, 3})]


def counter_class():
    """
    https://docs.python.org/3/library/collections.html#collections.Counter
    """

    from collections import Counter

    cnt = Counter()
    for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
        cnt[word] += 1
    # Counter({'blue': 3, 'red': 2, 'green': 1})
    
    # Comare two Counters
    c1 = Counter('aabbc')
    c2 = Counter({'a': 2, 'b': 2, 'c': 1})

    are_equal = c1 == c2  # True
    
    del(c1['c'])
    print(c1)
    
    c2['c'] -= 1
    print(c2)
    
    are_equal = c1 == c2  # True
    print(are_equal)

    # Elements are counted from an iterable or initialized from another mapping (or counter)
    c = Counter()  # a new, empty counter
    c = Counter('gallahad')  # a new counter from an iterable
    c = Counter({'red': 4, 'blue': 2})  # a new counter from a mapping
    c = Counter(cats=4, dogs=8)  # a new counter from keyword args
    c = Counter(['eggs', 'ham'])
    cnt = c['bacon']  # count of a missing element is zero
    pass


def stacks():
    """
    We will just use a list
    """

    stack = []

    # Pushing elements:
    stack.append(1)
    stack.append(2)
    stack.append(3)

    # Popping elements:
    stack.pop()  # 3
    stack.pop()  # 2

    # Check if empty
    is_empty = not stack  # False

    # Check an element at the top
    peek = stack[-1]

    # Get size
    size = len(stack)


def deques():
    """
    We will use deque from the collections module
    https://docs.python.org/3/library/collections.html#deque-objects
    https://docs.python.org/3/library/collections.html#collections.deque
    """
    deque0 = collections.deque()
    # If you want to initialize it with some initial values:
    deque = collections.deque([1, 2, 3])

    # Enqueueing/adding elements
    deque.append(4)
    deque.appendleft(5)

    # De-queuing/removing elements:
    d1 = deque.pop()
    d2 = deque.popleft()

    # Check an element at front of queue (next element to be removed)
    d3 = deque[0]
    d4 = deque[-1]

    d5 = deque.pop()

    # Get size
    d6 = len(deque)
    pass


def queues():
    """
    We will use deque from the collections module
    """

    queue = collections.deque()

    # If you want to initialize it with some initial values:
    # queue = collections.deque([1, 2, 3])

    # Enqueueing/adding elements:
    queue.append(4)
    queue.append(5)
    queue.append(6)

    # De-queuing/removing elements:
    cur = queue.popleft()
    cur = queue.popleft()

    # Check an element at front of queue (next element to be removed)
    peek = queue[0]

    # Get size
    size = len(queue)
    pass


def heaps():
    """
    heapq only implements min heaps
    """

    # Declaration: heapq does not give you a heap data structure.
    # You just use a normal list, and heapq provides you with
    # methods that can be used on this list to perform heap operations
    heap = []

    # Add to heap
    heappush(heap, 1)
    heappush(heap, 2)
    heappush(heap, 3)

    # Check minimum element
    peek_min = heap[0]

    # Pop minimum element
    pop_min = heappop(heap)

    # Get size
    size = len(heap)  # 2

    # Bonus: convert a list to a heap in linear time
    nums = [43, 2, 13, 634, 120]
    heapify(nums)

    # Now, you can use heappush and heappop on nums
    # and nums[0] will always be the minimum element
    # import heapq
    stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    stones = [-stone for stone in stones]  # max heap
    heapq.heapify(stones)  # turns an array into a heap in linear time
    pass


def type_annotations():
    """
    https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
    """
    pass


def dp_with_cache(nums):
    @cache
    def dp(i):
        # Base cases
        if i == 0:
            return nums[0]
        if i == 1:
            return max(nums[0], nums[1])
        # Recurrence relation
        return max(dp(i - 1), dp(i - 2) + nums[i])

    return dp(len(nums) - 1)


class Ops:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y


class Account:
    # Class variable
    num_accounts = 0

    # Type hints
    owner: str
    balance: float

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self._owner2 = owner
        Account.num_accounts += 1

    @classmethod
    def from_xml(cls, data):
        from xml.etree.ElementTree import XML
        doc = XML(data)
        return cls(doc.findtext('owner'), doc.findtext('amount'))

    @property
    def owner2(self):
        return self._owner2

    @owner2.setter
    def owner2(self, value):
        self._owner2 = value

    @owner2.deleter
    def owner2(self):
        del self._owner2


class SuperAccount(Account):
    def __init__(self, owner, balance, factor):
        super().__init__(owner, balance)
        self.factor = factor

    def inquiry(self):
        return super().balance


def zip_lists():
    letters = ['a', 'b', 'c']
    nums = [1, 2, 3]

    for letter, num in zip(letters, nums):
        print("{}: {}".format(letter, num))

    some_list = [('a', 1), ('b', 2), ('c', 3)]
    letters, nums = zip(*some_list)

    print(letters)
    print(nums)
    pass


def positional_params(a, b, /):
    return a + b


x_1 = positional_params(1, 2)


def named_params(*, a, b):
    return a + b


x_2 = named_params(a=1, b=2)

# Convert characters to ASCII numbers
x = 'x'
z = 'z'

ascii_x = ord(x)  # ASCII value of 'x'
ascii_z = ord(z)  # ASCII value of 'z'

difference = ascii_z - ascii_x 

def compare_obj_addresses():
    # You can compare the addresses (identities) of two objects in Python using the built-in `id()` function or the `is` operator:
    a = object()
    b = object()
    same_address = id(a) == id(b)  # False
    # Or, more idiomatically:
    same_object = a is b  # False
    #Both `id(a) == id(b)` and `a is b` check if `a` and `b` refer to the exact same object in memory.
    
def list_init(n):
    ans = [float("inf")] * n
    print(ans)
    

if __name__ == '__main__':
    functions_scope()
    walrus_operator()
    ranges()
    iterables()
    sequences()
    mutable_sequences()
    comprehensions()
    map_filter_reduce()
    pipes()
    useful_funcs()
    copy_and_deepcopy()
    math_funcs()
    strings()
    tuples()
    lists()
    sets()
    dictionaries()
    default_dict_class()
    counter_class()
    stacks()
    deques()
    queues()
    heaps()
    type_annotations()
    dp_with_cache([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    zip_lists()
    compare_obj_addresses()
    list_init(10)