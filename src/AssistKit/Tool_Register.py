class Registry:
    def __init__(self):
        self._tools: list[function] = []

    def register(self, level:int):
        def decorator(func):
            
            func.__doc__ = f"level = {level} | {func.__doc__}"
          
            self._tools.append(func)
          
            return func
        return decorator

    def parseOllama(self):
        return self._tools
