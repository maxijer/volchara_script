from Parser import Parser
from context import Context
from interpreter import Interpreter
from lexer import Lexer
from symbol_table import SymbolTable
from value import Number

global_symbol_tabel = SymbolTable()
global_symbol_tabel.set("NULL", Number(0))
global_symbol_tabel.set("TRUE", Number(1))
global_symbol_tabel.set("FALSE", Number(0))

def run(fn, text):
    # GET Tokens
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error:
        return None, error
    # Create AST
    parser = Parser(tokens)
    AST = parser.parse()
    if AST.error:
        return None, AST.error

    # interpreter

    interpreter = Interpreter()
    context = Context("<program>")
    context.symbol_table = global_symbol_tabel
    result = interpreter.visit(AST.node, context)

    return result.value, result.error
