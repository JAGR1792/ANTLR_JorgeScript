# Generated from Calc.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,56,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,3,1,18,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,
        29,8,2,10,2,12,2,32,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,
        43,8,3,10,3,12,3,46,9,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,54,8,4,1,4,0,
        2,4,6,5,0,2,4,6,8,0,0,57,0,10,1,0,0,0,2,17,1,0,0,0,4,19,1,0,0,0,
        6,33,1,0,0,0,8,53,1,0,0,0,10,11,3,2,1,0,11,12,5,0,0,1,12,1,1,0,0,
        0,13,14,5,8,0,0,14,15,5,1,0,0,15,18,3,4,2,0,16,18,3,4,2,0,17,13,
        1,0,0,0,17,16,1,0,0,0,18,3,1,0,0,0,19,20,6,2,-1,0,20,21,3,6,3,0,
        21,30,1,0,0,0,22,23,10,3,0,0,23,24,5,2,0,0,24,29,3,6,3,0,25,26,10,
        2,0,0,26,27,5,3,0,0,27,29,3,6,3,0,28,22,1,0,0,0,28,25,1,0,0,0,29,
        32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,5,1,0,0,0,32,30,1,0,0,
        0,33,34,6,3,-1,0,34,35,3,8,4,0,35,44,1,0,0,0,36,37,10,3,0,0,37,38,
        5,4,0,0,38,43,3,8,4,0,39,40,10,2,0,0,40,41,5,5,0,0,41,43,3,8,4,0,
        42,36,1,0,0,0,42,39,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,
        0,0,0,45,7,1,0,0,0,46,44,1,0,0,0,47,54,5,9,0,0,48,54,5,8,0,0,49,
        50,5,6,0,0,50,51,3,4,2,0,51,52,5,7,0,0,52,54,1,0,0,0,53,47,1,0,0,
        0,53,48,1,0,0,0,53,49,1,0,0,0,54,9,1,0,0,0,6,17,28,30,42,44,53
    ]

class CalcParser ( Parser ):

    grammarFileName = "Calc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+'", "'-'", "'*'", "'/'", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "WS" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_expr = 2
    RULE_term = 3
    RULE_factor = 4

    ruleNames =  [ "prog", "stmt", "expr", "term", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    ID=8
    INT=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(CalcParser.StmtContext,0)


        def EOF(self):
            return self.getToken(CalcParser.EOF, 0)

        def getRuleIndex(self):
            return CalcParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CalcParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.stmt()
            self.state = 11
            self.match(CalcParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprOnlyContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprOnly" ):
                listener.enterExprOnly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprOnly" ):
                listener.exitExprOnly(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprOnly" ):
                return visitor.visitExprOnly(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CalcParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = CalcParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 17
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = CalcParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.match(CalcParser.ID)
                self.state = 14
                self.match(CalcParser.T__0)
                self.state = 15
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = CalcParser.ExprOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(CalcParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class SubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(CalcParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub" ):
                listener.enterSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub" ):
                listener.exitSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub" ):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)


    class ToTermContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(CalcParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToTerm" ):
                listener.enterToTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToTerm" ):
                listener.exitToTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToTerm" ):
                return visitor.visitToTerm(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalcParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = CalcParser.ToTermContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 20
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 30
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 28
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = CalcParser.AddContext(self, CalcParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 22
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 23
                        self.match(CalcParser.T__1)
                        self.state = 24
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = CalcParser.SubContext(self, CalcParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 25
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 26
                        self.match(CalcParser.T__2)
                        self.state = 27
                        self.term(0)
                        pass

             
                self.state = 32
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DivContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(CalcParser.TermContext,0)

        def factor(self):
            return self.getTypedRuleContext(CalcParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiv" ):
                listener.enterDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiv" ):
                listener.exitDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiv" ):
                return visitor.visitDiv(self)
            else:
                return visitor.visitChildren(self)


    class ToFactorContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(CalcParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToFactor" ):
                listener.enterToFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToFactor" ):
                listener.exitToFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToFactor" ):
                return visitor.visitToFactor(self)
            else:
                return visitor.visitChildren(self)


    class MulContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(CalcParser.TermContext,0)

        def factor(self):
            return self.getTypedRuleContext(CalcParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul" ):
                listener.enterMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul" ):
                listener.exitMul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul" ):
                return visitor.visitMul(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalcParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = CalcParser.ToFactorContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 34
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 44
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 42
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = CalcParser.MulContext(self, CalcParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 36
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 37
                        self.match(CalcParser.T__3)
                        self.state = 38
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = CalcParser.DivContext(self, CalcParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 39
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 40
                        self.match(CalcParser.T__4)
                        self.state = 41
                        self.factor()
                        pass

             
                self.state = 46
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VarContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CalcParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(CalcParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = CalcParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_factor)
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                localctx = CalcParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(CalcParser.INT)
                pass
            elif token in [8]:
                localctx = CalcParser.VarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.match(CalcParser.ID)
                pass
            elif token in [6]:
                localctx = CalcParser.ParensContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.match(CalcParser.T__5)
                self.state = 50
                self.expr(0)
                self.state = 51
                self.match(CalcParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        self._predicates[3] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




