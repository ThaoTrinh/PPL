import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_identifier_chain(self):
        self.assertTrue(TestLexer.test("Trinh Thi Thu Thao","Trinh,Thi,Thu,Thao,<EOF>",101))
    
    def test_identifier_simple(self):
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",102))
    
    def test_identifier_simple_case2(self):
        self.assertTrue(TestLexer.test("FunCtion123","FunCtion123,<EOF>",103))
    
    def test_identifier_case_insensitive(self):
        self.assertTrue(TestLexer.test("aBC","aBC,<EOF>",104))
    
    def test_identifier_special(self):
        self.assertTrue(TestLexer.test("_123_a","_123_a,<EOF>",105))
    
    def test_identifier_wrong(self):
        self.assertTrue(TestLexer.test("1_variable","1,_variable,<EOF>",106))
   
    def test_identifier_wrong_case2(self):
        self.assertTrue(TestLexer.test("+wrong","+,wrong,<EOF>",107))
    
    def test_identifier_wrong_case3(self):
        self.assertTrue(TestLexer.test("wrong+","wrong,+,<EOF>",108))
    
    def test_identifier_wrong_case4(self):
        self.assertTrue(TestLexer.test("wrong+123","wrong,+,123,<EOF>",109))
    
    def test_identifier_wrong_case5(self):
        self.assertTrue(TestLexer.test("*(a)*","*,(,a,),*,<EOF>",110))
    
    def test_keyword_uppercase(self):
        self.assertTrue(TestLexer.test("VAR","VAR,<EOF>",111))
    
    def test_keyword_lowercase(self):
        self.assertTrue(TestLexer.test("function","function,<EOF>",112))
    
    def test_keyword_case_insensitive(self):
        self.assertTrue(TestLexer.test("fuNcTion","fuNcTion,<EOF>",113))
    
    def test_keyword_wrong(self):
        self.assertTrue(TestLexer.test("123function","123,function,<EOF>",114))
    
    def test_keyword_wrong_case2(self):
        self.assertTrue(TestLexer.test("123function+xyz","123,function,+,xyz,<EOF>",115))
    
    def test_special_wrong_case2(self):
        self.assertTrue(TestLexer.test("123function+xyz()AND","123,function,+,xyz,(,),AND,<EOF>",116))
    
    def test_integer_wrong(self):
        self.assertTrue(TestLexer.test("123a123","123,a123,<EOF>",117))
    
    def test_integer_chain(self):
        self.assertTrue(TestLexer.test("123123 56789 87654","123123,56789,87654,<EOF>",118))
    
    def test_integer_simple(self):
        self.assertTrue(TestLexer.test("123","123,<EOF>",119))
    
    def test_integer_simple_case2(self):
        self.assertTrue(TestLexer.test("012345","012345,<EOF>",120))
    
    def test_integer_simple_case3(self):
        self.assertTrue(TestLexer.test("0","0,<EOF>",121))
    
    def test_real_simple(self):
        self.assertTrue(TestLexer.test("123.123","123.123,<EOF>",122))
    
    def test_real_with_point_after(self):
        self.assertTrue(TestLexer.test("123.","123.,<EOF>",123))
    
    def test_real_with_point_before(self):
        self.assertTrue(TestLexer.test(".123",".123,<EOF>",124))
    
    def test_real_with_exponent_case1(self):
        self.assertTrue(TestLexer.test("123e123","123e123,<EOF>",125))
    
    def test_real_with_exponent_case2(self):
        self.assertTrue(TestLexer.test("123e-123","123e-123,<EOF>",126))
    
    def test_real_with_exponent_case3(self):
        self.assertTrue(TestLexer.test("3E-3","3E-3,<EOF>",127))
    
    def test_real_with_exponent_case4(self):
        self.assertTrue(TestLexer.test("45E123","45E123,<EOF>",128))
    
    def test_real_with_fraction_exponent_case1(self):
        self.assertTrue(TestLexer.test("123.1e23","123.1e23,<EOF>",129))
    
    def test_real_with_fraction_exponent_case2(self):
        self.assertTrue(TestLexer.test("123.1E-12","123.1E-12,<EOF>",130))
    
    def test_real_with_fraction_exponent_wrong(self):
        self.assertTrue(TestLexer.test("123.1E-12+","123.1E-12,+,<EOF>",131))
    
    def test_real_with_fraction_exponent_wrong_case2(self):
        self.assertTrue(TestLexer.test("123.o1E+12.1e2","123.,o1E,+,12.1e2,<EOF>",132))
    
    def test_real_with_no_num_part(self):
        self.assertTrue(TestLexer.test(".123e-12",".123e-12,<EOF>",133))
    
    def test_real_wrong_case1(self):
        self.assertTrue(TestLexer.test("123.123e-13abcd","123.123e-13,abcd,<EOF>",134))
    
    def test_real_wrong_case2(self):
        self.assertTrue(TestLexer.test("123.e","123.,e,<EOF>",135))
    
    def test_real_wrong_case3(self):
        self.assertTrue(TestLexer.test("e123","e123,<EOF>",136))
    
    def test_real_wrong_case4(self):
        self.assertTrue(TestLexer.test("e123.123","e123,.123,<EOF>",137))
    
    def test_real_wrong_case5(self):
        self.assertTrue(TestLexer.test("123e","123,e,<EOF>",138))
    
    def test_real_wrong_case6(self):
        self.assertTrue(TestLexer.test("123ea3","123,ea3,<EOF>",139))

    def test_string_simple(self):
        self.assertTrue(TestLexer.test(" \"This is string\" ","This is string,<EOF>",140))
    
    def test_string_simple_case2(self):
        self.assertTrue(TestLexer.test(" \"This is string\"This is not string ","This is string,This,is,not,string,<EOF>",141))
    
    def test_string(self):
        self.assertTrue(TestLexer.test(" \"This is string\"\"This is string too\" ","This is string,This is string too,<EOF>",142))
    
    def test_string_case2(self):
        self.assertTrue(TestLexer.test(" \"This is string\\ttoo\" ","This is string\\ttoo,<EOF>",143))
    
    def test_string_unclosed_string(self):
        self.assertTrue(TestLexer.test(" \"thao\"s\" ","thao,s,Unclosed String:  ",144))
    
    def test_string_unclosed_string_case2(self):
        self.assertTrue(TestLexer.test("\"String\"\"\"\"","String,,Unclosed String: ",145))
    
    def test_string_unclosed_string_case3(self):
        self.assertTrue(TestLexer.test("\"Thu\nThao\"","Unclosed String: Thu",146))
    
    def test_string_unclosed_string_case4(self):
        self.assertTrue(TestLexer.test("\"HELLO \f\"","Unclosed String: HELLO ",147))
    
    def test_string_illegal_escape(self):
        self.assertTrue(TestLexer.test("\"D:\Desktop\PPL \" ","Illegal Escape In String: D:\D",148))
    
    def test_string_illegal_escape_case2(self):
        self.assertTrue(TestLexer.test("\"Thu Thao \c \" ","Illegal Escape In String: Thu Thao \c",149))
    
    def test_errorToken(self):
        self.assertTrue(TestLexer.test("thao's","thao,Error Token '",150))
    
    def test_errorToken_case2(self):
        self.assertTrue(TestLexer.test("char a='$'","char,a,=,Error Token '",151))
    
    def test_errorToken_case3(self):
        self.assertTrue(TestLexer.test("\"string s=\" HELLO %\h","string s=,HELLO,Error Token %",152))
    
    def test_string_special(self):
        self.assertTrue(TestLexer.test("\"String\\nChain\"","String\\nChain,<EOF>",153))
    
    def test_many_operator(self):
        self.assertTrue(TestLexer.test("ANd Then >= <= = <>","ANd,Then,>=,<=,=,<>,<EOF>",154))
    
    def test_operator_with_andthen(self):
        self.assertTrue(TestLexer.test("ANd Then","ANd,Then,<EOF>",155))
    
    def test_operator_with_add(self):
        self.assertTrue(TestLexer.test("+","+,<EOF>",156))
    
    def test_operator_with_less_than_equal(self):
        self.assertTrue(TestLexer.test("<=","<=,<EOF>",157))
    
    def test_operator_logical_not(self):
        self.assertTrue(TestLexer.test("NOT","NOT,<EOF>",158))
    
    def test_operator_logical_AND(self):
        self.assertTrue(TestLexer.test("and","and,<EOF>",159))
    
    def test_operator_logical_OR(self):
        self.assertTrue(TestLexer.test("Or","Or,<EOF>",160))

    def test_comment_line_case1(self):
        self.assertTrue(TestLexer.test("//\n","<EOF>",161))
    
    def test_comment_line_case2(self):
        self.assertTrue(TestLexer.test("//This is comment line//\n","<EOF>",162))
    
    def test_comment_line_case3(self):
        self.assertTrue(TestLexer.test("\"This is string\"//This is comment line\n","This is string,<EOF>",163))
    
    def test_comment_block_type1(self):
        self.assertTrue(TestLexer.test("{This is comment}","<EOF>",164))
    
    def test_comment_block_type1_case2(self):
        self.assertTrue(TestLexer.test("{Comment}Not comment{This is comment}","Not,comment,<EOF>",165))
    
    def test_comment_block_type2(self):
        self.assertTrue(TestLexer.test("(*This is comment*)","<EOF>",166))

    def test_comment_block_type2_case2(self):
        self.assertTrue(TestLexer.test("abc(*This is comment*)","abc,<EOF>",167))
    
    def test_comment_block_type2_case3(self):
        self.assertTrue(TestLexer.test("abc(*\\This is comment*)","abc,<EOF>",168))
    
    def test_comment_block_type2_and_type3(self):
        self.assertTrue(TestLexer.test("{abc}(*\\This is comment*)","<EOF>",169))
    
    def test_comment_block_and_line(self):
        self.assertTrue(TestLexer.test("{abc}//This is comment\n","<EOF>",170))
    
    def test_comment_with_string(self):
        self.assertTrue(TestLexer.test("\"This is a string follow by comment\"{This is comment}","This is a string follow by comment,<EOF>",171))

    def test_comment_special_character(self):
        self.assertTrue(TestLexer.test("\"This is a special comment\"{This is $comment}","This is a special comment,<EOF>",172))

    def test_comment_special_character_case2(self):
        self.assertTrue(TestLexer.test("{'$#@!}","<EOF>",173))
    
    def test_function_simple(self):
        self.assertTrue(TestLexer.test("function foo(a:real):real;","function,foo,(,a,:,real,),:,real,;,<EOF>",174))

    def test_function_case2(self):
        self.assertTrue(TestLexer.test("function foo(b:integer):real; var c:boolean; begin d = c + b end","function,foo,(,b,:,integer,),:,real,;,var,c,:,boolean,;,begin,d,=,c,+,b,end,<EOF>",175))
    
    def test_procedure_simple(self):
        self.assertTrue(TestLexer.test("procedure pro(a:real);","procedure,pro,(,a,:,real,),;,<EOF>",176))
    
    def test_array_type(self):
        self.assertTrue(TestLexer.test("Array [1 .. 2] of integer;","Array,[,1,..,2,],of,integer,;,<EOF>",177))
    
    def test_array_type_case2(self):
        self.assertTrue(TestLexer.test("Array [] of boolean;","Array,[,],of,boolean,;,<EOF>",178))

    def test_assignment(self):
        self.assertTrue(TestLexer.test("a:=b:=c();","a,:=,b,:=,c,(,),;,<EOF>",179))
    
    def test_assignment_case2(self):
        self.assertTrue(TestLexer.test(":=foo(arr)",":=,foo,(,arr,),<EOF>",180))

    def test_arithmetic_expression(self):
        self.assertTrue(TestLexer.test("a[3]*5/2","a,[,3,],*,5,/,2,<EOF>",181))

    def test_equality_expression(self):
        self.assertTrue(TestLexer.test("(b+5*9) == c","(,b,+,5,*,9,),=,=,c,<EOF>",182))

    def test_equality_expression_case2(self):
        self.assertTrue(TestLexer.test("(b+5*9) == true","(,b,+,5,*,9,),=,=,true,<EOF>",183))

    def test_equality_expression_case3(self):
        self.assertTrue(TestLexer.test("(b+5*9) == (c==d)","(,b,+,5,*,9,),=,=,(,c,=,=,d,),<EOF>",184))

    def test_relational_expression(self):
        self.assertTrue(TestLexer.test("(a+5.0e-2)*10 >= (d+100)/2","(,a,+,5.0e-2,),*,10,>=,(,d,+,100,),/,2,<EOF>",185))

    def test_relational_expression_case2(self):
        self.assertTrue(TestLexer.test("result = (b[1]==5)(c==2)","result,=,(,b,[,1,],=,=,5,),(,c,=,=,2,),<EOF>",186))

    def test_open_close_parentheses(self):
        self.assertTrue(TestLexer.test("}thu thao{","},thu,thao,{,<EOF>",187))

    def test_complex_expression(self):
        self.assertTrue(TestLexer.test("int a = foo(2)[3+x]+array[3]*b[a[2][3]]+foo1(b,c,d);","int,a,=,foo,(,2,),[,3,+,x,],+,array,[,3,],*,b,[,a,[,2,],[,3,],],+,foo1,(,b,,,c,,,d,),;,<EOF>",188))

    def test_for_loop(self):
        self.assertTrue(TestLexer.test("for(int i =0;i<10;i++)","for,(,int,i,=,0,;,i,<,10,;,i,+,+,),<EOF>",189))

    def test_while_loop(self):
        self.assertTrue(TestLexer.test("int i=0; while(i++ <= 10)","int,i,=,0,;,while,(,i,+,+,<=,10,),<EOF>",190))

    def test_expession_statement(self):
        self.assertTrue(TestLexer.test("foo(2)[3]=a OR b(c+35.4e10)*9+10.0 DIV 4+true;","foo,(,2,),[,3,],=,a,OR,b,(,c,+,35.4e10,),*,9,+,10.0,DIV,4,+,true,;,<EOF>",191))

    def test_separator_token(self):
        self.assertTrue(TestLexer.test("}{[()],;","},{,[,(,),],,,;,<EOF>",192))

    def test_expression_case1(self):
        self.assertTrue(TestLexer.test("a+123e-1+-1*.3","a,+,123e-1,+,-,1,*,.3,<EOF>",193))

    def test_expression_case2(self):
        self.assertTrue(TestLexer.test("a+12.4+e32-43e","a,+,12.4,+,e32,-,43,e,<EOF>",194))
    
    def test_legal_escape_backspace(self):
        self.assertTrue(TestLexer.test("\"HELLO \\f\"","HELLO \\f,<EOF>",195))
    
    def test_legal_escape_newline(self):
        self.assertTrue(TestLexer.test("\"This is old line \\n\"","This is old line \\n,<EOF>",196))

    def test_legal_escape_tab(self):
        self.assertTrue(TestLexer.test("\"This is test for tab \\t\"","This is test for tab \\t,<EOF>",197))
    
    def test_legal_carriage_return(self):
        self.assertTrue(TestLexer.test("\"This is test for carriage return \\r\"","This is test for carriage return \\r,<EOF>",198))
    
    def test_legal_formfeed(self):
        self.assertTrue(TestLexer.test("\"This is test for formfeed \\f\"","This is test for formfeed \\f,<EOF>",199))
    
    def test_main_function(self):
        self.assertTrue(TestLexer.test("procedure main();","procedure,main,(,),;,<EOF>",200))
