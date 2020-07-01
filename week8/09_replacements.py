# По данному числу N выведите все перестановки чисел от 1 до N в лексикографическом порядке.

import itertools

print(
    *map(
        lambda x: ''.join(x),
        map(
            lambda x: list(
                        map(
                            lambda y: str(y),
                            x
                        )
                        ),
            itertools.permutations(
                range(1, int(input()) + 1)
            )
        )
    ),
    sep='\n'
)

