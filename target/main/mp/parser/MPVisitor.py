# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#vardecl.
    def visitVardecl(self, ctx:MPParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcdecl.
    def visitFuncdecl(self, ctx:MPParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#procdecl.
    def visitProcdecl(self, ctx:MPParser.ProcdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#paramdecl.
    def visitParamdecl(self, ctx:MPParser.ParamdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#param.
    def visitParam(self, ctx:MPParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp.
    def visitExp(self, ctx:MPParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp1.
    def visitExp1(self, ctx:MPParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp2.
    def visitExp2(self, ctx:MPParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp3.
    def visitExp3(self, ctx:MPParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp4.
    def visitExp4(self, ctx:MPParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp5.
    def visitExp5(self, ctx:MPParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp6.
    def visitExp6(self, ctx:MPParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#indexexp.
    def visitIndexexp(self, ctx:MPParser.IndexexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#invocationexp.
    def visitInvocationexp(self, ctx:MPParser.InvocationexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#listexpression.
    def visitListexpression(self, ctx:MPParser.ListexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#statements.
    def visitStatements(self, ctx:MPParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#linestatement.
    def visitLinestatement(self, ctx:MPParser.LinestatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#blockstatement.
    def visitBlockstatement(self, ctx:MPParser.BlockstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignmentstm.
    def visitAssignmentstm(self, ctx:MPParser.AssignmentstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignments.
    def visitAssignments(self, ctx:MPParser.AssignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ifstm.
    def visitIfstm(self, ctx:MPParser.IfstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#whilestm.
    def visitWhilestm(self, ctx:MPParser.WhilestmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#forstm.
    def visitForstm(self, ctx:MPParser.ForstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#breakstm.
    def visitBreakstm(self, ctx:MPParser.BreakstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#continuestm.
    def visitContinuestm(self, ctx:MPParser.ContinuestmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#returnstm.
    def visitReturnstm(self, ctx:MPParser.ReturnstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compoundstm.
    def visitCompoundstm(self, ctx:MPParser.CompoundstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#withstm.
    def visitWithstm(self, ctx:MPParser.WithstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#callstm.
    def visitCallstm(self, ctx:MPParser.CallstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#mptype.
    def visitMptype(self, ctx:MPParser.MptypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#primitivetype.
    def visitPrimitivetype(self, ctx:MPParser.PrimitivetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compoundtype.
    def visitCompoundtype(self, ctx:MPParser.CompoundtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#arrayvalue.
    def visitArrayvalue(self, ctx:MPParser.ArrayvalueContext):
        return self.visitChildren(ctx)



del MPParser