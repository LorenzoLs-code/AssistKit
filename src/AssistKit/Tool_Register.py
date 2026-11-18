from typing import Any
import inspect

class _ToolArg:
  def __init__(self, name:str, type:Any, required=True, default=None):
    self.name     = name
    self.type     = type
    self.required = required
    self.default  = default


class _Tool:
  def __init__(self, func:function, name:str, level:int, doc:str, args:list[_ToolArg]| None=[]):
    self.func   = func
    self.name   = name
    self.level  = level
    self.doc    = doc
    self.args   = args


class Registry:
    def __init__(self):
        self._tools: list[_Tool] = []

    def register(self, level:int):
      def decorator(func):
        signatur = inspect.signature(func)
        args:list[_ToolArg] = []
        for name, param in signatur.parameters.items():
          
            required = False
            default  = None
            if param.default is inspect.Parameter.empty:
                required=True
            else:
                default = param.default
          
            args.append(_ToolArg(
                name     = name, 
                type     = param.annotation,  
                required = required, 
                default  = default
            ))
          
        
        self._tools.append(_Tool(
            func  = func,
            name  = func.__name__,
            level = level,
            doc   = func.__doc__,
            args  = []
        ))
        
        return func
      return decorator
