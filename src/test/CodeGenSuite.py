import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_int(self):
    #     """Simple program: int main() {} """
    #     input = """procedure main(); begin putInt(100); end"""
    #     expect = "100"
    #     self.assertTrue(TestCodeGen.test(input,expect,500))

    # def test_int4(self):
    #     """Simple program: int main() {} """
    #     input = """procedure main(); begin putFloat(100.0); end"""
    #     expect = "100.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,503))

    # def test_int_ast(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putInt"),[IntLiteral(5)])])])
    # 	expect = "5"
    # 	self.assertTrue(TestCodeGen.test(input,expect,501))

    # def test2(self):
    #     input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putFloat"),[FloatLiteral(5.0)])])])
    #     expect = "5.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,502))

    # def abc(self):
    #     input = '''
    #     var a: integer;
    #     procedure main(b: integer);
    #     var c: real;
    #     begin
    #         a := b;
    #     end
    #     '''

    #     self.env = [a,main] Symbol(Cname)

    #     main:
    #         subbody
    #             frame
    #             symbol_local:
    #                 Symbol(Index)
    #                 args: 0
    #                 b: 1
    #                 c: 2

    #     a + 1
    #     1 + 1

    #     code, type = self.visit()

    #     lhs, rhs, op

    #     self.emit.printout(code)

    #     BinaryOp: code, type

    def test_0(self):
        """Simple program: int main() {} """
        # input = """void main() {putInt(100);}"""
        case = '''
        procedure main();
        begin
            putInt(1000);
        end
        '''
        expectation = "1000"
        self.assertTrue(TestCodeGen.test(case, expectation, 500))

    def test_1(self):
        case = Program([
            FuncDecl(Id("foo"), [
            ], [], [
                CallStmt(Id("putInt"), [IntLiteral(100)])
            ], VoidType()),

            FuncDecl(Id("main"), [
            ], [
            ], [
                CallStmt(Id("foo"), []),
                CallStmt(Id("putFloat"), [FloatLiteral(5.5)])
            ], VoidType())
        ])
        expectation = "1005.5"
        self.assertTrue(TestCodeGen.test(case, expectation, 501))

    # def test_2(self):
    #     ''' test redeclared func - func '''
    #     case = """
    #     procedure main();
    #     begin
    #         putInt(foo());
    #         putFloat(foo1());
    #         return;
    #     end

    #     function foo(): integer;
    #     begin
    #         return 1;
    #     end

    #     function foo1(): real;
    #     begin
    #         return 1.0;
    #     end
    #     """
    #     expectation = '1\n1.0'
    #     self.assertTrue(TestCodeGen.test(case, expectation, 502))

    def test_3(self):
        ''' test int + int '''
        case = '''
        procedure main();
        begin
            putInt(1 + 1);
        end
        '''
        expectation = '2'
        self.assertTrue(TestCodeGen.test(case, expectation, 503))

    def test_4(self):
        ''' test float + int '''
        case = '''
        procedure main();
        begin
            putFloat(1.1 + 2);
        end
        '''
        expectation = '3.1'
        self.assertTrue(TestCodeGen.test(case, expectation, 504))

    def test_5(self):
        ''' test float + float '''
        case = '''
        procedure main();
        begin
            putFloat(1.0 + 2.3);
        end
        '''
        expectation = '3.3'
        self.assertTrue(TestCodeGen.test(case, expectation, 505))

    def test_6(self):
        ''' test int - int '''
        case = '''
        procedure main();
        begin
            putInt(2 - 1);
        end
        '''
        expectation = '1'
        self.assertTrue(TestCodeGen.test(case, expectation, 506))

    def test_7(self):
        ''' test float - float '''
        case = '''
        procedure main();
        begin
            putFloat(2.3 - 1.2);
        end
        '''
        expectation = '1.0999999'
        self.assertTrue(TestCodeGen.test(case, expectation, 507))

    def test_8(self):
        ''' test int - float '''
        case = '''
        procedure main();
        begin
            putFloat(2 - 1.1);
        end
        '''
        expectation = '0.9'
        self.assertTrue(TestCodeGen.test(case, expectation, 508))

    def test_9(self):
        ''' test float - int '''
        case = '''
        procedure main();
        begin
            putFloat(2.4 - 1);
        end
        '''
        expectation = '1.4000001'
        self.assertTrue(TestCodeGen.test(case, expectation, 509))

    def test_10(self):
        case = '''
        procedure main();
        begin
            putInt(1 * 2);
            putFloat(1.2 * 4);
        end
        '''
        expectation = '24.8'
        self.assertTrue(TestCodeGen.test(case, expectation, 510))

    def test_11(self):
        case = '''
        procedure main();
        begin
            putFloat(4 / 2);
            putFloat(4.2 / 2);
        end
        '''
        expectation = '2.02.1'
        self.assertTrue(TestCodeGen.test(case, expectation, 511))

    def test_12(self):
        case = '''
        var x, y: integer;
        procedure main();
        var x,y: real;
        begin
            foo();
        end
        procedure foo();
        var x,y: real;
        begin
        end
        '''
        expectation = ''
        self.assertTrue(TestCodeGen.test(case, expectation, 512))

    def test_13(self):
        case = '''
        var x, y: integer;
        var a, b, c: real;
        procedure main();
        var x,y: real;
        begin
            foo();
        end
        procedure foo();
        var x,y: real;
        begin
        end
        '''
        expectation = ''
        self.assertTrue(TestCodeGen.test(case, expectation, 513))

    def test_14(self):
        case = '''
        var a: integer;
        procedure main();
        begin
            a := 1;
            putInt(a);
        end
        '''
        expectation = '1'
        self.assertTrue(TestCodeGen.test(case, expectation, 514))

    def test_15(self):
        case = '''
        var a: real;
        procedure main();
        begin
            a := 1.34;
            putFloat(a);
        end
        '''
        expectation = '1.34'
        self.assertTrue(TestCodeGen.test(case, expectation, 515))

    def test_16(self):
        case = '''
        var a: real;
        procedure main();
        begin
            a := 43;
            a := 1.34 + a;
            putFloat(a);
        end
        '''
        expectation = '44.34'
        self.assertTrue(TestCodeGen.test(case, expectation, 516))

    def test_17(self):
        case = '''
        procedure main();
        var a: integer;
        begin
            a := 1;
            putInt(a);
        end
        '''
        expectation = '1'
        self.assertTrue(TestCodeGen.test(case, expectation, 517))

    def test_18(self):
        case = '''
        procedure main();
        begin
            putString("Hello World");
        end
        '''
        expectation = 'Hello World'
        self.assertTrue(TestCodeGen.test(case, expectation, 518))

    def test_19(self):
        case = '''
        procedure main();
        var a: boolean;
        begin
            a := 1 < 2;
            putBool(a);
        end
        '''
        expectation = 'true'
        self.assertTrue(TestCodeGen.test(case, expectation, 519))

    def test_20(self):
        case = '''
        procedure main();
        var a: integer;
        begin
            a := 1;
            a := -a;
            putInt(a);
        end
        '''
        expectation = '-1'
        self.assertTrue(TestCodeGen.test(case, expectation, 520))

    def test_21(self):
        case = '''
        procedure main();
        var a: real;
        begin
            a := 1.123;
            a := -a;
            putFloat(a);
        end
        '''
        expectation = '-1.123'
        self.assertTrue(TestCodeGen.test(case, expectation, 521))

    def test_22(self):
        case = '''
        procedure main();
        var a: boolean;
        begin
            a := True;
            a := not a;
            putBool(a);
        end
        '''
        expectation = 'false'
        self.assertTrue(TestCodeGen.test(case, expectation, 522))

    def test_23(self):
        case = '''
        procedure main();
        var a: boolean;
        begin
            if (True) then
                putString("true");
            else
                putString("false");
        end
        '''
        expectation = 'true'
        self.assertTrue(TestCodeGen.test(case, expectation, 523))

    def test_24(self):
        case = '''
        procedure main();
        var a: integer;
            b: integer;
        begin
            a := 10;
            b := 0 ;
            while(b < a) do
                b := b + 1 ;

            putInt(b);
        end
        '''
        expectation = '10'
        self.assertTrue(TestCodeGen.test(case, expectation, 524))