def get_length(text: str) -> int:
    return len(text)

def to_upper(text: str) -> str:
    return text.upper()

def add_numbers(a: float, b: float) -> float:
    return a + b

TOOL_REGISTRY = {
    "len": get_length,
    "upper": to_upper,
    "add": add_numbers,
}




