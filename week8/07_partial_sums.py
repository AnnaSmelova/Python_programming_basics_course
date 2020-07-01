# По заданной последовательности:
# (a₁,…,an)
# посчитайте последовательность частичных сумм:
# (S₁,…,Sn),
# где Sk=a₁+a₂+…+ak.

import itertools

print(
    *itertools.accumulate(
        list(
            map(
                int,
                input().split()
            )
        ),
        lambda x, y: x + y
    )
)
