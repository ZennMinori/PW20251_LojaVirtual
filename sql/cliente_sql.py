CREATE_TABLE_CLIENTE = """
CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL UNIQUE,
    telefone TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    data_nascimento TEXT NOT NULL);
"""

INSERT_CLIENTE = """
INSERT INTO cliente (nome, cpf, telefone, email, data_nascimento)
VALUES (?, ?, ?, ?, ?);
"""

UPDATE_CLIENTE = """
UPDATE cliente
SET nome = ?, cpf = ?, telefone = ?, email = ?, data_nascimento = ?
WHERE id_cliente = ?;
"""
DELETE_CLIENTE = """
DELETE FROM cliente
WHERE id_cliente = ?;
"""
GET_CLIENTE_BY_ID = """
SELECT id_cliente, nome, cpf, telefone, email, data_nascimento
FROM cliente
WHERE id_cliente = ?;
"""

GET_CLIENTES_BY_PAGE = """
SELECT id_cliente, nome, cpf, telefone, email, data_nascimento
FROM cliente
ORDER BY nome ASC
LIMIT ? OFFSET ?;
"""