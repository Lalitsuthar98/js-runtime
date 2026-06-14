import sys
import quickjs


def py_log(*args):
    output = []

    for arg in args:
        if isinstance(arg, bool):
            output.append(str(arg).lower())
        elif arg is None:
            output.append("null")
        else:
            output.append(str(arg))

    print(*output)


ctx = quickjs.Context()

ctx.add_callable("py_log", py_log)

ctx.eval("""
const console = {
    log: (...args) => py_log(...args)
};
""")


if len(sys.argv) != 2:
    print("Usage: python runtime.py <file.js>")
    sys.exit(1)

js_file = sys.argv[1]

try:
    with open(js_file, "r", encoding="utf-8") as file:
        js_code = file.read()

    ctx.eval(js_code)

except FileNotFoundError:
    print(f"File not found: {js_file}")

except Exception as e:
    print(f"Runtime Error: {e}")