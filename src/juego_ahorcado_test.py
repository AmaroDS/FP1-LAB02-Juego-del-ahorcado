from juego_ahorcado import normalizar, enmascarar, ha_ganado

def test_normalizar():
    assert normalizar("Árbol") == "arbol"
    assert normalizar("Canción") == "cancion"
    assert normalizar("Ñandú") == "ñandu"
    assert normalizar("Python") == "python"
    assert normalizar("") == ""

def test_enmascarar():
    assert enmascarar("python", "py") == "py____"
    assert enmascarar("ahorcado", "oa") == "a_o__a_o"
    assert enmascarar("prueba", "") == "______"
    assert enmascarar("prueba", "i") == "______"
    assert enmascarar("prueba", "prueba") == "prueba"

def test_ha_ganado():
    assert ha_ganado("python") == True
    ha_ganado("p____n") == False
    ha_ganado("______") == False


test_normalizar()
test_enmascarar()
test_ha_ganado()
print("✅ Todas las pruebas han pasado correctamente.")