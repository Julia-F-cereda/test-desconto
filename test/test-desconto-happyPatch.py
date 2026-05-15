from desconto.desconto import calcular_desconto
def test_inteiros():
    assert calcular_desconto(200, 20) == 160.00

def test_quebrados():
    assert calcular_desconto(215, 13) == 187.05

def test_decimais():
    assert calcular_desconto(340.00, 12.5) == 297.50
    
def test_descontoZero():
    assert calcular_desconto(100, 0) == 100.00

def test_precoZero():
    assert calcular_desconto(0, 10) == 0.00
    