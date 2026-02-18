from app.calculation import Calculator
from app.calculator_config import Config

def run():
    Config.validate()
    calc = Calculator()

    print("Calculator REPL started. Type help.")

    while True:
        try:
            user_input = input(">> ").strip()

            if user_input == "exit":
                print("Goodbye!")
                break

            if user_input == "help":
                print("Commands: add, sub, mul, div, pow, root, history, undo, redo")
                continue

            parts = user_input.split()

            if len(parts) == 3:
                op, a, b = parts
                a = float(a)
                b = float(b)

                result = calc.calculate(a, b, op)
                print("Result:", result)
            else:
                print("Invalid command")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":  # pragma: no cover
    run()