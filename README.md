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

### Comandos Makefile (Em desenvolvimento, não utilizar)
```bash
# Executar testes
make run-tests

# Criar uma nova migração
make create-migration description="<Descrição da migração>"

# Aplicar migração
make migrate

# Realizar rollback da ultima migração aplicada
make rollback-migration
```

### Comandos via docker-compose
```bash
# Executar testes
docker compose exec api make run-tests

# Criar uma nova migração
docker compose exec api make create-migration description="<Descrição da migração>"

# Aplicar migração
docker compose exec api make migrate

# Realizar rollback da ultima migração aplicada
docker compose exec api make rollback-migration
```

### Migrações

Para gerenciar as migrações de banco de dados estamos utilizando o `dbmate`,
todas as migrações ficam disponíveis em `migrations`, para gerencia-las existe os comandos no `Makefile`.
Foi utilizado o dbmate para poder escrever código sql puro e não ficar limitado a comandos do alembic ou algo parecido.


### Testes
Estamos utilizando o `pytest` para o desenvolvimento dos testes.
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

### Autenticação e autorização

A lógica de autorização não foi adicionado na aplicação, foi considerado que existirá outra aplicação para fazer a autenticação e autorização dentro do cluster.
Para testar a api só é preciso informar o header `Authorization`:
```json
{"Authorization": "token test"}
```

### Variáveis de ambiente
```shell
POSTGRES_PASSWORD=test123
POSTGRES_USER=mais_todos_creditcard
POSTGRES_DB=mais_todos_creditcard
POSTGRES_URL=db
POSTGRES_PORT=5432
POSTGRES_CONNECTION_URL="postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_URL}:${POSTGRES_PORT}/${POSTGRES_DB}"
DATABASE_URL="${POSTGRES_CONNECTION_URL}?sslmode=disable"
CRYPTOGRAPHY_KEY=Us_TeDQyQrkiSbcz8kkavCOYRhJhKa0UEFn0ce0P6kc=
```

### Etapas para subir a aplicação
Configurar variaveis de ambiente;

Executar os seguintes comandos:
```shell
docker compose build
docker compose up
docker compose exec api make migrate
```

Acessar local `http://127.0.0.1:5000`, swagger `http://127.0.0.1:5000/docs`

### Testes
Teste integrado com o banco de dados:
* Teste integrados `tests/routes/test_api_v1_credit_card_viewer.py``

Os outros são testes unitários.

Antes de executar os testes deve subir o docker:
```bash
docker compose up
```

Comando para executar os testes:
```bash
docker compose exec api-test make run-tests
```
