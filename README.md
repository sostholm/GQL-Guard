# GQL-Guard
Access restriction for graphene with starlette.
The guard decorator will look in the JWT provided by the request for a string matching the called wrapped function.
In order to provide access, the token's payload must contain the key 'access' with a list of queries and mutations the user is allowed to make.

## Usage

Wrap query resolvers with @guard

```python
@guard
async def resolve_me(self, info):
    return {"name": "me"}
```