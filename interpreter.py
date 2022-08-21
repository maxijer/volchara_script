from lexer import TT_PLUS, TT_MINUS, TT_MUL, TT_DIV
from value import Number


class Interpreter:
    def visit(self, node):
        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name, self.no_visit_method)
        return method(node)

    def no_visit_method(self, node):
        raise Exception(f"No visit_{type(node).__name__} method defined")

    def visit_NumberNode(self, node):
        return Number(node.tok.value).set_pos(node.pos_start, node.pos_end)

    def visit_BinOpNode(self, node):
        left = self.visit(node.left_node)
        right = self.visit(node.right_node)

        if node.op_tok.type == TT_PLUS:
            result = left.added_to(right)
        if node.op_tok.type == TT_MINUS:
            result = left.subbed_by(right)
        if node.op_tok.type == TT_MUL:
            result = left.multed_by(right)
        if node.op_tok.type == TT_DIV:
            result = left.dived_by(right)
        return result.set_pos(node.pos_start, node.pos_end)

    def visit_UnaryOpNode(self, node):
        number = self.visit(node.node)

        if node.op_tok.type == TT_MINUS:
            number = number.multed_by(Number(-1))
        return number.set_pos(node.pos_start, node.pos_end)
