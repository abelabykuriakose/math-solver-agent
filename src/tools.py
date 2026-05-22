from langchain_core.tools import tool

@tool
def add(a: float, b: float) -> float:
    """Adds two numbers together (a + b)."""
    result = float(a + b)
    print(f"🧮 [Tool Execution] Running: {a} + {b} = {result}")
    return result

@tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together (a * b)."""
    result = float(a * b)
    print(f"🧮 [Tool Execution] Running: {a} * {b} = {result}")
    return result

@tool
def power(base: float, exponent: float) -> float:
    """Raises a base number to the power of an exponent (base ^ exponent)."""
    result = float(base ** exponent)
    print(f"🧮 [Tool Execution] Running: {base} ^ {exponent} = {result}")
    return result

# Export all tools as a simple list
math_tool_registry = [add, multiply, power]