"""CS 61A Homework 3: Due online by 5pm on Friday, September 23.

This interval arithmetic example is based on Structure and Interpretation of
Computer Programs, Section 2.1.4:
http://mitpress.mit.edu/sicp/full_text/book/book_Z_H-14.html#%_sec_2.1.4

Alyssa P. Hacker is designing a system to help people solve engineering
problems. One feature she wants to provide in her system is the ability to
manipulate inexact quantities (such as measured parameters of physical devices)
with known precision, so that when computations are done with such approximate
quantities the results will be numbers of known precision.

Alyssa's idea is to implement interval arithmetic as a set of arithmetic
operations for combining "intervals" (objects that represent the range of
possible values of an inexact quantity). The result of adding, subracting,
multiplying, or dividing two intervals is itself an interval, representing the
range of the result.

Alyssa postulates the existence of an abstract object called an "interval" that
has two endpoints: a lower bound and an upper bound. She also presumes that,
given the endpoints of an interval, she can construct the interval using the
data constructor make_interval.   Using the constructor and selectors, she
defines the following operations.
"""

def str_interval(x):
    """Return a string representation of interval x.
    
    >>> str_interval(make_interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(make_interval(-1, 2), make_interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return make_interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(make_interval(-1, 2), make_interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return make_interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))



"""Alyssa's program is incomplete because she has not specified the
implementation of the interval abstraction. Define the constructor and selectors
in terms of two_element tuples.
"""

def make_interval(a, b):
    """Construct an interval from a to b."""
    return (a, b)

def lower_bound(x):
    """Return the lower bound of interval x."""
    return min(x)

def upper_bound(x):
    """Return the upper bound of interval x."""
    return max(x)

"""Alyssa implements division below, by multiplying by the reciprocal of y. Ben
Bitdiddle, an expert systems programmer, looks over Alyssa's shoulder and
comments that it is not clear what it means to divide by an interval that spans
zero. Add an assert statement to Alyssa's code to ensure that no such interval
is used as a divisor.
"""

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided
    by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(make_interval(-1, 2), make_interval(4, 8)))
    '-0.25 to 0.5'
    """
    if y!=0:
        reciprocal_y = make_interval(1/upper_bound(y), 1/lower_bound(y))
        return mul_interval(x, reciprocal_y)
    else:
        raise ValueError("Cannot do devision by 0, please select different y")

