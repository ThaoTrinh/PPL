import unittest
from TestUtils import TestChecker
from AST import *
from StaticError import *

class CheckerSuite(unittest.TestCase):
    

    def test_1(self):
        """Simple program: int main() {} """
        input = """procedure main();
            var a: integer;
            begin 
                
            end
            function main(): integer;
            begin end
            """
            
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_2(self):
        """Simple program: int main() {} """
        input = """procedure main();
            var a: integer;
            begin 
                
            end
            var b, b: integer;
            """
            
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_3(self):
        """Simple program: int main() {} """
        input = """
        procedure main();
        begin return; end
        procedure foo(a, a, c: integer);
            var e: integer;
            begin 
                return;
            end
        var d: integer;
            """
            
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_4(self):
        """Simple program: int main() {} """
        input = """
        procedure main();
        begin
            return;
        end
        procedure foo(a, b, c: integer);
            var a: integer;
            begin 
                return;
            end
        var d: integer;
            """
            
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_5(self):
        """Simple program: int main() {} """
        input = """
        procedure main();
        begin 
            return ;
        end
        procedure getInt(a, b, c: integer);
            var a: integer;
            begin 
                
            end
        var d: integer;
            """
            
        expect = "Redeclared Procedure: getInt"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_6(self):
        """Simple program: int main() {} """
        input = """
        
        procedure main();
        begin
            return ;
        end
        procedure foo(a: integer);
            var A: integer;
            begin 
                return;
            end
        var a: integer;
            """
            
        expect = "Redeclared Variable: A"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_7(self):
        """Simple program: int main() {} """
        input = """
        
        procedure main(a: integer);
            var a: integer;
            begin 
                return;
            end
        var c: integer;
            """
            
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_8(self):
        """Simple program: int main() {} """
        input = """
        
        procedure main();
            var a: integer;
            begin 
                
            end
        var MAIN: integer;
            """
            
        expect = "Redeclared Variable: MAIN"
        self.assertTrue(TestChecker.test(input,expect,408))    
    
    def test_9(self):
        """Simple program: int main() {} """
        input = """
        
        procedure main();
            var a: integer;
            begin 
                
            end
        var b: integer;
        function B(): integer;
        begin end
            """
            
        expect = "Redeclared Function: B"
        self.assertTrue(TestChecker.test(input,expect,409))  

    def test_10(self):
        """Simple program: int main() {} """
        input = """
        
        procedure main();
            var a: integer;
            begin 
                return;
            end
        var b: integer;
        function foo(c, C: integer): integer;
        begin
            return 5;
        end
            """
            
        expect = "Redeclared Parameter: C"
        self.assertTrue(TestChecker.test(input,expect,410)) 

    def test_11(self):
        """Simple program: int main() {} """
        input = """
        function foo(c, C: integer): integer;
        begin
            return 5;
         end

        procedure main();
            var a: integer;
            begin 
                return ;
            end
        var b: integer;
            """
            
        expect = "Redeclared Parameter: C"
        self.assertTrue(TestChecker.test(input,expect,411)) 
    
    def test_12(self):
        """Simple program: int main() {} """
        input = """
        function foo(c, d: integer): integer;
        var a: integer;
        begin 
            a := t();
            return 7;
        end

        procedure main();
            var a: integer;
            begin 
                return ;
            end
        var b: integer;
            """
            
        expect = "Undeclared Function: t"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_13(self):
        """Simple program: int main() {} """
        input = """
        function foo(c, d: integer): integer;
        begin 
          return 5;
        end
        

        procedure main();
            var a: integer;
            begin 
                a := foo(3);
                return;
            end
        var b: integer;
            """
        ast = CallExpr(Id("foo"),[IntLiteral(3)])

        expect = str(TypeMismatchInExpression(ast))
        self.assertTrue(TestChecker.test(input,expect,413))
    

    def test_14(self):
        """Simple program: int main() {} """
        input = """
        function foo(c, d: integer): integer;

        
        begin 
            for a:= c to 7 do begin end
                return 3;
        end


        procedure main();
            begin return; end
        var b: integer;
            """
            
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_15(self):
        """Simple program: int main() {} """
        input = """
        function foo(c, d: integer): integer;
        var a: integer;
        
        begin 
            for a := c to 7 do begin end
            for e := a to 9 do begin end
                return 3;
        end


        procedure main();
            begin
                return;
             end
        var b: integer;
            """
            
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_16(self):
        """Simple program: int main() {} """
        input = """
        function foo(c, d: integer): integer;
        var a: integer;
        
        begin 
            for a := c to 7 do begin 
                for e := a to 9 do begin end
            end
            
            return 7;
        end


        procedure main();
            begin 
                return;
            end
        var b: integer;
            """
            
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_17(self):
        """Simple program: int main() {} """
        input = """
        function foo(c, d: integer): integer;
        var a: real;
        
        begin 
            for a := c to 7 do begin 
               
            end
            
        end


        procedure main();
            begin end
        var b: integer;
            """
        ast = For(Id("a"),Id("c"),IntLiteral(7),True,[])

        expect = str(TypeMismatchInStatement(ast))
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_18(self):
        """Simple program: int main() {} """
        input = """
        function foo(c, d: real): integer;
        var a, e: integer;
        
        begin 
            for a := 3 to c do begin 
                for e := a to d do begin end
            end
            
        end


        procedure main();
            begin end
        var b: integer;
            """
        ast = For(Id("a"),IntLiteral(3),Id("c"),True,[For(Id("e"),Id("a"),Id("d"),True,[])])

        expect = str(TypeMismatchInStatement(ast))
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_19(self):
        """Simple program: int main() {} """
        input = """
        function foo(c, d: real): integer;
        var a, e: integer;
        
        begin 
            for a := 3 to 7 do begin 
                for e := d to d do begin end
            end
            
        end


        procedure main();
            begin end
        var b: integer;
            """
        ast = For(Id("e"),Id("d"),Id("d"),True,[])
        expect = str(TypeMismatchInStatement(ast))
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_20(self):
        """Simple program: int main() {} """
        input = """
        function foo(c, d: integer): integer;
        var a, e: integer;
        
        begin 
            break;
            for a := 3 to 7 do begin 
                for e := d to d do begin end
            end
            
        end


        procedure main();
            begin end
        var b: integer;
            """
            
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_21(self):
        """Simple program: int main() {} """
        input = """
        function foo(c, d: integer): integer;
        var a, e: integer;
        
        begin 
            continue;
            for a := 3 to 7 do begin 
                for e := d to d do begin end
            end
            
        end


        procedure main();
            begin end
        var b: integer;
            """
            
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_22(self):
        """Simple program: int main() {} """
        input = """
        function foo(c, d: integer): integer;
        var a, e: real;
        
        begin 
            while a + 3 do begin end
            
        end


        procedure main();
            begin end
        var b: integer;
            """
            
        expect = str(TypeMismatchInStatement(While(BinaryOp("+",Id("a"),IntLiteral(3)),[])))
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_23(self):
        """Simple program: int main() {} """
        input = """
        function foo(c, d: integer): integer;
        var a: real;
        
        begin 
            while e > 3 do begin end
            return 5;
        end


        procedure main();
            begin 
                return;
            end
        var b: integer;
            """
            
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_24(self):
        """Simple program: int main() {} """
        input = """
        function foo(c, d: integer): integer;
        var a: integer;
        
        begin 
            
            continue;
            while e > 3 do begin 
                break;
            end
            a := 3;
            
        end


        procedure main();
            begin end
        var b: integer;
            """
            
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_25(self):
        """Simple program: int main() {} """
        input = """
        function foo(c, d: integer): integer;
        var a: integer;
        
        begin 
            
            while a > 3 do begin 
                break;
            end
            continue;
            
        end


        procedure main();
            begin end
        var b: integer;
            """
            
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_26(self):
        """Simple program: int main() {} """
        input = """
        function foo(c, d: integer): integer;
        var a: real;
        
        begin 
            
           a := c := d := e;
            return 5;
        end


        procedure main();
            begin 
                return;
            end
        var b: integer;
            """
            
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_27(self):
        """Simple program: int main() {} """
        input = """
        function foo(c, d: integer): integer;
        var a: boolean;
        
        begin 
            
           a := c := d ;
            
        end


        procedure main();
            begin end
        var b: integer;
            """
            
        expect = str(TypeMismatchInStatement(Assign(Id("a"),Id("c"))))
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_28(self):
        """Simple program: int main() {} """
        input = """
        function foo(c, d: integer): integer;
        var a: integer;
        
        begin 
            
           a := c := b := e;
            return 5;
        end


        procedure main();
            begin return ; end
        var b: integer;
            """
            
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_29(self):
        """Simple program: int main() {} """
        input = """
        function foo(c, d: integer): integer;
        var a: integer;
            b: boolean;
        begin 
            
           if a + 7 then begin end
        end


        procedure main();
            begin end
        var b: integer;
            """
            
        expect = str(TypeMismatchInStatement(If(BinaryOp("+",Id("a"),IntLiteral(7)),[],[])))
        self.assertTrue(TestChecker.test(input,expect,429))
    
    def test_30(self):
        """Simple program: int main() {} """
        input = """
        function foo(c, d: integer): integer;
        var a: integer;
            b: boolean;
        begin 
            
           if not a then begin end
        end


        procedure main();
            begin end
        var b: integer;
            """
            
        expect = str(TypeMismatchInExpression(UnaryOp("not",Id("a"))))
        self.assertTrue(TestChecker.test(input,expect,430))
    

    def test_31(self):
        """Simple program: int main() {} """
        input = """
        function foo(c, d: integer): integer;
        var a: integer;
            b: boolean;
        begin 
            
           a := b [ 10 ] ;
        end


        procedure main();
            begin end
        var b: integer;
            """
            
        expect = str(TypeMismatchInExpression(ArrayCell(Id("b"),IntLiteral(10))))
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_32(self):
        """Simple program: int main() {} """
        input = """
        function foo(c, d: real): integer;
        var a: integer;
            b: array [1 .. 3] of integer;
        begin 
            
           a := b [ a[c] ] ;
        end


        procedure main();
            begin end
        var b: integer;
            """
            
        expect = str(TypeMismatchInExpression(ArrayCell(Id("a"),Id("c"))))
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_33(self):
        """Simple program: int main() {} """
        input = """
        function foo(c, d: integer): integer;
        var a, e: boolean;
        
        begin 
            while a > 3 do begin end
            
        end


        procedure main();
            begin end
        var b: integer;
            """
            
        expect = str(TypeMismatchInExpression(BinaryOp(">",Id("a"),IntLiteral(3))))
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_34(self):
        """Simple program: int main() {} """
        input = """
        function foo(a: integer; b: integer): integer;

        begin 
            
            return 5;
        end


        procedure main();
            var k: array [2 .. 3] of real;
            begin 
                b := foo(3, k);
            end
        var b: integer;
            """
            
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[IntLiteral(3),Id("k")])))
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_35(self):
        """Simple program: int main() {} """
        input = """
        function foo(a: integer; b: integer): array [2 .. 3] of integer;

        var t: array [2 .. 3] of real;
        begin 
            
            return t;
        end


        procedure main();
            var k: array [2 .. 3] of real;
            begin 
            return;
            end
        var b: integer;
            """
            
        expect = str(TypeMismatchInStatement(Return(Id("t"))))
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_36(self):
        """Simple program: int main() {} """
        input = """

        procedure main();
            begin 
                return 5;
            end
            """
            
        expect = str(TypeMismatchInStatement(Return(IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_37(self):
        """Simple program: int main() {} """
        input = """

        procedure main();
            var i: integer;
            begin 
                for i := 3 to 7
                    do return;
                return;
            end

        function a(): integer;
            var i: integer;
            begin 
                for i := 3 to 7
                    do return 7;
                
            end
            """
            
        expect = str(FunctionNotReturn("a"))
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_38(self):
            
        input = """

        procedure main();
            var i: integer;
            begin 
                for i := 3 to 7
                    do return;
                while i > 7 do return;
            end

        function a(): integer;
            var i: integer;
            begin 
                for i := 3 to 7
                    do return 7;
                while i > 7 do return 5;
            end
            """
            
        expect = str(FunctionNotReturn("a"))
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_39(self):
            
        input = """

        procedure main();
            var i: integer;
            begin 
                for i := 3 to 7
                    do return;
                while i > 7 do return;
                if i > 3 then return;
                else return 5;
            end
            """
            
        expect = str(TypeMismatchInStatement(Return(IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_40(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin foo();end"""
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_41(self):
        """More complex program"""
        input = """procedure main (); begin
            putIntLn();
        end"""
        expect = str(TypeMismatchInStatement(CallStmt(Id("putIntLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_42(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],[],[
            CallStmt(Id("foo"),[])])])
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_43(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putIntLn"),[])])])
                        
        expect = str(TypeMismatchInStatement(CallStmt(Id("putIntLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,443))

    
    def test_44(self):
        """Simple program: int main() {} """
        input = """procedure main();
            begin end
            var main: integer;"""
        expect = "Redeclared Variable: main"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_45(self):
        """Simple program: int main() {} """
        input = """
        var main: integer;
        procedure main();
            begin end
            var main: integer;"""
        expect = "Redeclared Procedure: main"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_46(self):
        input = """
        var x, y : array[1 .. 3] of integer;
            a, b: integer;
            c, d: real;
            e, f: boolean;
            m, n : string;
        procedure main();
        begin
        end

        function foo() : array[1 .. 3] of integer;
        begin   
            return x;    
        end

        function foo2 (n: real; m : integer) : array[1 .. 3] of integer;
        begin
            with a, b: integer; b: real; do 
                c := b; 
            return foo();
        end
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_47(self):
        input = """
        var x, y : array[1 .. 3] of integer;
            a, b: integer;
            c, d: real;
            e, f: boolean;
            m, n : string;
        procedure main();
        begin
        end

        function foo() : array[1 .. 3] of integer;
        begin   
            return x;    
        end

        procedure foo2 (n: real; m : integer);
        begin
            with a, b: integer; c: real; do 
                with a, b: boolean; d, a: integer; do 
                    a := b;
        end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_48(self):
        input = """
        var x, y : array[1 .. 3] of integer;
            a, b: integer;
            c, d: real;
            e, f: boolean;
            m, n : string;
        procedure main();
        begin
        end

        function foo() : array[1 .. 3] of integer;
        begin   
            return x;    
        end

        procedure foo2 (n: real; m : integer; b, m: real);
        begin
        end
        """
        expect = "Redeclared Parameter: m"
        self.assertTrue(TestChecker.test(input,expect,448))


    def test_49(self):
        input = """
        var x, y : array[1 .. 3] of integer;
            a, b: integer;
            c, d: real;
            e, f: boolean;
            m, n : string;
        procedure main();
        begin
        end

        function foo() : array[1 .. 3] of integer;
        begin   
            d := f;
            return x;    
        end

        procedure foo (n: real; m : integer; b, m: real);
        begin
        end
        """
        expect = "Redeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_50(self):
        input = """
        var x, y : array[1 .. 3] of integer;
            a, b: integer;
            c, d: real;
            e, f: boolean;
            m, n : string;
        procedure main();
        begin
        end

        function foo() : array[1 .. 3] of integer;
        begin   
            return x;    
        end

        procedure foo2 (n: real; m : integer);
        var n: string;
        begin
        end
        """
        expect = "Redeclared Variable: n"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_51(self):
        input = """
        var x, y : array[1 .. 3] of integer;
            a, b: integer;
            c, d: real;
            e, f: boolean;
            m, n : string;
        procedure main();
        begin
        end

        function getInt() : array[1 .. 3] of integer;
        begin   
            return x;    
        end

        procedure foo2 (n: real; m : integer);
        var n: string;
        begin
        end
        """
        expect = "Redeclared Function: getInt"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_52(self):
        input = """
        var x, y : array[1 .. 3] of integer;
            a, b: integer;
            c, d: real;
            e, f: boolean;
            m, n : string;
        procedure main();
        begin
        end

        function putInt() : array[1 .. 3] of integer;
        begin   
            return x;    
        end

        procedure foo2 (n: real; m : integer);
        begin
        end
        """
        expect = "Redeclared Function: putInt"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_53(self):
        input = """
        var x, y : array[1 .. 3] of integer;
            a, b: integer;
            c, d: real;
            e, f: boolean;
            m, n : string;
        procedure main();
        begin
        end

        function foo() : array[1 .. 3] of integer;
        begin   
            return x;    
        end

        procedure foo2 (n: real; m : integer);
        begin
            x := g;
        end
        """
        expect = str(Undeclared(Identifier(), "g"))
        self.assertTrue(TestChecker.test(input,expect,453))
    
    def test_54(self):
        ''' test type mismatch statement assign 1 '''
        case = """
        procedure main();
        var sum: string;
        begin
            // lhs cannot be string
            sum := "Hello World";
            return;
        end
        """
        expectation = str(TypeMismatchInStatement(Assign(Id("sum"),StringLiteral("Hello World"))))
        self.assertTrue(TestChecker.test(case, expectation, 454))

    def test_55(self):
        ''' test type mismatch statement assign 2 '''
        case = """
        procedure main();
        var sum, arr: array [1 .. 2] of integer;
        begin
            // lhs cannot be array
            sum := arr;
            return;
        end
        """
        expectation = str(TypeMismatchInStatement(Assign(Id("sum"),Id("arr"))))
        self.assertTrue(TestChecker.test(case, expectation, 455))

    def test_56(self):
        ''' test typemismatchinstatement assign 4 '''
        case = """
        procedure main();
        var sum: boolean;
        begin
            // wrong coerce int->bool
            // common mistake if come from other languages
            sum := 1;
            return;
        end
        """
        expectation = str(TypeMismatchInStatement(Assign(Id("sum"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(case, expectation, 456))

    def test_57(self):
        ''' test typemismatchinstatement assign 5 '''
        case = """
        procedure main();
        var sum: real;
        begin
            sum := 1; // this should pass
            sum := true; // this should fail
            return;
        end
        """
        expectation = str(TypeMismatchInStatement(Assign(Id("sum"),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(case, expectation, 457))

    def test_58(self):
        ''' test type mismatch in return 1 '''
        case = """
        procedure main();
        begin
            return 1;
        end
        """
        expectation = str(TypeMismatchInStatement(Return(IntLiteral(1))))
        self.assertTrue(TestChecker.test(case, expectation, 458))

    def test_59(self):
        ''' test type mismatch in return 2 '''
        case = """
        procedure main();
        begin
        end

        function foo(): integer;
        begin
            return 1.0;
        end
        """
        expectation = str(TypeMismatchInStatement(Return(FloatLiteral(1.0))))
        self.assertTrue(TestChecker.test(case, expectation, 459))

    def test_60(self):
        ''' test type mismatch in return 3 '''
        case = """
        procedure main();
        begin
        end

        function foo(): array [1 .. 3] of integer;
        var x: array [2 .. 3] of integer;
        begin
            return x;
        end
        """
        expectation = str(TypeMismatchInStatement(Return(Id("x"))))
        self.assertTrue(TestChecker.test(case, expectation, 460))

    def test_61(self):
        ''' test type mismatch in return 4 '''
        case = """
        procedure main();
        begin
        end

        function foo(): array [1 .. 3] of integer;
        var x: array [1 .. 4] of integer;
        begin
            return x;
        end
        """
        expectation = str(TypeMismatchInStatement(Return(Id("x"))))
        self.assertTrue(TestChecker.test(case, expectation, 461))

    def test_62(self):
        ''' test type mismatch in return 5 '''
        case = """
        procedure main();
        begin
        end

        function foo(): array [1 .. 3] of integer;
        var x: array [1 .. 3] of real;
        begin
            return x;
        end
        """
        expectation = str(TypeMismatchInStatement(Return(Id("x"))))
        self.assertTrue(TestChecker.test(case, expectation, 462))

    def test_63(self):
        ''' test type mismatch in callstmt 1'''
        case = """
        procedure main();
        begin
            foo();
        end

        procedure foo(x: integer);
        begin
        end
        """
        expectation = str(TypeMismatchInStatement(CallStmt(Id("foo"),[])))
        self.assertTrue(TestChecker.test(case, expectation, 463))

    def test_64(self):
        ''' test type mismatch in callstmt 2 '''
        case = """
        procedure main();
        begin
            foo(1.0);
        end

        procedure foo(x: integer);
        begin
        end
        """
        
        expectation = str(TypeMismatchInStatement(CallStmt(Id("foo"),[FloatLiteral(1.0)])))
        self.assertTrue(TestChecker.test(case, expectation, 464))

    def test_65(self):
        ''' test type mismatch in callstmt 3 '''
        case = """
        procedure main();
        var x: array [2 .. 3] of integer;
        begin
            foo(x);
        end

        procedure foo(x: array [1 .. 3] of integer);
        begin
        end
        """
        expectation = str(TypeMismatchInStatement(CallStmt(Id("foo"),[Id("x")])))
        self.assertTrue(TestChecker.test(case, expectation, 465))

    def test_66(self):
        ''' test type mismatch in callstmt 4 '''
        case = """
        procedure main();
        var x: array [1 .. 4] of integer;
        begin
            foo(x);
        end

        procedure foo(x: array [1 .. 3] of integer);
        begin
        end
        """
        expectation = str(TypeMismatchInStatement(CallStmt(Id("foo"),[Id("x")])))
        self.assertTrue(TestChecker.test(case, expectation, 466))

    def test_67(self):
        ''' test type mismatch in callstmt 5 '''
        case = """
        procedure main();
        var x: array [1 .. 3] of real;
        begin
            foo(x);
        end

        procedure foo(x: array [1 .. 3] of integer);
        begin
        end
        """
        
        expectation = str(TypeMismatchInStatement(CallStmt(Id("foo"),[Id("x")])))
        self.assertTrue(TestChecker.test(case, expectation, 467))

    def test_68(self):
        ''' test type mismatch in callstmt 6 '''
        case = """
        procedure main();
        var x: array [1 .. 3] of real;
            y: array [1 .. 3] of integer;
            z: array [1 .. 3] of boolean;
        begin
            foo(x); // ok
            foo(y); // type coercion
            foo(z); // fail
        end

        procedure foo(x: array [1 .. 3] of real);
        begin
        end
        """
        expectation = str(TypeMismatchInStatement(CallStmt(Id("foo"),[Id("y")])))
        self.assertTrue(TestChecker.test(case, expectation, 468))

    def test_69(self):
        ''' test typemismatchinstatement assign 3 '''
        case = """
        procedure main();
        var sum: integer;
        begin
            // wrong coerce float->int
            sum := 1.0;
            return;
        end
        """
        expectation = str(TypeMismatchInStatement(Assign(Id("sum"),FloatLiteral(1.0))))
        self.assertTrue(TestChecker.test(case, expectation, 469))

    def test_70(self):
        input = """
        var a, b: integer; c: real;
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
            end
        """
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_71(self):
        input = """procedure main();
        var a: real;
            b: integer;
        begin
            if a + b then return;
        end"""
        expect = str(TypeMismatchInStatement(If(BinaryOp("+",Id("a"),Id("b")),[Return()],[])))
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_72(self):
        input = """procedure main();
        var a: real;
        begin
            for a := 2.2 to 5.5 do
                a := a + 1; 
        end"""
        ast = For(Id("a"),FloatLiteral(2.2),FloatLiteral(5.5),True,[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])

        expect = str(TypeMismatchInStatement(For(Id("a"),FloatLiteral(2.2),FloatLiteral(5.5),True,[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])))
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_73(self):
        input = """procedure main();
        var a: integer;
        begin
            while a do
                a := a + 1;
        end"""
        expect = str(TypeMismatchInStatement(While(Id("a"),[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])))
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_74(self):
        input = """procedure foo(a: integer; b:real);
        begin
        end
        procedure main();
        var x,y: real;
        begin
            foo(x,y);
        end"""
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[Id("x"),Id("y")])))
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_75(self):
        input = """procedure main();
        var a: integer;
            b: real;
        begin
            for a := 1 to b do
                a := a + 1; 
        end"""
        ast = For(Id("a"),IntLiteral(1),Id("b"),True,[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])

        expect =str(TypeMismatchInStatement(ast))
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_76(self):
        input = """procedure main();
        var arr: array [1 .. 5] of real;
            a, b: real;
        begin
            a := b + arr[1.2];
        end"""
        expect = str(TypeMismatchInExpression(ArrayCell(Id("arr"),FloatLiteral(1.2))))
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_77(self):
        input = """procedure main();
        var a,b,c:real;
        begin
            a := b + c[1];
        end"""
        expect = str(TypeMismatchInExpression(ArrayCell(Id("c"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_78(self):
        input = """procedure main();
        var a: boolean;
            b,c: real;
            d: integer;
        begin
            b := c + d + a;
        end"""
        expect = str(TypeMismatchInExpression(BinaryOp("+",BinaryOp("+",Id("c"),Id("d")),Id("a"))))
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_79(self):
        input = """procedure main();
        var a,b,c:integer;
        begin
            a := b mod not c;
        end"""
        expect = str(TypeMismatchInExpression(UnaryOp("not",Id("c"))))
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_80(self):
        input = """procedure main();
        var a: boolean;
            b,c: integer;
        begin
            b := c div -a;
        end"""
        expect = str(TypeMismatchInExpression(UnaryOp("-",Id("a"))))
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_81(self):
        input = """function main(): integer;
        var a: boolean;
            b,c: integer;
        begin
            b := c div -a;
            return 5;
        end"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_82(self):
        input = """procedure main();
        var a: boolean;
            b,c: integer;
        begin

        end
        
        FunCtion a(): integer;
            var b: real;
            begin
                return b;
            end
        """
        expect = str(TypeMismatchInStatement(Return(Id("b"))))
        self.assertTrue(TestChecker.test(input, expect, 482))


    def test_83(self):
        input = """procedure main();
        var a: boolean;
            b,c: integer;
        begin

        end
        
        FunCtion a(): integer;
            var b: real;
             a: integer;
            begin
                if a< 4 then
                return b;
            end
        """
        expect = str(TypeMismatchInStatement(Return(Id("b"))))
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_84(self):
        input = """procedure main();
        var a: boolean;
            b,c: integer;
        begin

        end
        
        FunCtion a(): integer;
            var b: real;
             a: integer;
            begin
                if a< 4 then
                return b;
                else main();
            end
        """
        expect = str(TypeMismatchInStatement(Return(Id("b"))))
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_85(self):
        input = """procedure main();
        var a: boolean;
            b,c: integer;
        begin
            break;
        end
        FunCtion a(): integer;
            var b: real;
             a: integer;
            begin
                return 6;
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_86(self):
        input = """procedure main();
        var a: boolean;
            b,c: integer;
        begin
        end
        FunCtion a(): real;
            var b: real;
             a: integer;
            begin
                return True;
            end
        """
        expect = str(TypeMismatchInStatement(Return(BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_87(self):
        input = """procedure main();
        var a: boolean;
            b,c: integer;
        begin
        end
        FunCtion a(): real;
            var b: real;
             a: integer;
            begin
                a := b;
                return 6;
            end
        """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),Id("b"))))
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_88(self):
        input = """procedure main();
        var a: boolean;
            b,c: integer;
        begin
        end
        FunCtion putFloatLn(): real;
            var b: real;
             a: integer;
            begin
                a := b;
                return 6;
            end
        """
        expect = "Redeclared Function: putFloatLn"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_89(self):
        input = """procedure main();
        var a: boolean;
            b,c: integer;
        begin
        end
        Var putBool: integer;
        FunCtion thao(): real;
            var b: real;
             a: integer;
            begin
                a := b;
                return 6;
            end
        """
        expect = "Redeclared Variable: putBool"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_90(self):
        input = """procedure main();
        var a: boolean;
            b,c: integer;
        begin
        end
        FunCtion putK(): array [2 .. 3] of real;
            var b: Array [2 .. 3] of integer;
             a: integer;
            begin
                return b;
            end
        """
        expect = str(TypeMismatchInStatement(Return(Id("b"))))
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_91(self):
        input = """procedure main();
        var a: array [2 .. 3] of real;
            b,c: array [2 .. 3] of integer;

        begin
            a:= putK(b);
        end
        FunCtion putK(a: array [2 .. 3] of real): array [2 .. 3] of real;
            var b: Array [2 .. 3] of real;
            begin
                return b;
            end
        """
        ast = CallExpr(Id("putK"),[Id("b")])
        expect = str(TypeMismatchInExpression(ast))
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_92(self):
        input = """procedure main();
        var a: array [2 .. 3] of integer;
            b,c: array [2 .. 3] of real;

        begin
            a:= putK(b);
        end
        FunCtion putK(a: array [2 .. 3] of real): array [2 .. 3] of real;
            var b: Array [2 .. 3] of real;
            begin
                return b;
            end
        """
        ast = Assign(Id("a"),CallExpr(Id("putK"),[Id("b")]))
        expect = str(TypeMismatchInStatement(ast))
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_93(self):
        input = """procedure main();
        var a: array [2 .. 3] of integer;
            b,c: array [2 .. 3] of real;

        begin
        end

        function e(): integer;
        begin
            with a , b : integer ; c : array [ 1 .. 2 ] of real ; do
                return c [ a ] + b ;

        end
        """

        ast = Return(BinaryOp("+",ArrayCell(Id("c"),Id("a")),Id("b")))

        expect = str(TypeMismatchInStatement(ast))
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_94(self):
        input = """procedure main();
        var a: array [2 .. 3] of integer;
            b,c: array [2 .. 3] of real;

        begin
        end

        function e(): integer;
        begin
            e();

        end
        """
        expect = "Undeclared Procedure: e"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_95(self):
        input = """procedure main();
        var a: array [2 .. 3] of integer;
            b,c: array [2 .. 3] of real;

        begin
        end

        function e(): integer;
        var a: integer;
        begin
            a:= main();

        end
        """
        expect = "Undeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_96(self):
        input = """procedure main();

        begin
            return 7;
        end

        function e(): integer;
        var a: integer;
        begin
            return 5;
        end
        """
        ast = Return(IntLiteral(7))
        expect = str(TypeMismatchInStatement(ast))
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_97(self):
        input = """procedure main();

        begin
            return;
        end

        function e(): integer;
        var a: integer;
        begin
            return;
        end
        """
        ast = Return()
        expect = str(TypeMismatchInStatement(ast))
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_98(self):
        input = """
        var x, y : array[1 .. 3] of boolean;
            a, b: integer;
            c, d: real;
            e, f: boolean;
            m, n : string;
        
        function foo() : integer ;
        begin   
            return a;    
        end

        procedure main(); 
        begin
            x[foo()] := f or b;
        end

        procedure foo2 (n: string; m : array[2 .. 3] of real);
        begin          
        end
        """
        ast = BinaryOp("or",Id("f"),Id("b"))
        expect = str(TypeMismatchInExpression(ast))
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_99(self):
        input = """
        var x, y : array[1 .. 3] of boolean;
            a, b: integer;
            c, d: real;
            e, f: boolean;
            m, n : string;
        
        function foo() : integer ;
        begin   
            return a;    
        end

        procedure main(); 
        begin
            x[foo()] := e and f or not m;
        end

        procedure foo2 (n: string; m : array[2 .. 3] of real);
        begin          
        end
        """
        ast = UnaryOp("not",Id("m"))
        expect = str(TypeMismatchInExpression(ast))
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_100(self):
        input = """
        var x, y : array[2 .. 3] of integer;
            a, b: integer;
            c, d: real;
            e, f: boolean;
            m, n : string;
        
        function foo() : array[2 .. 3] of integer;
        begin   
            return x;    
        end

        procedure main(); 
        begin
            foo2(m, foo());
        end

        procedure foo2 (n: string; m : array[2 .. 3] of real);
        begin          
        end
        """
        ast = CallStmt(Id("foo2"),[Id("m"),CallExpr(Id("foo"),[])])

        expect = str(TypeMismatchInStatement(ast))
        self.assertTrue(TestChecker.test(input,expect,500))