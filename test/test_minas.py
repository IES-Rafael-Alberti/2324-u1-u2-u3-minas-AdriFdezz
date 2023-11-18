from src.minas import iniciar_tablero, revelar_celda, marcar_celda, verificar_victoria, revelar_celdas_vacias

def test_iniciar_tablero():
    filas, columnas, num_minas = 8, 8, 10
    tablero, minas = iniciar_tablero(filas, columnas, num_minas)

    assert len(tablero) == filas
    assert len(tablero[0]) == columnas
    assert len(minas) == num_minas
    assert all(0 <= fila < filas and 0 <= columna < columnas for fila, columna in minas)

    for fila in tablero:
        assert all(celda == '*' or celda.isdigit() for celda in fila)

def test_revelar_celda():
        tablero = [['0', '0', '0'], ['0', '*', '0'], ['0', '0', '0']]
        celdas_reveladas = set()
        celdas_marcadas = set()
        minas = [(1, 1)]
        result = revelar_celda(1, 2, tablero, celdas_reveladas, celdas_marcadas, minas)
        
        assert result == False
        assert (1, 2) in celdas_reveladas
        
        celdas_reveladas = set()
        celdas_marcadas = set()
        minas = [(1, 1)]
        result = revelar_celda(1, 2, tablero, celdas_reveladas, celdas_marcadas, minas)
       
        assert result == False
        assert (1, 2) in celdas_reveladas

def test_marcar_celda():
    celdas_marcadas = set()
    marcar_celda(1, 1, celdas_marcadas)
    
    assert (0, 0) in celdas_marcadas

    celdas_marcadas = {(0, 0)}
    marcar_celda(1, 1, celdas_marcadas)
    
    assert (0, 0) not in celdas_marcadas

def test_verificar_victoria():
    tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    celdas_reveladas = {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)}
    minas = {(0, 0), (1, 1), (2, 2)}
    assert verificar_victoria(tablero, celdas_reveladas, minas) == False

def test_revelar_celdas_vacias():
    tablero = [['0', '0', '0'],
                ['0', '*', '0'],
                ['0', '0', '0']]
    celdas_reveladas = set()
    revelar_celdas_vacias(1, 1, tablero, celdas_reveladas)
    assert celdas_reveladas == {(1, 1)}