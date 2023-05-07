from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache
from fastapi_cache.backends.inmemory import InMemoryBackend

from starlette.requests import Request
from starlette.responses import Response

from slowapi.errors import RateLimitExceeded
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

from classes.logic import top10_tvshow_byprovider, TvShow, list_ofall_tvshows


# import all you need from fastapi-pagination
from fastapi_pagination import Page, add_pagination, paginate

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# cached data key, for handling pagination effectively during caching process.
def my_key(
        func,
        namespace: str = "",
        request: Request = None,
        response: Response = None,
        *args,
        **kwargs,
):
    prefix = FastAPICache.get_prefix()
    cache_key = f"{prefix}:{namespace}:{func.__module__}:{func.__name__}:{args}:{kwargs}:{request.query_params}"
    return cache_key

@app.get('/tvshows', response_model=Page[TvShow])
@limiter.limit("60/minute")
@cache(expire=60, key_builder=my_key)
async def all(request: Request):
    print(request.query_params)
    return paginate(list_ofall_tvshows())  # use paginate function to paginate your data

@app.get('/top10/{provider}')
@limiter.limit("60/minute")
@cache(expire=60)
async def top10(request: Request, provider: str):
    data = top10_tvshow_byprovider(provider)
    json_data = jsonable_encoder(data)
    return JSONResponse(content = json_data)

add_pagination(app)  # important! add pagination to your app

@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend())


#todos:
# pip install "fastapi-cache"
# pip install pandas
# pip install fastapi
# pip install slowapi
# pip install fastapi-pagination
# pip install 
