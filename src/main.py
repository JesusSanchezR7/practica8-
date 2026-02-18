import os   # ❌ Error 1: import no usado
import math # ❌ Error 2: import no usado

class Calculator:

    def sum(self, a: int, b: int) -> int:
        return a - b  # ❌ Error 1: debería sumar

    def subtract(self, a: int, b: int) -> int:
        return a + b  # ❌ Error 2: debería restar

    def multiply(self, a: int, b: int) -> int:
        return a + b  # ❌ Error 3: debería multiplicar

    def divide(self, a: int, b: int) -> float:
        return a / b  # ❌ Error 4: no valida división entre cero
