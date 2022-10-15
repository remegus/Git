from curses import erasechar
from zadacha_1 import *
from zadacha_2 import *
from zadacha_3 import *
from zadacha_4 import *
import pytest


@pytest.mark.parametrize("a, expected_result", [(123, 6), (234, 9), (34.5, 12)])
def test_summa_chisla_good(a, expected_result):
    assert summa_chisla(a) == expected_result


def test_summa_chisla_error():
    with pytest.raises(TypeError):
        summa_chisla('123')


@pytest.mark.parametrize('a, res', [(4, [1, 2, 6, 24]), (6, [1, 2, 6, 24, 120, 720]), (1, [1])])
def test_number_2_good(a, res):
    assert number_2(a) == res


@pytest.mark.parametrize('er, a', [(TypeError, 2.5), (TypeError, 'sef')])
def test_number_2_error(er, a):
    with pytest.raises(er):
        number_2(a)


@pytest.mark.parametrize('a, res', [(4, 9.06), (6, 14.07), (8, 19.19)])
def test_number_3_good(a, res):
    assert number_3(a) == res


@pytest.mark.parametrize('er, a', [(TypeError, 9.06), (TypeError, '14.07')])
def test_number_3_error(er, a):
    with pytest.raises(er):
        number_3(a)


@pytest.mark.parametrize('a, res', [(8, (-70)), (11, (-400)), (3, 0)])
def test_number_4_good(a, res):
    assert number_4(a) == res


@pytest.mark.parametrize('er, a', [(TypeError, 1.2), (IndexError, -40), (TypeError, '3e')])
def test_number_4_error(er, a):
    with pytest.raises(er):
        number_4(a)
