# mais-todos-creditcard

Api responsável pelo gerenciamento dos cartões de credito.

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
