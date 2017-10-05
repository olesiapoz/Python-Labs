"""Homework 7: Recursion"""

"""1) The number of partitions of a positive integer n is the number of ways in
which n can be expressed as the sum of positive integers in increasing order.
For example, the number 5 has 7 partitions:

    5 = 5
    5 = 1 + 4
    5 = 2 + 3
    5 = 1 + 1 + 3
    5 = 1 + 2 + 2
    5 = 1 + 1 + 1 + 2
    5 = 1 + 1 + 1 + 1 + 1

Write a tree-recursive function part(n) that returns the number of partitions
of n. 

Hint: Introduce a locally defined function that computes partitions of n using only
a subset of the integers less than or equal to n.  Once you have done so, you
can use very similar logic to the count_change function from lecture.  
"""

def part(n):
    """Return the number of partitions of positive integer n.

    >>> part(5)
    7
    """

    def test(p, s=1):
        m = p
        if p >= 0:
            if p % 2 == 0:
                x = int(p / 2)
            else:
                x = int((p + 1) / 2)
            while m >= x:
                m = m - 1
                s += 1
            return test(m, s)
        else:
            return s

    return test(n)

"""2) A mathematical function g is defined by two cases:
   
   g(n) = n,                                       if n < 4
   g(n) = g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3),  if n > 3 
   
Write a recursive function that computes g. Then, write an iterative function
that computes g.
"""

def g(n):
    """Return the value of g, defined above, computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> g(6)
    51
      """
    if n < 4:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)


def pi_g_iter(n):
    """Return the value of g, defined above, computed recursively.
    >>> pi_g_iter(1)
    1
    >>> pi_g_iter(2)
    2
    >>> pi_g_iter(3)
    3
    >>> pi_g_iter(4)
    10
    >>> pi_g_iter(5)
    22
    >>> pi_g_iter(6)
    51
    >>> pi_g_iter(12)
    9330
    """
    if n < 4:
        return n
    else:
        k = 4
        (p1, p2, p3) = (3, 2, 1)
        while k <= n:
            p = p1 + 2 * p2 + 3 * p3
            (p3, p2, p1) = (p2, p1, p)
            k = k + 1
        return p

def g_iter(n):
    """Return the value of g, defined above, computed iteratively.
    g(n) = n,                                       if n < 4
    g(n) = g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3),  if n > 3

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    if n < 4:
        return n
    else:
        k = 4
        (p1, p2, p3) = (3, 2, 1)
        while k <= n:
            p = p1 + 2 * p2 + 3 * p3
            (p3, p2, p1) = (p2, p1, p)
            k = k + 1
        return p

######################
# OPTIONAL QUESTIONS #
######################

"""3) A perfect number is defined as a positive integer equal to the sum of all
its factors less than itself. For example, the first perfect number is 6,
because its factors are 1, 2, 3, and 6, and 1+2+3=6. The second perfect number
is 28, because 1+2+4+7+14=28.

Write a function next_perfect(n) that tests numbers starting with n and
continuing with n+1, n+2, etc. until a perfect number is found. You will need
to implement sum_of_factors as well.
"""

def sum_of_factors(n):
    """Return the sum of the factors of n less than n. A factor of a positive
    integer n is a positive integer that divides n evenly.

    >>> sum_of_factors(21)
    11
    >>> sum_of_factors(28)
    28
    """
    def devider(n, sum = 0):
        for k in range(1,n):
            if n%(n-k) == 0:
                sum += (n-k)
        return sum

    if n < 2:
        return n
    else:
        return devider(n)



def next_perfect(n):
    """Return the smallest perfect number greater than or equal to n.

    >>> next_perfect(1)
    1
    """
    "*** YOUR CODE HERE ***"
    if sum_of_factors(n) == n:
        return n
    else:
        return next_perfect(n + 1)




"""4) Write an iterative function that computes the number of partitions of n.

Hint: Try building the cache that would result from memoizing the part function
you already wrote, but iteratively.
"""

def part_iter(n):
    """Return the number of partitions of positive integer n.

    >>> part_iter(5)
    7
    """
    "*** YOUR CODE HERE ***"

    def memo(f):
        """Return a memoized version of single-argument function f."""
        cache = {}
        def memoized(n):
            if n not in cache:
                cache[n] = f(n)
            return cache[n]
        return memoized
    s = memo(part)
    return s(n)




"""4.5) Write a data-directed apply function that computes the area or
perimeter of either a square or a rectangle.

Note: This question was added Friday night 10/14, after hw7 was originally
released.
"""

class Square(object):
    def __init__(self, side):
        self.side = side

class Rect(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

def apply(operator_name, shape):
    """Apply operator to shape.

    >>> apply('area', Square(10))
    100
    >>> apply('perimeter', Square(5))
    20
    >>> apply('area', Rect(5, 10))
    50
    >>> apply('perimeter', Rect(2, 4))
    12
    """
    "*** YOUR CODE HERE ***"


#####################
# EXTRA FOR EXPERTS #
#####################

from operator import sub, mul

"""5) The Y-combinator

The recursive factorial function can be written as a single expression by using
a conditional expression (Python syntax not introduced in the notes).
http://docs.python.org/py3k/reference/expressions.html#conditional-expressions

>>> fact = lambda n: 1 if n == 1 else mul(n, fact(sub(n, 1)))
>>> fact(5)
120

To write a recursive function previously, we have always given it a name using
a def or assignment statement so that we can refer to the function within its
own body.  In this question, your job is to define fact without giving it a
name!

Write an expression that computes n factorial using only call expressions,
conditional expressions, and lambda expressions (no assignment or def
statements).  The sub and mul functons from the operator module are the only
built-in function required to solve this problem. 

Write your solution as a doctest by filling in the expression below.

>>> (lambda n: YOUR_CODE_HERE)(5)
120

Hint: Googling Y-combinator will tell you the solution, so don't do that until
you've tried to solve the problem yourself!
"""


"""6) Lists with loops.

The Rlist class (copied below) can represent lists with cycles.  That is, a
list may contain itself as a sublist.

>>> s = Rlist(1, Rlist(2, Rlist(3)))
>>> s.rest.rest.rest = s
>>> s[20]
3

This question has two parts: 
  A) Write a function has_cycle that returns True if and only if its argument,
     an Rlist instance, contains a cycle.
  B) Write a function has_cycle_constant that has the same behavior as
     has_cycle but requires only a constant amount of space.

Hint: The solution to B is short (~10 lines of code), but requires a clever
idea. Try to discover the solution yourself before asking around.
"""

def has_cycle(s):
    """Return whether Rlist s contains a cycle.
    
    
    >>> s = Rlist(1, Rlist(2, Rlist(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Rlist(1, Rlist(2, Rlist(3)))
    >>> has_cycle(t)
    False
    """
    "*** YOUR CODE HERE ***"

def has_cycle_constant(s):
    """Return whether Rlist s contains a cycle.
    
    
    >>> s = Rlist(1, Rlist(2, Rlist(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Rlist(1, Rlist(2, Rlist(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"

#####################
# CODE FROM LECTURE #
#####################

class Rlist(object):
    """A recursive list consisting of a first element and the rest."""
    class EmptyList(object):
        def __len__(self):
            return 0

    empty = EmptyList()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __repr__(self):
        args = repr(self.first)
        if self.rest is not Rlist.empty:
            args += ', {0}'.format(repr(self.rest))
        return 'Rlist({0})'.format(args)

    def __len__(self):
        return 1 + len(self.rest)

    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.rest[i-1]


