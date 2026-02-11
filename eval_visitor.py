from CalcVisitor import CalcVisitor
from CalcParser import CalcParser

class EvalVisitor(CalcVisitor):
    def __init__(self):
        super().__init__()
        self.memory = {}

    def visitProg(self, ctx: CalcParser.ProgContext):
        return self.visit(ctx.expr())

    def visitAssign(self, ctx: CalcParser.AssignContext):
        value = self.visit(ctx.expr())
        name = ctx.ID().getText()
        self.memory[name] = value
        return value

    def visitAdd(self, ctx: CalcParser.AddContext):
        return self.visit(ctx.expr()) + self.visit(ctx.term())

    def visitSub(self, ctx: CalcParser.SubContext):
        return self.visit(ctx.expr()) - self.visit(ctx.term())

    def visitMul(self, ctx: CalcParser.MulContext):
        return self.visit(ctx.term()) * self.visit(ctx.factor())

    def visitDiv(self, ctx: CalcParser.DivContext):
        right = self.visit(ctx.factor())
        if right == 0:
            raise ZeroDivisionError("division by zero")
        return self.visit(ctx.term()) // right

    def visitInt(self, ctx: CalcParser.IntContext):
        return int(ctx.INT().getText())

    def visitParens(self, ctx: CalcParser.ParensContext):
        return self.visit(ctx.expr())

    def visitVar(self, ctx: CalcParser.VarContext):
        name = ctx.ID().getText()
        if name not in self.memory:
            raise NameError(f"variable '{name}' is not defined")
        return self.memory[name]
