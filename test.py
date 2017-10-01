
def evens(n):
    """ Return the n-th even number. """
    return 2 * n

def make_seq_generator(seq_fn):
    """
   """
    i=0
    i= i+1
    return seq_fn(i)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)