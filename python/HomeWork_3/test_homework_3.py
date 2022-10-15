
from zadachi_2 import *
from zadachi_4 import *
from zadachi_0 import *
import pytest


@pytest.mark.parametrize('a, res', [('5.6.1991', 31), ('1.6.1990', 26), ('26.9.2022', 23)])
def test_data_sum_good(a, res):
    assert data_sum(a) == res


@pytest.mark.parametrize('er, a', [(AttributeError, 1.2), (AttributeError, 12345), (ValueError, '133gd53')])
def test_data_sum_error(er, a):
    with pytest.raises(er):
        data_sum(a)


@pytest.mark.parametrize('a, res', [(10, [10, 18, 24, 28, 30]), (2, [2]), (17, [17, 32, 45, 56, 65, 72, 77, 80, 81])])
def test_umn_par_good(a, res):
    assert umn_par(a) == res


@pytest.mark.parametrize('er, a', [(TypeError, 1.2), (TypeError, '3da')])
def test_umn_par_error(er, a):
    with pytest.raises(er):
        umn_par(a)


@pytest.mark.parametrize('a, res', [(110, '1101110'), (256, '100000000'), (3, '11')])
def test_dvo_good(a, res):
    assert dvo(a) == res


@pytest.mark.parametrize('er, a', [(TypeError, '311')])
def test_dvo_error(er, a):
    with pytest.raises(er):
        dvo(a)
