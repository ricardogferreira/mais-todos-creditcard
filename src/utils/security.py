from fastapi.security import APIKeyHeader

authorizer = APIKeyHeader(
    name="Authorization",
    scheme_name="Token de autenticação",
    description="Token gerado por uma aplicação de gerenciamento de usuários",
)
