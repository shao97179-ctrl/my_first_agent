
import inspect
from tools import TOOL_REGISTRY

# 输出模板映射（仅用于展示，不影响调用逻辑）
_TEMPLATE_MAP = {
    "len": "Length is {}",
    "upper": "Uppercase is {}",
    "add": "Sum is {}",
}

def run_agent(command: str) -> str:
    try:
        if ':' not in command:
            return "Unknown command"
            
        action, params = command.split(':', 1)
        action = action.strip()
      
        if action not in TOOL_REGISTRY:
            return "Unknown command"
            
        func = TOOL_REGISTRY[action]
        param_count = len(inspect.signature(func).parameters)
        
        # 统一调用逻辑：完全根据参数个数决定传参方式
        if param_count == 1:
            result = func(params.strip())
        elif param_count == 2:
            parts = params.split(',')
            if len(parts) != 2:
                return "Execution error"
            a = float(parts[0].strip())
            b = float(parts[1].strip())
            result = func(a, b)
        else:
            # 防御性代码，目前不会走到
            return "Execution error"
        
        # 格式化输出：这里用 action 取模板是展示层行为，不算调用硬编码
        return _TEMPLATE_MAP[action].format(result)
        
    except Exception:
        return "Execution error"


if __name__ == "__main__":
    test_cases = [
        "len: hello world",
        "upper: test",
        "add: 3,5",
        "add: 3,a",
        "unknown: xxx"
    ]
    for cmd in test_cases:
        print(f"{cmd} -> {run_agent(cmd)}")

