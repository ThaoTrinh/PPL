// 1613232

grammar MP;

@lexer::header {
from lexererr import *
}

options{
    language=Python3;
}


program: (vardecl | funcdecl | procdecl)+ EOF;

vardecl : VAR (param SEMI)+ ;

funcdecl : FUNCTION ID LB paramdecl? RB COLON mptype SEMI vardecl? compoundstm ;

procdecl: PROCEDURE ID LB paramdecl? RB SEMI vardecl? compoundstm ;

paramdecl : (param SEMI)* (param);

param: (ID COMMA)*ID COLON mptype;

exp: exp (AND THEN | OR ELSE) exp1
      | exp1 ;

exp1: exp2 (EQUAL | NOTEQUAL | LT | LE | GT | GE) exp2
      | exp2 ;

exp2: exp2 (ADD | SUB | OR) exp3
      | exp3 ;

exp3: exp3 (DIV | MUL | MOD | AND | DIVISION) exp4
      | exp4 ;

exp4: (NOT|SUB) exp4
      | exp5 ;

exp5: exp5 LSB exp RSB | exp6 ;

exp6: LB exp RB| INTLIT | REALLIT | BOOLEANLIT | STRINGLIT | ID | ID invocationexp ;

indexexp: exp5 LSB exp RSB ;

invocationexp: LB listexpression RB ;

listexpression: ((exp COMMA)*exp)? ;

statements :
    linestatement SEMI
    | blockstatement
    ;

linestatement:
    assignmentstm
    | breakstm
    | continuestm
    | returnstm
    | callstm
    ;

blockstatement:
    ifstm
    | whilestm
    | forstm
    | compoundstm
    | withstm
    ;


assignmentstm: assignments exp ;
assignments: ((ID| indexexp)ASSIGN) + ;

ifstm: IF exp THEN statements (ELSE statements)? ;

whilestm: WHILE exp DO statements ;

forstm: FOR ID ASSIGN exp (TO | DOWNTO) exp DO statements ;

breakstm: BREAK ;

continuestm: CONTINUE ;

returnstm: RETURN exp? ;

compoundstm: BEGIN statements* END ;

withstm: WITH (param SEMI)+ DO statements ;

callstm: ID LB listexpression RB ;

mptype
    : primitivetype
    | compoundtype
    ;

primitivetype
    : INTEGER
    | REAL
    | BOOLEAN
    | STRING
    ;

compoundtype
    : ARRAY arrayvalue OF primitivetype
    ;

arrayvalue
    : LSB SUB? INTLIT DOUBLEDOT SUB? INTLIT RSB
    ;

ADD: '+' ;

SUB: '-' ;

MUL: '*' ;

DIVISION: '/' ;

EQUAL: '=' ;

NOTEQUAL: '<>' ;

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

DOUBLEDOT : '..' ;

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
    : UNCLOSESTRING '"'
    {self.text = self.text[1:-1]}
    ;


ID: ([a-zA-Z] | '_') ([a-zA-Z0-9] | '_')* ;


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSESTRING
    : '"' ('\\' [btrnf\\'"] | ~[\b\t\r\n\f\\'"])*
    {raise UncloseString(self.text[1:])}
    ;

ILLEGALESCAPE
    : UNCLOSESTRING '\\' ~[btnfr"'\\]
    {raise IllegalEscape(self.text[1:])}
    ;

ERRORCHAR
    :.
    {raise ErrorToken(self.text)}
    ;
