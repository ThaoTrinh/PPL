import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """var a, b: integer; c: real;
            var f: array [1 .. 5] of integer;
            function foo(x: integer; c: real): real;
                var a, b: integer; n: real;
                begin
                    with s:boolean; do 
                        return 5;
                end
            procedure main(); 
                begin
                    for a:=1 to 5 do
                        for b:=8 downto 2 do
                            a:=2;
                            for b:=1 to 9 do
                                begin
                                end
                    foo(a, b);
                end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_simple_function(self):
        """More complex program"""
        input = """function foo ():INTEGER; begin
            putIntLn(4);
        end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """procedure main (); begin
            getIntLn();
        end
        function foo ():INTEGER; begin
            putIntLn(4);
        end"""
        expect = str(Program([
                FuncDecl(Id("main"),[],[],[CallStmt(Id("getIntLn"),[])]),
                FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_single_var_arr(self):
        """More complex program"""
        input = """var a:array [1 .. 2] of integer;"""
        expect = str(Program([
            VarDecl(Id("a"),
            ArrayType(1,2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_single_var(self):
        """More complex program"""
        input = """var a:integer;"""
        expect = str(Program([VarDecl(Id("a"),IntType())]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_multi_var(self):
        """More complex program"""
        input = """var a,b,c:integer;
                        d: real;
                    var e: integer;"""
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType()),VarDecl(Id("d"),FloatType()),VarDecl(Id("e"),IntType())]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test_ifstm(self):
        """More complex program"""
        input =""" function foo ():BOOLEAN; 
        begin
            if a = 9 then
            begin
                bar(TrUe AND tHeN false);
            end
        end
        """
        expect = str(Program([   
            FuncDecl(
                Id("foo"),
                [],
                [],
                [
                    If(BinaryOp('=',Id("a"),IntLiteral(9)),
                    [
                        CallStmt(Id("bar"),
                        [
                            BinaryOp('andthen',BooleanLiteral(True),BooleanLiteral(False))
                        ])
                    ],
                    [])
                ],
                BoolType()
            )
            ]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_function_simple_var(self):
        """More complex program"""
        input = """function main (a:integer):integer;
        var i:integer;
        begin
            getIntLn();
        end"""
        expect = str(Program([
            FuncDecl(
                Id("main"),
                [VarDecl(Id("a"),IntType())],
                [VarDecl(Id("i"),IntType())],[CallStmt(Id("getIntLn"),[])],
                IntType()
                )
                ]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_while(self):
        """More complex program"""
        input = """function main (a:integer):integer;
        var i:integer;
        begin
            while a > b do getIntLn();
        end"""
        expect = str(Program([
            FuncDecl(
                Id("main"),
                [VarDecl(Id("a"),IntType())],
                [VarDecl(Id("i"),IntType())],
                [While(
                    BinaryOp('>',Id("a"),Id("b")),[CallStmt(Id("getIntLn"),[])])],
                    
                IntType()    
                )]))
        self.assertTrue(TestAST.test(input,expect,308))

    def test_for(self):
        """More complex program"""
        input = """function main (a:integer):integer;
        var i:integer;
        begin
            for i := 3 TO 7 do print("a");
        end"""
        expect = str(Program([
            FuncDecl(
                Id("main"),
                [VarDecl(Id("a"),IntType())],
                [VarDecl(Id("i"),IntType())],[For(Id("i"),IntLiteral(3),IntLiteral(7),True,
                [CallStmt(Id("print"),[StringLiteral("a")])])],
                IntType()
                )
                
                ]))
        self.assertTrue(TestAST.test(input,expect,309))

    def test_return(self):
        """More complex program"""
        input = """function main (a:integer):integer;
        var i:integer;
        begin
            for i := 3 TO 7 do return 5;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),[VarDecl(Id("a"),IntType())],
            [VarDecl(Id("i"),IntType())],
            [For(Id("i"),IntLiteral(3),IntLiteral(7),True,
            [Return(IntLiteral(5))])],
            IntType()
            )]))
        self.assertTrue(TestAST.test(input,expect,310))

    def test_multi(self): # xem cho nay cai 1.e1
        """More complex program"""
        input = """procedure main (a:integer);
        var i:integer;
        begin
            for i := 3 TO 7 do print(5 + 4 + 1.e1); 
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
            [VarDecl(Id("a"),IntType())],
            [VarDecl(Id("i"),IntType())],
            [For(Id("i"),IntLiteral(3),IntLiteral(7),True,
            [CallStmt(Id("print"),[BinaryOp('+',BinaryOp('+',IntLiteral(5),IntLiteral(4)),FloatLiteral(1.e1))])])])]))
        self.assertTrue(TestAST.test(input,expect,311))

    def test_with(self): # xem cho nay cai 1.e1
        """More complex program"""
        input = """function main (a:integer):integer;
        var i:integer;
        begin
            with i : integer; dO return 5 + 1.e1;
        end"""
        expect = str(Program([
            FuncDecl(
                Id("main"),
                [VarDecl(Id("a"),IntType())],
                [VarDecl(Id("i"),IntType())],
                [With(
                    [VarDecl(Id("i"),IntType())],
                    [Return(BinaryOp('+',IntLiteral(5),FloatLiteral(1.e1)))])],
                    IntType()
                    )]))
        self.assertTrue(TestAST.test(input,expect,312))

    def test_callExpr(self): # xem cho nay cai 1.e1
        """More complex program"""
        input = """function main (a:integer):integer;
        var i:array [1 .. 2] of integer;
        begin
            return a + foo();
        end"""
        expect = str(Program([
            FuncDecl(
                Id("main"),
                [VarDecl(Id("a"),IntType())],
                [VarDecl(Id("i"),ArrayType(1,2,IntType()))],[Return(BinaryOp('+',Id("a"),CallExpr(Id("foo"),[])))],
                IntType()
                )]))
        self.assertTrue(TestAST.test(input,expect,313))

    def test_assign(self): # xem cho nay cai 1.e1
        """More complex program"""
        input = """Procedure main (a:integer);
        var i:integer;
        begin
            a:=b:=c:=1;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
            [VarDecl(Id("a"),IntType())],
            [VarDecl(Id("i"),IntType())],[Assign(Id("c"),IntLiteral(1)),Assign(Id("b"),Id("c")),Assign(Id("a"),Id("b"))])]))
        self.assertTrue(TestAST.test(input,expect,314))

    def test_mix(self): # xem cho nay cai 1.e1
        """More complex program"""
        input = """pROcedure _1(A,__b,c_2:INTEGER; x,y,z:array[1 .. 3] of BOOLEAN) ;
                var x_, _y_, z : real; m,n: INTEGER;
                begin
                end"""
        expect = str(Program([
            FuncDecl(
                Id("_1"),
                [VarDecl(Id("A"),IntType()),
                VarDecl(Id("__b"),IntType()),
                VarDecl(Id("c_2"),IntType()),
                VarDecl(Id("x"),ArrayType(1,3,BoolType())),
                VarDecl(Id("y"),ArrayType(1,3,BoolType())),
                VarDecl(Id("z"),ArrayType(1,3,BoolType()))],
                [VarDecl(Id("x_"),
                FloatType()),
                VarDecl(Id("_y_"),FloatType()),
                VarDecl(Id("z"),FloatType()),
                VarDecl(Id("m"),IntType()),
                VarDecl(Id("n"),IntType())],[])]))
        self.assertTrue(TestAST.test(input,expect,315))

    def test_multi_var_decl4(self):
        input = """
                var a,k,t,y:integer;
                    b,l,m,n: array [1 .. 2] of string;
                var c,x,z: array [1 .. 2] of boolean;
                    d,y: boolean;
                    e,_something,something: array [1 .. 4] of real;
                procedure main();
                    var g,h:integer;
                        i:array[1 .. 2] of string;
                begin
                end"""
        expect = str(Program([
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("k"),IntType()),
            VarDecl(Id("t"),IntType()),
            VarDecl(Id("y"),IntType()),
            VarDecl(Id("b"),ArrayType(1,2,StringType())),VarDecl(Id("l"),ArrayType(1,2,StringType())),VarDecl(Id("m"),ArrayType(1,2,StringType())),VarDecl(Id("n"),ArrayType(1,2,StringType())),VarDecl(Id("c"),ArrayType(1,2,BoolType())),VarDecl(Id("x"),ArrayType(1,2,BoolType())),VarDecl(Id("z"),ArrayType(1,2,BoolType())),VarDecl(Id("d"),BoolType()),VarDecl(Id("y"),BoolType()),
            VarDecl(Id("e"),ArrayType(1,4,FloatType())),VarDecl(Id("_something"),ArrayType(1,4,FloatType())),
            VarDecl(Id("something"),ArrayType(1,4,FloatType())),
            FuncDecl(Id("main"),[],
            [VarDecl(Id("g"),IntType()),
            VarDecl(Id("h"),IntType()),
            VarDecl(Id("i"),ArrayType(1,2,StringType()))],[])]))
        self.assertTrue(TestAST.test(input,expect,316))

    def test_function_decl1(self):
        input = """function foo(a, b: integer ; c: real):array [1 .. 2] of integer ;
                var c,x,z: array [1 .. 2] of boolean;
                    d,y: boolean;
                    e,_something,something: array [1 .. 4] of real;
                BEGIN
                END     
                """
        expect = str(Program([
            FuncDecl(Id("foo"),
            [VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),FloatType())],
            [VarDecl(Id("c"),ArrayType(1,2,BoolType())),
            VarDecl(Id("x"),ArrayType(1,2,BoolType())),
            VarDecl(Id("z"),ArrayType(1,2,BoolType())),
            VarDecl(Id("d"),BoolType()),VarDecl(Id("y"),BoolType()),
            VarDecl(Id("e"),ArrayType(1,4,FloatType())),
            VarDecl(Id("_something"),ArrayType(1,4,FloatType())),
            VarDecl(Id("something"),ArrayType(1,4,FloatType()))],[],
            ArrayType(1,2,IntType()),
            )]))
        self.assertTrue(TestAST.test(input,expect,317))

    def test_procedure_decl2(self):
        input = """
                procedure foo() ;
                var c,x,z: array [1 .. 2] of boolean;
                    d,y: boolean;
                    e,_something,something: array [15 .. 4] of real;
                BEGIN
                END"""
        expect = str(Program([
            FuncDecl(Id("foo"),[],
            [
            VarDecl(Id("c"),ArrayType(1,2,BoolType())),
            VarDecl(Id("x"),ArrayType(1,2,BoolType())),
            VarDecl(Id("z"),ArrayType(1,2,BoolType())),
            VarDecl(Id("d"),BoolType()),
            VarDecl(Id("y"),BoolType()),
            VarDecl(Id("e"),ArrayType(15,4,FloatType())),
            VarDecl(Id("_something"),ArrayType(15,4,FloatType()))
            ,VarDecl(Id("something"),ArrayType(15,4,FloatType()))],[])]))
        self.assertTrue(TestAST.test(input,expect,318))

    def test_assign_statement1(self):
        input = """procedure foo(a, b: integer ; c: real) ;
                  var x,y: real ;
                  BEGIN
                    a := 1;
                    a := 1.1;
                    a := .1;
                    a := 1.;
                    b := a + b ;
                    a := b := c/a;
                  END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),FloatType())],
            [
            VarDecl(Id("x"),FloatType()),
            VarDecl(Id("y"),FloatType())],
            [
            Assign(Id("a"),IntLiteral(1)),
            Assign(Id("a"),FloatLiteral(1.1)),
            Assign(Id("a"),FloatLiteral(0.1)),
            Assign(Id("a"),FloatLiteral(1.0)),
            Assign(Id("b"),BinaryOp('+',Id("a"),Id("b"))),
            Assign(Id("b"),BinaryOp('/',Id("c"),Id("a"))),
            Assign(Id("a"),Id("b"))])]))
        self.assertTrue(TestAST.test(input,expect,319))

    def test_assign_statement2(self):
        input = """procedure foo(a, b: integer ; c: real) ;
                  var x,y: real ;
                  BEGIN
                     t := true = false;
                  END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),FloatType())],
            [
            VarDecl(Id("x"),FloatType()),
            VarDecl(Id("y"),FloatType())],
            [Assign(Id("t"),BinaryOp('=',BooleanLiteral(True),BooleanLiteral(False)))])]))
        self.assertTrue(TestAST.test(input,expect,320))

    def test_assign_statement3(self):
        input = """procedure foo(a, b: integer ; c: real) ;
                  var x,y: real ;
                  BEGIN
                    a := b[10] := b[b/a] := a + b;
                  END"""
        expect = str(
            Program([
                FuncDecl(Id("foo"),
                [
                VarDecl(Id("a"),IntType()),
                VarDecl(Id("b"),IntType()),
                VarDecl(Id("c"),FloatType())],[
                VarDecl(Id("x"),FloatType()),
                VarDecl(Id("y"),FloatType())],
                [
                Assign(ArrayCell(Id("b"),BinaryOp('/',Id("b"),Id("a"))),BinaryOp('+',Id("a"),Id("b"))),
                Assign(ArrayCell(Id("b"),IntLiteral(10)),ArrayCell(Id("b"),BinaryOp('/',Id("b"),Id("a")))),
                Assign(Id("a"),ArrayCell(Id("b"),IntLiteral(10)))])])
        )
        self.assertTrue(TestAST.test(input,expect,321))

    def test_assign_statement4(self):
        input = """FUNcTION foo(a, b: integer ; c: real):array [1 .. 2] of integer ;
                  var x,y: real ;
                  BEGIN  
                  a[2] := "haha";
                  END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),FloatType())],[
            VarDecl(Id("x"),FloatType()),
            VarDecl(Id("y"),FloatType())],
            [Assign(ArrayCell(Id("a"),IntLiteral(2)),StringLiteral("haha"))]
            ,ArrayType(1,2,IntType())
            )]))
        self.assertTrue(TestAST.test(input,expect,322))

    def test_assign_statement5(self):
        input = """procedure foo(a, b: integer ; c: real);
                   var x,y: real ;
                   BEGIN
                    a := foo();
                    a[12] := foo(2,3+a,_something);
                    foo(2)[2] := haha(2+4,3+6,1.1);
                    c := a[12] ;
                   END"""
        expect = str(
            Program([
                FuncDecl(Id("foo"),
                [
                VarDecl(Id("a"),IntType()),
                VarDecl(Id("b"),IntType()),
                VarDecl(Id("c"),FloatType())],[
                VarDecl(Id("x"),FloatType()),
                VarDecl(Id("y"),FloatType())],
                [
                Assign(Id("a"),
                CallExpr(Id("foo"),[])),
                Assign(ArrayCell(Id("a"),IntLiteral(12)),
                CallExpr(Id("foo"),[IntLiteral(2),BinaryOp('+',IntLiteral(3),Id("a")),Id("_something")])),
                Assign(ArrayCell(
                CallExpr(Id("foo"),[IntLiteral(2)]),IntLiteral(2)),
                CallExpr(Id("haha"),[BinaryOp('+',IntLiteral(2),IntLiteral(4)),BinaryOp('+',IntLiteral(3),IntLiteral(6)),FloatLiteral(1.1)])),
                Assign(Id('c'),ArrayCell(Id('a'),IntLiteral(12)))])])
        )
        self.assertTrue(TestAST.test(input,expect,323))

    def test_assign_statement6(self): 
        input = """procedure foo(a, b: integer ; c: real) ;
                   var x,y: array[-1 .. 5] of real;
                   BEGIN
                    a[m+n] := b[10] ;
                    foo(a,a+b)[m*n] := a[a div 3] ;
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),FloatType())],[
            VarDecl(Id("x"),ArrayType(-1,5,FloatType())),
            VarDecl(Id("y"),ArrayType(-1,5,FloatType()))],[
            Assign(ArrayCell(Id("a"),BinaryOp('+',Id("m"),Id("n"))),ArrayCell(Id("b"),IntLiteral(10))),
            Assign(ArrayCell(CallExpr(Id("foo"),[Id("a"),BinaryOp('+',Id("a"),Id("b"))]),BinaryOp('*',Id("m"),Id("n"))),ArrayCell(Id("a"),BinaryOp('div',Id("a"),IntLiteral(3))))])]))
        self.assertTrue(TestAST.test(input,expect,324))

    def test_assign_statement7(self):
        input = """
                   procedure foo(a, b: integer ; c: real) ;
                   var x: integer ;
                   BEGIN
                       a[m+n] := a[m*n] := foo(2,3,a+b)[m*n] := a[a div 10] := (a>m) and then (b<n);
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),FloatType())],[
            VarDecl(Id("x"),IntType())],
            [
            Assign(ArrayCell(Id("a"),BinaryOp('div',Id("a"),IntLiteral(10))),BinaryOp('andthen',BinaryOp('>',Id("a"),Id("m")),BinaryOp('<',Id("b"),Id("n")))),
            
            Assign(ArrayCell(CallExpr(Id("foo"),[IntLiteral(2),IntLiteral(3),BinaryOp('+',Id("a"),Id("b"))]),BinaryOp('*',Id("m"),Id("n"))),ArrayCell(Id("a"),BinaryOp('div',Id("a"),IntLiteral(10)))),
            
            Assign(ArrayCell(Id("a"),BinaryOp('*',Id("m"),Id("n"))),ArrayCell(CallExpr(Id("foo"),[IntLiteral(2),IntLiteral(3),BinaryOp('+',Id("a"),Id("b"))]),BinaryOp('*',Id("m"),Id("n")))),
            
            Assign(ArrayCell(Id("a"),BinaryOp('+',Id("m"),Id("n"))),ArrayCell(Id("a"),BinaryOp('*',Id("m"),Id("n"))))])]))
        self.assertTrue(TestAST.test(input,expect,325))

    def test_if_statement1(self):
        input = """function foo(a, b: integer ; c: real):array [1 .. 2] of integer ;
                   var x:real ;
                   BEGIN
                    if(true = false) then dosomething() ;
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),FloatType())],
            [VarDecl(Id("x"),FloatType())],
            [If(BinaryOp('=',BooleanLiteral(True),BooleanLiteral(False)),[CallStmt(Id("dosomething"),[])],[])],
            ArrayType(1,2,IntType())
            )]))
        self.assertTrue(TestAST.test(input,expect,326))

    def test_if_statement2(self):
        input = """procedure foo(a, b: integer ; c: real) ;
                   var x:real ;
                   BEGIN
                    if(true = false) then dosomething() ;
                    else foo();
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),FloatType())],[
            VarDecl(Id("x"),FloatType())],
            [If(BinaryOp('=',BooleanLiteral(True),BooleanLiteral(False)),
            [CallStmt(Id("dosomething"),[])],[CallStmt(Id("foo"),[])])])]))
        self.assertTrue(TestAST.test(input,expect,327))

    def test_if_statement3(self):
        input = """procedure foo(a, b: integer ; c: real) ;
                   var x:real ;
                   BEGIN
                    if(true = false) then a := b := c[2] := foo(2,a+b)[d] := c/a ;
                    else foo();
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),FloatType())],[
            VarDecl(Id("x"),FloatType())],
            [If(BinaryOp('=',BooleanLiteral(True),BooleanLiteral(False)),
            [Assign(ArrayCell(CallExpr(Id("foo"),[IntLiteral(2),BinaryOp('+',Id("a"),Id("b"))]),Id("d")),BinaryOp('/',Id("c"),Id("a"))),
            
            Assign(ArrayCell(Id("c"),IntLiteral(2)),ArrayCell(CallExpr(Id("foo"),[IntLiteral(2),BinaryOp('+',Id("a"),Id("b"))]),Id("d"))),
            
            Assign(Id("b"),ArrayCell(Id("c"),IntLiteral(2))),
            
            Assign(Id("a"),Id("b"))],[CallStmt(Id("foo"),[])])])]))
        self.assertTrue(TestAST.test(input,expect,328))

    def test_if_statement4(self):
        input = """procedure foo(a, b: integer ; c: real) ;
                   var x:real ;
                   BEGIN
                    if(true = false) then
                    BEGIN 
                        a := b := c[2] := foo(2,a+b)[d] := c/a ;
                        dosomething1();
                        dosomething2();
                    END
                    else foo();
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),FloatType())],[
            VarDecl(Id("x"),FloatType())],
            [If(BinaryOp('=',BooleanLiteral(True),BooleanLiteral(False)),[    
            Assign(ArrayCell(CallExpr(Id("foo"),[IntLiteral(2),BinaryOp('+',Id("a"),Id("b"))]),Id("d")),BinaryOp('/',Id("c"),Id("a"))),
            
            Assign(ArrayCell(Id("c"),IntLiteral(2)),ArrayCell(CallExpr(Id("foo"),[IntLiteral(2),BinaryOp('+',Id("a"),Id("b"))]),Id("d"))),
            
            Assign(Id("b"),ArrayCell(Id("c"),IntLiteral(2))),
            
            Assign(Id("a"),Id("b")),CallStmt(Id("dosomething1"),[]),CallStmt(Id("dosomething2"),[])],[CallStmt(Id("foo"),[])])])]))
        self.assertTrue(TestAST.test(input,expect,329))

    def test_if_statement5(self):
        input = """function foo(a, b: integer ; c: real):array [1 .. 2] of integer ;
                   var x:real ;
                   BEGIN
                    if(a>1) then a:=1 ;
                    else if (1<2)<>(2<3) then x:=1 ;
                    else foo(a+1,2);
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),FloatType())],[
            VarDecl(Id("x"),FloatType())],
            [If(BinaryOp('>',Id("a"),IntLiteral(1)),
            [Assign(Id("a"),IntLiteral(1))],
            [If(BinaryOp('<>',BinaryOp('<',IntLiteral(1),IntLiteral(2)),BinaryOp('<',IntLiteral(2),IntLiteral(3))),
            [Assign(Id("x"),IntLiteral(1))],[CallStmt(Id("foo"),[BinaryOp('+',Id("a"),IntLiteral(1)),IntLiteral(2)])])])],
            ArrayType(1,2,IntType())
            )]))
        self.assertTrue(TestAST.test(input,expect,330))

    def test_if_statement6(self):
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>1) then beGin
                        a:=1 ;
                        if(1=1) then a:= b[1];
                        else b:=a[1]:= 1;
                    end
                    END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [VarDecl(Id("c"),FloatType())],
            [VarDecl(Id("x"),FloatType())],
            [If(BinaryOp('>',Id("a"),IntLiteral(1)),
            [Assign(Id("a"),IntLiteral(1)),
            If(BinaryOp('=',IntLiteral(1),IntLiteral(1)),
            [Assign(Id("a"),ArrayCell(Id("b"),IntLiteral(1)))],
            [Assign(ArrayCell(Id("a"),IntLiteral(1)),IntLiteral(1))
            ,Assign(Id("b"),ArrayCell(Id("a"),IntLiteral(1)))])],[])])]))
        self.assertTrue(TestAST.test(input,expect,331))

    def test_while_statement1(self):
        input = """function foo(a, b: integer ; c: real):array [1 .. 2] of integer ;
                   var x:real ;
                   BEGIN
                    while true do something();
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),FloatType())],
            [VarDecl(Id("x"),FloatType())],
            [While(BooleanLiteral(True),[CallStmt(Id("something"),[])])]
            ,ArrayType(1,2,IntType())
            )]))
        self.assertTrue(TestAST.test(input,expect,332))

    def test_while_statement2(self):
        input = """function foo(a, b: integer ; c: real):array [1 .. 2] of integer ;
                   var x:real ;
                   BEGIN
                    while (true or a+b = 6) do 
                    begin
                        something1();
                        a := b := c;
                        something2();
                    end
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),FloatType())],[
            VarDecl(Id("x"),FloatType())],
            [While(BinaryOp('=',BinaryOp('+',BinaryOp('or',BooleanLiteral(True),Id("a")),Id("b")),IntLiteral(6)),
            [CallStmt(Id("something1"),[]),
            Assign(Id("b"),Id("c")),
            Assign(Id("a"),Id("b")),
            CallStmt(Id("something2"),[])])]
            ,ArrayType(1,2,IntType())
            )]))
        self.assertTrue(TestAST.test(input,expect,333))

    def test_while_statement3(self):
        input = """function foo(a, b: integer ; c: real):array [1 .. 2] of integer ;
                   var x:real ;
                   BEGIN
                    while (true or a+b = 6) do 
                    begin
                        something1();
                        a := b := c;
                        something2();

                        if(a>1) then 
                        beGin
                            a:=1 ;
                            if(1=1) then a:= b[1];
                            else b:=a[1]:= 1;
                        end         
                    end
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),FloatType())],[
            VarDecl(Id("x"),FloatType())],
            [While(BinaryOp('=',BinaryOp('+',BinaryOp('or',BooleanLiteral(True),Id("a")),Id("b")),IntLiteral(6)),
            [CallStmt(Id("something1"),[]),
            
            Assign(Id("b"),Id("c")),
            
            Assign(Id("a"),Id("b")),CallStmt(Id("something2"),[]),If(BinaryOp('>',Id("a"),IntLiteral(1)),[
                
            Assign(Id("a"),IntLiteral(1)),If(BinaryOp('=',IntLiteral(1),IntLiteral(1)),[
                
            Assign(Id("a"),ArrayCell(Id("b"),IntLiteral(1)))],
            
            [Assign(ArrayCell(Id("a"),IntLiteral(1)),IntLiteral(1)),
            
            Assign(Id("b"),ArrayCell(Id("a"),IntLiteral(1)))])],[])])]
            ,ArrayType(1,2,IntType())
            )]))
        self.assertTrue(TestAST.test(input,expect,334))

    def test_while_statement4(self):
        input = """function foo(a, b: integer ; c: real):array [1 .. 2] of integer ;
                   var x:real ;
                   BEGIN
                    while (true or a+b = 6) do 
                    begin
                        something1();
                        a := b := c;
                        something2();
                        
                        while (a+b <> 6) do something();

                        if(a>1) then 
                        beGin
                            a:=1 ;
                            if(1=1) then a:= b[1];
                            else b:=a[1]:= 1;
                        end         
                    end
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),FloatType())],
            [VarDecl(Id("x"),FloatType())],
            [While(BinaryOp('=',BinaryOp('+',BinaryOp('or',BooleanLiteral(True),Id("a")),Id("b")),IntLiteral(6)),
            [CallStmt(Id("something1"),[]),
            
            Assign(Id("b"),Id("c")),
            
            Assign(Id("a"),Id("b")),
            CallStmt(Id("something2"),[]),While(BinaryOp('<>',BinaryOp('+',Id("a"),Id("b")),IntLiteral(6)),[CallStmt(Id("something"),[])]),If(BinaryOp('>',Id("a"),IntLiteral(1)),[
            
            Assign(Id("a"),IntLiteral(1)),If(BinaryOp('=',IntLiteral(1),IntLiteral(1)),[
            
            Assign(Id("a"),ArrayCell(Id("b"),IntLiteral(1)))],[
            
            Assign(ArrayCell(Id("a"),IntLiteral(1)),IntLiteral(1)),
            
            Assign(Id("b"),ArrayCell(Id("a"),IntLiteral(1)))])],[])])]
            ,ArrayType(1,2,IntType())
            )]))
        self.assertTrue(TestAST.test(input,expect,335))
       
    def test_while_statement5(self):
        input = """function foo(a, b: integer ; c: real):array [1 .. 2] of integer ;
                   var x:real ;
                   BEGIN
                    while (true or a+b = 6) do 
                    begin
                        something1();
                        a := b := c;
                        something2();
                        
                        while (a+b <> 6) do
                        begin
                            something1();
                            a := b := c;
                            something2();
                        
                            while (a+b <> 6) do something();
                            if(a>1) then 
                            beGin
                                a:=1 ;
                                if(1=1) then a:= b[1];
                            else b:=a[1]:= 1;
                            end         
                        end

                        if(a>1) then 
                        beGin
                            a:=1 ;
                            if(1=1) then a:= b[1];
                            else b:=a[1]:= 1;
                        end         
                    end
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),FloatType())],
            [
            VarDecl(Id("x"),FloatType())],
            [
            
            While(BinaryOp('=',BinaryOp('+',BinaryOp('or',BooleanLiteral(True),Id("a")),Id("b")),IntLiteral(6)),[
            CallStmt(Id("something1"),[]),
            Assign(Id("b"),Id("c")),
            Assign(Id("a"),Id("b")),
            CallStmt(Id("something2"),[]),
            
            While(BinaryOp('<>',BinaryOp('+',Id("a"),Id("b")),IntLiteral(6)),[
            CallStmt(Id("something1"),[]),
            Assign(Id("b"),Id("c")),
            Assign(Id("a"),Id("b")),
            CallStmt(Id("something2"),[]),
            
            While(BinaryOp('<>',BinaryOp('+',Id("a"),Id("b")),IntLiteral(6)),[
            CallStmt(Id("something"),[])]),If(BinaryOp('>',Id("a"),IntLiteral(1)),[
            Assign(Id("a"),IntLiteral(1)),If(BinaryOp('=',IntLiteral(1),IntLiteral(1)),[
            Assign(Id("a"),ArrayCell(Id("b"),IntLiteral(1)))],[
            Assign(ArrayCell(Id("a"),IntLiteral(1)),IntLiteral(1)),
            Assign(Id("b"),ArrayCell(Id("a"),IntLiteral(1)))])],[])]),If(BinaryOp('>',Id("a"),IntLiteral(1)),[
            Assign(Id("a"),IntLiteral(1)),If(BinaryOp('=',IntLiteral(1),IntLiteral(1)),
            [Assign(Id("a"),ArrayCell(Id("b"),IntLiteral(1)))],[
            Assign(ArrayCell(Id("a"),IntLiteral(1)),IntLiteral(1)),
            Assign(Id("b"),ArrayCell(Id("a"),IntLiteral(1)))])],[])])]

            ,ArrayType(1,2,IntType())
            )]))
        self.assertTrue(TestAST.test(input,expect,336))

    def test_with_statement1(self):
        input = """procedure foo(a, b: integer ; c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real ; do
                    d := c [a] + b ;
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),FloatType())]
            ,[],
            [With([
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),ArrayType(1,2,FloatType()))],
            [Assign(Id("d"),BinaryOp('+',ArrayCell(Id("c"),Id("a")),Id("b")))])])]))
        self.assertTrue(TestAST.test(input,expect,337))
    
    def test_with_statement2(self):
        input = """function foo(a, b: integer ; c: real):array [1 .. 2] of integer ;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real ; do 
                    begin
                        something1();
                        a := b := c;
                        something2();
                    end
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),FloatType())],[],
            [With([
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),ArrayType(1,2,FloatType()))],
            [CallStmt(Id("something1"),[]),
            Assign(Id("b"),Id("c")),
            Assign(Id("a"),Id("b")),
            CallStmt(Id("something2"),[])])]
            ,ArrayType(1,2,IntType())
            )]))
        self.assertTrue(TestAST.test(input,expect,338))

    def test_with_statement3(self):
        input = """function foo(a, b: integer ; c: real):array [1 .. 2] of integer ;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real ; do 
                    begin
                        something1();
                        a := b := c;
                        something2();
                        with a , b : integer ; c : array [1 .. 2] of real ; do 
                        begin
                            something1();
                            a := b := c;
                            something2();
                        end
                    end
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType())
            ,VarDecl(Id("c"),FloatType())],[],[With([
            VarDecl(Id("a"),IntType())
            ,VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),ArrayType(1,2,FloatType()))],[
            CallStmt(Id("something1"),[]),
            Assign(Id("b"),Id("c")),
            Assign(Id("a"),Id("b")),
            CallStmt(Id("something2"),[]),
            With([
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),ArrayType(1,2,FloatType()))],[
            CallStmt(Id("something1"),[]),
            Assign(Id("b"),Id("c")),
            Assign(Id("a"),Id("b")),
            CallStmt(Id("something2"),[])])])]
            ,ArrayType(1,2,IntType())
            )]))
        self.assertTrue(TestAST.test(input,expect,339))

    def test_with_statement4(self):
        input = """procedure foo(a, b: integer ; c: real) ;
                   BEGIN
                    with c , d : integer ; c : array [1 .. 2] of real ; do
                    with a , b : integer ; do
                        something1(a,2,c+b);
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),FloatType())]
            ,[],[With([
            VarDecl(Id("c"),IntType()),
            VarDecl(Id("d"),IntType()),
            VarDecl(Id("c"),ArrayType(1,2,FloatType()))],[With([
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType())],[CallStmt(Id("something1"),[Id("a"),IntLiteral(2),BinaryOp('+',Id("c"),Id("b"))])])])])]))
        self.assertTrue(TestAST.test(input,expect,340))

    def test_for_statement1(self):
        input = """function foo(n : integer): integer;
                   BEGIN
                    FOR i:=1 to n do 
                        s := s + 1;
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [VarDecl(Id("n"),IntType())],[],[For(Id("i"),IntLiteral(1),Id("n"),True,[Assign(Id("s"),BinaryOp('+',Id("s"),IntLiteral(1)))])]
            ,IntType()
            )]))
        self.assertTrue(TestAST.test(input,expect,341))

    def test_for_statement2(self):
        input = """function foo(n: integer; m:integer): integer;
                   BEGIN
                    FOR i:=1 to m+n do 
                    begin
                        s := s + 1;
                        if(i = (m+n)/2) then s:=s-1;
                    end
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [
            VarDecl(Id("n"),IntType()),
            VarDecl(Id("m"),IntType())],[],[For(Id("i"),IntLiteral(1),BinaryOp('+',Id("m"),Id("n")),True,
            
            [Assign(Id("s"),BinaryOp('+',Id("s"),IntLiteral(1))),
            If(BinaryOp('=',Id("i"),BinaryOp('/',BinaryOp('+',Id("m"),Id("n")),IntLiteral(2))),
            
            [Assign(Id("s"),BinaryOp('-',Id("s"),IntLiteral(1)))],[])])]
            ,IntType()
            )]))
        self.assertTrue(TestAST.test(input,expect,342))

    def test_for_statement3(self):
        input = """function foo(n: integer; m:integer): integer;
                   BEGIN
                    for i:=100 downto 1 do 
                    begin
                        s := s + 1;
                        if(i = (m+n)/2) then s:=s-1;
                    end
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [
            VarDecl(Id("n"),IntType()),
            VarDecl(Id("m"),IntType())],[],[For(Id("i"),IntLiteral(100),IntLiteral(1),False,

            [Assign(Id("s"),BinaryOp('+',Id("s"),IntLiteral(1))),If(BinaryOp('=',Id("i"),BinaryOp('/',BinaryOp('+',Id("m"),Id("n")),IntLiteral(2))),
            
            [Assign(Id("s"),BinaryOp('-',Id("s"),IntLiteral(1)))],[])])]
            ,IntType()
            )]))
        self.assertTrue(TestAST.test(input,expect,343))

    def test_for_statement4(self):
        input = """function foo(n: integer; m:integer): integer;
                   BEGIN
                    for i:=1 downto n do
                        for j := i to n -1 do
                        begin
                            s := s + 1;
                            if(i = (m+n)/2) then s:=s-1;
                        end
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [
            VarDecl(Id("n"),IntType()),
            VarDecl(Id("m"),IntType())],[],
            
            [For(Id("i"),IntLiteral(1),Id("n"),False,
            
            [For(Id("j"),Id("i"),BinaryOp('-',Id("n"),IntLiteral(1)),True,
            
            [Assign(Id("s"),BinaryOp('+',Id("s"),IntLiteral(1))),
            
            If(BinaryOp('=',Id("i"),BinaryOp('/',BinaryOp('+',Id("m"),Id("n")),IntLiteral(2))),
            
            [Assign(Id("s"),BinaryOp('-',Id("s"),IntLiteral(1)))],[])])])]
            ,IntType()
            )]))
        self.assertTrue(TestAST.test(input,expect,344))

    def test_break_statement1(self):
        input = """function foo(n: integer; m:integer): integer;
                   BEGIN
                    for i:=1 downto n do
                        for j := i to n -1 do
                        begin
                            s := s + 1;
                            if(i = (m+n)/2) then break;
                        end
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [VarDecl(Id("n"),IntType()),
            VarDecl(Id("m"),IntType())],[],
            
            [For(Id("i"),IntLiteral(1),Id("n"),False,
            
            [For(Id("j"),Id("i"),BinaryOp('-',Id("n"),IntLiteral(1)),True,
            
            [Assign(Id("s"),BinaryOp('+',Id("s"),IntLiteral(1))),
            
            If(BinaryOp('=',Id("i"),BinaryOp('/',BinaryOp('+',Id("m"),Id("n")),IntLiteral(2))),[Break()],[])])])]
            ,IntType()
            )]))
        self.assertTrue(TestAST.test(input,expect,345))

    def test_break_statement2(self):
        input = """function foo(n: integer; m:integer): integer;
                   BEGIN
                    while(true) do
                    begin
                        s := s-1;
                        if(s = 0) then break;
                    end
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),[
            VarDecl(Id("n"),IntType()),
            VarDecl(Id("m"),IntType())],[],
            
            [While(BooleanLiteral(True),
            
            [Assign(Id("s"),BinaryOp('-',Id("s"),IntLiteral(1))),
            
            If(BinaryOp('=',Id("s"),IntLiteral(0)),[Break()],[])])]
            ,IntType()
            )]))
        self.assertTrue(TestAST.test(input,expect,346))

    def test_continue_statement1(self):
        input = """function foo(n: integer; m:integer): integer;
                   BEGIN
                    for i:=1 downto n do
                        for j := i to n -1 do
                        begin
                            if(i = (m+n)/2) then continue;
                            s := s + 1; 
                        end
                   END"""
        expect = str(Program(
            [FuncDecl(Id("foo"),[
            VarDecl(Id("n"),IntType()),
            VarDecl(Id("m"),IntType())],[],
            
            [For(Id("i"),IntLiteral(1),Id("n"),False,
            
            [For(Id("j"),Id("i"),BinaryOp('-',Id("n"),IntLiteral(1)),True,
            
            [If(BinaryOp('=',Id("i"),BinaryOp('/',BinaryOp('+',Id("m"),Id("n")),IntLiteral(2))),
            [Continue()],[]),
            
            Assign(Id("s"),BinaryOp('+',Id("s"),IntLiteral(1)))])])]
            ,IntType()
            )]))
        self.assertTrue(TestAST.test(input,expect,347))
    
    def test_continue_statement2(self):
        input = """function foo(n: integer; m:integer): integer;
                   BEGIN
                    while(true) do
                    begin
                        s := s-1;
                        if(s = 0) then continue;
                    end
                   END"""
        expect = str(Program(
            [FuncDecl(Id("foo"),[
            VarDecl(Id("n"),IntType()),
            VarDecl(Id("m"),IntType())]
            ,[],[While(BooleanLiteral(True),[Assign(Id("s"),BinaryOp('-',Id("s"),IntLiteral(1))),If(BinaryOp('=',Id("s"),IntLiteral(0)),[Continue()],[])])]
            ,IntType()
            )]))
        self.assertTrue(TestAST.test(input,expect,348))

    def test_return_statement1(self):
        input = """function foo(n: integer; m:integer): integer;
                   BEGIN
                    while(true) do
                    begin
                        s := s-1;
                        if(s div k = 0) then return s ;
                    end
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [VarDecl(Id("n"),IntType()),
            VarDecl(Id("m"),IntType())],[],[While(BooleanLiteral(True),
            
            [Assign(Id("s"),BinaryOp('-',Id("s"),IntLiteral(1))),If(BinaryOp('=',BinaryOp('div',Id("s"),Id("k")),IntLiteral(0)),[Return(Id("s"))],[])])]
            ,IntType()
            )]))
        self.assertTrue(TestAST.test(input,expect,349))

    def test_return_statement2(self):
        input = """function foo(n: integer; m:integer): integer;
                   BEGIN
                    while(true) do
                    begin
                        s := s-1;
                        if(s div k = 0) then return _something(a,b,1+2) ;
                    end
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),[
            VarDecl(Id("n"),IntType()),
            VarDecl(Id("m"),IntType())],[],
            [While(BooleanLiteral(True),
            [Assign(Id("s"),BinaryOp('-',Id("s"),IntLiteral(1))),
            If(BinaryOp('=',BinaryOp('div',Id("s"),Id("k")),IntLiteral(0)),
            [Return(CallExpr(Id("_something"),[Id("a"),Id("b"),BinaryOp('+',IntLiteral(1),IntLiteral(2))]))],[])])]
            ,IntType()
            )]))
        self.assertTrue(TestAST.test(input,expect,350))

    def test_compound_statement1(self):
        input = """function foo(n: integer; m:integer): integer;
                   BEGIN
                    begin
                    end
                   END"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),IntType()),VarDecl(Id("m"),IntType())],[],[]
        ,IntType()
        )]))
        self.assertTrue(TestAST.test(input,expect,351))

    def test_call_statement1(self):
        input = """function foo(n: integer; m:integer): integer;
                   BEGIN           
                    something();
                   END"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),IntType()),VarDecl(Id("m"),IntType())],[],[CallStmt(Id("something"),[])]
        ,IntType()
        )]))
        self.assertTrue(TestAST.test(input,expect,352))

    def test_call_statement2(self):
        input = """function foo(n: integer; m:integer): integer;
                   BEGIN
                    something1(2);           
                    something2(_a);
                    something3(3+4);
                    something4("haha");
                    something5(1.);
                    something6(something7());

                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),[
            VarDecl(Id("n"),IntType()),
            VarDecl(Id("m"),IntType())],[],[CallStmt(Id("something1"),[IntLiteral(2)]),CallStmt(Id("something2"),[Id("_a")]),CallStmt(Id("something3"),[BinaryOp('+',IntLiteral(3),IntLiteral(4))]),CallStmt(Id("something4"),[StringLiteral("haha")]),CallStmt(Id("something5"),[FloatLiteral(1.0)]),CallStmt(Id("something6"),[CallExpr(Id("something7"),[])])]
            ,IntType()
            )]))
        self.assertTrue(TestAST.test(input,expect,353))

    def test_call_statement3(self):
        input = """function foo(n: integer; m:integer): integer;
                   BEGIN
                    something(3,a+1,x and then y,a[1],foo(1,2)[m+1]);
                    return something2();
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),[
            VarDecl(Id("n"),IntType()),
            VarDecl(Id("m"),IntType())],[],[CallStmt(Id("something"),[IntLiteral(3),BinaryOp('+',Id("a"),IntLiteral(1)),BinaryOp("andthen",Id("x"),Id("y")),ArrayCell(Id("a"),IntLiteral(1)),ArrayCell(CallExpr(Id("foo"),[IntLiteral(1),IntLiteral(2)]),BinaryOp('+',Id("m"),IntLiteral(1)))]),Return(CallExpr(Id("something2"),[]))]
            ,IntType()
            )]))
        self.assertTrue(TestAST.test(input,expect,354))

    def test_call_statement4(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    something(x,y,z,something(something(something(a+b+c,a+1))));
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [VarDecl(Id("c"),FloatType())],[],[CallStmt(Id("something"),[Id("x"),Id("y"),Id("z"),
            CallExpr(Id("something"),
            [CallExpr(Id("something"),
            [CallExpr(Id("something"),[BinaryOp('+',BinaryOp('+',Id("a"),Id("b")),Id("c")),BinaryOp('+',Id("a"),IntLiteral(1))])])])])]
            ,IntType()
            )]))
        self.assertTrue(TestAST.test(input,expect,355))

    def test_call_statement5(self):
        input = """function foo(c: real): integer;
                   BEGIN
                    textbackground(brown); {background colour}
                    ClrScr(); {Clear screen with a brown colour. Try run the program without this..}
                    return func(a(1,2));
                   END"""
        expect = str(Program([
            FuncDecl(Id("foo"),
            [VarDecl(Id("c"),FloatType())],[],[CallStmt(Id("textbackground"),[Id("brown")]),CallStmt(Id("ClrScr"),[]),Return(CallExpr(Id("func"),[CallExpr(Id("a"),[IntLiteral(1),IntLiteral(2)])]))]
            ,IntType()
            )]))
        self.assertTrue(TestAST.test(input,expect,356))

    def test_combine1(self):
        input = """
                function foo(n: integer; m:integer): integer;
                begin
                   if bool = true then
                   begin
                         if(e > f) then foo(a,c) ;
                   end
                end
                """
        expect = str(Program([
            FuncDecl(Id("foo"),
            [VarDecl(Id("n"),IntType()),
            VarDecl(Id("m"),IntType())],[],[If(BinaryOp('=',Id("bool"),BooleanLiteral(True)),
            [If(BinaryOp('>',Id("e"),Id("f")),
            [CallStmt(Id("foo"),[Id("a"),Id("c")])],[])],[])]
            ,IntType()
            )]))
        self.assertTrue(TestAST.test(input,expect,357))

    def test_combine2(self):
        input = """
                function foo(n: integer; m:integer): integer;
                begin
                   if a=b then if c=d then while (d=e) do
                   beGin
                   eND
               else c := 1;
                end
                """
        expect = str(Program([
            FuncDecl(Id("foo"),
            [VarDecl(Id("n"),IntType()),
            VarDecl(Id("m"),IntType())],[],[If(BinaryOp('=',Id("a"),Id("b")),
            [If(BinaryOp('=',Id("c"),Id("d")),
            [While(BinaryOp('=',Id("d"),Id("e")),[])],[Assign(Id("c"),IntLiteral(1))])],[])]
            ,IntType()
            )]))
        self.assertTrue(TestAST.test(input,expect,358))

    def test_combine3(self):
        input = """
                function foo(n: integer; m:integer): integer;
                var x,  y, z: real;
                begin
                    write("x = ");
                    readln(x);
                    write("y = ");
                    readln(y);

                if y=0 then
                    writeln("Can not divide by 0");
                else begin
                    z:=x/y;
                    writeln("z" = z);
                end
                end
                """
        expect = str(Program([
            FuncDecl(Id("foo"),
            [VarDecl(Id("n"),IntType()),
            VarDecl(Id("m"),IntType())],[
            VarDecl(Id("x"),FloatType()),
            VarDecl(Id("y"),FloatType()),
            VarDecl(Id("z"),FloatType())],
            [CallStmt(Id("write"),[StringLiteral("x = ")]),
            CallStmt(Id("readln"),[Id("x")])
            ,CallStmt(Id("write"),[StringLiteral("y = ")]),
            CallStmt(Id("readln"),[Id("y")]),If(BinaryOp('=',Id("y"),IntLiteral(0)),[
            CallStmt(Id("writeln"),[StringLiteral("Can not divide by 0")])],
            [Assign(Id("z"),BinaryOp('/',Id("x"),Id("y"))),
            CallStmt(Id("writeln"),[BinaryOp('=',StringLiteral("z"),Id("z"))])])]
            ,IntType()
            )]))
        self.assertTrue(TestAST.test(input,expect,359))

    def test_multi_1(self):
        input = """procedure foo();
begin
    x := True;
end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("x"),BooleanLiteral(True))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,360))
    def test_multi_2(self):
        input = """procedure foo();
