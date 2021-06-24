import jwt
import time

EXPIRATION_TIME = 3600 #1 hora
EXPIRATION_TIME_MAX = 2678400 #31 dias
JWT_SECRET = '443535353'

def encode_jwt(cpf: str, remember: bool = False) -> str:
    payload = {'cpf':cpf, "exp": time.time() + (EXPIRATION_TIME_MAX if remember else EXPIRATION_TIME)}
    return jwt.encode(
            payload,
            JWT_SECRET,
            algorithm='HS256'
        )

def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(
            token,
            JWT_SECRET,
            algorithms='HS256'
        )
        is_expired = decoded_token["exp"] >= time.time()

        return decoded_token if is_expired else None
    except:
        return None