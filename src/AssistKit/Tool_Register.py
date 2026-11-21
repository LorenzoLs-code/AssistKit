class Registry:
    def __init__(self, registrys:list[Registry] = []):
        self._tools: dict[str, function] = {}
        self._attributes = {}

        for registry in registrys:
            self._tools     .update(registry._tools)
            self._attributes.update(registry._attributes)

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

    
    def ollamaParse(self):
        return list(self._tools.values())

    def ollamaCall(self, messages, response):
        for call in response.message.tool_calls:
            func = self._tools.get(call.function.name)
            if not func: 
                messages.append({
                    "role": "tool",
                    "content": f"Error: Tool '{call.function.name}' not found.",
                    "tool_name": call.function.name,
                })
                continue

            try:
                result = func(**call.function.arguments)
            except Exception as exc:
                result = f"Error executing tool '{call.function.name}': {exc}"

            messages.append({
                "role": "tool",
                "content": str(result),
                "tool_name": call.function.name,
            })

        return messages
