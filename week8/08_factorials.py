# По заданному на входе числу 0≤n≤2000 выведите последовательность факториалов:
# 0!,1!,2!,…,n!

import itertools

print(
    *itertools.accumulate(
        [1] + list(
                range(
                    1,
                    int(
                        input()
                    ) + 1
                )
                ),
        lambda x, y: x * y
    )
)
