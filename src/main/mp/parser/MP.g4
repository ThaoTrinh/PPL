// 1613232

grammar MP;

@lexer::header {
from lexererr import *
}

options{
    language=Python3;
}


program: (var_decl | func_decl | procedure_decl)+ EOF;

var_decl : VAR (var_list COLON mptype SEMI)+ ;

var_list : (ID COMMA)*ID ;

func_decl : FUNCTION ID LB param_decl? RB COLON mptype SEMI var_decl? compound_stm ;

procedure_decl: PROCEDURE ID LB param_decl? RB SEMI var_decl? compound_stm ;

param_decl : (var_list COLON mptype SEMI)* (var_list COLON mptype);

exp: exp (AND THEN | OR ELSE) exp1
      | exp1 ;

exp1: exp2 (EQUAL | NOT_EQUAL | LT | LE | GT | GE) exp2
      | exp2 ;

exp2: exp2 (ADD | SUB | OR) exp3
      | exp3 ;

exp3: exp3 (DIV | MUL | MOD | AND | DIVISION) exp4
      | exp4 ;

exp4: (NOT|'-') exp4
      | exp5 ;

exp5: exp5 LSB exp RSB | exp6 ;

exp6: LB exp RB| INTLIT | REALLIT | BOOLEANLIT | STRINGLIT | ID | ID invocation_exp ;

index_exp: exp5 LSB exp RSB ;

invocation_exp: LB list_expression RB ;

list_expression: ((exp COMMA)*exp)? ;

statements :
    line_statement SEMI
    | block_statement
    ;

line_statement:
    assignment_stm
    | break_stm
    | continue_stm
    | return_stm
    | call_stm
    ;

block_statement:
    if_stm
    | while_stm
    | for_stm
    | compound_stm
    | with_stm
    ;


assignment_stm: assignments exp ;
assignments: ((ID| index_exp)':=') + ;

if_stm: IF exp THEN statements (ELSE statements)? ;

while_stm: WHILE exp DO statements ;

for_stm: FOR ID ':=' exp (TO | DOWNTO) exp DO statements ;

break_stm: BREAK ;

continue_stm: CONTINUE ;

return_stm: RETURN exp? ;

compound_stm: BEGIN statements* END ;

with_stm: WITH (var_list COLON mptype SEMI)+ DO statements ;

call_stm: ID LB list_expression RB ;

mptype
    : primitive_type
    | compound_type
    ;

primitive_type
    : INTEGER
    | REAL
    | BOOLEAN
    | STRING
    ;

compound_type
    : ARRAY array_value OF primitive_type
    ;

array_value
    : LSB (('-'? INTLIT)|exp) DOUBLE_DOT (('-'? INTLIT)|exp) RSB
    ;

ADD: '+' ;

SUB: '-' ;

MUL: '*' ;

DIVISION: '/' ;

EQUAL: '=' ;

NOT_EQUAL: '<>' ;

LT: '<' ;

LE: '<=' ;

GE: '>=' ;

GT: '>' ;

LB: '(' ;

RB: ')' ;

LSB: '[' ;

RSB: ']' ;

LP: '{';

RP: '}';

SEMI: ';' ;

COLON : ':' ;

COMMA : ',' ;

DOUBLE_DOT : '..' ;

ASSIGN: ':=' ;

CMT1: '(*' .*? '*)' -> skip ;

CMT2: '{' .*? '}' -> skip ;

CMT3:  '//' .*? [\r]*[\n] -> skip ;

fragment EXPONENT: E ('-')? [0-9]+ ;



fragment A : ('A' | 'a') ;
fragment B : ('B' | 'b') ;
fragment C : ('C' | 'c') ;
fragment D : ('D' | 'd') ;
fragment E : ('E' | 'e') ;
fragment F : ('F' | 'f') ;
fragment G : ('G' | 'g') ;
fragment H : ('H' | 'h') ;
fragment I : ('I' | 'i') ;
fragment J : ('J' | 'j') ;
fragment K : ('K' | 'k') ;
fragment L : ('L' | 'l') ;
fragment M : ('M' | 'm') ;
fragment N : ('N' | 'n') ;
fragment O : ('O' | 'o') ;
fragment P : ('P' | 'p') ;
fragment Q : ('Q' | 'q') ;
fragment R : ('R' | 'r') ;
fragment S : ('S' | 's') ;
fragment T : ('T' | 't') ;
fragment U : ('U' | 'u') ;
fragment V : ('V' | 'v') ;
fragment W : ('W' | 'w') ;
fragment X : ('X' | 'x') ;
fragment Y : ('Y' | 'y') ;
fragment Z : ('Z' | 'z') ;

BOOLEANLIT: TRUE | FALSE ;

VAR : V A R ;

FUNCTION : F U N C T I O N ;

PROCEDURE :P R O C E D U R E ;

BREAK : B R E A K ;

CONTINUE : C O N T I N U E ;

FOR : F O R ;

TO : T O ;

DOWNTO : D O W N T O ;

DO : D O ;

IF : I F ;

THEN : T H E N ;

ELSE : E L S E ;

RETURN : R E T U R N ;

WHILE : W H I L E ;

BEGIN : B E G I N ;

END : E N D ;

TRUE : T R U E ;

FALSE : F A L S E ;

ARRAY : A R R A Y ;

OF : O F ;

INTEGER : I N T E G E R ;

BOOLEAN: B O O L E A N ;

REAL: R E A L ;

STRING: S T R I N G ;

NOT : N O T ;

AND : A N D ;

OR : O R ;

DIV : D I V ;

MOD : M O D ;

WITH : W I T H ;


INTLIT:[0-9]+ ;

REALLIT: ([0-9]+ (('.' [0-9]* (EXPONENT)?)? | EXPONENT ))
        |('.' [0-9]+ (EXPONENT)?)
        |('.' EXPONENT) ;



STRINGLIT
    : UNCLOSE_STRING '"'
    {self.text = self.text[1:-1]}
    ;


ID: ([a-zA-Z] | '_') ([a-zA-Z0-9] | '_')* ;


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING
    : '"' ('\\' [btrnf\\'"] | ~[\b\t\r\n\f\\'"])*
    {raise UncloseString(self.text[1:])}
    ;

ILLEGAL_ESCAPE
    : UNCLOSE_STRING '\\' ~[btnfr"'\\]
    {raise IllegalEscape(self.text[1:])}
    ;

ERROR_CHAR
    :.
    {raise ErrorToken(self.text)}
    ;