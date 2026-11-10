import pytest


# Exemplo de teste que passa
def test_right_example():
    lista = [1, 2, 3, 4, 5, 6, 7, 8]

    _inicio, *meio, _fim = lista

    assert meio == lista[1:-1]


# Exemplo de teste que da erro
@pytest.mark.xfail()
def test_fail_example():
    with pytest.raises(AssertionError):
        lista = [1, 2, 3, 4, 5, 6, 7, 8]

        _primeiro, _segundo, *fim = lista

        assert fim == lista[0:]
