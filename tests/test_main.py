from main import max_c
import pytest


@pytest.mark.parametrize("n, expected_result", [(54321, 5),(9876523,9),(0000000,0)])
def test_main(n, expected_result):
    assert max_c(n) == expected_result


def test_type_error():
    with pytest.raises(TypeError):
        assert max_c('dadadada')
