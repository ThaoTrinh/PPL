import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):

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

    def test_2(self):
        ''' test int + int '''
        case = '''
        procedure main();
        begin
            putInt(1 + 1);
        end
        '''
        expectation = '2'
        self.assertTrue(TestCodeGen.test(case, expectation, 502))

    def test_3(self):
        ''' test float + float '''
        case = '''
        procedure main();
        begin
            putFloat(1.0 + 2.3);
        end
        '''
        expectation = '3.3'
        self.assertTrue(TestCodeGen.test(case, expectation, 503))

    def test_4(self):
        ''' test float - float '''
        case = '''
        procedure main();
        begin
            putFloat(2.3 - 1.2);
        end
        '''
        expectation = '1.0999999'
        self.assertTrue(TestCodeGen.test(case, expectation, 504))

    def test_5(self):
        ''' test int - float '''
        case = '''
        procedure main();
        begin
            putFloat(2 - 1.1);
        end
        '''
        expectation = '0.9'
        self.assertTrue(TestCodeGen.test(case, expectation, 505))

    def test_6(self):
        ''' test float + int '''
        case = '''
        procedure main();
        begin
            putFloat(1.1 + 2);
        end
        '''
        expectation = '3.1'
        self.assertTrue(TestCodeGen.test(case, expectation, 506))

    def test_7(self):
        ''' test redeclared func - func '''
        case = """
        procedure main();
            var a: integer;
                d: real;
        begin
            a:= foo();

            putInt(a);
            putFloat(foo1());
            return;
        end

        function foo(): integer;
        begin
            return 1;
        end

        function foo1(): real;
        begin
            return 1.0;
        end
        """
        expectation = '11.0'
        self.assertTrue(TestCodeGen.test(case, expectation, 507))

    def test_8(self):
        ''' test float - int '''
        case = '''
        procedure main();
        begin
            putFloat(2.4 - 1);
        end
        '''
        expectation = '1.4000001'
        self.assertTrue(TestCodeGen.test(case, expectation, 508))

    def test_9(self):
        case = '''
        procedure main();
        begin
            putFloat(4 / 2);
            putFloat(4.2 / 2);
        end
        '''
        expectation = '2.02.1'
        self.assertTrue(TestCodeGen.test(case, expectation, 509))

    def test_10(self):
        ''' test int - int '''
        case = '''
        procedure main();
        begin
            putInt(2 - 1);
        end
        '''
        expectation = '1'
        self.assertTrue(TestCodeGen.test(case, expectation, 510))

    def test_11(self):
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
        self.assertTrue(TestCodeGen.test(case, expectation, 511))

    def test_12(self):
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
        self.assertTrue(TestCodeGen.test(case, expectation, 512))

    def test_13(self):
        case = '''
        var a: real;
        procedure main();
        begin
            a := 1.34;
            putFloat(a);
        end
        '''
        expectation = '1.34'
        self.assertTrue(TestCodeGen.test(case, expectation, 513))

    def test_14(self):
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
        self.assertTrue(TestCodeGen.test(case, expectation, 514))

    def test_15(self):
        case = '''
        procedure main();
        begin
            putString("Hello World");
        end
        '''
        expectation = 'Hello World'
        self.assertTrue(TestCodeGen.test(case, expectation, 515))

    def test_16(self):
        case = '''
        procedure main();
        begin
            putInt(1 * 2);
            putFloat(1.2 * 4);
        end
        '''
        expectation = '24.8'
        self.assertTrue(TestCodeGen.test(case, expectation, 516))

    def test_17(self):
        case = '''
        procedure main();
        var a: boolean;
        begin
            a := 1 < 2;
            putBool(a);
        end
        '''
        expectation = 'true'
        self.assertTrue(TestCodeGen.test(case, expectation, 517))

    def test_18(self):
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
        self.assertTrue(TestCodeGen.test(case, expectation, 518))

    def test_19(self):
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
        self.assertTrue(TestCodeGen.test(case, expectation, 519))

    def test_20(self):
        case = '''
        var a: integer;
        procedure main();
        begin
            a := 1;
            putInt(a);
        end
        '''
        expectation = '1'
        self.assertTrue(TestCodeGen.test(case, expectation, 520))

    def test_21(self):
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
        self.assertTrue(TestCodeGen.test(case, expectation, 521))

    def test_22(self):
        case = '''
        procedure main();
        var a: integer;
        begin
            a := 1;
            putInt(a);
        end
        '''
        expectation = '1'
        self.assertTrue(TestCodeGen.test(case, expectation, 522))

    def test_23(self):
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
        self.assertTrue(TestCodeGen.test(case, expectation, 523))

    def test_24(self):
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
        self.assertTrue(TestCodeGen.test(case, expectation, 524))

    def test_25(self):
        case = '''
        procedure main();
        var a: integer;
            b: integer;
        begin
            a := 10;
            b := 0 ;
            while(b < a) do
                begin
                b := b + 1 ;
                if (b = 7) then 
                    break;
            end
            putInt(b);

        end
        '''
        expectation = '7'
        self.assertTrue(TestCodeGen.test(case, expectation, 525))

    def test_26(self):
        case = '''
        procedure main();
        var a: integer;
            b: integer;
            c: integer;
        begin
            a := 10;
            b := 0 ;
            c:=0;
            while(b < a) do
                begin

                b := b + 1 ;
                if (b = 7) then
                    continue;
                c:= c+1;
            end
            putInt(c);

        end
        '''
        expectation = '9'
        self.assertTrue(TestCodeGen.test(case, expectation, 526))

    def test_27(self):
        case = '''
        procedure main();
        var a: integer;
            b: integer;
            c: integer;
        begin
            a := 10;
            b := 0 ;
            c:=0;
                if (b = 7) then
                    return;
                else
                    return;
        end
        '''
        expectation = ''
        self.assertTrue(TestCodeGen.test(case, expectation, 527))

    def test_28(self):
        case = '''
        function foo(): integer;
        begin
            return 3;
        end
        procedure main();
            var a: integer;
        begin
            a:=foo();
            putInt(a);
        end
        '''
        expectation = '3'
        self.assertTrue(TestCodeGen.test(case, expectation, 528))

    def test_29(self):
        case = '''
        
        procedure main();
            var a: integer;
                b: integer;
        begin
            b:=0;
            for a:=3 to 7 do
                begin
                    b:=b+1;
                end
            putInt(b);
        end
        '''
        expectation = '5'
        self.assertTrue(TestCodeGen.test(case, expectation, 529))

    def test_30(self):
        case = '''
        
        procedure main();
            
        begin
            with a, b: integer; do
                begin
                a:=3;
                b:=4;
                putInt(a);
                end

        end
        '''
        expectation = '3'
        self.assertTrue(TestCodeGen.test(case, expectation, 530))

    def test_31(self):
        case = '''
        
        procedure main();
            
        begin
            putBool(1 < 2 and then 3 > 4);

        end
        '''
        expectation = 'false'
        self.assertTrue(TestCodeGen.test(case, expectation, 531))

    def test_32(self):
        case = '''
        
        procedure main();
            
        begin
            putBool(1 < 2 or else 3 > 4);

        end
        '''
        expectation = 'true'
        self.assertTrue(TestCodeGen.test(case, expectation, 532))

    def test_33(self):
        case = '''
        function foo(): real;
        begin
            return 3.4;
        end
        procedure main();
            var a: real;
        begin
            a:= foo();
            putFloat(a);
        end
        '''
        expectation = '3.4'
        self.assertTrue(TestCodeGen.test(case, expectation, 533))

    def test_34(self):
        case = '''
        function foo(): boolean;
        begin
            return true;
        end
        procedure main();
            var a: boolean;
        begin
            a:= foo();
            putBool(a);
        end
        '''
        expectation = 'true'
        self.assertTrue(TestCodeGen.test(case, expectation, 534))

    def test_35(self):
        case = '''

        procedure main();
            
        begin
        putBool(1<2 and then 2 < 3 and then 4<3);
        end
        '''
        expectation = 'false'
        self.assertTrue(TestCodeGen.test(case, expectation, 535))

    def test_36(self):
        case = '''

        procedure main();
            
        begin
        if (1<2) then
            begin
                if(3<4) then
                    begin
                        putInt(3);
                    end
            end
        end
        '''
        expectation = '3'
        self.assertTrue(TestCodeGen.test(case, expectation, 536))

    def test_37(self):
        case = '''

        procedure main();
            var a, b, c: integer;
        begin
            c:=0;
            for a:=3 to 7 do
                begin
                    for b:=5 downto 3 do
                        begin
                        end
                end

            putInt(c);
        end
        '''
        expectation = '0'
        self.assertTrue(TestCodeGen.test(case, expectation, 537))

    def test_38(self):
        case = '''
        
        procedure main();
            
        begin
            putBool(1 > 2 or else 3 > 4 or else 4 < 5);

        end
        '''
        expectation = 'true'
        self.assertTrue(TestCodeGen.test(case, expectation, 538))

    def test_39(self):
        case = '''
        
        procedure main();
            
        begin
            putBool(1 > 2 or else 3 > 4 or else 4 > 5);

        end
        '''
        expectation = 'false'
        self.assertTrue(TestCodeGen.test(case, expectation, 539))

    def test_40(self):
        case = '''
        
        procedure main();
            
        begin
            putBool((1 > 2 or else 3 < 4) and (1 < 2));

        end
        '''
        expectation = 'true'
        self.assertTrue(TestCodeGen.test(case, expectation, 540))

    def test_41(self):
        case = '''
        
        procedure main();
            
        begin
            putBool((1 > 2 and then 3 < 4) and (1 < 2));

        end
        '''
        expectation = 'false'
        self.assertTrue(TestCodeGen.test(case, expectation, 541))

    def test_42(self):
        case = '''
        
        procedure main();
            
        begin
            putBool((1 > 2 and then 3 < 4) or (1 < 2));

        end
        '''
        expectation = 'true'
        self.assertTrue(TestCodeGen.test(case, expectation, 542))

    def test_43(self):
        case = '''
        
        procedure main();
            
        begin
            putBool((1 > 2 and then 3 < 4) or (1 < 2 and then 2 < 1));

        end
        '''
        expectation = 'false'
        self.assertTrue(TestCodeGen.test(case, expectation, 543))

    def test_44(self):
        case = '''
        
        procedure main();
            
        begin
            putInt(5 div 3);

        end
        '''
        expectation = '1'
        self.assertTrue(TestCodeGen.test(case, expectation, 544))

    def test_45(self):
        case = '''
        
        procedure main();
            
        begin
            putInt(5 mod 3);

        end
        '''
        expectation = '2'
        self.assertTrue(TestCodeGen.test(case, expectation, 545))

    def test_46(self):
        case = '''
        
        function foo(a: integer; b: integer): integer;
        begin
            return a + b;
        end
        procedure main();
            var c: integer;
        begin
            c:=foo(1,2);
            putInt(c);

        end
        '''
        expectation = '3'
        self.assertTrue(TestCodeGen.test(case, expectation, 546))

    def test_46(self):
        case = '''
        
        function foo(a: integer; b: real): real;
        begin
            return a + b;
        end
        procedure main();
            var c: real;
        begin
            c:=foo(1,2);
            putFloat(c);

        end
        '''
        expectation = '3.0'
        self.assertTrue(TestCodeGen.test(case, expectation, 546))

    def test_47(self):
        ''' test redeclared func - func '''
        case = """
        procedure main();
        begin
            putInt(foo());
            putFloat(foo1());
            return;
        end

        function foo(): integer;
        begin
            return 1;
        end

        function foo1(): real;
        begin
            return 1.0;
        end
        """
        expectation = '11.0'
        self.assertTrue(TestCodeGen.test(case, expectation, 547))

    def test_48(self):
        ''' test redeclared func - func '''
        case = """
        procedure main();
        var a, b: real;
        begin
            a := 100;
            b := 0;
            while (a - b <> 0) do
                b := b + 1;

            if b = 100.0 then
            begin
                putString("ok");
                return;
            end
        end
        """
        expectation = 'ok'
        self.assertTrue(TestCodeGen.test(case, expectation, 548))

    def test_49(self):
        input = """ var a:real;
                    procedure main(); 
                                                                            
                    begin
                        a:=9.5;
                        with a,b: integer;
                        do
                        begin
                            b:=859;
                            a:= b-179;
                            //putInt(a);
                        end
                        putFloat(a);                          
                    end 
                                        
                """
        expect = "9.5"
        self.assertTrue(TestCodeGen.test(input,expect,549))

    def test_50(self):
        input = """ var a:real;
                    function foo(a: integer; b:integer; c: integer): integer;
                    begin
                        return a div b mod c;
                    end
                    procedure main(); 
                        
                    begin
                            putInt(foo(15,2,2));
                    end 
                                        
                """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,550))

    def test_51(self):
        input = """ var a:real;
                    function foo(): boolean;
                    begin
                        return (1 > 3 or else 3 > 4) or True;
                    end
                    procedure main(); 
                        
                    begin
                            putBool(foo());
                    end 
                                        
                """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,551))

    def test_52(self):
        input = """ var a:real;
                    procedure foo();
                    begin
                        putBool((1 > 3 or else 3 > 4) or True);
                    end
                    procedure main(); 
                        
                    begin
                            foo();
                    end 
                                        
                """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,552))

    def test_53(self):
        input = """ var a:integer;
                    procedure foo();
                    begin
                        for a:=3 to 7 do
                            begin
                            end
                        putInt(a);
                    end
                    procedure main(); 
                        
                    begin
                            foo();
                    end 
                                        
                """
        expect = "8"
        self.assertTrue(TestCodeGen.test(input,expect,553))

    def test_54(self):
        input = """ var a, b:integer;
                    procedure foo();
                    begin
                        b:=0;
                        for a:=3 to 7 do
                            begin
                                
                                a := a + 1;
                                while (a < 5) do
                                    begin
                                        b:=b+1;
                                        a:=a+1;
                                    end
                            end
                        putInt(b);
                    end
                    procedure main(); 
                        
                    begin
                            foo();
                    end 
                                        
                """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,554))

    def test_55(self):
        input = """ var a, b:integer;
                    procedure foo();
                    begin
                        b:=0;
                        for a:=3 to 7 do
                            begin
                                
                                a := a + 1;
                                while (a < 5) do
                                    begin
                                        b:=b+1;
                                        a:=a+1;
                                    end
                            end
                        putInt(b);
                    end
                    procedure main(); 
                        
                    begin
                            foo();
                    end 
                                        
                """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,555))

    def test_56(self):
        input = """ var a, b:integer;
                    procedure foo();
                    begin
                        with a, b: integer ; do
                            with c: integer; do
                                begin 
                                    a:=1;
                                    b:= 3;
                                    c:=4;
                                    putInt(a+b*c);
                                end
                    end
                    procedure main(); 
                        
                    begin
                            foo();
                    end 
                                        
                """
        expect = "13"
        self.assertTrue(TestCodeGen.test(input,expect,556))

    def test_57(self):
        input = """ var a, b:integer;
                    procedure foo();
                    begin
                        with a, b: integer ; do
                            with c: real; do
                                begin 
                                    a:=1;
                                    b:= 3;
                                    c:=4;
                                    putFloat(a+b*c);
                                end
                    end
                    procedure main(); 
                        
                    begin
                            foo();
                    end 
                                        
                """
        expect = "13.0"
        self.assertTrue(TestCodeGen.test(input,expect,557))

    def test_58(self):
        input = """ var a, b:integer;
                    procedure foo();
                    begin
                        with a, b: integer ; do
                            with c: integer; do
                                begin
                                a:= 0;
                                b:=0;
                                c:=3;
                                while(a<>c) do
                                    begin
                                        a:= a+1;
                                        b:=b+1;
                                    end
                            putInt(c);
                            end
                    end
                    procedure main(); 
                        
                    begin
                            foo();
                    end 
                                        
                """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,558))

    def test_59(self):
        input = """ var a, b:integer;
                    procedure foo();
                    begin
                        with a, b: integer ; do
                            with c: integer; do
                                begin
                                a:= 0;
                                b:=0;
                                c:=3;
                                while(a>c) do
                                    begin
                                        a:= a+1;
                                        b:=b+1;
                                    end
                            putInt(b);
                            end
                    end
                    procedure main(); 
                        
                    begin
                            foo();
                    end 
                                        
                """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,559))

    def test_60(self):
        input = """ var c, b:integer;
                    procedure foo(a, b: integer);
                        
                    begin
                        for c:=a to b do
                            begin
                                putInt(c);
                            end
                    end
                    procedure main(); 
                        
                    begin
                            foo(1,2);
                    end 
                                        
                """
        expect = "12"
        self.assertTrue(TestCodeGen.test(input,expect,560))

    def test_61(self):
        input = """ var c, b:integer;
                    procedure foo(a, b: integer);
                        
                    begin
                    c:=3;
                        if(a<b and then a<c) then
                            putInt(1);
                        else
                            putInt(0);
                    end
                    procedure main(); 
                        
                    begin
                            foo(1,2);
                    end 
                                        
                """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,561))

    def test_62(self):
        input = """ var c, b:integer;
                    procedure foo(a, b: integer);
                        
                    begin
                    c:=3;
                        if(a<b and then a<c) then
                            putInt(1);
                        else
                            putInt(0);
                    end
                    procedure main(); 
                        
                    begin
                            foo(5,2);
                    end 
                                        
                """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,562))

    def test_63(self):
        input = """ var c, b:integer;
                    procedure foo(a, b: integer);
                        
                    begin
                    c:=3;
                        if(a<b or else a<c) then
                            putInt(1);
                        else
                            putInt(0);
                    end
                    procedure main(); 
                        
                    begin
                            foo(2,2);
                    end 
                                        
                """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,563))

    def test_64(self):
        input = """ var c, b:integer;
                    procedure foo(a, b: integer);
                        
                    begin
                    c:=3;
                        if(a mod b = 0) then
                            putInt(1);
                        else
                            putInt(0);
                    end
                    procedure main(); 
                        
                    begin
                            foo(2,2);
                    end 
                                        
                """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,564))

    def test_65(self):
        input = """ var c, b:integer;
                    procedure foo(a, b: integer);
                        
                    begin
                    c:=3;
                        if(a mod b <> 0) then
                            putInt(1);
                        else
                            putInt(0);
                    end
                    procedure main(); 
                        
                    begin
                            foo(2,2);
                    end 
                                        
                """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,565))

    def test_66(self):
        input = """ var c, b:integer;
                    procedure foo(a, b: integer);
                        var d: boolean;
                    begin
                        d:=foo1();
                        putBool(d);
                        if (a = 2) then
                            for a:= 1 to 7 do
                                begin
                                    if (a=5) then break;
                                    else continue;
                                end
                        putInt(a);
                    end
                    procedure main(); 
                        
                    begin
                            foo(2,2);
                    end 

                    function foo1(): boolean;
                    begin
                        return True;
                    end
                """
        expect = "true5"
        self.assertTrue(TestCodeGen.test(input,expect,566))

    def test_67(self):
        input = """ 
            var a: integer;
                b: real;    
            procedure main();
            var d: boolean;
            begin
                d := true;
                putBool(not ((d and (1<2)) and then 5>4 and then 2<3));
            end
            var c: real;
            """  
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,567))

    def test_68(self):
    	input = """ 
            var a: integer;
                b: real;    
            procedure main();
            var d: boolean;
            begin
                d := true;
                putBool(not ((d and (1>2)) and then 5>4 and then 2>3));
            end
            var c: real;
            """  
    	expect = "true"
    	self.assertTrue(TestCodeGen.test(input,expect,568))

    def test_69(self):
    	input = """ 
            var a: integer;
                b: real;    
            procedure main();
            var d: boolean;
            begin
                d := true;
                putBool(not ((d and (1<2)) and then 5>4 and then 2>-3));
            end
            var c: real;
            """  
    	expect = "false"
    	self.assertTrue(TestCodeGen.test(input,expect,569))

    def test_70(self):
    	input = """ 
            var a: integer;
                b: real;    
            procedure main();
            var d: boolean;
            begin
                d := true;
                putBool(not ((d and (1<2)) and then 5>4 or else 2<-3));
            end
            var c: real;
            """  
    	expect = "false"
    	self.assertTrue(TestCodeGen.test(input,expect,570))

    def test_71(self):
    	input = """ 
            var a: integer;
                b: real;    
            procedure main();
            var d: boolean;
            begin
                d := true;
                putFloat(-5/2);
            end
            var c: real;
            """  
    	expect = "-2.5"
    	self.assertTrue(TestCodeGen.test(input,expect,571))

    def test_72(self):
    	input = """ 
            var a: integer;
                b: real;    
            procedure main();
            var d: boolean;
            begin
                d := true;
                putFloat(-5/(2 * 5) + 3);
            end
            var c: real;
            """  
    	expect = "2.5"
    	self.assertTrue(TestCodeGen.test(input,expect,572))

    def test_73(self):
    	input = """ 
            var a: integer;
                b: real;    
            procedure main();
            var d: boolean;
            begin
                d := true;
                if d then putFloat(-5/(2 * 5) + 3);
            end
            var c: real;
            """  
    	expect = "2.5"
    	self.assertTrue(TestCodeGen.test(input,expect,573))

    def test_74(self):
    	input = """ 
            var a: integer;
                b: real;    
            procedure main();
            var d: boolean;
            begin
                d := true;
                if not d then putFloat(-5/(2 * 5) + 3);
                else a:=1;
            end
            var c: real;
            """  
    	expect = ""
    	self.assertTrue(TestCodeGen.test(input,expect,574))

    def test_75(self):
    	input = """ 
            var a: integer;
                b: real;    
            procedure main();
            var d: boolean;
            begin
                d := true;
                if not d then putFloat(-5/(2 * 5) + 3);
                else if d then putFloat(-5/(2 * 5));
            end
            var c: real;
            """  
    	expect = "-0.5"
    	self.assertTrue(TestCodeGen.test(input,expect,575))

    def test_76(self):
    	input = """ 
            var a: integer;
                b: real;    
            procedure main();
            var d: boolean;
            begin
                with e: real; do
                begin 
                    e := 1.2;
                    putFloat(e);
                end
            end
            var c: real;
            """  
    	expect = "1.2"
    	self.assertTrue(TestCodeGen.test(input,expect,576))

    def test_77(self):
    	input = """ 
            var a: integer;
                b: real;    
            procedure main();
            var d: boolean;
            begin
                with e: real; do
                begin
                    with e: integer; do 
                    begin
                        e:= 1;
                        putInt(e);
                    end
                end
            end
            var c: real;
            """  
    	expect = "1"
    	self.assertTrue(TestCodeGen.test(input,expect,577))

    def test_78(self):
    	input = """ 
            var a: integer;
                b: real; 

            procedure foo();
            begin
                putInt(1);
            end   
            procedure main();
            var d: boolean;
            begin
                foo();
            end
            var c: real;
            """  
    	expect = "1"
    	self.assertTrue(TestCodeGen.test(input,expect,578))

    def test_79(self):
        input = """ 
            var a: integer;
                b: real;    
            procedure main();
            var d: boolean;
            begin
                d := true;
                putBool(not (d and (1>2) and then 5>4));
            end
            var c: real;
            """  
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,579))

    def test_80(self):
        input = """procedure main();
                begin
                    foo(1,-1);
                end
                procedure foo(x:integer; y:real);
                begin
                    putFloat(x + y);
                end"""
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 580))

    def test_81(self):
        input = """procedure main();
                begin
                    foo(1,-1,10,70+10);
                end
                procedure foo(x:integer; y:real; z:integer; t:real);
                begin
                    putFloat(t + y);
                end"""
        expect = "79.0"
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    def test_82(self):
        input = """procedure main();
                var x : integer;
                begin
                    x := foo(1,-1,10,70+10);
                    putInt(x);
                end
                function foo(x:integer; y:real; z:integer; t:real): integer;
                begin
                    return 10;
                end"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 582))

    def test_83(self):
        input = """procedure main();
                var x : integer;
                begin
                    putFloat(foo(1,-1,10,70+10));
                end
                function foo(x:integer; y:real; z:integer; t:real): real;
                begin
                    return x + y + z + t;
                end"""
        expect = "90.0"
        self.assertTrue(TestCodeGen.test(input, expect, 583))

    def test_84(self):
        input = """function foo(a,b:real;d:boolean):real;
                Begin
                    if d then
                            return 2;
                    else return 1;
                end
                procedure main();
                var a : real;
                Begin
                    putFloat(foo(1,2,true));
                end"""
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 584))

    def test_85(self):
        input = """function foo(a,b:real;d:boolean):real;
                Begin
                    return 6;
                end
                procedure main();
                var a : real;
                Begin
                    a := foo(1,2,true);
                    putFloat(a);
                end"""
        expect = "6.0"
        self.assertTrue(TestCodeGen.test(input, expect, 585))

    def test_86(self):
        input = """procedure main();
                Begin
                    with a:integer; b:real; do
                    begin
                        a := 6;
                        b := 10;
                        putFloat(a+b);
                    end
                end"""
        expect = "16.0"
        self.assertTrue(TestCodeGen.test(input, expect, 586))

    def test_87(self):
        input = """procedure main();
                var a,b:integer;
                Begin
                    a := 100;
                    b:= 60;
                    with a:integer; b:real; do
                    begin
                        a := 6;
                        b := 10;
                        putFloat(a+b);
                    end
                    putInt(a);
                end"""
        expect = "16.0100"
        self.assertTrue(TestCodeGen.test(input, expect, 587))

    def test_88(self):
        input = """procedure main();
                var a,b:integer;
                Begin
                    a := 100;
                    b:= 60;
                    while(true) do return;
                    putInt(a);
                end"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 588))

    def test_89(self):
        input = """procedure main();
                var a,b:integer;
                Begin
                    with a:integer; b:real; do
                    begin
                        a := 6;
                        b := 10;
                        if b > a then return;
                    end
                    putInt(100);
                end"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 589))

    
    def test_90(self):
        input = """procedure main();
                var a, b: integer;
                begin
                    for a := 5 dowNto -1 do
                    begin
                        putInt(a);
                        if a < 1 then putInt(a);
                    end
                end
                """
        expect = "5432100-1-1"
        self.assertTrue(TestCodeGen.test(input, expect, 590))

    def test_91(self):
        input = """procedure main();
                var a, b: integer;
                begin
                    for a := 5 downto 1 do
                    begin
                        continue;
                    end
                end
                """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 591))

    def test_92(self):
        input = """procedure main();
                var a, b: integer;
                begin
                    b := 10;
                    for a := 5 to b do
                    begin
                        putInt(a);
                        if a > 7 then
                            break;
                    end
                end
                """
        expect = "5678"
        self.assertTrue(TestCodeGen.test(input, expect, 592))

    def test_93(self):
        input = """procedure main();
                var a, b: integer;
                begin
                    b := 10;
                    for a := 5 to b do
                    begin
                        putInt(a);
                        if a > b then
                            break;
                    end
                end
                """
        expect = "5678910"
        self.assertTrue(TestCodeGen.test(input, expect, 593))

    def test_94(self):
        input = """procedure main();
                var a, b: integer;
                begin
                    b := 10;
                    for a := 5 to b do
                    begin
                        if a < 1 then
                            continue;
                        putInt(a);
                    end
                end
                """
        expect = "5678910"
        self.assertTrue(TestCodeGen.test(input, expect, 594))

    def test_95(self):
        input = """ 
            var a: integer;
                b: real;    
            procedure main();
            var a: real;
            begin
                putBool((2 * 3 <=  5) or (1 < 6 mod 7) );
            end
            var c: real;
            """  
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,595))

    def test_96(self):
    	input = """ 
            var a: integer;
                b: real;    
            procedure main();
            var a: real;
            begin
                putBool((2 * 3 <=  5) and then (1 < 6 mod 7) );
            end
            var c: real;
            """  
    	expect = "false"
    	self.assertTrue(TestCodeGen.test(input,expect,596))

    def test_97(self):
    	input = """ 
            var a: integer;
                b: real;    
            procedure main();
            var a: string;
            begin
                putStringLn("khoi");
            end
            var c: real;
            """  
    	expect = "khoi\n"
    	self.assertTrue(TestCodeGen.test(input,expect,597))

    def test_98(self):
    	input = """ 
            var a: integer;
                b: real;    
            procedure main();
            var a: real;
            begin
                putBool((2 * 3 <=  5) and then (1 < 6 mod 7) );
            end
            var c: real;
            """  
    	expect = "false"
    	self.assertTrue(TestCodeGen.test(input,expect,598))

    def test_99(self):
    	input = """ 
            var a: integer;
                b: real;    
            procedure main();
            var a: real;
            begin
                putBool(2 < 5 and then 1 < 6 and then 3>=4 );
            end
            var c: real;
            """  
    	expect = "false"
    	self.assertTrue(TestCodeGen.test(input,expect,599))