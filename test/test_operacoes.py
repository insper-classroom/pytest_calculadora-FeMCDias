import pytest
from matematica.Calculadora import *


@pytest.mark.op_simples
def test_soma_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 12 == soma(v1, v2)
@pytest.mark.exercicio_1
def test_divisao_por_zero():
    v1 = 5.0
    v2 = 0.0
    assert np.inf == divisao(v1, v2)
@pytest.mark.exercicio_1
def test_media_lista_valores():
    v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert 5.5 == media_lista_valores(v1)
    v2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a']
    assert 5.5 == media_lista_valores(v2)
    #Testa se a função retorna 0 quando a lista está vazia
    assert 0 == media_lista_valores([])
