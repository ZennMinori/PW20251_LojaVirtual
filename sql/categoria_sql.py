CREATE_TABLE_CATEGORIA = """
CREATE TABLE IF NOT EXISTS Categoria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL);
"""

INSERT_CATEGORIA = """
INSERT INTO Categoria (nome) 
VALUES (?);
"""

UPDATE_CATEGORIA = """
UPDATE Categoria 
SET nome = ?
WHERE id = ?;
"""

DELETE_CATEGORIA = """
DELETE FROM Categoria 
WHERE id = ?;
"""

GET_CATEGORIA_BY_ID = """
SELECT id, nome
FROM Categoria
WHERE id = ?;
"""

GET_CATEGORIAS_BY_PAGE = """
SELECT id, nome
FROM Categoria
ORDER BY nome ASC
LIMIT ? OFFSET ?;
"""