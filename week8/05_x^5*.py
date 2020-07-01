# На вход подаётся последовательность натуральных чисел длины n≤1000.
# Посчитайте произведение пятых степеней чисел в последовательности.

import functools

print(
    functools.reduce(
        lambda x, y: x * y,
        list(
            map(
                lambda x: x**5,
                list(
                    map(
                        int,
                        input().split()
                    )
                )
            )
        )
    )
)
