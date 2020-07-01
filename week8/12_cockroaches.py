# Перед началом тараканьих бегов всем болельщикам было предложено сделать
# по две ставки на результаты бегов. Каждая ставка имеет вид
# "Таракан №A придет раньше, чем таракан №B".
# Организаторы бегов решили выяснить, могут ли тараканы прийти в таком порядке,
# чтобы у каждого болельщика сыграла ровно одна ставка из двух
# (то есть чтобы ровно одно из двух утверждений
# каждого болельщика оказалось верным).
# Считается, что никакие два таракана не могут прийти к финишу одновременно.


from itertools import combinations, permutations

print(*next(
        *map(lambda d:
                filter(
                    lambda t: set(
                                map(
                                    lambda x:
                                        (int(x[0] in [*combinations(t, 2)])
                                         + int(x[1] in [*combinations(t, 2)])) == 1,
                                    d[1]
                                )
                    ) == {True},
                    d[0]
                ),
                 tuple(
                     map(
                         lambda y: [
                             permutations(range(1, y[0] + 1)),
                             tuple(
                                 map(
                                     lambda z: ((z[0], z[1]), (z[2], z[3])),
                                     tuple(
                                         map(
                                             lambda q: tuple(map(int, input().split())),
                                             range(y[1])
                                         )
                                     )
                                 )
                             )
                         ],
                        [tuple(map(int, input().split()))]
                    )
                 )
             )
        , [0])
      )
