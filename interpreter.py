import os
import sys
from textx import metamodel_from_file
icltspmo_mm = metamodel_from_file('icltcpmo.tx')
if len(sys.argv) < 2:
    print("😐 yo...  GIVE ME A FILE BRO")
    sys.exit(1)
filename = sys.argv[1]
if not os.path.exists(filename):
    print(f"😐 yo... file {filename} doesn't exist...")
    sys.exit(1)
if not filename.endswith('.pmo'):
    print(f"😐 yo... {filename} isn't a .pmo file...")
    sys.exit(1)

# Load the model from the .pmo file
icltspmo_model = icltspmo_mm.model_from_file(filename)

class Interpreter:

    # stores variables
    def __init__(self):
        self.variables = {}

    # goes through the program and handles each statement
    def interpret(self, program):
        for stmt in program.statements:
            self.handle_statement(stmt)

    # handles each statement
    # checks the type of statement and calls based on the type
    def handle_statement(self, stmt):
        stmt_type = stmt.__class__.__name__
        if stmt_type == 'PrintStatement':
            self.handle_print(stmt)
        elif stmt_type == 'Assignment':
            self.handle_assignment(stmt)
        elif stmt_type == 'FizzBuzzStatement':
            self.handle_fizzbuzz(stmt)
        elif stmt_type == 'YogurtStatement':
            self.handle_yogurt(stmt)

    # handles 'PrintStatement'
    def handle_print(self, stmt):
        if hasattr(stmt, 'expr') and stmt.expr:
            result = self.eval_expr(stmt.expr)
            if result is not None:
                print(result)
        elif hasattr(stmt, 'value') and stmt.value:
            print(stmt.value.strip('"'))

    # handles 'Assignment'
    def handle_assignment(self, stmt):
        if hasattr(stmt.value, 'value'):
            value = int(stmt.value.value)
        else:
            value = self.eval_expr(stmt.value)
        self.variables[stmt.var] = value

    # handles 'FizzBuzzStatement'
    def handle_fizzbuzz(self, stmt):
        fizznum = int(stmt.fizznum)
        buzznum = int(stmt.buzznum)
        end = int(stmt.end)

        for i in range(1, end + 1):
            output = ""
            if i % fizznum == 0:
                output += "yo"
            if i % buzznum == 0:
                output += "gurt"
            print(output or i)

    # handles 'YogurtStatement'
    def handle_yogurt(self, stmt):
        name = stmt.name.lower()
        if name == "gurt":
            print("gurt: yo wassup")
        elif name == "dabish":
            print("yo wsg prof dabish js icl iltcsm srs fr vro ong im js atp jus evry 1 an A vro 💯😭🙏")
        elif name == "calc":
            print("calc is short for calculator if you didn't know that")
        elif name == "sybau":
            print("stay young, beautiful, and unstoppable")
        else:
            print("sybau 💔🥀")

    # for evaluating expressions
    def eval_expr(self, expr):
        if isinstance(expr, int):
            return expr

        # checks if the expression is a string, then checks if it is a special case
        if isinstance(expr, str):
            if expr.strip().lower() == 'yogurt':
                print("gurt: yo wassup")
                return None
            if expr.strip().lower() == 'ts':
                print("icl ts pmo n ts pmo sm ngl ru fr rnb fr I h8 ts y r u sob so fr w me rn cz lol oms icl ts pmo sm n sb rn ngl, r u srsly srs n fr rn vro? lol atp js qt icl u pmo n ts pmo sm ngl ru fr rn be fr I h8 bein diff idek anm mn js I h8 ts y r u so b so fr w me rn cz… lol oms icl ts pmo sm n sb rn ngl, r u srsly srs n fr rn vro? lol atp is go icl u pmo n ts pmo sm ngl ru fr rnb fr I h8 bein diff idek anm mn js I h8 tsy rusob so fr w me rn cz… lol oms icl ts pmo sm n sb rn ngl, ru srsly srs n fr rn vro? lol atp js go")
                return None
            elif expr.strip().lower() == 'support':
                print("port: wsg gng")
                return None
            return self.variables.get(expr, 0)
        
        # goes through the expressions and checks what type of expression
        if expr.__class__.__name__ == 'ID':
            return self.variables.get(expr.name, 0)

        if expr.__class__.__name__ == 'Factor':
            return self.eval_expr(expr.value)

        if expr.__class__.__name__ == 'Term':
            result = self.eval_expr(expr.left)
            for op in expr.ops:
                right = self.eval_expr(op.right)
                if op.operator == '*':
                    result *= right
                elif op.operator == '/':
                    result /= right
            return result

        if expr.__class__.__name__ == 'Expr':
            result = self.eval_expr(expr.left)
            for op in expr.ops:
                right = self.eval_expr(op.right)
                if op.operator == '+':
                    result += right
                elif op.operator == '-':
                    result -= right
            return result

        return 0

icltspmo = Interpreter()
icltspmo.interpret(icltspmo_model)
