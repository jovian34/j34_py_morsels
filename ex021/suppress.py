from contextlib import contextmanager

@contextmanager
def suppress(error):
    try:
        suppress(error)
    except error:
        pass

    yield
    pass