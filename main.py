from lexer import Lexer

text_input = """
auf(4 + 4 - 2);
"""

lexer_ = Lexer().get_lexer()
tokens = lexer_.lex(text_input)

for token in tokens:
    print(token)
