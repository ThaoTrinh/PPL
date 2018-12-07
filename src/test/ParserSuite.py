import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_simple_program(self):
        input = """
                procedure main() ;begin end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    
    def test_wrong_miss_close(self):
        input = """
                procedure main(
                """
        expect = "Error on line 3 col 16: <EOF>"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_wrong_program(self):
        input = """
                )procedure main(
                """
        expect = "Error on line 2 col 16: )"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_wrong_program_case2(self):
        input = """
                int main();
                """
        expect = "Error on line 2 col 16: int"
        self.assertTrue(TestParser.test(input,expect,204))

    def test_wrong_program_case3(self):
        input = """
                main() : array [1 .. 2] of real;
                begin
                    // This is a line comment 
                    {
                        begin
                            return foo(a,b,456)[a[a[a[1]]]];
                        end
                    }
                end
                a, b, c: integer;
                procedure foo();
                        y : array [2 .. 3] of real ;
                        z : array [1 .. 2] of integer ;
                    begin
                        foo (x ) ; // Call function
                        foo (y ) ; // Call function
                        foo ( z ) ; // Call function
                    end
                """
        expect = "Error on line 2 col 16: main"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_many_declare(self):
        input = """
                VAR i : real;
                function main(): integer;
                begin end
                procedure main();
                begin end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))

    def test_many_declare_case2(self):
        input = """
                VAR i : real;
                function main(): integer;
                begin
                
                
                    begin end
                
                
                end
                procedure main();
                begin
                
                
                
                end
                
                \n\t
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))

    def test_vardecl_simple(self):
        input = """
                VAR i : real;
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))

    def test_many_vardecl(self):
        input = """
                VAR i : real;
                VAR i : real;
                VAR i : real;
                VAR i : real;
                VAR i : real;
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))

    def test_invalid_vardecl_name_of_type(self):
        input = """
                VAR i : thao;
                """
        expect = "Error on line 2 col 24: thao"
        self.assertTrue(TestParser.test(input,expect,210))

    def test_invalid_vardecl_two_dimension(self):
        input = """
                var i : array [ 1 .. 2 , 3 .. 4 ] of integer ;
                """
        expect = "Error on line 2 col 39: ,"
        self.assertTrue(TestParser.test(input,expect,211))
    
    def test_vardecl(self):
        input = """
                VAR a,b,c : real;
                    thao: boolean;
                    i: array [1 .. 2] of integer;
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))

    def test_invalid_vardecl_no_type(self):
        input = """
                VAR a,b,c ;
                    i: array [1 .. 2] of interger;
                    d: array [] of boolean
                """
        expect = "Error on line 2 col 26: ;"
        self.assertTrue(TestParser.test(input,expect,213))

    def test_function(self):
        input = """
                function foo (a , b : integer ; c : real ) : array [ 1 .. 2 ] of integer ;
                    var x , y : real ;
                    begin
                        i := i + 1;
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))

    def test_function_case2(self):
        input = """
                function foo (a , b : integer ; c : real ) : array [ 1 .. 2 ] of integer ;
                    begin
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))

    def test_function_case3(self):
        input = """
                function foo (a , b : integer ; c : real ) : array [ 1 .. 2 ] of integer ;
                    begin
                        begin
                            begin
                                begin
                                end 
                            end
                        end
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))

    def test_function_wrong_end(self):
        input = """
                function foo (a , b : integer ; c : real ) : array [ 1 .. 2 ] of integer ;
                    var x , y : real ;
                    begin
                        i := i + 1;
                    end
                    end
                """
        expect = "Error on line 7 col 20: end"
        self.assertTrue(TestParser.test(input,expect,217))

    def test_invalid_function_miss_semi(self):
        input = """
                function foo (a , b : integer , c : real ) : array [ 1 .. 2 ] of integer ;
                    var x , y : real ;
                    begin
                        i = i + 1;
                    end
                """
        expect = "Error on line 2 col 46: ,"
        self.assertTrue(TestParser.test(input,expect,218))

    def test_invalid_function_type_return(self):
        input = """
                function foo (a , b : integer ; c : real );
                    var x , y : real ;
                    begin
                        i = i + 1;
                    end
                """
        expect = "Error on line 2 col 58: ;"
        self.assertTrue(TestParser.test(input,expect,219))

    def test_invalid_function_no_namefunction(self):
        input = """
                function (a , b : integer ; c : real ) : array [ 1 .. 2 ] of integer ;
                    var x , y : real ;
                    begin
                        i = i + 1;
                    end
                """
        expect = "Error on line 2 col 25: ("
        self.assertTrue(TestParser.test(input,expect,220))

    def test_procedure(self):
        input = """procedure foo (a , b : integer ; c : real );
                        var x , y : real ;
                        begin
                            i := i + 1;
                        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))

    def test_procedure_case2(self):
        input = """procedure foo ();
                    var x , y : real ;
                        a: array [1 .. 2] of integer;
                        c: boolean;
                        d: integer;
                    begin
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))

    def test_procedure_case3(self):
        input = """procedure foo ();
                    var x , y : real ;
                    begin
                        i := i + 1;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))

    def test_procedure_case4(self):
        input = """procedure foo ();
                    var x , y : real ;
                    begin
                        begin
                            begin
                                c := 5;
                            end
                        end
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))

    def test_invalid_procedure_no_argument(self):
        input = """procedure foo;
                        var x , y : real ;
                        begin
                            i = i + 1;
                        end"""
        expect = "Error on line 1 col 13: ;"
        self.assertTrue(TestParser.test(input,expect,225))

    def test_wrong_index_exp(self):
        input = """
                procedure foo(a: integer);
                begin
                    a:= a[b[]] +3;
                end"""
        expect = "Error on line 4 col 28: ]"
        self.assertTrue(TestParser.test(input,expect,226))

    def test_index_exp(self):
        input = """
                procedure foo(a: integer);
                begin
                    a(2)[3+x] := a[b[2]] +3;
                end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))

    def test_index_exp_case2(self):
        input = """
            procedure main();
                begin
                    a := foo(1+a[i-goo(t*hoo(t[x]))]*6-(a[(2+1)*3]+1)*a[2])[(2-5)+a[x]];
                end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))

    def test_index_exp_case3(self):
        input = """
            procedure main();
                begin
                    a := c[c[c[c[c[c[b]]]]]] + foo(2)[a[4[r[1[g]]]]];
                end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))

    def test_index_exp_case4(self):
        input = """
            procedure main();
                begin
                    a := c[c[c[c[c[c[b][x][y][z]]]]]];
                end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))

    def test_index_exp_case5(self):
        input = """
            procedure main();
                begin
                    a := (Not 5 + 8) - 3;
                end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))

    def test_index_exp_case6(self):
        input = """
            procedure main();
                begin
                    a := 6-3;
                end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))

    def test_index_exp_case7(self):
        input = """
            procedure main();
                begin
                    a := 9+12 = 3 ;
                end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))

    def test_index_exp_case8(self):
        input = """
            procedure main();
                begin
                    a := a()[(cbef)]:=a[1[a]] :=1[1] :=(a)[a]:= a()[b] ;
                end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))

    def test_wrong_expression(self):
        input = """
            procedure main();
                begin
                    a = d;
                end"""
        expect = "Error on line 4 col 22: ="
        self.assertTrue(TestParser.test(input,expect,235))

    def test_expression(self):
        input = """
            procedure main();
                begin
                    a := x-y*z+(3/y);
                end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))

    def test_expression_case2(self):
        input = """
            procedure main();
                begin
                    a := 4 OR 6 OR 10 OR ------ NOT NOT NOT 7;
                end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))

    def test_expression_case3(self):
        input = """
            procedure main();
                begin
                    a := foo(2)/3 mod 4 OR (110 ANd 7 -63);
                end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))

    def test_wrong_assignment_stm(self):
        input = """
                procedure foo(a: integer);
                begin
                    a + 1 := a[b[2]] +3;
                end"""
        expect = "Error on line 4 col 22: +"
        self.assertTrue(TestParser.test(input,expect,239))

    def test_assignment_statement(self):
        input = """
                procedure foo(a: integer);
                begin
                    a(2)[3+x] := a[b[2]] +3;
                    a := b [ 10 ] := foo ( ) [ 3 ] := x := 1 ;
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))

    def test_if_no_then(self):
        input = """
                procedure main();
                begin
                    if (a>=b) return a;
                end"""
        expect = "Error on line 4 col 30: return"
        self.assertTrue(TestParser.test(input,expect,241))

    def test_if_then_no_params(self):
        input = """
                procedure main();
                begin
                    if () then return a;
                end"""
        expect = "Error on line 4 col 24: )"
        self.assertTrue(TestParser.test(input,expect,242))

    def test_if_then_stm(self):
        input = """
                procedure main();
                begin
                    if (a>=b) then return a;
                end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))

    def test_if_then_stm_case2(self):
        input = """
                procedure main();
                begin
                    if (a>=b) then
                        if x = 9  then
                    return a;
                end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))

    def test_if_then_stm_case3(self):
        input = """
                procedure main();
                begin
                    if (a>=b) then
                        if x = 9  then
                            return a;
                        else x:= 90;
                    
                end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))

    def test_if_then_stm_case4(self):
        input = """
                procedure main();
                begin
                    if (a>=b) then
                        if x = 9  then
                            return a;
                        else x:= 90;
                    else foo(3);
                end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))

    def test_if_then_else_stm(self):
        input = """
                procedure main();
                begin
                    if (a>=b) then return a;
                    if (a>=b) then return a;
                    else return b;
                end
         """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))

    def test_while_stm_no_params(self):
        input = """
                procedure main();
                    begin
                        while do b := c + d;
                    end"""
        expect = "Error on line 4 col 30: do"
        self.assertTrue(TestParser.test(input,expect,248))

    def test_while_stm_no_do(self):
        input = """
                procedure main();
                    begin
                        while (a>=6) b := c + d;
                    end"""
        expect = "Error on line 4 col 37: b"
        self.assertTrue(TestParser.test(input,expect,249))

    def test_while_stm(self):
        input = """
                procedure main();
                    begin
                        while a = 5 do b := c + d;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))

    def test_while_stm_case1(self):
        input = """
                procedure main();
                    begin
                        while a = 5 do b := c + d;
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))

    def test_while_stm_case2(self):
        input = """
            procedure main();
            begin
                while a do b();
                while a do
                    begin
                        c();
                    end
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))

    def test_while_stm_case3(self):
        input = """
            procedure main();
            begin
                while a=true do foo();
                while a=false do
                    begin
                        while a = 4 do while b >=8 do while c = true do foo()[4]:= a[a[a[a[a[true]]]]];
                    end
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))

    def test_while_stm_case4(self):
        input = """
            procedure main();
            begin
                while a=false do
                    begin
                        while a = 4 do while b >=8 do while c = true do foo()[4]:= a[a[a[a[a[true]]]]];
                    end
                    break ;
                    continue;
                    return;
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))

    def test_for_stm_no_to(self):
        input = """
            procedure main();
            begin
                for i:=1 N do a := a+N ;
            end"""
        expect = "Error on line 4 col 25: N"
        self.assertTrue(TestParser.test(input,expect,255))

    def test_for_stm_no_do(self):
        input = """
            procedure main();
            begin
                for i:=1 to N a := a+N ;
            end"""
        expect = "Error on line 4 col 30: a"
        self.assertTrue(TestParser.test(input,expect,256))

    def test_for_stm_no_params(self):
        input = """
            procedure main();
            begin
                for to N do a := a+N ;
            end"""
        expect = "Error on line 4 col 20: to"
        self.assertTrue(TestParser.test(input,expect,257))

    def test_for_stm(self):
        input = """
            procedure main();
            begin
                for i:=1 to N do a := a+N ;
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))

    def test_for_stm_case2(self):
        input = """
            procedure main();
            begin
                for i:=1 to N do
                    for i:=4 downto 1 do a := a - N ;
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))

    def test_for_stm_case3(self):
        input = """
            procedure main();
            begin
                for i:=1 to N do
                    for i:=4 downto 1 do a := a - N ;
                        for i:=foo(3)[4] to 4-3 do a := a - N ;
                for i:=5 to 9 do return a;
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))

    def test_for_stm_case4(self):
        input = """
            procedure main();
            begin
                for i:=1 to N do
                    for i:=4 downto 1 do a := a - N ;
                        for i:=foo(3)[4] to 4-3 do a := a - N ;
                for i:=5 to 9 do
                    for i:=foo(3)[4] + 5- 6/foo(1) to e do
                        begin
                            for i:= true to false do x := 3;
                        end
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))

    def test_with_stm_no_do(self):
        input = """
            procedure main();
            begin
                with a,b,c:array[0 .. 1] of boolean; d: string; e: integer ;
                    begin
                    end
            end"""
        expect = "Error on line 5 col 20: begin"
        self.assertTrue(TestParser.test(input,expect,262))
    
    def test_with_stm_no_body(self):
        input = """
            procedure main();
            begin
                with a,b,c:array[0 .. 1] of boolean; d: string; e: integer ; do
            end"""
        expect = "Error on line 5 col 12: end"
        self.assertTrue(TestParser.test(input,expect,263))

    def test_with_stm(self):
        input = """
            procedure main();
            begin
                with a,b,c:array[0 .. 1] of boolean; d: string; e: integer ; do
                    begin
                        return foo(a,b,4,5,6)[a(1)[4]];
                    end
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))

    def test_with_stm_case2(self):
        input = """
            procedure main();
            begin
                 with a:real; do with b:real; do with c:real; do
                    begin
                        return foo(a,b,456)[a[a[a[1]]]];
                    end
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))

    def test_compound_stm(self):
        input = """
            procedure main();
            begin
                 with a:real; do with b:real; do with c:real; do
                    begin
                        a:= b[10] := foo()[3] :=x :=1 ;
                        return foo(a,b,456)[a[a[a[1]]]];
                    end
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))

    def test_more_complex_program(self):
        """More complex program"""
        input = """procedure main ();
            begin
                putIntLn(4);
            end
            end
        """
        expect = "Error on line 5 col 12: end"
        self.assertTrue(TestParser.test(input,expect,267))

    def test_more_complex_program_case2(self):
        input = """
            procedure main();
            begin
                 with a:real; do with b:real; do with c:real; do
                    begin
                        return foo(a,b,456)[a[a[a[1]]]];
                    end
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))

    def test_more_complex_program_case3(self):
        input = """
            function main() : array [1 .. 2] of real;
            begin
                { This is a block comment }
                begin
                    return foo(a,b,456)[a[a[a[1]]]];
                end
            end
            procedure main1();
            begin
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))

    def test_more_complex_program_case4(self):
        input = """
            function main() : array [1 .. 2] of real;
            begin
                // This is a line comment 
                {
                    begin
                        return foo(a,b,456)[a[a[a[1]]]];
                    end
                }
            end
            var a, b, c: integer;
            procedure foo();
                var
                    y : array [2 .. 3] of real ;
                    z : array [1 .. 2] of integer ;
                begin
                    foo (x ) ; // Call function
                    foo (y ) ; // Call function
                    foo ( z ) ; // Call function
                end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))

    def test_more_complex_program_case5(self):
        input = """
        (*
        procedure foo();
            var
                y : array [2 .. 3] of real ;
                z : array [1 .. 2] of integer ;
            begin
                foo (x ) ; // Call function
                foo (y ) ; // Call function
                foo ( z ) ; // Call function
            end
        *)
        """
        expect = "Error on line 13 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,271))

    def test_more_complex_program_case6(self):
        input = """
        function foo ( ) : real ;
            begin
                if ( a <> 6 ) then return 2.3 ; //CORRECT
                else return 2; //CORRECT
            end
            
            function foo (b : array [ 1 .. 2 ] of integer ) : array [2 .. 3] of real; 

            var
                a : array [ 2 .. 3 ] of real ;
                begin
                    if (c>d ) then return a ; //CORRECT
                    else return b ; //WRONG
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))

    def test_more_complex_program_case7(self):
        input = """
                var i : integer ;
                function f ( ) : integer ;
                begin
                    a:= 200;
                end
                procedure main ( ) ;
                    var
                    main : integer ;
                    begin
                        main := f ( ) ;
                        putIntLn ( main ) ;
                        with
                            i : integer ;
                            main : integer ;
                            f : integer ;
                        do begin
                            main := f := i := 100;
                            putIntLn ( i ) ;
                            putIntLn ( main ) ;
                            putIntLn ( f ) ;
                        end
                        putIntLn ( main ) ;
                    end
                    var g : real ;
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))

    def test_more_complex_program_case8(self):
        input = """
                var i : integer ;
                function f ( ) : integer ;
                begin
                    a:= 1.e12 + 34.;
                    return 200;
                end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))

    def test_wrong_with_end(self):
        input = """
        function foo ( ) : real ;
            begin
                if ( a <> 6 ) then return 2.3 ; //CORRECT
                else return 2; //CORRECT
            end
            end
        """
        expect = "Error on line 7 col 12: end"
        self.assertTrue(TestParser.test(input,expect,275))

    def test_wrong_with_begin(self):
        input = """
        function foo ( ) : real ;
            begin
            end
            begin
        """
        expect = "Error on line 5 col 12: begin"
        self.assertTrue(TestParser.test(input,expect,276))

    def test_wrong_with_begin_end(self):
        input = """
        function foo ( ) : real ;
            begin
            end

            begin
            end
        """
        expect = "Error on line 6 col 12: begin"
        self.assertTrue(TestParser.test(input,expect,277))

    def test_more_complex_program_case9(self):
        input = """
            procedure main();
            begin
                a := "This is my test";
                {PPL is very difficult but interesting}
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))

    def test_more_complex_program_case10(self):
        input = """
            procedure main();
            begin
                a := "This is my test";
                {PPL is very difficult but interesting}
                a := c+d/5 and              then 1;
                c := a+7-----7 or          else 2;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))

    def test_statement(self):
        input = """
        procedure main();
        begin
            foo(2)[3+x] := a[b[2]] +3;
            a[10+3] := abcd := fer := 5+6+9*10/8 ;
            a := b [ 10 ] := foo( ) [ 3 ] := x := 1 ;
            with a, b : integer ; c : array [1 .. 2] of real ; do
                d := c[a] + b;
                foo(3, a+1, m(2));
                if 1+2=3 then a := 10;
                else a := 9;
                if 5+6=8 then b := 5;
                while 5<6 do d:=6;
                for x := 7*9+6 Downto 6-(-3) do abc := 5+6*12/8; 
                    break;
                    continue;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))

    def test_character(self):
        input = """
        procedure main();
        begin
            //a:=10%d;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))

    def test_empty_file(self):
        input = """ """
        expect = "Error on line 1 col 1: <EOF>"
        self.assertTrue(TestParser.test(input,expect,282))

    def test_empty_file_2(self):
        input = """ \n """
        expect = "Error on line 2 col 1: <EOF>"
        self.assertTrue(TestParser.test(input,expect,283))

    def test_empty_file_3(self):
        input = """ {This is a comment} """
        expect = "Error on line 1 col 21: <EOF>"
        self.assertTrue(TestParser.test(input,expect,284))

    def test_wrong_file_3(self):
        input = """ This is wrong """
        expect = "Error on line 1 col 1: This"
        self.assertTrue(TestParser.test(input,expect,285))

    def test_wrong_keyword(self):
        input = """
        procedure main();
        began
            //a:=10%d;
        end """
        expect = "Error on line 3 col 8: began"
        self.assertTrue(TestParser.test(input,expect,286))

    def test_more_complex_program_case11(self):
        input = """function foo(a : array [ 12 .. 103 ] of real) : array [2 .. 7] of boolean;
        begin
            if a + b then 
               for i := 1 to n do break; else
                for y := 1 to s do 
                    if a + v - h then fo(a[0]);        
        end"""  
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))

    def test_more_complex_program_case12(self):
        input = """function foo(a : array [ 12 .. 103 ] of real) : array [2 .. 7] of boolean;
        begin
            if a + b then 
               for i := 1 to n do break else
                for y := 1 to s do 
                    if a + v - h then fo(a[0]);        
        end"""  
        expect = "Error on line 4 col 40: else"
        self.assertTrue(TestParser.test(input,expect,288))

    def test_more_complex_program_case13(self):
        input = """function foo(a : array [ 12 .. 103 ] of real) : array [2 .. 7] of boolean;
        begin
            if a + b then 
               for i := 1 to n do break; else
                for y := 1 to s do 
                    if a + v - h then fo(9); else fo(a[9]);        
        end"""  
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))

    def test_more_complex_program_case14(self):
        input = """function foo(a : array [ 12 .. 103 ] of real) : array [2 .. 7] of boolean;
        begin
               for i := 1 to n do
                for y := 1 to s do 
                    if a + v - h then fo(9); else fo(a[9]);        
        end"""  
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))

    def test_more_complex_program_case15(self):
        input = """function foo(a : array [ 12 .. 103 ] of real) : array [2 .. 7] of boolean;
        begin
            if a + b then 
               for i := 1 to n do break; else
                for y := 1 to s do 
                   with a: integer; do return f(a[6]) ;      
        end"""  
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))

    def test_more_complex_program_case16(self):
        input = """function foo(a : array [ 12 .. 103 ] of real) : array [2 .. 7] of boolean;
        var x,y : array[1 .. -9] of real; 
            b : integer;
        begin
            if a + b then 
               for i := 1 to n do break; else
                for y := 1 to s do 
                   with a: integer; do return f(a[6]) ;      
        end"""  
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))

    def test_more_complex_program_case17(self):
        input = """function foo(a : array [ 12 .. 103 ] of real) : array [2 .. 7] of boolean;
        var x,y : array[1 .. -9] of real; 
            b : integer;
        begin
            if a + b then 
               for i := 1 to n do break; else
                for y := 1 to s do 
                   with a: integer; do return f(a[6]) ;     

             with a,b: integer; x : boolean; do
                with c: real; do 
                        if x or e then fo(9); else with a,b: real; do fo(9);
        end"""  
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))

    def test_more_complex_program_case18(self):
        input = """procedure foo(a : array [ 12 .. 103 ] of real);
        var x,y : array[1 .. -9] of real; 
            b : integer;
        begin
            if a + b then 
               for i := 1 to n do break; else
                for y := 1 to s do 
                   with a: integer; do while x div y do 
                        a:=b:=g[fo(9, x + 2, y mod r)];     

             with a,b: integer; x : boolean; do
                with c: real; do 
                        if x or e then fo(9); else with a,b: real; do fo(9);
        end"""  
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))

    def test_more_complex_program_case19(self):
        input = """procedure foo(a : array [ 12 .. 103 ] of real);
        var x,y : array[1 .. -9] of real; 
            b : integer;
        begin
            if a + b then 
               for i := 1 to n do break; else
                for y := 1 to s do 
                   with a: integer; do while x div y do 
                        a:=b:=g[fo(9, x + 2, y mod r)];     

             with a,b: integer; x : boolean; do
                with c: real; do 
                        if x or e then fo(9); else with a,b: real; do fo(9);
        end"""  
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))

    def test_more_complex_program_case20(self):
        input = """procedure foo(a : array [ 12 .. 103 ] of real);
        var x,y : array[1 .. -9] of real; 
            b : integer;
        begin
            if a + b then 
               for i := 1 to n do break; else
                for y := 1 to s do 
                   with a: integer; do while x div y do 
                        a:=b:=g[fo(9, x + 2, y mod r)];     

             with a,b: integer; x : boolean; do
                with c: real; do 
                        if x or e then fo(9); else with a,b: real; do fo(9);
            return a[fo(9)[h(a[g[t[2 + 6 div e - 7 / 3]]])]];
        end"""  
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,296))

    def test_more_complex_program_case21(self):
        input = """procedure foo(a : array [ 12 .. 103 ] of real);
        var x,y : array[1 .. -9] of real; 
            b : integer;
        begin
            if a + b then 
               for i := 1 to n do break; else
                for y := 1 to s do 
                   with a: integer; do while x div y do 
                        a:=b:=g[fo(9, x + 2, y mod r)];     

             with a,b: integer; x : boolean; do
                with c: real; do 
                        if x or e then fo(9); else with a,b: real; do fo(9);
            return a[fo(9)[h(a[g[t[2 + 6 div e - 7 / 3]]])]];
            f(9)[a[r]] := r[fo(9)] := a := 2 + x - 7 * 8 / 3;
        end"""  
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))

    def test_more_complex_program_case22(self):
        input = """procedure foo(a : array [ 12 .. 103 ] of real);
        var x,y : array[1 .. -9] of real; 
            b : integer;
        begin
            if a + b then 
               for i := 1 to n do break; else
                for y := 1 to s do 
                   with a: integer; do while x div y do 
                        a:=b:=g[fo(9, x + 2, y mod r)];     

             with a,b: integer; x : boolean; do
                with c: real; do 
                        if x or e then fo(9); else with a,b: real; do fo(9);
            return a[fo(9)[h(a[g[t[2 + 6 div e - 7 / 3]]])]];
            f(9)[a[r]] := r[fo(9)] := a := 2 + x - 7 * 8 / 3;
            beGin 
                 x := a and then a[g[s[ro(x+3)]]] mod not f(v[d[go(5)]]);
                with a,b: integer; x : boolean; do
                    with c: real; do 
                        if x or e then fo(9); else with a,b: real; do fo(9);
            End
        end"""  
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,298))

    def test_more_complex_program_case23(self):
        input = """procedure foo(a : array [ 12 .. 103 ] of real);
        var x,y : array[1 .. -9] of real; 
            b : integer;
            c: boolean;
            d,f: real;
        begin
            if a + b then 
               for i := 1 to n do break; else
                for y := 1 to s do 
                   with a: integer; do while x div y do 
                        a:=b:=g[fo(9, x + 2, y mod r)];     

             with a,b: integer; x : boolean; do
                with c: real; do 
                        if x or e then fo(9); else with a,b: real; do fo(9);
            return a[fo(9)[h(a[g[t[2 + 6 div e - 7 / 3]]])]];
            f(9)[a[r]] := r[fo(9)] := a := 2 + x - 7 * 8 / 3;
            beGin 
                 x := a and then a[g[s[ro(x+3)]]] mod not f(v[d[go(5)]]);
                with a,b: integer; x : boolean; do
                    with c: real; do 
                        if x or e then fo(9); else with a,b: real; do fo(9);

                return x * 5;

                while a = b do if a = 2 then continue; else
                    fo(4);
                break;
            End
        end"""  
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))

    def test_more_complex_program_case24(self):
        input = """
            procedure main();
            begin
                 with a:real; do with b:real; do with c:real; do
                    begin
                        return foo(a,b,456)[a[a[a[1]]]];
                    end
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,300))