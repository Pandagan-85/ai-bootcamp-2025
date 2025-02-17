import pytest
from main import conta_valore_stringhe

def test_conta_valore():
    assert conta_valore_stringhe(["aldo"]) == {"aldo":1}
    assert conta_valore_stringhe(["aldo", "aldo"]) == {"aldo": 2}
    assert conta_valore_stringhe(["aldo", "aldo", "aldo"]) == {"aldo": 3}
    assert conta_valore_stringhe(["aldo", "aldo", "ciccio"]) == {"aldo": 2, "ciccio":1}

def test_input_sbagliato():
    with pytest.raises(TypeError):
        conta_valore_stringhe(2)
