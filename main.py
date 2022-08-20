from Parser import Parser
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
    return AST, None
