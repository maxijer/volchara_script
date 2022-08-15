from lexer import Lexer
from parser_ import Parser

text_input = """
auf(4 + 4 - 2);
"""
lexer_ = Lexer().get_lexer()
tokens = lexer_.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()
