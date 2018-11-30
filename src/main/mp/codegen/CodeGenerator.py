'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from AST import *
class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("getFloat",MType(list(),FloatType()), CName(self.libName)),
                    Symbol("putFloat",MType([FloatType()],VoidType()), CName(self.libName)),
                    Symbol("putFloatLn",MType([FloatType()],VoidType()), CName(self.libName)),
                    Symbol("putBool",MType([BoolType()],VoidType()), CName(self.libName)),
                    Symbol("putBoolLn",MType([BoolType()],VoidType()), CName(self.libName)),
                    Symbol("putString",MType([StringType()],VoidType()), CName(self.libName)),
                    Symbol("putStringLn",MType([StringType()],VoidType()), CName(self.libName)),
                    Symbol("putLn",MType(list(),VoidType()), CName(self.libName))
                    ]


    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

# class StringType(Type):

#     def __str__(self):
#         return "StringType"

#     def accept(self, v, param):
#         return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None

class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None

class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MPClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env)

        for x in ast.decl:
            e = self.visit(x,e)


        fun_ref = list(filter(lambda x: isinstance(x,FuncDecl), ast.decl))

        e.frame = Frame(None, None)
        for fun in fun_ref:
            self.visit(fun, e)
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(),None), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame

        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        if isMain:
            intype = [ArrayPointerType(StringType())]
        else:
            intype = [x.varType for x in consdecl.param]
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))


        if glenv is None:
            glenv = []

        s = SubBody(frame, glenv)
        for x in consdecl.param:
            s = self.visit(x, s)

        for x in consdecl.local:
            s = self.visit(x, s)

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        # visit stmt => dont return
        list(map(lambda x: self.visit(x, s), body))
        
        self.emit.printout(self.emit.jvm.INDENT + 'nop' + self.emit.jvm.END)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        else:
            # self.emit.printout(self.emit.jvm.INDENT + 'nop' + self.emit.jvm.END)
            pass
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope();

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any


        subctxt = o
        frame = subctxt.frame
        if frame is not None:
            frame = Frame(ast.name.name, ast.returnType)
            self.genMETHOD(ast, subctxt.sym, frame)
        else:
            return SubBody(None, [
                    Symbol(ast.name.name, MType([x.varType for x in ast.param], ast.returnType), CName(self.className))
                ] + subctxt.sym)

    def visitVarDecl(self, ast, o):

        subctxt = o
        frame = subctxt.frame

        if frame is None:
            self.emit.printout(self.emit.emitATTRIBUTE(ast.variable.name, ast.varType, False, ""))
            return SubBody(None, [Symbol(ast.variable.name, ast.varType, CName(self.className))] + subctxt.sym)
        else:
            index = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(index, ast.variable.name, ast.varType, frame.getStartLabel(), frame.getEndLabel(), frame))
            return SubBody(frame, [Symbol(ast.variable.name, ast.varType, Index(index))] + subctxt.sym)

    def visitCallExpr(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name.lower(), nenv, lambda x: x.name.lower())
        cname = sym.value.value
        ctype = sym.mtype # model
        params = ctype.partype

        in_ = ("", list())
        for i, arg in enumerate(ast.param):
            '''
            arg: Expr
            '''
            str1, typ1 = self.visit(arg, Access(frame, nenv, False, True))

            if isinstance(typ1, MType):
                
                if not isinstance(typ1.rettype, type(params[i])):
                    in_ = (in_[0] + self.emit.emitI2F(frame), in_[1])
                continue
            if not isinstance(typ1, type(params[i])):
                
                str1 = str1 + self.emit.emitI2F(frame)
            in_ = (in_[0] + str1, in_[1] + [typ1])
            
        # self.emit.printout(in_[0])
        # self.emit.printout(self.emit.emitINVOKESTATIC(
        #     cname + "/" + ast.method.name,
        #     ctype,
        #     frame))

        # return str1, ctype.rettype

        return in_[0] + (self.emit.emitINVOKESTATIC(
            cname + "/" + sym.name,
            ctype,
            frame)), ctype.rettype # xem lai

    def visitCallStmt(self, ast, o):
        #ast: CallStmt
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name.lower(), nenv, lambda x: x.name.lower())
        cname = sym.value.value

        ctype = sym.mtype # model
        params = ctype.partype
        params = ctype.partype

        in_ = ("", list())
        for i, arg in enumerate(ast.param):
            '''
            arg: Expr
            '''
            str1, typ1 = self.visit(arg, Access(frame, nenv, False, True))
           
            if isinstance(typ1, MType):
                
                if not isinstance(typ1.rettype, type(params[i])):
                    in_ = (in_[0] + self.emit.emitI2F(frame), in_[1])
                continue
            if not isinstance(typ1, type(params[i])):

                str1 = str1 + self.emit.emitI2F(frame)
            in_ = (in_[0] + str1, in_[1] + [typ1])
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(
            cname + "/" + sym.name,
            ctype,
            frame))

    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast, o):
        #ast: FloatLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitStringLiteral(self, ast, o):
        #ast: FloatLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST( '"' + ast.value +'"', StringType() ,frame), StringType()

    def visitBooleanLiteral(self, ast, o):
        #ast: FloatLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value).lower() ,frame), BoolType()

    def visitAssign(self, ast, o):
        #lhs:Expr
        #exp:Expr
        #frame: Frame
        #sym: List[Symbol]

        subctxt = o
        frame = subctxt.frame
        sym = subctxt.sym
        # input(ast.exp)
        # input(ast.lhs)
        exp, type_exp = self.visit(ast.exp, Access(frame, sym, False, True))

        lhs, type_lhs = self.visit(ast.lhs, Access(frame, sym, True, True))

        
        if isinstance(type_exp, MType):
            type_exp = type_exp.rettype
            exp = ""

        if not isinstance(type_exp, type(type_lhs)):
            exp = exp + self.emit.emitI2F(frame)

        self.emit.printout(exp+lhs)
    def visitId(self, ast, o):
        subctxt = o
        frame = subctxt.frame
        sym = subctxt.sym
        isLeft = subctxt.isLeft

        res = self.lookup(
            ast.name.lower(),
            sym,
            lambda env: env.name.lower()
        )
        # res = symbol(,,Cname)
        if res is None:
            return None, None

        if isLeft is True:
            if isinstance(res.value, CName):
                varname = res.value.value + '/' +res.name
                code = self.emit.emitPUTSTATIC(varname, res.mtype,frame)
            else:
                code = self.emit.emitWRITEVAR(res.name, res.mtype, res.value.value, frame)

        else:
            if isinstance(res.value, CName):
                varname = res.value.value + '/' +res.name
                code = self.emit.emitGETSTATIC(varname, res.mtype,frame)
            else:
                code = self.emit.emitREADVAR(res.name, res.mtype, res.value.value, frame)

        return code, res.mtype

    def visitBinaryOp(self, ast, o):
        subctxt = o
        frame = subctxt.frame
        sym = subctxt.sym

        left, type_left = self.visit(ast.left, Access(frame, sym, False, True))
        right, type_right = self.visit(ast.right, Access(frame, sym, False, True))
        #input(ast.right)
        op = ast.op.lower()
        if not isinstance(type_left, type(type_right)):
            if isinstance(type_left, FloatType):
                right = right + self.emit.emitI2F(frame)
                type_right = FloatType()
            else:
                left = left + self.emit.emitI2F(frame)
                type_left = FloatType()

        if op in ["+", "-"]:
            code = left + right + self.emit.emitADDOP(op, type_left, frame)
        elif op in ["*"]:
            code = left + right + self.emit.emitMULOP(op, type_left, frame)
        elif op in ["/"]:
            if isinstance(type_left, IntType):
                left = left + self.emit.emitI2F(frame)
                right = right + self.emit.emitI2F(frame)
                type_left = FloatType()
                type_right = FloatType()
            code = left + right + self.emit.emitMULOP(op, type_left, frame)
        elif op in ["<=", ">=", "=", ">", "<", "<>"]:
            code = left + right + self.emit.emitREOP(op, type_left, frame)
            return code, BoolType()
        elif op == "or":
            code = left + right + self.emit.emitOROP(frame)
        elif op == "and":
            code = left + right + self.emit.emitANDOP(frame)
        elif op == "div":
            code = left + right + self.emit.emitDIV(frame)
        elif op == "mod":
            code = left + right + self.emit.emitMOD(frame)
        # and then, or else
        elif op == "andthen":
            falseLabel = frame.getNewLabel()
            endLabel = frame.getNewLabel()
            code = ''
            code = code + left
            # if left = 0 False
            code = code + self.emit.emitIFEQ(falseLabel, frame)
            code = code + right
            code = code + self.emit.emitIFEQ(falseLabel, frame)
            code = code + self.emit.emitPUSHICONST(1, frame)
            code = code + self.emit.emitGOTO(endLabel, frame)
            code = code + self.emit.emitLABEL(falseLabel, frame)
            code = code + self.emit.emitPUSHICONST(0, frame)
            code = code + self.emit.emitLABEL(endLabel, frame)
            type_left = BoolType()

        elif op == "orelse":
            trueLabel = frame.getNewLabel()
            endLabel = frame.getNewLabel()
            code = ''
            code = code + left
            code = code + self.emit.emitIFNE(trueLabel, frame)
            code = code + right
            code = code + self.emit.emitIFNE(trueLabel, frame)
            code = code + self.emit.emitPUSHICONST(0, frame)
            code = code + self.emit.emitGOTO(endLabel, frame)
            code = code + self.emit.emitLABEL(trueLabel, frame)
            code = code + self.emit.emitPUSHICONST(1, frame)
            code = code + self.emit.emitLABEL(endLabel, frame)
            type_left = BoolType()
            

        return code, type_left

    def visitUnaryOp(self, ast, o):
        subctxt = o
        frame = subctxt.frame
        sym = subctxt.sym

        body, type_body = self.visit(ast.body, Access(frame, sym, False, True))
        op = ast.op.lower()

        if op == "not":
            code = body + self.emit.emitNOT(type_body, frame)
        else:
            code = body + self.emit.emitNEGOP(type_body, frame)

        return code, type_body

    def visitIf(self, ast, o):
        subctxt = o
        frame = subctxt.frame
        sym = subctxt.sym

        exp, type_exp = self.visit(ast.expr, Access(frame, sym, False, True))

        self.emit.printout(exp)

        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()

        self.emit.printout(self.emit.emitIFEQ(label1, frame))

        for x in ast.thenStmt:
            self.visit(x, SubBody(frame, sym))

        self.emit.printout(self.emit.emitGOTO(label2, frame))

        self.emit.printout(self.emit.emitLABEL(label1, frame))

        for x in ast.elseStmt:
            self.visit(x, SubBody(frame, sym))

        self.emit.printout(self.emit.emitLABEL(label2, frame))

    def visitWhile(self, ast, o):
        subctxt = o
        frame = subctxt.frame
        sym = subctxt.sym

        frame.enterLoop()
        breakLabel = frame.getBreakLabel()
        continueLabel = frame.getContinueLabel()
        self.emit.printout(self.emit.emitLABEL(continueLabel, frame))

        exp , type_exp = self.visit(ast.exp, Access(frame, sym, False, True))

        self.emit.printout(exp)
        self.emit.printout(self.emit.emitIFEQ(breakLabel, frame))

        for x in ast.sl:
            self.visit(x, SubBody(frame, sym))

        self.emit.printout(self.emit.emitGOTO(continueLabel, frame))

        self.emit.printout(self.emit.emitLABEL(breakLabel, frame))
        frame.exitLoop()

    def visitFor(self, ast, o):
        # if ast.up is False:
        #     condition = BinaryOp(">=", ast.id, ast.expr2)
        # else:
        #     condition = BinaryOp("<=", ast.id, ast.expr2)

        # self.visit(Assign(ast.id, ast.expr1), o)
        # increment = BinaryOp(inrop, ast.id, IntLiteral(1))
        # loop = ast.loop[:] + [increment]
        # self.visit(While(condition, loop), o)

        subctxt = o
        frame = subctxt.frame
        sym = subctxt.sym

        frame.enterLoop()
        breakLabel = frame.getBreakLabel()
        startLabel = frame.getNewLabel()
        continueLabel = frame.getContinueLabel()

        expr1 = ast.expr1
        self.visit(Assign(ast.id, expr1), o)
        self.emit.printout(self.emit.emitLABEL(startLabel, frame))


        if ast.up is False:
            exp, type_exp = self.visit(BinaryOp(">=", ast.id, ast.expr2),o)
        else:
            exp, type_exp = self.visit(BinaryOp("<=", ast.id, ast.expr2),o)

        self.emit.printout(exp)
        self.emit.printout(self.emit.emitIFEQ(breakLabel, frame))

        for x in ast.loop:
            self.visit(x, SubBody(frame, sym))
        self.emit.printout(self.emit.emitGOTO(continueLabel, frame))
            #tang giam 1
        self.emit.printout(self.emit.emitLABEL(continueLabel, frame))


        if ast.up is False:
            expr1= BinaryOp("-", ast.id, IntLiteral(1))
        else:
            expr1=BinaryOp("+", ast.id, IntLiteral(1))

        # input(expr1)
       
        #self.emit.printout(expr1)
        
        self.visit(Assign(ast.id, expr1), o)

        self.emit.printout(self.emit.emitGOTO(startLabel, frame))
        
        self.emit.printout(self.emit.emitLABEL(breakLabel, frame))

        frame.exitLoop()



    def visitWith(self, ast, o):
        subctxt = o
        frame = subctxt.frame
        sym = subctxt.sym

        frame.enterScope(False)
        s = SubBody(frame, sym[:])

        for x in ast.decl:
            s = self.visit(x, s)

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        for x in ast.stmt:
            self.visit(x,s)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))

        frame.exitScope()


    def visitReturn(self, ast, o):
        subctxt = o
        frame = subctxt.frame
        sym = subctxt.sym
        code = ''

        if ast.expr:
            exp , type_exp = self.visit(ast.expr, Access(frame, sym, False, True))
            code += exp
            if not isinstance(type_exp, type(frame.returnType)):
                # func returns Float, while "return Int"
                # other cases, checker

                code += self.emit.emitI2F(frame);
            
        code += self.emit.emitRETURN(frame.returnType, frame)


        self.emit.printout(code)

    def visitBreak(self, ast, o):
        subctxt = o
        frame = subctxt.frame
        sym = subctxt.sym

        breakLabel = frame.getBreakLabel()
        self.emit.printout(self.emit.emitGOTO(breakLabel, frame))


    def visitContinue(self, ast, o):
        subctxt = o
        frame = subctxt.frame
        sym = subctxt.sym

        continueLabel = frame.getContinueLabel()

        self.emit.printout(self.emit.emitGOTO(continueLabel, frame))
