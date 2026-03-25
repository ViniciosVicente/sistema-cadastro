from passlib.context import CryptContext
import hashlib

config_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # Se caso no futuro ele mudar, ele irá se adaptar.

def gerar_hash(senha: str):
    senha_bytes = senha.encode("utf-8")
    senha_hash = hashlib.sha256(senha_bytes).hexdigest()
    return config_context.hash(senha_hash) # Senha se transforma em hash.

def verificar_senha(senha: str, hash: str):
    senha_bytes = senha.encode("utf-8")
    senha_hash = hashlib.sha256(senha_bytes).hexdigest()
    return config_context.verify(senha_hash,hash) # Faz a verificação se a senha é igual o hash (dentro do banco).

