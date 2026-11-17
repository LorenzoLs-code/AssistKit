from typing import Any

class _ToolArg:
  def __init__(self, name:str, type:Any, required=True, default=None):
    self.name     = name
    self.type     = type
    self.required = required
    self.default  = default


class _Tool:
  def __init__(self, name:str, level:int, doc:str, args:list[_ToolArg]| None=[]):
    self.name   = name
    self.level  = level
    self.doc    = doc
    self.args   = args


class Registry:
    def __init__(self):
        self._tools: list[_Tool] = []

    def register(self, level:int):
      def decorator(func):

        self._tools.append(_Tool(
            name  = func.__name__,
            level = level,
            doc   = func.__doc__,
            args  = []
        ))
        
        return func
      return decorator
