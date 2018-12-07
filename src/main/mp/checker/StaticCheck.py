
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype
    def __str__(self):
        return 'MPType([' + ','.join(str(i) for i in self.partype) + "]" +',' + str(self.rettype) + ")"
class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return 'Symbol(' + self.name + ',' + str(self.mtype) + ')'

class StaticChecker(BaseVisitor,Utils):

    global_envi =  [Symbol("getInt",MType([],IntType())),
                    Symbol("putInt",MType([IntType()],IntType())),
    			    Symbol("putIntLn",MType([IntType()],VoidType())),
                    Symbol("getFloat",MType([],FloatType())),
                    Symbol("putFloat",MType([FloatType()],VoidType())),
                    Symbol("putFloatLn",MType([FloatType()],VoidType())),
                    Symbol("putBool",MType([BoolType()],VoidType())),
                    Symbol("putBoolLn",MType([BoolType()],VoidType())),
                    Symbol("putString",MType([StringType()],VoidType())),
                    Symbol("putStringLn",MType([StringType()],VoidType())),
                    Symbol("putLn",MType([],VoidType())),
                    ]


    def __init__(self,ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def checkRedeclared(self, sym, kind, env):
        if self.lookup(sym.name.lower(), env, lambda x: x.name.lower()):
            raise Redeclared(kind, sym.name)
        else:
            return sym


    def merge(self, a, b):
        name_list = [x.name.lower() for x in a]
        for x in b:
            if x.name.lower() not in name_list:
                a += [x]
        return a


    def visitProgram(self, ast, env):

        proc_ref = 0
        for x in ast.decl:
            if isinstance(x, FuncDecl):
                if isinstance(x.returnType, VoidType) and x.name.name.lower() == "main" and len(x.param) == 0:
                    proc_ref = 1
        # input(proc_ref)
        if proc_ref == 0:
            raise NoEntryPoint()

        global_ref = env[:]
        for x in ast.decl:
            if not isinstance(x, FuncDecl):
                global_ref += [self.visit(x, global_ref)]
            else:
                kind = Procedure() if type(x.returnType) is VoidType else Function()
                global_ref += [self.checkRedeclared(
                    Symbol(
                        x.name.name,
                        MType(
                            [i.varType for i in x.param],
                            x.returnType
                        )
                    ),
                    kind,
                    global_ref
                )]


        fun_ref = filter(lambda x: isinstance(x,FuncDecl), ast.decl)
        for fun in fun_ref:
            self.visit(fun, global_ref)

        return global_ref

    def visitFuncDecl(self, ast, env):

        listlocal = []
        for param in ast.param:
            # try except de raise lai Redeclared(Parameter)
            try:
                listlocal += [self.visit(param, listlocal)]
            except Redeclared as e:
                raise Redeclared(Parameter(), e.n)
        for var in ast.local:
            listlocal += [self.visit(var, listlocal)]

        #listlocal = merge(listlocal, env)

        isReturn = False
        for stmt in ast.body:
            if self.visit(stmt, (listlocal + env, False, ast.returnType)) is True:
                isReturn = True

        if not isinstance(ast.returnType, VoidType):
            if isReturn is False:
                raise FunctionNotReturn(ast.name.name)

    def visitVarDecl(self, ast, c):
        return self.checkRedeclared(
            Symbol(
                ast.variable.name, ast.varType),
                Variable(),
                c)

    def visitIntLiteral(self,ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitBinaryOp(self, ast, env):
        left = self.visit(ast.left, env)
        right = self.visit(ast.right, env)
        op = ast.op.lower()
        def CheckType(acceptType, returnType = None):
            if not isinstance(left, acceptType) or\
               not isinstance(right, acceptType):
                raise TypeMismatchInExpression(ast)

            if returnType:
                return returnType
            if isinstance(left, FloatType) and isinstance(right, (IntType, FloatType)):
                return FloatType()
            if isinstance(left, IntType) and isinstance(right, FloatType):
                return FloatType()
            if isinstance(left, type(right)):
                return left
            else:
                raise TypeMismatchInExpression(ast)
        if op == '/':
            return CheckType((FloatType, IntType), FloatType())
        if op in ['+', '-', '*']:
            return CheckType((FloatType, IntType))
        if op in ['div', 'mod']:
            return CheckType((IntType), IntType())
        if op in ['and', 'or', 'andthen', 'orelse']:
            return CheckType((BoolType), BoolType())
        if op in ['<', '<=', '=', '>=', '>', '<>']:
            return CheckType((IntType, FloatType), BoolType())

    def visitUnaryOp(self, ast, env):
        op = ast.op.lower()
        exp = self.visit(ast.body, env)

        if op in ['not']:
            if not isinstance(exp, BoolType):
                raise TypeMismatchInExpression(ast)
            else:
                return BoolType()

        if op in ['-']:
            if not isinstance(exp, (IntType, FloatType)):
                raise TypeMismatchInExpression(ast)
            else:
                return exp



    def visitAssign(self, ast, c):
        '''
        ast: Assign
        env: (List[Symbol], bool inloop, returnType)
        raise TypeMismatchInStatement
            Float := Float/Int
            Int := Int
            Bool := Bool
        => Returned?
        '''

        #visit Expression
        left = self.visit(ast.lhs, c[0])
        exp = self.visit(ast.exp, c[0])

        if isinstance(left, StringType) or isinstance(left, ArrayType):
            raise TypeMismatchInStatement(ast)

        elif isinstance(left, FloatType):
            if not isinstance(exp, (FloatType, IntType)):
                raise TypeMismatchInStatement(ast)

        elif isinstance(left, IntType):
            if not isinstance(exp, IntType):
                raise TypeMismatchInStatement(ast)

        elif isinstance(left, BoolType):
            if not isinstance(exp, BoolType):
                raise TypeMismatchInStatement(ast)

        return False

    def visitArrayCell(self, ast, env):
        arr = self.visit(ast.arr, env)
        idx = self.visit(ast.idx, env)

        if not isinstance(idx, IntType):
            raise TypeMismatchInExpression(ast)
        if not isinstance(arr, ArrayType):
            raise TypeMismatchInExpression(ast)

        return arr.eleType

    def visitId(self, ast, c):

        '''
        ast: Id
        param: List[Symbol] or [List[Symbol], kind]
        raise Undeclared
        => Type: Symbol.mtype
        '''

        kind = Identifier() if not isinstance(c, tuple) else c[1]
        env = c if not isinstance(c, tuple) else c[0]
        res = self.lookup(ast.name.lower(), env, lambda x: x.name.lower())

        if res is None:
            raise Undeclared(kind,ast.name)

        if isinstance(kind, Identifier):
            if isinstance(res.mtype, MType):
                raise Undeclared(kind, ast.name)
            return res.mtype

        if isinstance(kind, Function):
            if not isinstance(res.mtype, MType) or isinstance(res.mtype.rettype, VoidType):
                raise Undeclared(kind, ast.name)
        if isinstance(kind, Procedure):
            if not isinstance(res.mtype, MType) or not isinstance(res.mtype.rettype, VoidType):
                raise Undeclared(kind, ast.name)

        return res.mtype

    def visitIf(self, ast, c):
        exp_type = self.visit(ast.expr, c[0])
        if not isinstance(exp_type, BoolType):
            raise TypeMismatchInStatement(ast)

        isReturnThen = False
        isReturnElse = False
        for stmt in ast.thenStmt:
            if isinstance(stmt, Return):
                isReturnThen = True
            self.visit(stmt, c)
        for stmt in ast.elseStmt:
            if isinstance(stmt, Return):
                isReturnElse = True
            self.visit(stmt, c)

        if isReturnThen is True and isReturnElse is True:
            return True
        else:
            return False

    def visitWhile(self, ast, c):
        exp_type = self.visit(ast.exp, c[0])
        if not isinstance(exp_type, BoolType):
            raise TypeMismatchInStatement(ast)

        #isReturn = False
        outFlag = False
        for stmt in ast.sl:
            # if isinstance(stmt, Return):
            #     isReturn = True
            if self.visit(stmt, (c[0], True, c[2])):
                outFlag = True

        return False

    def visitBreak(self, ast, c):
        if c[1] is False:
            raise BreakNotInLoop(ast)
        return True

    def visitContinue(self, ast, c):
        if c[1] is False:
            raise ContinueNotInLoop(ast)
        return True

    def visitReturn(self, ast, c):
        if ast.expr is None:
            if not isinstance(c[2],VoidType):
                raise TypeMismatchInStatement(ast)

        elif isinstance(c[2], VoidType):
            raise TypeMismatchInStatement(ast)
        else:
            res = self.visit(ast.expr, c[0])
            if isinstance(c[2], FloatType):
                if not isinstance(res, (FloatType, IntType)):
                    raise TypeMismatchInStatement(ast)
            elif not isinstance(res, type(c[2])):
                raise TypeMismatchInStatement(ast)
            elif isinstance(c[2], ArrayType):
                if not isinstance(res, ArrayType):
                    raise TypeMismatchInStatement(ast)
                else:

                    if res.lower != c[2].lower or\
                    res.upper != c[2].upper or\
                    not isinstance(res.eleType, type(c[2].eleType)):
                        raise TypeMismatchInStatement(ast)

        return True


    def visitWith(self, ast, c):
        localBlock = []
        for decl in ast.decl:
            localBlock += [self.visit(decl, localBlock)]

        localBlock += c[0]
        isReturn = False
        for stmt in ast.stmt:
            if isinstance(stmt, Return):
                isReturn = True
            self.visit(stmt, (localBlock ,c[1], c[2]))

        return isReturn

    def checkType(self, left, right, ast, kind):
        if isinstance(left, ArrayType):
            if not isinstance(right, ArrayType):
                if type(kind) is Procedure:
                    raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInExpression(ast)
            if left.upper != right.upper or \
               left.lower != right.lower or \
               not isinstance(left.eleType, type(right.eleType)):
                if type(kind) is Procedure:
                    raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInExpression(ast)

        elif isinstance(left, FloatType):
            if not isinstance(right, (FloatType, IntType)):
                if type(kind) is Procedure:
                    raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInExpression(ast)

        elif not isinstance(left, type(right)):
            if type(kind) is Procedure:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)

    def callBody(self, ast, c):
        '''
        c: List[Symbol]
        '''
        at = [self.visit(x,c) for x in ast.param]
        kind = Function() if isinstance(ast, CallExpr) else Procedure()
        res = self.visit(ast.method, (c, kind))
        if res is None:
            raise Undeclared(kind, ast.method.name)
        elif not isinstance(res, MType):
            if type(kind) is Procedure:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        if len(res.partype) != len(at):
            if type(kind) is Procedure:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)

        for x in zip(res.partype, at):
            left = x[0]
            right = x[1]
            self.checkType(left, right, ast, kind)
        return res.rettype

    def visitCallStmt(self, ast, c):
        '''
        c: ()
        '''
        return self.callBody(ast, c[0])

    def visitCallExpr(self, ast, c):
        return self.callBody(ast, c)

    def visitFor(self, ast, env):
        '''
        env = (List[Symbol], Inloop, Rettype)
        '''
        id_type = self.visit(ast.id, env[0])
        expr1_type = self.visit(ast.expr1, env[0])
        expr2_type = self.visit(ast.expr2, env[0])

        if not isinstance(id_type, IntType) or \
           not isinstance(expr1_type, IntType) or \
           not isinstance(expr2_type, IntType):
            raise TypeMismatchInStatement(ast)

        #isReturn = False
        outFlag = False
        for stmt in ast.loop:
            # if isinstance(stmt, Return):
            #     isReturn = True
            if self.visit(stmt, (env[0], True, env[2])):
                outFlag = True
        return False