def sudoku_solver(puzzle):
    ethalon = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  ##Может быть ошибка
    global solution

    solution = puzzle

    if len(puzzle) == 9:
        for array in puzzle:
            if len(array) != 9:
                raise

    for i_place in range(9):
        for j_place in range(9):
            try:
                ethalon.index(solution[i_place][j_place])
            except ValueError:
                raise
    if start_check():
        raise
    puzzle_unsolved = True
    global deep
    deep = []
    while puzzle_unsolved:
        glag = False
        print(solution)
        all_stats = []
        counter_update = 0
        counter_zeros = 0
        for i_place in range(9):
            for j_place in range(9):
                if solution[i_place][j_place] == 0:
                    counter_zeros += 1
                    probably = checker(i_place, j_place)
                    stats_element = [i_place, j_place, probably]
                    all_stats.append(stats_element)

                    if len(probably) == 1:
                        solution[i_place][j_place] = probably[0]
                        counter_update += 1
                    if len(probably) == 0:
                        move_on_deep()
                        glag = True

        if glag == False:
            if counter_zeros > 64:
                raise

            if counter_zeros == 0:
                puzzle_unsolved = False
                return solution
            if counter_update == 0:
                print(all_stats)
                sort_list = sorted(all_stats, key=sort_key)
                attempt_left = len(sort_list[0][2]) - 1
                PAZLA = []
                for i in range(9):
                    PAZLA.append(solution[i].copy())
                for_append = [PAZLA, sort_list[0][0], sort_list[0][1], sort_list[0][2], attempt_left]
                deep.append(for_append)
                print(sort_list[0][2])
                print(str(sort_list[0][0]) + ' ' + str(sort_list[0][1]))
                solution[sort_list[0][0]][sort_list[0][1]] = sort_list[0][2][0]


def sort_key(e):
    return len(e[2])


def start_check():
    for i_place in range(9):
        for j_place in range(9):
            q = solution[i_place][j_place]
            if q != 0:
                solution[i_place][j_place] = 0
                if q in checker(i_place, j_place):
                    solution[i_place][j_place] = q
                else:
                    return True
    return False


def move_on_deep():
    global solution
    global deep
    if len(deep) != 0:
        if deep[-1][4] == 0:
            deep.pop()
            move_on_deep()

        else:
            deep[-1][4] = deep[-1][4] - 1
            deep[-1][3].pop(0)
            solution = deep[-1][0]
            solution[deep[-1][1]][deep[-1][2]] = deep[-1][3][0]

    else:
        raise


def checker(i_place, j_place):
    probably = []
    rows = check_rows(i_place)
    columns = check_columns(j_place)
    boxes = check_box(i_place, j_place)
    probably = list(set(columns) & set(boxes) & set(rows))
    return probably


def check_rows(i_place):
    ethalon = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    i_list = solution[i_place].copy()
    here_ = clear_list(i_list)
    for i in range(len(here_)):
        ethalon.remove(here_[i])
    return ethalon


def check_columns(j_place):
    ethalon = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    j_list = []
    for i in solution.copy():
        j_list.append(i[j_place])
    here_ = clear_list(j_list)
    for i in range(len(here_)):
        ethalon.remove(here_[i])
    return ethalon


def check_box(i_place, j_place):
    ethalon = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    box_list = []
    area_i = i_place // 3
    area_i = area_i * 3
    area_j = j_place // 3
    area_j = area_j * 3
    for i in range(area_i, (area_i + 3)):
        for j in range(area_j, (area_j + 3)):
            a = [i, j]
            add_ = solution[i][j]
            box_list.append(add_)
    here_ = clear_list(box_list)
    for i in range(len(here_)):
        ethalon.remove(here_[i])
    return ethalon


def clear_list(some_list):
    zeros = some_list.count(0)
    while zeros > 0:
        some_list.remove(0)
        zeros = zeros - 1
    return some_list


### Для примера
puzzle = [
            [0, 0, 6, 1, 0, 0, 0, 0, 8],
            [0, 8, 0, 0, 9, 0, 0, 3, 0],
            [2, 0, 0, 0, 0, 5, 4, 0, 0],
            [4, 0, 0, 0, 0, 1, 8, 0, 0],
            [0, 3, 0, 0, 7, 0, 0, 4, 0],
            [0, 0, 7, 9, 0, 0, 0, 0, 3],
            [0, 0, 8, 4, 0, 0, 0, 0, 6],
            [0, 2, 0, 0, 5, 0, 0, 8, 0],
            [1, 0, 0, 0, 0, 2, 5, 0, 0]
        ]

sudoku_solver(puzzle)

