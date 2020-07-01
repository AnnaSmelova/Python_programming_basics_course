# XOR для произвольного числа аргументов определяется следующим образом:
# xor(a₁,a₂,…,an)= xor(a₁, xor(a₂, xor(a₃,… xor(an))…)
# XOR от n последовательностей A₁,…,An (Aᵢ=Aᵢ₁,…,Aᵢk) равных длин k — это последовательность C=xor(A₁,…,An),такая, что:
# cᵢ=xor(A₁ᵢ,…Anᵢ)
# Посчитайте XOR от n последовательностей равной длины k.

import functools

print(
    *list(
        map(
            lambda x: functools.reduce(
                                    lambda y, z: (y + z) % 2,
                                    x
                                    ),
            list(
                zip(
                    *list(
                        map(
                            lambda x: tuple(
                                        map(
                                            int,
                                            (input().split())
                                        )
                                        ),
                            range(
                                int(
                                    input()
                                )
                            )
                        )
                    )
                )
            )
        )
    )
)
