# Papelaria

Este é um projeto em Python com fins didáticos para a disciplina da instituição Fatec de Ribeirão Preto chamada "Tópicos Especiais em Informática".

### Instalação 
Execute os seguintes comandos para instalar as dependências necessárias:
- 'pip install mysql-connector-python'
- 'pip install sqlalchemy'
- 'pip install pymysql'
- 'pip install requests'

### Table 

```sql
CREATE TABLE usuarios (
  id_usuario INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(255),
  email VARCHAR(255),
  senha VARCHAR(255)
);

CREATE TABLE produtos (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(200),
    preco_venda DECIMAL(10, 2),
    preco_compra  DECIMAL(10, 2),
    grupo VARCHAR(200),
    quantidade_em_estoque INT
);

CREATE TABLE vendas (
    id_venda INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_produto INT,
    quantidade_comprada INT,
    data_compra DATE,
    valor_total DECIMAL(10, 2),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);

CREATE TABLE sobreProj (
	id_sobre INT AUTO_INCREMENT PRIMARY KEY,
	sobre VARCHAR(3000)
);
```
### Para rodar
- Compilador de python (rodar pelo arquivo main.py)

### Equipe
- Abner Willian Mioti Manha
- Elaine Cristina Tome
