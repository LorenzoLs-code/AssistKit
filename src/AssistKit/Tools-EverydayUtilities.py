from Tool_Register import Registry
EverydayUtilities_Registry = Registry()

# TOOLS

# =================
#       Math
# =================
import ast
import operator

_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}

@EverydayUtilities_Registry.register(level=0)
def calculator(expression: str) -> str:
    """Evaluates a math expression. Always use this tool for calculations.

    Args:
        expression: Valid Python math string using '+', '-', '*', '/', '**', '()', 
            and '.' for decimals. No units or variables. Example: "(124 * 18) / 4 + 15"
    """
    def _eval(node):
        if isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.BinOp):
            return _OPS[type(node.op)](_eval(node.left), _eval(node.right))
        elif isinstance(node, ast.UnaryOp):
            return _OPS[type(node.op)](_eval(node.operand))
        raise ValueError("Unsupported operation")

    try:
        tree = ast.parse(expression, mode='eval')
        return str(_eval(tree.body))
    except Exception as e:
        return f"Error in calculation: {e}"


# ====================
#  Currency converter
# ====================
import requests

@EverydayUtilities_Registry.register(level=0)
def currency_converter(base:str, quotes:str, amount:float = 1.0):
    """Convert an amount between two currencies using live exchange rates.

    Args:
        base: Source currency ISO 4217 code (e.g., "EUR").
        quotes: Target currency ISO 4217 code (e.g., "USD").
        amount: Amount to convert (default 1.0 for exchange rate).
    """

    response = requests.get(f"https://api.frankfurter.dev/v2/rate/{base.upper()}/{quotes.upper()}")
    response.raise_for_status()

    data = response.json()
    return round(amount * data["rate"], 2)


# =======================
#       Time & Date
# =======================
from datetime import datetime, timedelta

@EverydayUtilities_Registry.register(level=0)
def get_time(add:bool = True, add_days:int=0, add_minutes:int=0, add_hours:int=0, add_weeks:int=0):
    """Get current date/time (leave args at 0) or calculate a past/future date/time.

    Args:
        add: True to add time (future), False to subtract time (past).
        add_days: Days to add or subtract.
        add_minutes: Minutes to add or subtract.
        add_hours: Hours to add or subtract.
        add_weeks: Weeks to add or subtract.
    """
    
    time_now = datetime.now()
    time_add = timedelta(days=add_days, minutes=add_minutes, hours=add_hours, weeks=add_weeks)

    if add:
        time_result = time_now + time_add
    else:
        time_result = time_now - time_add

    return time_result.strftime("%d.%m.%Y-Date | %H:%M-Time")
