from desconto.desconto import calcular_desconto
import pytest

def test_string():
    with pytest.raises(TypeError, match="Erro: O valor total e o desconto devem ser numéricos."):
        calcular_desconto('CASA', 'CASA')

def test_precoZero():
    with pytest.raises(ValueError, match="Erro: O valor do produto não pode ser negativo."):
        calcular_desconto(-5, 200)

def test_descontoZero():
    with pytest.raises(ValueError, match="Erro: O desconto deve estar entre 0 e 100."):
        calcular_desconto(100, -20)

def test_descontoCem():
    with pytest.raises(ValueError, match="Erro: O desconto deve estar entre 0 e 100."):
        calcular_desconto(200, 100)
