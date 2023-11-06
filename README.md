# mais-todos-creditcard

Api responsável pelo gerenciamento dos cartões de crédito.

### Uso do poetry

```bash
# Adicionar dependência
poetry add <nome do pacote>

# Adicionar uma dependência de desenvolvimento
poetry add -G dev <nome do pacote>

# Remover dependência
poetry remove <nome do pacote>
```

### Comandos Makefile
```bash
# Executar testes
make tests

# Criar uma nova migração
make create-migration description="<Descrição da migração>"

# Aplicar migração
make migrate

# Realizar rollback da ultima migração aplicada
make rollback-migration
```

### Migrações

Para gerenciar as migrações de banco de dados estamos utilizando o `dbmate`,
todas as migrações ficam disponíveis em `migrations`, para gerencia-las existe os comandos no `Makefile`.


### Testes
Estamos utilizando o `pytest` para os testes unitários e `vcrpy` para gerar os cassettes dos testes integrados.
Os testes estão na pasta `tests`.

### Swagger
Para acessar o swagger basta inserir o endpoint `/docs`.

### Como fazer o build do projeto?
```bash
docker compose build
```

### Como iniciar o projeto?
```bash
docker compose up
```

### Criptografia
Vejo que a melhor forma de criptografar seria no client, utilizando chave publica e privada.
Mas para teste e considerando que só estou desenvolvendo a api, estou utilizando o modulo `Fernet` para fazer uma criptografia simples,
 somente para teste.

Para configurar uma chave abra o python e utilize esse comando:
```python
>>> from cryptography.fernet import Fernet
>>> key = Fernet.generate_key()
```
Com a chave gerada configure a variável de ambiente `CRYPTOGRAPHY_KEY` com o valor da chave.
