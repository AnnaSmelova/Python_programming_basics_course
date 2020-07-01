# Выведите все простые на отрезке [2;n].

import math

print(
    *filter(
        lambda x: all(
                    map(
                        lambda y: x % y != 0,
                        range(
                            2,
                            int(
                                math.sqrt(x)
                            ) + 1
                        )
                    )
                    ),
        range(
            2,
            int(
                input()
            ) + 1
        )
    )
)
