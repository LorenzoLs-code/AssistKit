from .Tool_Register import Registry
EverydayUtilities_Registry = Registry()

# TOOLS

# =================
#       Math
# =================
import ast
import operator

OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}

@EverydayUtilities_Registry.register(level=0)
def calculate(expression: str) -> str:
    """Evaluates a math expression. Always use this tool for calculations.

    Args:
        expression: Valid Python math string using '+', '-', '*', '/', '**', '()', 
            and '.' for decimals. No units or variables. Example: "(124 * 18) / 4 + 15"
    """
    def _eval(node):
        if isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.BinOp):
            return OPS[type(node.op)](_eval(node.left), _eval(node.right))
        elif isinstance(node, ast.UnaryOp):
            return OPS[type(node.op)](_eval(node.operand))
        raise ValueError("Unsupported operation")

    try:
        tree = ast.parse(expression, mode='eval')
        return str(_eval(tree.body))
    except Exception as e:
        return f"Error in calculation: {e}"
