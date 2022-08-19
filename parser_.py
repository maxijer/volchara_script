from rply import ParserGenerator
from AST import Number, Sum, Sub, Auf


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # Список всех токенов, принятых парсером.
            ['STRING', 'INTEGER', 'FLOAT', 'IDENTIFIER', 'BOOLEAN',
             'PLUS', 'MINUS', 'MUL', 'DIV',
             'IF', 'ELSE', 'COLON', 'END', 'AND', 'OR', 'NOT', 'LET', 'WHILE',
             '(', ')', '=', '==', '!=', '>=', '<=', '<', '>', '[', ']', ',',
             '{', '}',
             '$end', 'NEWLINE', 'FUNCTION']
        )

    def parse(self):
        @self.pg.production('program : AUF OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p):
            return Auf(p[2])

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
