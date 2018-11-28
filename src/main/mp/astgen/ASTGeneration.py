from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
from functools import reduce

def flatten(lst):
    return reduce(lambda x,y: x + list(y),lst,[])

class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        numChild = ctx.getChildCount() - 1
        return Program(flatten([self.visit(ctx.getChild(x)) for x in range(numChild)]))

    def visitParam(self,ctx:MPParser.ParamContext):
        idList = [Id(x.getText()) for x in ctx.ID()]
        mptype = self.visit(ctx.mptype())
        return [VarDecl(id,mptype) for id in idList]

    def visitParamdecl(self,ctx:MPParser.ParamdeclContext):
        return flatten([self.visit(param) for param in ctx.param()])

    def visitVardecl(self,ctx:MPParser.VardeclContext):
        return flatten([self.visit(param) for param in ctx.param()])

    def visitMptype(self,ctx:MPParser.MptypeContext):
        return self.visit(ctx.getChild(0))

    def visitPrimitivetype(self,ctx:MPParser.PrimitivetypeContext):
        if ctx.INTEGER():
            return IntType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.REAL():
            return FloatType()
        elif ctx.STRING():
            return StringType()

    def visitFuncdecl(self,ctx:MPParser.FuncdeclContext):
        id = Id(ctx.ID().getText())
        param = self.visit(ctx.paramdecl()) if ctx.paramdecl() else[]
        mptype = self.visit(ctx.mptype())
        var = self.visit(ctx.vardecl()) if ctx.vardecl() else []
        body = flatten([self.visit(ctx.compoundstm())])
        
        return [FuncDecl(id, param, var, body, mptype)]

    def visitProcdecl(self,ctx:MPParser.ProcdeclContext):
        id = Id(ctx.ID().getText())
        param = self.visit(ctx.paramdecl()) if ctx.paramdecl() else[]
        var = self.visit(ctx.vardecl()) if ctx.vardecl() else []
        body = flatten([self.visit(ctx.compoundstm())])
        
        return [FuncDecl(id, param, var, body)]

    def visitCompoundstm(self,ctx:MPParser.CompoundstmContext):
        return flatten([self.visit(x) for x in ctx.statements()])

    def visitStatements(self, ctx:MPParser.StatementsContext):
        return self.visit(ctx.getChild(0))

    def visitLinestatement(self, ctx:MPParser.LinestatementContext):
        if ctx.assignmentstm():
            return self.visit(ctx.assignmentstm())
        return [self.visit(ctx.getChild(0))]

    def visitBlockstatement(self, ctx:MPParser.BlockstatementContext):
        if ctx.compoundstm():
            return self.visit(ctx.compoundstm())
        return [self.visit(ctx.getChild(0))]

    def visitAssignmentstm(self, ctx:MPParser.AssignmentstmContext):
        lhs_list = self.visit(ctx.assignments())
        exp = self.visit(ctx.exp())

        rhs_list = lhs_list[1:] + [exp]

        return [Assign(lhs, rhs) for lhs, rhs in zip(lhs_list, rhs_list)][::-1]


    def visitAssignments(self, ctx:MPParser.AssignmentsContext):
        childCount = ctx.getChildCount()
        lhs_list = []
        for i in range(0,childCount,2):
            lhs = self.visit(ctx.getChild(i))
            if lhs is None:
                lhs = Id(ctx.getChild(i).getText())
            lhs_list.append(lhs)
        return lhs_list

    def visitIfstm(self, ctx:MPParser.IfstmContext):
        exp = self.visit(ctx.exp())
        if ctx.ELSE():
            thenstm = self.visit(ctx.statements(0))
            elsestm = self.visit(ctx.statements(1))
        else:
            thenstm = self.visit(ctx.statements(0))
            elsestm = []
        return If(exp, thenstm, elsestm)

    def visitWhilestm(self, ctx:MPParser.WhilestmContext):
        exp = self.visit(ctx.exp())
        stm = self.visit(ctx.statements())
        return While(exp, stm)

    def visitForstm(self, ctx:MPParser.ForstmContext):
        id = Id(ctx.ID().getText())
        exp_1 = self.visit(ctx.exp(0))
        exp_2 = self.visit(ctx.exp(1))
        stm = self.visit(ctx.statements())
        if ctx.TO():
            up = True
        else: up = False
        return For(id, exp_1, exp_2, up, stm)

    def visitBreakstm(self, ctx:MPParser.BreakstmContext):
        return Break()

    def visitContinuestm(self, ctx:MPParser.ContinuestmContext):
        return Continue()

    def visitReturnstm(self, ctx:MPParser.ReturnstmContext):
        if ctx.exp():
            exp = self.visit(ctx.exp())
        else: exp = None
        return Return(exp)

    def visitWithstm(self, ctx:MPParser.WithstmContext):
        param = flatten([self.visit(param) for param in ctx.param()])
        stm = self.visit(ctx.statements())
        return With(param, stm)

    def visitCallstm(self, ctx:MPParser.CallstmContext):
        return CallStmt(Id(ctx.ID().getText()),
            self.visit(ctx.listexpression()))

    def visitExp6(self, ctx:MPParser.Exp6Context):
        if ctx.getChildCount() == 1:
            if ctx.ID():
                return Id(ctx.ID().getText())
            elif ctx.INTLIT():
                return IntLiteral(ctx.INTLIT().getText())
            elif ctx.BOOLEANLIT():
                boolit = ctx.BOOLEANLIT().getText().lower()
                if boolit == "true":
                    return BooleanLiteral(True)
                else:
                    return BooleanLiteral(False)
            elif ctx.REALLIT():
                return FloatLiteral(float(ctx.REALLIT().getText()))
            elif ctx.STRINGLIT(): 
                return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.getChildCount() == 3:
            return self.visit(ctx.exp())
        else: return CallExpr(Id(ctx.ID().getText()),self.visit(ctx.invocationexp()))

    def visitInvocationexp(self, ctx:MPParser.InvocationexpContext):
        return self.visit(ctx.listexpression()) if ctx.listexpression() else []

    def visitListexpression(self, ctx:MPParser.ListexpressionContext):
        return [self.visit(x) for x in ctx.exp()]

    def visitExp(self, ctx:MPParser.ExpContext):
        if ctx.getChildCount() == 1: 
            return self.visit(ctx.exp1())
        elif ctx.AND():
            op = "andthen"
        else: op = "orelse"
        exp = self.visit(ctx.exp())
        exp1 = self.visit(ctx.exp1())
        return BinaryOp(op, exp, exp1)

    def visitExp1(self, ctx:MPParser.Exp1Context):
        if ctx.getChildCount() == 1: 
            return self.visit(ctx.exp2(0))

        op = ctx.getChild(1).getText()
        exp2_1 = self.visit(ctx.exp2(0))
        exp2_2 = self.visit(ctx.exp2(1))
        return BinaryOp(op, exp2_1, exp2_2)

    def visitExp2(self, ctx:MPParser.Exp2Context):
        
        if ctx.getChildCount() == 1: 
            return self.visit(ctx.exp3())
        op = ctx.getChild(1).getText()
        exp2 = self.visit(ctx.exp2())
        exp3 = self.visit(ctx.exp3())
        return BinaryOp(op, exp2, exp3)

    def visitExp3(self, ctx:MPParser.Exp3Context):
        if ctx.getChildCount() == 1: 
            return self.visit(ctx.exp4())
        op = ctx.getChild(1).getText()
        exp3 = self.visit(ctx.exp3())
        exp4 = self.visit(ctx.exp4())
        return BinaryOp(op, exp3, exp4)

    def visitExp4(self, ctx:MPParser.Exp4Context):
        if ctx.getChildCount() == 1: 
            return self.visit(ctx.exp5())
        op = ctx.getChild(0).getText()
        exp4 = self.visit(ctx.exp4())
        return UnaryOp(op, exp4)

    def visitExp5(self, ctx:MPParser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp6())
        exp5 = self.visit(ctx.exp5())
        exp = self.visit(ctx.exp())

        return ArrayCell(exp5, exp)

    def visitIndexexp(self, ctx:MPParser.IndexexpContext):
        exp5 = self.visit(ctx.exp5())
        exp = self.visit(ctx.exp())
        return ArrayCell(exp5, exp)

    def visitCompoundtype(self,ctx:MPParser.CompoundtypeContext):
        lower,upper = self.visit(ctx.arrayvalue())
        type = self.visit(ctx.primitivetype())
        return ArrayType(lower, upper, type)

    def visitArrayvalue(self, ctx:MPParser.ArrayvalueContext):
        lower = int(ctx.INTLIT(0).getText())
        upper = int(ctx.INTLIT(1).getText())
        sub = len(ctx.SUB())

        if sub == 0:
            pass
        elif sub == 2:
            lower = -lower
            upper = -upper
        elif ctx.getChild(1).getText() == "-":
            lower = -lower
        else: upper = -upper
        return int(lower), int(upper)

    