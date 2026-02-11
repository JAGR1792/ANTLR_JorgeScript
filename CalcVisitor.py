# Generated from Calc.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalcParser import CalcParser
else:
    from CalcParser import CalcParser

# This class defines a complete generic visitor for a parse tree produced by CalcParser.

class CalcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalcParser#prog.
    def visitProg(self, ctx:CalcParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#Assign.
    def visitAssign(self, ctx:CalcParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#ExprOnly.
    def visitExprOnly(self, ctx:CalcParser.ExprOnlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#Add.
    def visitAdd(self, ctx:CalcParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#Sub.
    def visitSub(self, ctx:CalcParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#ToTerm.
    def visitToTerm(self, ctx:CalcParser.ToTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#Div.
    def visitDiv(self, ctx:CalcParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#ToFactor.
    def visitToFactor(self, ctx:CalcParser.ToFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#Mul.
    def visitMul(self, ctx:CalcParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#Int.
    def visitInt(self, ctx:CalcParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#Var.
    def visitVar(self, ctx:CalcParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#Parens.
    def visitParens(self, ctx:CalcParser.ParensContext):
        return self.visitChildren(ctx)

    def visitProg(self, ctx: CalcParser.ProgContext):
        return self.visit(ctx.expr())



del CalcParser