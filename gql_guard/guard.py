from functools import wraps
from starlette.requests import Request
from starlette.exceptions import HTTPException
import os

def guard(func):
    @wraps(func)
    async def check_permissions(*args, **kwargs):
        
        request = args[1].context['request']
        assert isinstance(request, Request)
        

        if (
            not getattr(request.user, 'payload') or 
            (
                not func.__name__ in request.user.payload['access'] and
                not func.__qualname__ in request.user.payload['access']
            )
            and not(
                'DEVELOPMENT_ACCESS' in os.environ and
                os.environ['DEVELOPMENT_ACCESS'].lower() == 'true'
            ) 
        ): 
            raise HTTPException(status_code=403)
        
        return  await func(*args, **kwargs)
        
    return check_permissions

