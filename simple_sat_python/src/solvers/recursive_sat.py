# from __future__ import division
# from __future__ import print_function

from sys import stderr

from .watchlist import update_watchlist


def solve(instance, watchlist, assignment, d, verbose):
    """
    Recursively solve SAT by assigning to variables d, d+1, ..., n-1. Assumes
    variables 0, ..., d-1 are assigned so far. A generator for all the
    satisfying assignments is returned.
    """
    if d == len(instance.variables):
        yield assignment
        return

    for a in [0, 1]:
        if verbose:
            print('Trying {} = {}'.format(instance.variables[d], a),
                  file=stderr)
        assignment[d] = a
        # false literal is calculated as d<<1 | a:
        # if we assign var to true(a=1), (d<<1 | a) will set
        # the false_literal to ~var based on the literal encoding rule: var<<1 | negate_sign.
        if update_watchlist(instance,
                            watchlist,
                            (d << 1) | a,
                            assignment,
                            verbose):
            for assignment in solve(instance, watchlist, assignment, d + 1, verbose):
                yield assignment

    assignment[d] = None
