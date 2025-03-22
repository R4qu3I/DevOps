import pytest

# Função para converter número decimal em binário
def converter_para_binario(num):
    partes = str(num).split(".")
    parte_int = int(partes[0])
    parte_dec = float("0." + partes[1])

    binario_int = ""
    while parte_int:
        binario_int = str(parte_int % 2) + binario_int
        parte_int //= 2

    binario_dec = []
    while parte_dec:
        parte_dec *= 2
        x = int(parte_dec)
        if x == 1:
            parte_dec -= x
            binario_dec.append("1")
        else:
            binario_dec.append("0")

    # Garantir que a parte decimal tenha "0." como prefixo e lidar com casos de "1."
    binario_int = binario_int if binario_int != "" else "0"
    binario_dec = "".join(binario_dec)
    binario = f"{binario_int}.{binario_dec}" if binario_dec else f"{binario_int}.0"

    return binario

# Testes para verificar os resultados
def test_numero_inteiro():
    assert converter_para_binario(10.0) == "1010.0"
    assert converter_para_binario(4.0) == "100.0"
    assert converter_para_binario(0.0) == "0.0"

def test_numero_fracionado():
    assert converter_para_binario(10.25) == "1010.01"
    assert converter_para_binario(4.5) == "100.1"
    assert converter_para_binario(0.625) == "0.101"

def test_edge_cases():
    assert converter_para_binario(1.0) == "1.0"
    assert converter_para_binario(0.125) == "0.001"