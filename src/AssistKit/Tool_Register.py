class Registry:
    def __init__(self):
        self._tools: dict[str, function] = []
        self._attributes = {}

    def register(self, level:int):
        def decorator(func):
            
            func.__doc__ = f"level = {level} | {func.__doc__}"
          
            self._tools[func.__name__] = func
          
            return func
        return decorator

    def setAttributes(self **attributes):
        self._attributes.update(attributes)

    def getAttributes(self, name:str):
        try:
            return self._attributes[name]
        except KeyError:
            raise AttributeError(name=name, obj=self)

    
    def parseOllama(self):
        return list(self._tools.values())

    def callOllama(self, response):
        if not response.message.tool_calls: return response

        for call in response.message.tool_calls:
            func = self._tools.get(call.function.name)
            if not func: 
                messages.append({
                    "role": "tool",
                    "content": f"Error: Tool '{call.function.name}' not found.",
                    "tool_name": call.function.name,
                })
                continue
            
            result = func(**call.function.arguments)
            response.messages.append({
                "role": "tool",
                "content": str(result),
                "tool_name": call.function.name,
            })

        return response
