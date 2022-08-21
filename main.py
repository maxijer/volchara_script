from Parser import Parser
from interpreter import Interpreter
from lexer import Lexer


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
    result = interpreter.visit(AST.node)

    return result, None
