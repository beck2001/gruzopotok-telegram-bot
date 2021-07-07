from loader import dp

from . throttling import ThrottlingMiddleware
from .middleware_stages import MiddlewareStages
from .acl import ACLMiddleware

if __name__ == "middlewares":
    dp.setup_middleware(ThrottlingMiddleware())
    dp.setup_middleware(MiddlewareStages())
    dp.setup_middleware(ACLMiddleware())
