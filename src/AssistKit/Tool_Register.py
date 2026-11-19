class Registry:
    def __init__(self):
        self._tools: list[function] = []
        self._attributes = {}

    def register(self, level:int):
        def decorator(func):
            
            func.__doc__ = f"level = {level} | {func.__doc__}"
          
            self._tools.append(func)
          
            return func
        return decorator

    def setAttributes(self **attributes):
        self._attributes.update(attributes)

    def getAttributes(self, name:str):
        try:
            return self._attributes[name]
        except KeyError:
            # placeholder for custom error
            raise AttributeError(name=name, obj=self)

    def parseOllama(self):
        return self._tools
