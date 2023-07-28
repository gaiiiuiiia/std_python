import pytest
from custom_filter import custom_filter


@pytest.mark.parametrize(
    ['filter', 'sequence', 'result'],
    [
        (filter, list(range(10)), [0, 6]),
        (custom_filter, list(range(10)), [0, 6]),
    ],
)
def test_filter(filter, sequence, result):
    def func1(i) -> bool:
        return i % 2 == 0

    def func2(i) -> bool:
        return i % 3 == 0

    filtered = filter(func1, sequence)
    filtered = filter(func2, filtered)

    filtered_result = list(filtered)

    assert filtered_result == result

    with pytest.raises(StopIteration):
        next(filtered)
