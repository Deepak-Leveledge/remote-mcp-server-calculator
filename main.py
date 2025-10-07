from fastmcp import FastMCP
import random
import json

mcp = FastMCP("Simple Calculator remote server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b    

@mcp.tool()
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@mcp.tool()
def random_number(min_val: int = 1,max_val: int = 100) -> int:
    """Generate a random number between min_val and max_val"""
    return random.randint(min_val, max_val)


@mcp.resource("info://server")
def server_info() -> str:
    """Get server information"""
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0",
        "description": "A simple calculator server that can perform basic arithmetic operations."
    }
    return json.dumps(info, indent=4)



if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
