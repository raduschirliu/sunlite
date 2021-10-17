from flask import request
import jwt
import os

JWT_SECRET = os.getenv('JWT_SECRET')
JWT_AUDIENCE = os.getenv('JWT_AUDIENCE')

# Check if the request header includes a valid JWT
def verify_jwt():
    if not hasattr(request.headers, 'Authorization'):
        print('No authorization')
        return False

    authorization = request.headers.get('Authorization')
    parts = authorization.split(' ')
    
    if len(parts) != 2:
        print('Invalid parts')
        return False
    
    if parts[0] != 'Bearer':
        print('No bearer')
        return False
    
    try:
        audience = [JWT_AUDIENCE]
        decoded = jwt.decode(parts[1], JWT_SECRET, audience=audience, algorithms=['HS256'])
        return decoded
    except Exception:
        print('Invalid JWT')
        return False