from antlr4 import *
from CalcLexer import CalcLexer
from CalcParser import CalcParser
from eval_visitor import EvalVisitor


def main():
    text = input(">>> ")

    input_stream = InputStream(text)
    lexer = CalcLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = CalcParser(tokens)

    tree = parser.prog()

    visitor = EvalVisitor()
    result = visitor.visit(tree)

    print(result)


if __name__ == "__main__":
    main()
