from typing import Any

class _ToolArg:
  def __init__(self, name:str, type:Any, default=None):
    self.name    = name
    self.type    = type
    self.default = default


class _Tool:
  def __init__(self, name:str, level:int, doc:str, args:list[_ToolArg]):
    self.name   = name
    self.level  = level
    self.doc    = doc
    self.args   = args


class Registry:
    def __init__(self):
        pass

    def register(self):
      def decorator(func):

        
        
        return func
      return decorator