begin
    arr[-1] := 2;
end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(ArrayCell(Id("arr"),UnaryOp("-",IntLiteral(1))),IntLiteral(2))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,361))
    def test_multi_3(self):
        input = """procedure foo();
begin
    if (a < 1) and then x > 2 then
    begin
        x := 2*a;
        for i := n downto 1 do
            a := a + 1;
    end
end"""
        expect = str(Program([FuncDecl(Id("foo"),
                    [],
                    [],
                    [If(BinaryOp("andthen",BinaryOp("<",Id("a"),IntLiteral(1)),BinaryOp(">",Id("x"),IntLiteral(2))),
                        [Assign(Id("x"),BinaryOp("*",IntLiteral(2),Id("a"))),
                        For(Id("i"),Id("n"),IntLiteral(1),False,
                            [Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])],
                        [])],
                    VoidType())]))
        self.assertTrue(TestAST.test(input,expect,362))
    def test_multi_4(self):
        input = """procedure foo();
begin
    x := a --------------------- b;
end"""
        expect = str(Program([FuncDecl(Id("foo"),
                    [],
                    [],
                    [Assign(Id("x"),BinaryOp("-",Id("a"),
                                        UnaryOp("-",
                                            UnaryOp("-",
                                                UnaryOp("-",
                                                    UnaryOp("-",
                                                        UnaryOp("-",
                                                            UnaryOp("-",
                                                                UnaryOp("-",
                                                                    UnaryOp("-",
                                                                        UnaryOp("-",
                                                                            UnaryOp("-",
                                                                                UnaryOp("-",
                                                                                    UnaryOp("-",
                                                                                        UnaryOp("-",
                                                                                            UnaryOp("-",
                                                                                                UnaryOp("-",
                                                                                                    UnaryOp("-",
                                                                                                        UnaryOp("-",
                                                                                                            UnaryOp("-",
                                                                                                                UnaryOp("-",
                                                                                                                    UnaryOp("-",Id("b")))))))))))))))))))))))],
                    VoidType())]))
        self.assertTrue(TestAST.test(input,expect,363))
    def test_multi_5(self):
        input = """procedure foo();
begin
    x := 1 + 2 - 3 * 4 / 5 mod 6 div 7;
end"""
        expect = str(Program([FuncDecl(Id("foo"),
                    [],
                    [],
                    [Assign(Id("x"),
                        BinaryOp("-",
                            BinaryOp("+",IntLiteral(1),IntLiteral(2)),
                            BinaryOp("div",
                                BinaryOp("mod",
                                    BinaryOp("/",
                                        BinaryOp("*",IntLiteral(3),IntLiteral(4)),
                                        IntLiteral(5)),
                                    IntLiteral(6)),
                                IntLiteral(7))))],
                    VoidType())]))
        self.assertTrue(TestAST.test(input,expect,364))
    def test_multi_6(self):
        input = """procedure foo();
var a,b: array [-5 .. -1] of integer;
begin
    for i := -5 to -1 do
        for j := -1 downto -5 do
            a[i] := a[i] + b[j];
end"""
        expect = str(Program([FuncDecl(Id("foo"),
                    [],
                    [VarDecl(Id("a"),ArrayType(-5,-1,IntType())),VarDecl(Id("b"),ArrayType(-5,-1,IntType()))],
                    [For(Id("i"),UnaryOp("-",IntLiteral(5)),UnaryOp("-",IntLiteral(1)),True,
                        [For(Id("j"),UnaryOp("-",IntLiteral(1)),UnaryOp("-",IntLiteral(5)),False,
                            [Assign(ArrayCell(Id("a"),Id("i")),BinaryOp("+",ArrayCell(Id("a"),Id("i")),ArrayCell(Id("b"),Id("j"))))])])],
                    VoidType())]))
        self.assertTrue(TestAST.test(input,expect,365))
    def test_multi_7(self):
        input = """procedure foo(x,y:real);
begin
    if x <= y then return -1;
    return foo(x-1,y+1);
end"""
        expect = str(Program([FuncDecl(Id("foo"),
                    [VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType())],
                    [],
                    [If(BinaryOp("<=",Id("x"),Id("y")),[Return(UnaryOp("-",IntLiteral(1)))],[]),
                        Return(CallExpr(Id("foo"),[BinaryOp("-",Id("x"),IntLiteral(1)),BinaryOp("+",Id("y"),IntLiteral(1))]))],
                    VoidType())]))
        self.assertTrue(TestAST.test(input,expect,366))
    def test_multi_8(self):
        input = """procedure foo();
begin
    arr[x+y-z div 2] := ((3+4)*t div 9) - 1000;
end"""
        expect = str(Program([FuncDecl(Id("foo"),
                    [],
                    [],
                    [Assign(ArrayCell(Id("arr"),BinaryOp("-",BinaryOp("+",Id("x"),Id("y")),BinaryOp("div",Id("z"),IntLiteral(2)))),
                        BinaryOp("-",BinaryOp("div",BinaryOp("*",BinaryOp("+",IntLiteral(3),IntLiteral(4)),Id("t")),IntLiteral(9)),IntLiteral(1000)))],
                    VoidType())]))
        self.assertTrue(TestAST.test(input,expect,367))
    def test_multi_9(self):
        input = """procedure foo();
begin
    a[m+n] := a[m*n] := foo(2,3,a mod b)[m*n] := a[a div 10] := (a>m) and then (b<n);
end"""
        expect = str(Program([FuncDecl(Id("foo"),
                    [],
                    [],
                    [Assign(ArrayCell(Id("a"),BinaryOp("div",Id("a"),IntLiteral(10))),BinaryOp("andthen",BinaryOp(">",Id("a"),Id("m")),BinaryOp("<",Id("b"),Id("n")))),
                        Assign(ArrayCell(CallExpr(Id("foo"),[IntLiteral(2),IntLiteral(3),BinaryOp("mod",Id("a"),Id("b"))]),BinaryOp("*",Id("m"),Id("n"))),ArrayCell(Id("a"),BinaryOp("div",Id("a"),IntLiteral(10)))),
                        Assign(ArrayCell(Id("a"),BinaryOp("*",Id("m"),Id("n"))),ArrayCell(CallExpr(Id("foo"),[IntLiteral(2),IntLiteral(3),BinaryOp("mod",Id("a"),Id("b"))]),BinaryOp("*",Id("m"),Id("n")))),
                        Assign(ArrayCell(Id("a"),BinaryOp("+",Id("m"),Id("n"))),ArrayCell(Id("a"),BinaryOp("*",Id("m"),Id("n"))))],
                    VoidType())]))
        self.assertTrue(TestAST.test(input,expect,368))
    def test_multi_10(self):
        input = """function foo(a:boolean):real;
var b:integer;
begin
    with a:boolean; do b := toString(a);
end"""
        expect = str(Program([FuncDecl(Id("foo"),
                    [VarDecl(Id("a"),BoolType())],
                    [VarDecl(Id("b"),IntType())],
                    [With([VarDecl(Id("a"),BoolType())],
                        [Assign(Id("b"),CallExpr(Id("toString"),[Id("a")]))])],
                    FloatType())]))
        self.assertTrue(TestAST.test(input,expect,369))
    def test_multi_11(self):
        input = """procedure foo();
begin
    call1(x,call2(a,call3(call1(3 mod 4,5 * call4(arr[m - n]))),c));
end"""
        expect = str(Program([FuncDecl(Id("foo"),
                    [],
                    [],
                    [CallStmt(Id("call1"),[Id("x"),CallExpr(Id("call2"),[Id("a"),CallExpr(Id("call3"),[CallExpr(Id("call1"),[BinaryOp("mod",IntLiteral(3),IntLiteral(4)),BinaryOp("*",IntLiteral(5),CallExpr(Id("call4"),[ArrayCell(Id("arr"),BinaryOp("-",Id("m"),Id("n")))]))])]),Id("c")])])],
                    VoidType())]))
        self.assertTrue(TestAST.test(input,expect,370))
    
    def test_multi_12(self):
        input = """
        function foo(): BOOLEAN;
        var x: real;
        begin
        if x = 5 then x:=9;
        end
        """
        expect = str(Program([
        FuncDecl(
        Id("foo"),
        [],
        [VarDecl(Id("x"),FloatType())],
        [If(
         BinaryOp("=",Id("x"),IntLiteral(5)),
         [Assign(Id("x"),IntLiteral(9))]
        )],
        BoolType()
        )
        ]))
        self.assertTrue(TestAST.test(input,expect,371))

    def test_multi_13(self):
        input = """
        function foo(): BOOLEAN;
        var x: real;
        begin
        if x = 5 then x:=9;
        else x:=7;
        end
        """
        expect = str(Program([
        FuncDecl(
        Id("foo"),
        [],
        [VarDecl(Id("x"),FloatType())],
        [If(
         BinaryOp("=",Id("x"),IntLiteral(5)),
         [Assign(Id("x"),IntLiteral(9))],
         [Assign(Id("x"),IntLiteral(7))]
        )],
        BoolType()
        )
        ]))
        self.assertTrue(TestAST.test(input,expect,372))
    def test_multi_14(self):
        input = """
        function foo(): BOOLEAN;
        begin
        if x = 5 then x:=9;
        else 
           if x > 9 then x:=3/2;
        end
        """
        expect = str(Program([FuncDecl(
        Id("foo"),
        [],[],
        [If(
        BinaryOp("=",Id("x"),IntLiteral(5)),
        [Assign(Id("x"),IntLiteral(9))],
        [If(
        BinaryOp(">",Id("x"),IntLiteral(9)),
        [Assign(Id("x"),BinaryOp("/",IntLiteral(3),IntLiteral(2)))]
        )])],
        BoolType()
        )
        ]))
        self.assertTrue(TestAST.test(input,expect,373))
    def test_multi_15(self):
        input = """
        function foo(): BOOLEAN;
        begin
        x:= (3+2)/5;
        end
        """
        expect = str(Program([FuncDecl(
        Id("foo"),
        [],[],
        [Assign(Id("x"),BinaryOp("/",BinaryOp("+",IntLiteral(3),IntLiteral(2)),IntLiteral(5)))],
        BoolType()
        )]))
        self.assertTrue(TestAST.test(input,expect,374))
    def test_multi_16(self):
        input = """
        function foo(): BOOLEAN;
        begin
        if (x = 5) then x:=9;
        else 
           if (x > 9) then x:=0;
           else x:=foo(a,b,x);
        end
        """
        expect = str(Program([FuncDecl(
        Id("foo"),[],[],
        [If(BinaryOp("=",Id("x"),IntLiteral(5)),
        [Assign(Id("x"),IntLiteral(9))],
        [If(BinaryOp(">",Id("x"),IntLiteral(9)),
        [Assign(Id("x"),IntLiteral(0))],
        [Assign(Id("x"),CallExpr(Id("foo"),[Id("a"),Id("b"),Id("x")]))]
        )])
        ],BoolType()
        )
        ]))
        self.assertTrue(TestAST.test(input,expect,375))
    def test_multi_17(self):
        input = """
        function foo(): BOOLEAN;
        begin
        if (x = 5) then
            x:=-foo(a,b);
        begin
        a:=9;
        a:=x+9;
        end 
        end
        """
        expect = str(Program([FuncDecl(
            Id("foo"),
            [],[],
            [If(
             BinaryOp("=",Id("x"),IntLiteral(5)),
             [
              Assign(Id("x"),UnaryOp("-",CallExpr(Id("foo"),[Id("a"),Id("b")]))),
             ]),
                Assign(Id("a"), IntLiteral(9)),
                Assign(Id("a"), BinaryOp("+", Id("x"), IntLiteral(9)))
            ],
            BoolType()
        )]))
        self.assertTrue(TestAST.test(input,expect,376))

    def test_multi_18(self):
        input = """
           function foo(): BOOLEAN;
           begin
           if (x = 5) then
           begin
               x:=-foo(a,b);
               a:=x+9;
           end
           a:=9;
           end
           """
        expect = str(Program([FuncDecl(
            Id("foo"),
            [], [],
            [If(
                BinaryOp("=", Id("x"), IntLiteral(5)),
                [
                    Assign(Id("x"), UnaryOp("-", CallExpr(Id("foo"), [Id("a"), Id("b")]))),
                    Assign(Id("a"), BinaryOp("+", Id("x"), IntLiteral(9)))
                ]),
                Assign(Id("a"), IntLiteral(9)),

            ],
            BoolType()
        )]))
        self.assertTrue(TestAST.test(input, expect, 377))
    def test_multi_19(self):
        input = """
        function foo(): String;
        begin
        if (true) then 
            begin
            x:=9;
            a:=x;
            end
        else 
           begin
              x:=5/2;
              break;
           end
        end
        """
        expect = str(Program([FuncDecl(
        Id("foo"),
        [],[],
        [If(
        BooleanLiteral(True),
        [Assign(Id("x"),IntLiteral(9)),Assign(Id("a"),Id("x"))],
        [Assign(Id("x"),BinaryOp("/",IntLiteral(5),IntLiteral(2))),Break()]
        )],
        StringType())
        ]))
        self.assertTrue(TestAST.test(input,expect,378))
    def test_multi_20(self):
        input = """
        procedure foo();
        var x: real; y:array[1 .. 3] of boolean;
        begin
           
        end
        """
        expect = str(Program([FuncDecl(
         Id("foo"),
         [],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),ArrayType(1,3,BoolType()))],
         []
        )
        ]))
        self.assertTrue(TestAST.test(input,expect,379))

    def test_multi_21(self):
        input = """
           procedure foo();
           var x: real; y:array[1 .. 3] of boolean;
           begin
              if (x <> 5 and then foo(x) ) then
                x:=x+1; 
           end
           """
        expect = str(Program([FuncDecl(
            Id("foo"),
            [], [VarDecl(Id("x"), FloatType()), VarDecl(Id("y"), ArrayType(1, 3, BoolType()))],
            [If(
                BinaryOp("andthen",BinaryOp("<>",Id("x"),IntLiteral(5)),CallExpr(Id("foo"),[Id("x")])),
                [Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]

            )]
        )
        ]))
        self.assertTrue(TestAST.test(input, expect, 380))
    def test_multi_22(self):
        input = """
           procedure foo();
           var x: real; y:array[1 .. 3] of boolean;
           begin
              if (x <> 5 and then foo(x) ) then
                y[0]:=x; 
           end
           """
        expect = str(Program([FuncDecl(
            Id("foo"),
            [], [VarDecl(Id("x"), FloatType()), VarDecl(Id("y"), ArrayType(1, 3, BoolType()))],
            [If(
                BinaryOp("andthen",BinaryOp("<>",Id("x"),IntLiteral(5)),CallExpr(Id("foo"),[Id("x")])),
                [Assign(ArrayCell(Id("y"),IntLiteral(0)),Id("x"))]
            )]
        )
        ]))
        self.assertTrue(TestAST.test(input, expect, 381))
    def test_multi_23(self):
        input = """
           procedure foo();
           var x: real; y:array[1 .. 3] of boolean;
           begin
              if (x <> 5 Or ELSE foo(x) ) then
                y[0]:=x; 
           end
           """
        expect = str(Program([FuncDecl(
            Id("foo"),
            [], [VarDecl(Id("x"), FloatType()), VarDecl(Id("y"), ArrayType(1, 3, BoolType()))],
            [If(
                BinaryOp("orelse",BinaryOp("<>",Id("x"),IntLiteral(5)),CallExpr(Id("foo"),[Id("x")])),
                [Assign(ArrayCell(Id("y"),IntLiteral(0)),Id("x"))]
            )]
        )
        ]))
        self.assertTrue(TestAST.test(input, expect, 382))
    def test_multi_24(self):
        input = """
           procedure foo();
           begin
              x:=y:=5;
           end
           """
        expect = str(Program([FuncDecl(
            Id("foo"),
            [], [],
            [
            Assign(Id("y"),IntLiteral(5)),
            Assign(Id("x"),Id("y"))
            ]
        )
        ]))
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_multi_25(self):
        input = """
        procedure foo_123(a,b,c: integer;y: boolean);
        begin
            begin

            end
        end
        """
        expect = str(Program([FuncDecl(
            Id("foo_123"),
            [VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType()), VarDecl(Id("c"), IntType()),
             VarDecl(Id("y"), BoolType())],
             [],[])
        ]))
        self.assertTrue(TestAST.test(input,expect,384))
    def test_multi_26(self):
        input = """
        procedure foo_123();
        begin
            foo(2)[3] := a[b[2]] +3;
        end
        """
        expect = str(Program([FuncDecl(
        Id("foo_123"),
        [],[],
        [Assign(ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),IntLiteral(3)),
                BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))
        )])
        ]))
        self.assertTrue(TestAST.test(input,expect,385))
    def test_multi_27(self):
        input = """
        function count_digit(x:integer):integer;
        var count: integer;
        begin
        count:=0;
        while(x>0) do 
           begin
              x := x/10;
              count:= count+1;
           end
        end
        """
        expect = str(Program([FuncDecl(
            Id("count_digit"),
            [VarDecl(Id("x"),IntType())],
            [VarDecl(Id("count"),IntType())],
            [
               Assign(Id("count"),IntLiteral(0)),
               While(
                   BinaryOp(">",Id("x"),IntLiteral(0)),
                   [
                       Assign(Id("x"),BinaryOp("/",Id("x"),IntLiteral(10))),
                       Assign(Id("count"),BinaryOp("+",Id("count"),IntLiteral(1)))
                    ]
               )
            ],IntType())
        ]))
        self.assertTrue(TestAST.test(input,expect,386))

    def test_multi_28(self):
        """ test complex expr no invocation and index expr """
        case = """
        procedure main();
        begin
            a := ((1+1-1*1/1)mod 1)<>(((1<1)and(1>1))or((1<=1)or(1>=1)));
        end
        """
        expectation = str(Program([
            FuncDecl(
                Id("main"),
                [],
                [],
                [
                    Assign(
                        Id("a"),
                        BinaryOp(
                            "<>",
                            BinaryOp(
                                "mod",
                                BinaryOp(
                                    "-",
                                    BinaryOp(
                                        "+",
                                        IntLiteral(1),
                                        IntLiteral(1)),
                                    BinaryOp(
                                        "/",
                                        BinaryOp(
                                            "*",
                                            IntLiteral(1),
                                            IntLiteral(1)),
                                        IntLiteral(1)
                                    )
                                ),
                                IntLiteral(1)
                            ),
                            BinaryOp(
                                "or",
                                BinaryOp(
                                    "and",
                                    BinaryOp(
                                        "<",
                                        IntLiteral(1),
                                        IntLiteral(1)),
                                    BinaryOp(
                                        ">",
                                        IntLiteral(1),
                                        IntLiteral(1))
                                ),
                                BinaryOp(
                                    "or",
                                    BinaryOp(
                                        "<=",
                                        IntLiteral(1),
                                        IntLiteral(1)),
                                    BinaryOp(
                                        ">=",
                                        IntLiteral(1),
                                        IntLiteral(1))
                                )
                            )
                        )
                    )
                ], VoidType())
        ]))
        self.assertTrue(
            TestAST.test(
                case,
                expectation,
                387))

    def test_multi_29(self):
        """ test funcall """
        case = """
        procedure main();
        begin
            foo();
            foo(1);
            foo(true);
            foo("hello world");
            foo(1.1);
        end
        """
        expectation = str(Program([
            FuncDecl(Id("main"), [
            ], [
            ], [
                CallStmt(Id("foo"), [
                ]),
                CallStmt(Id("foo"), [
                    IntLiteral(1)
                ]),
                CallStmt(Id("foo"), [
                    BooleanLiteral(True)
                ]),
                CallStmt(Id("foo"), [
                    StringLiteral("hello world")
                ]),
                CallStmt(Id("foo"), [
                    FloatLiteral(1.1)
                ])
            ], VoidType())
        ]))
        self.assertTrue(
            TestAST.test(
                case,
                expectation,
                388))

    def test_multi_30(self):
        """ test funcall with expr """
        case = """
        procedure main();
        begin
            foo(1+2*3/4 mod 100);
            foo(1 and 2);
            foo(1>=2);
        end
        """
        expectation = str(Program([
            FuncDecl(Id("main"), [
            ], [
            ], [
                CallStmt(Id("foo"), [
                    BinaryOp(
                        "+",
                        IntLiteral(1),
                        BinaryOp(
                            "mod",
                            BinaryOp(
                                "/",
                                BinaryOp(
                                    "*",
                                    IntLiteral(2),
                                    IntLiteral(3)
                                ), IntLiteral(4)
                            ), IntLiteral(100)
                        )
                    )
                ]),
                CallStmt(Id("foo"), [
                    BinaryOp("and", IntLiteral(1), IntLiteral(2))
                ]),
                CallStmt(Id("foo"), [
                    BinaryOp(">=", IntLiteral(1), IntLiteral(2))
                ])], VoidType())
        ]))
        self.assertTrue(
            TestAST.test(
                case,
                expectation,
                389))

    def test_multi_31(self):
        """ test multi param funcall """
        case = """
        procedure main();
        begin
            foo(1,2,3);
            foo(a,b,c);
            foo(1+1, 2*2, 3 or 3);
        end
        """
        expectation = str(Program([
            FuncDecl(Id("main"), [
            ], [
            ], [
                CallStmt(Id("foo"), [
                    IntLiteral(1),
                    IntLiteral(2),
                    IntLiteral(3)
                ]),
                CallStmt(Id("foo"), [
                    Id("a"),
                    Id("b"),
                    Id("c")
                ]),
                CallStmt(Id("foo"), [
                    BinaryOp("+", IntLiteral(1), IntLiteral(1)),
                    BinaryOp("*", IntLiteral(2), IntLiteral(2)),
                    BinaryOp("or", IntLiteral(3), IntLiteral(3))
                ])
            ], VoidType())
        ]))
        self.assertTrue(
            TestAST.test(
                case,
                expectation,
                390))

    def test_multi_32(self):
        """ test if """
        case = """
        procedure main();
        begin
            if a or b then
                a := b;
        end
        """
        expectation = str(Program([
            FuncDecl(Id("main"), [
            ], [
            ], [
                If(BinaryOp("or", Id("a"), Id("b")), [
                    Assign(Id("a"), Id("b"))
                ], [
                ])
            ], VoidType())
        ]))
        self.assertTrue(
            TestAST.test(
                case,
                expectation,
                391))

    def test_multi_33(self):
        """ test if else """
        case = """
        procedure main();
        begin
            if a or b then
                a := b;
            else
                b := a;
        end
        """
        expectation = str(Program([
            FuncDecl(Id("main"), [
            ], [
            ], [
                If(BinaryOp("or", Id("a"), Id("b")), [
                    Assign(Id("a"), Id("b"))
                ], [
                    Assign(Id("b"), Id("a"))
                ])
            ], VoidType())
        ]))
        self.assertTrue(
            TestAST.test(
                case,
                expectation,
                392))

    def test_multi_34(self):
        """ test if else if else """
        case = """
        procedure main();
        begin
            if a > b then
                if a > c then
                    c := b := a;
                else
                    a := b := c;
            else
                if b > c then
                    c := b := a;
                else
                    a := b := c;
        end
        """
        expectation = str(Program([
            FuncDecl(Id("main"), [
            ], [
            ], [
                If(BinaryOp(">", Id("a"), Id("b")), [
                    If(BinaryOp(">", Id("a"), Id("c")), [
                        Assign(Id("b"), Id("a")),
                        Assign(Id("c"), Id("b"))
                    ], [
                        Assign(Id("b"), Id("c")),
                        Assign(Id("a"), Id("b"))
                    ])
                ], [
                    If(BinaryOp(">", Id("b"), Id("c")), [
                        Assign(Id("b"), Id("a")),
                        Assign(Id("c"), Id("b"))
                    ], [
                        Assign(Id("b"), Id("c")),
                        Assign(Id("a"), Id("b"))
                    ])
                ])
            ], VoidType())
        ]))
        self.assertTrue(
            TestAST.test(
                case,
                expectation,
                393))

    def test_multi_35(self):
        """ test for up """
        case = """
        procedure main();
        begin
            for i := 0 to 10 do
                sum := sum + arr[x];
        end
        """
        expectation = str(Program([
            FuncDecl(Id("main"), [
            ], [
            ], [
                For(Id("i"), IntLiteral(0), IntLiteral(10), True, [
                    Assign(Id("sum"), BinaryOp(
                        "+",
                        Id("sum"),
                        ArrayCell(Id("arr"), Id("x"))))
                ])
            ], VoidType())
        ]))
        self.assertTrue(
            TestAST.test(
                case,
                expectation,
                394))

    def test_multi_36(self):
        """ test for down """
        case = """
        procedure main();
        begin
            for i := 10 downto 0 do
                sum := sum + arr[x];
        end
        """
        expectation = str(Program([
            FuncDecl(Id("main"), [
            ], [
            ], [
                For(Id("i"), IntLiteral(10), IntLiteral(0), False, [
                    Assign(Id("sum"), BinaryOp(
                        "+",
                        Id("sum"),
                        ArrayCell(Id("arr"), Id("x"))))
                ])
            ], VoidType())
        ]))
        self.assertTrue(
            TestAST.test(
                case,
                expectation,
                395))

    def test_multi_37(self):
        """ test simple call expr """
        case = """
        procedure main();
        begin
            a := foo();
            b := foo(a);
            c := foo(a,b,c);
            d := foo(1,2,3);
            e := foo(1+2,3+4,5*6);
        end
        """
        expectation = str(Program([
            FuncDecl(Id("main"), [
            ], [
            ], [
                Assign(Id("a"), CallExpr(Id("foo"), [
                ])),
                Assign(Id("b"), CallExpr(Id("foo"), [
                    Id("a")
                ])),
                Assign(Id("c"), CallExpr(Id("foo"), [
                    Id("a"), Id("b"), Id("c")
                ])),
                Assign(Id("d"), CallExpr(Id("foo"), [
                    IntLiteral(1),
                    IntLiteral(2),
                    IntLiteral(3)
                ])),
                Assign(Id("e"), CallExpr(Id("foo"), [
                    BinaryOp("+", IntLiteral(1), IntLiteral(2)),
                    BinaryOp("+", IntLiteral(3), IntLiteral(4)),
                    BinaryOp("*", IntLiteral(5), IntLiteral(6))
                ]))
            ], VoidType())
        ]))
        self.assertTrue(
            TestAST.test(
                case,
                expectation,
                396))

    def test_multi_38(self):
        """ test complex call expr """
        case = """
        procedure main();
        begin
            a := foo();
            b := foo(bar());
            c := foo(bar(baz()));
            d := foo(a);
            e := foo(bar(b));
            f := foo(bar(baz(c)));
        end
        """
        expectation = str(Program([
            FuncDecl(Id("main"), [
            ], [
            ], [
                Assign(Id("a"), CallExpr(Id("foo"), [
                ])),
                Assign(Id("b"), CallExpr(Id("foo"), [
                    CallExpr(Id("bar"), [
                    ])
                ])),
                Assign(Id("c"), CallExpr(Id("foo"), [
                    CallExpr(Id("bar"), [
                        CallExpr(Id("baz"), [
                        ])
                    ])
                ])),
                Assign(Id("d"), CallExpr(Id("foo"), [
                    Id("a")
                ])),
                Assign(Id("e"), CallExpr(Id("foo"), [
                    CallExpr(Id("bar"), [
                        Id("b")
                    ])])),
                Assign(Id("f"), CallExpr(Id("foo"), [
                    CallExpr(Id("bar"), [
                        CallExpr(Id("baz"), [
                            Id("c")
                        ])
                    ])
                ]))
            ], VoidType())
        ]))
        self.assertTrue(
            TestAST.test(
                case,
                expectation,
                397))

    def test_multi_39(self):
        """ test while """
        case = """
        procedure main();
        begin
            while a > b do
                sum := sum + 1;
        end
        """
        expectation = str(Program([
            FuncDecl(Id("main"), [
            ], [
            ], [
                While(BinaryOp(">", Id("a"), Id("b")), [
                    Assign(
                        Id("sum"),
                        BinaryOp("+", Id("sum"), IntLiteral(1))
                    )
                ])
            ], VoidType())
        ]))
        self.assertTrue(
            TestAST.test(
                case,
                expectation,
                398))

    def test_multi_40(self):
        """ test continue """
        case = """
        procedure count_odd_number(max: integer);
        begin
            i := 0;
            while i < max do
                if i mod 2 = 0 then
                    continue;
                else
                    sum := sum + 1;
        end
        """
        expectation = str(Program([
            FuncDecl(Id("count_odd_number"), [
                VarDecl(Id("max"), IntType())
            ], [

            ], [
                Assign(Id("i"), IntLiteral(0)),
                While(BinaryOp("<", Id("i"), Id("max")), [
                    If(BinaryOp(
                        "=",
                        BinaryOp("mod", Id("i"), IntLiteral(2)),
                        IntLiteral(0)
                    ), [
                        Continue()
                    ], [
                        Assign(
                            Id("sum"),
                            BinaryOp("+", Id("sum"), IntLiteral(1)))
                    ])
                ])
            ], VoidType())
        ]))
        self.assertTrue(
            TestAST.test(
                case,
                expectation,
                399))