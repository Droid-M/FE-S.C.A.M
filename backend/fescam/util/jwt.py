import jwt
import time


JWT_SECRET = '443535353'

def encode_jwt(cpf: str) -> str:
    payload = {'cpf':cpf}
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
        is_expired = decoded_token["expires"] >= time.time()

        return decoded_token if is_expired else None
    except:
        return None