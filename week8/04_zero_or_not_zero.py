# Проверьте, есть ли среди данных N чисел нули.

print(
    any(
        map(lambda x: int(input()) == 0,
            range(
                int(
                    input()
                )
            )
        )
    )
)