"""Using reasoning analogous to Alyssa's, define a subtraction function for
intervals.  Add a doctest.
"""

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.

    >>> str_interval(sub_interval(make_interval(-1, 2), make_interval(4, 8)))
    '2 to 9'
    """
    lower = upper_bound(y) - lower_bound(x)
    upper = - upper_bound(x) + lower_bound(y)
    return make_interval(lower, upper)

"""In passing, Ben also cryptically comments, "By testing the signs of the
endpoints of the intervals, it is possible to break mul_interval into nine
cases, only one of which requires more than two multiplications."  Write a
fast multiplication function using Ben's suggestion.  Add a doctest.
"""

def mul_interval_fast(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y, using as few multiplications as possible.
    >>> str_interval(mul_interval_fast(make_interval(-2, -2), make_interval(4,8)))
    '-16 to -8'
    >>> str_interval(mul_interval_fast(make_interval(-2, -2), make_interval(-4,8)))
    '-16 to 8'
    >>> str_interval(mul_interval_fast(make_interval(-2, -2), make_interval(4,-8)))
    '-8 to 16'
    >>> str_interval(mul_interval_fast(make_interval(-2, -2), make_interval(-4,-8)))
    '8 to 16'
    >>> str_interval(mul_interval_fast(make_interval(2, 2), make_interval(4,8)))
    '8 to 16'
    >>> str_interval(mul_interval_fast(make_interval(2, 2), make_interval(-4, 8)))
    '-8 to 16'
    >>> str_interval(mul_interval_fast(make_interval(2, 2), make_interval(4, -8)))
    '-16 to 8'
    >>> str_interval(mul_interval_fast(make_interval(2, 2), make_interval(-4, -8)))
    '-16 to -8'
    >>> str_interval(mul_interval_fast(make_interval(-2, 2), make_interval(4, 8)))
    '-16 to 16'
    >>> str_interval(mul_interval_fast(make_interval(-2, 2), make_interval(-4, 8)))
    '-16 to 16'
    >>> str_interval(mul_interval_fast(make_interval(-2, 2), make_interval(4, -8)))
    '-16 to 16'
    >>> str_interval(mul_interval_fast(make_interval(-2, 2), make_interval(-4, -8)))
    '-16 to 16'
	
    """
    "*** YOUR CODE HERE ***"
    if upper_bound(x)<0:
        if upper_bound(y)<0:
            upper_xy = lower_bound(x)*lower_bound(y)
            lower_xy = upper_bound(x)*upper_bound(y)
        elif lower_bound(y)>0:
            upper_xy = lower_bound(x)*upper_bound(y)
            lower_xy = upper_bound(x)*lower_bound(y)
        else:
            upper_xy = upper_bound(x)*lower_bound(y)
            lower_xy = upper_bound(x)*upper_bound(y)
    elif lower_bound(x)>0:
        if upper_bound(y)<0:
            upper_xy = lower_bound(x)*upper_bound(y)
            lower_xy = upper_bound(x)*lower_bound(y)
        elif lower_bound(y)>0:
            upper_xy = lower_bound(x)*lower_bound(y)
            lower_xy = upper_bound(x)*upper_bound(y)
        else:
            upper_xy = upper_bound(x)*lower_bound(y)
            lower_xy = upper_bound(x)*upper_bound(y)
    elif lower_bound(x)<0 and upper_bound(x)>0:
        if upper_bound(y)<0:
            upper_xy = lower_bound(x)*lower_bound(y)
            lower_xy = upper_bound(x)*lower_bound(y)
        elif lower_bound(y)>0:
            upper_xy = upper_bound(x)*upper_bound(y)
            lower_xy = lower_bound(x)*upper_bound(y)
        else:
            """upper_bound(y)<0 and lower_bound(y)<0"""
            upper_xy = max(upper_bound(x)*upper_bound(y), lower_bound(x)*lower_bound(y))
            lower_xy = min(lower_bound(x)*upper_bound(y), upper_bound(x)*lower_bound(y))
    else:
        upper_xy = lower_bound(x)*lower_bound(y)
        lower_xy = upper_bound(x)*upper_bound(y)
    return make_interval(lower_xy, upper_xy)

	
	
	
	
"""After debugging her program, Alyssa shows it to a potential user, who
complains that her program solves the wrong problem. He wants a program that can
deal with numbers represented as a center value and an additive tolerance; for
example, he wants to work with intervals such as 3.5 +/- 0.15 rather than 3.35
to 3.65. Alyssa returns to her desk and fixes this problem by supplying an
alternate constructor and alternate selectors in terms of the existing ones:
"""

def make_center_width(c, w):
    """Construct an interval from center and width."""
    return make_interval(c - w, c + w)

def center(x):
    """Return the center of interval x."""
    return (upper_bound(x) + lower_bound(x)) / 2

def width(x):
    """Return the width of interval x."""
    return (upper_bound(x) - lower_bound(x)) / 2

"""Unfortunately, most of Alyssa's users are engineers. Real engineering
situations usually involve measurements with only a small uncertainty, measured
as the ratio of the width of the interval to the midpoint of the interval.
Engineers usually specify percentage tolerances on the parameters of devices.

Define a constructor make_center_percent that takes a center and a percentage
tolerance and produces the desired interval. You must also define a selector
percent that produces the percentage tolerance for a given interval. The center
selector is the same as the one shown above.
"""

