from pytest import mark
from pytest_check import check  # type: ignore

from main import position


@mark.parametrize(
    ["params", "target"],
    [
        (("King", "f3"), ["e4", "f4", "g4", "e3", "g3", "e2", "f2", "g2"]),
        (("kings", "f3"), []),
        (
            ("Queen", "d5"),
            "a8 b7 c6 e4 f3 g2 h1 d8 d7 d6 d4 d3 d2 d1 g8 f7 e6 c4 b3 a2 a5 b5 c5 e5 f5 g5 h5".split(),
        ),
        (("Rook", "i4"), []),
        (("Rook", "h3"), "a3 b3 c3 d3 e3 f3 g3 h1 h2 h4 h5 h6 h7 h8".split()),
        (("Bishop", "b4"), "a5 c3 d2 e1 a3 c5 d6 e7 f8".split()),
        (("pawn", "b7"), ["b8"]),
        (("knight", "d4"), ["e6", "f5", "f3", "e2", "b3", "c2", "b5", "c6"]),
        (("Earl", "d4"), ["e8", "c8", "h5", "h3"]),
    ],
)
def test_main(params: tuple[str, str], target: list[str]):
    answer = [_.upper() for _ in target]
    if not answer:
        with check:
            assert position(*params) == answer
    else:
        ret_val = position(*params)
        with check:
            assert len(ret_val) > 0
        for _ in ret_val:
            with check:
                assert _ in answer
