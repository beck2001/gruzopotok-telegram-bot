def rate_limit(limit: int, key=None):
    """
    decorator for setting limit on intervals of time to avoid flooding of the bot
    :param limit: time in seconds
    :param key: key to retrieve and set in next functions: setattr, getattr
    :return: decorator on the top of function
    """

    def decorator(func):
        setattr(func, "throttling_rate_limit", limit)
        if key:
            setattr(func, "", key)
        return func
    return decorator