def make_center_percent(c, p):
    """Construct an interval from center and percentage tolerance.
    
    >>> str_interval(make_center_percent(2, 50))
    '1.0 to 3.0'
    """
    "*** YOUR CODE HERE ***"
    return make_interval(c - c*p/100, c + c*p/100)

def percent(x):
    """Return the percentage tolerance of interval x.
    
    >>> percent(make_interval(1, 3))
    50.0
    """
    "*** YOUR CODE HERE ***"
    if center(x)!=0:
        return width(x)/center(x)*100
    else:
        return 0
		
"""After considerable work, Alyssa P. Hacker delivers her finished system.
Several years later, after she has forgotten all about it, she gets a frenzied
call from an irate user, Lem E. Tweakit. It seems that Lem has noticed that the
formula for parallel resistors can be written in two algebraically equivalent
ways:

    (r1 * r2) / (r1 + r2)

    and

    1 / (1/r1 + 1/r2)

He has written the following two programs, each of which computes the
parallel_resistors formula differently:
"""
"""Test (r1 * r2) / (r1 + r2) == 1 / (1/r1 + 1/r2)
    
    >>> par1(1, 3) == par2(1, 3)
    True
    """
def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = make_interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

"""Write a function quadratic that returns the interval of all values f(t) such
that t is in the argument interval x and 

f(t) = a * t * t + b * t + c

Make sure that your implementation returns the smallest such interval, one that
does not suffer from the multiple references problem.

Hint: the derivative f'(t) = 2 * a * t + b, and so the extreme point of the
quadratic is -b/(2*a).
"""

def quadratic(x, a, b, c):
    """Return the interval that is the range the quadratic defined by a, b, and
    c, for domain interval x.

    >>> str_interval(quadratic(make_interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(make_interval(1, 3), 2, -3, 1))
    '0 to 10'
    >>> str_interval(quadratic(make_interval(-1, 0), -3, 2, -5))
    '-10 to -5'
    """
    "*** YOUR CODE HERE ***"
    x_max=-b/(2*a)
    y1=a*lower_bound(x)*lower_bound(x)+lower_bound(x)*b+c
    y2=a*upper_bound(x)*upper_bound(x)+upper_bound(x)*b+c
    y3=a*x_max*x_max+x_max*b+c
    
    
    if x_max>upper_bound(x) or x_max<lower_bound(x):
        return(min(y1,y2),max(y1,y2))
    elif y3<y1:
        return(y3, max(y1,y2))
    else:
        return(min(y1,y2),y3)
     
     
    """Write three similar functions, each of which takes as an argument a sequence
of intervals and returns the sum of the square of each interval that does not
contain 0.

    1. Using a for statement containing an if statement.
    2. Using map and filter and reduce.
    3. Using generator expression and reduce.

Hint: Square is a special case of quadratic, but you can also use the simpler
square_interval function below for intervals that do not contain 0.
"""

def non_zero(x):
    """Return whether x contains 0."""
    return lower_bound(x) > 0 or upper_bound(x) < 0 

def square_interval(x):
    """Return the interval that contains all squares of values in x, where x
    does not contain 0.
    """
    assert non_zero(x), 'square_interval is incorrect for x containing 0'
    return mul_interval(x, x)

# The first two of these intervals contain 0, but the third does not.
seq = (make_interval(-1, 2),  make_center_percent(-1, 50), make_center_width(-1, 2))

zero = make_interval(0, 0)

def sum_nonzero_with_for(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using a for statement.
    
    >>> str_interval(sum_nonzero_with_for(seq))
    '0.25 to 2.25'
    """
    "*** YOUR CODE HERE ***"
    sum_sqr_interval=zero
    for elem in seq:
        if non_zero(elem)==True and elem!=zero:
            sum_sqr_interval=add_interval(sum_sqr_interval, square_interval(elem))
            return sum_sqr_interval
		
if __name__ == "__main__":
    import doctest
    doctest.testmod()