def move_king(r: int, c: int) -> list[tuple[int, int]]:
    """
    国王，可以向周围8个方格移动1格

    Args:
        r (int): 棋盘行索引
        c (int): 棋盘列索引

    Returns:
        list[tuple[int, int]]: 所有合法移动的棋盘位置索引
    """
    ret_val: list[tuple[int, int]] = []
    for _r in range(r - 1, r + 2):
        if _r < 1 or _r > 8:
            continue
        for _c in range(c - 1, c + 2):
            if _c < 1 or _c > 8 or (_r == r and _c == c):
                continue
            ret_val.append((_r, _c))
    return ret_val


def move_queen(r: int, c: int) -> list[tuple[int, int]]:
    """
    皇后，米字行棋

    Args:
        r (int): 棋盘行索引
        c (int): 棋盘列索引

    Returns:
        list[tuple[int, int]]: 所有合法移动的棋盘位置索引
    """
    # 皇后的米字行棋等效于同时具备城堡的十字行棋和主教的斜线行棋
    return move_rook(r, c) + move_bishop(r, c)


def move_rook(r: int, c: int) -> list[tuple[int, int]]:
    """
    城堡，十字行棋

    Args:
        r (int): 棋盘行索引
        c (int): 棋盘列索引

    Returns:
        list[tuple[int, int]]: 所有合法移动的棋盘位置索引
    """
    ret_val: list[tuple[int, int]] = []
    for _ in range(-8, 9):
        if _ == 0:
            continue
        if r + _ < 1 or r + _ > 8:
            continue
        # 竖线
        ret_val.append((r + _, c))
        if c + _ < 1 or c + _ > 8:
            continue
        # 横线
        ret_val.append((r, c + _))
    return ret_val


def move_bishop(r: int, c: int) -> list[tuple[int, int]]:
    """
    主教，斜线行棋

    Args:
        r (int): 棋盘行索引
        c (int): 棋盘列索引

    Returns:
        list[tuple[int, int]]: 所有合法移动的棋盘位置索引
    """
    ret_val: list[tuple[int, int]] = []
    for _ in range(-8, 9):
        if _ == 0:
            continue
        if r + _ < 1 or r + _ > 8:
            continue
        if c + _ < 1 or c + _ > 8:
            continue
        # 右斜线
        ret_val.append((r + _, c + _))
        if c - _ < 1 or c - _ > 8:
            continue
        # 左斜线
        ret_val.append((r + _, c - _))
    return ret_val


def move_knight(r: int, c: int) -> list[tuple[int, int]]:
    """
    骑士，日字行棋

    Args:
        r (int): 棋盘行索引
        c (int): 棋盘列索引

    Returns:
        list[tuple[int, int]]: 所有合法移动的棋盘位置索引
    """
    ret_val: list[tuple[int, int]] = []
    for _r in (r - 2, r + 2):
        for _c in (c - 1, c + 1):
            if _r < 1 or _r > 8 or _c < 1 or _c > 8:
                continue
            ret_val.append((_r, _c))
    for _r in (r - 1, r + 1):
        for _c in (c - 2, c + 2):
            if _r < 1 or _r > 8 or _c < 1 or _c > 8:
                continue
            ret_val.append((_r, _c))
    return ret_val


def move_pawn(r: int, c: int) -> list[tuple[int, int]]:
    """
    士兵，只能向上移动1格

    Args:
        r (int): 棋盘行索引
        c (int): 棋盘列索引

    Returns:
        list[tuple[int, int]]: 所有合法移动的棋盘位置索引
    """
    if r + 1 <= 8:
        return [(r + 1, c)]
    return []


def move_earl(r: int, c: int) -> list[tuple[int, int]]:
    """
    伯爵（虚拟棋），行四拐一

    Args:
        r (int): 棋盘行索引
        c (int): 棋盘列索引

    Returns:
        list[tuple[int, int]]: 所有合法移动的棋盘位置索引
    """
    ret_val: list[tuple[int, int]] = []
    for _r in (r - 4, r + 4):
        for _c in (c - 1, c + 1):
            if _r < 1 or _r > 8 or _c < 1 or _c > 8:
                continue
            ret_val.append((_r, _c))
    for _r in (r - 1, r + 1):
        for _c in (c - 4, c + 4):
            if _r < 1 or _r > 8 or _c < 1 or _c > 8:
                continue
            ret_val.append((_r, _c))
    return ret_val


def position(piece: str, loc: str) -> list[str]:
    """
    查询所有合法行棋位置

    Args:
        piece (str): 棋名
        c (str): 棋当前索引位置

    Returns:
        list[str]: 所有合法移动的棋盘位置索引
    """
    COLS = ["A", "B", "C", "D", "E", "F", "G", "H"]

    # 合法性校验
    ret_val: list[str] = []
    if loc[0].upper() not in COLS:
        return ret_val
    r, c, t = int(loc[1]), COLS.index(loc[0].upper()) + 1, piece.upper()
    if r < 1 or r > 8:
        return ret_val
    if t == "KING":
        for _r, _c in move_king(r, c):
            ret_val.append(f"{COLS[_c - 1]}{_r}")
    elif t == "QUEEN":
        for _r, _c in move_queen(r, c):
            ret_val.append(f"{COLS[_c - 1]}{_r}")
    elif t == "ROOK":
        for _r, _c in move_rook(r, c):
            ret_val.append(f"{COLS[_c - 1]}{_r}")
    elif t == "BISHOP":
        for _r, _c in move_bishop(r, c):
            ret_val.append(f"{COLS[_c - 1]}{_r}")
    elif t == "KNIGHT":
        for _r, _c in move_knight(r, c):
            ret_val.append(f"{COLS[_c - 1]}{_r}")
    elif t == "PAWN":
        for _r, _c in move_pawn(r, c):
            ret_val.append(f"{COLS[_c - 1]}{_r}")
    elif t == "EARL":
        for _r, _c in move_earl(r, c):
            ret_val.append(f"{COLS[_c - 1]}{_r}")

    return ret_val
