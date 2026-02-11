# Generated from Calc.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalcParser import CalcParser
else:
    from CalcParser import CalcParser

# This class defines a complete listener for a parse tree produced by CalcParser.
class CalcListener(ParseTreeListener):

    # Enter a parse tree produced by CalcParser#prog.
    def enterProg(self, ctx:CalcParser.ProgContext):
        pass

    # Exit a parse tree produced by CalcParser#prog.
    def exitProg(self, ctx:CalcParser.ProgContext):
        pass


    # Enter a parse tree produced by CalcParser#Assign.
    def enterAssign(self, ctx:CalcParser.AssignContext):
        pass

    # Exit a parse tree produced by CalcParser#Assign.
    def exitAssign(self, ctx:CalcParser.AssignContext):
        pass


    # Enter a parse tree produced by CalcParser#ExprOnly.
    def enterExprOnly(self, ctx:CalcParser.ExprOnlyContext):
        pass

    # Exit a parse tree produced by CalcParser#ExprOnly.
    def exitExprOnly(self, ctx:CalcParser.ExprOnlyContext):
        pass


    # Enter a parse tree produced by CalcParser#Add.
    def enterAdd(self, ctx:CalcParser.AddContext):
        pass

    # Exit a parse tree produced by CalcParser#Add.
    def exitAdd(self, ctx:CalcParser.AddContext):
        pass


    # Enter a parse tree produced by CalcParser#Sub.
    def enterSub(self, ctx:CalcParser.SubContext):
        pass

    # Exit a parse tree produced by CalcParser#Sub.
    def exitSub(self, ctx:CalcParser.SubContext):
        pass


    # Enter a parse tree produced by CalcParser#ToTerm.
    def enterToTerm(self, ctx:CalcParser.ToTermContext):
        pass

    # Exit a parse tree produced by CalcParser#ToTerm.
    def exitToTerm(self, ctx:CalcParser.ToTermContext):
        pass


    # Enter a parse tree produced by CalcParser#Div.
    def enterDiv(self, ctx:CalcParser.DivContext):
        pass

    # Exit a parse tree produced by CalcParser#Div.
    def exitDiv(self, ctx:CalcParser.DivContext):
        pass


    # Enter a parse tree produced by CalcParser#ToFactor.
    def enterToFactor(self, ctx:CalcParser.ToFactorContext):
        pass

    # Exit a parse tree produced by CalcParser#ToFactor.
    def exitToFactor(self, ctx:CalcParser.ToFactorContext):
        pass


    # Enter a parse tree produced by CalcParser#Mul.
    def enterMul(self, ctx:CalcParser.MulContext):
        pass

    # Exit a parse tree produced by CalcParser#Mul.
    def exitMul(self, ctx:CalcParser.MulContext):
        pass


    # Enter a parse tree produced by CalcParser#Int.
    def enterInt(self, ctx:CalcParser.IntContext):
        pass

    # Exit a parse tree produced by CalcParser#Int.
    def exitInt(self, ctx:CalcParser.IntContext):
        pass


    # Enter a parse tree produced by CalcParser#Var.
    def enterVar(self, ctx:CalcParser.VarContext):
        pass

    # Exit a parse tree produced by CalcParser#Var.
    def exitVar(self, ctx:CalcParser.VarContext):
        pass


    # Enter a parse tree produced by CalcParser#Parens.
    def enterParens(self, ctx:CalcParser.ParensContext):
        pass

    # Exit a parse tree produced by CalcParser#Parens.
    def exitParens(self, ctx:CalcParser.ParensContext):
        pass



del CalcParser