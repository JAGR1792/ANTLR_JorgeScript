grammar Calc;

prog : expr EOF ;

expr
    : ID '=' expr     # Assign
    | expr '+' term   # Add
    | expr '-' term   # Sub
    | term            # ToTerm
    ;

term
    : term '*' factor # Mul
    | term '/' factor # Div
    | factor          # ToFactor
    ;

factor
    : INT             # Int
    | ID              # Var
    | '(' expr ')'    # Parens
    ;

ID  : [a-zA-Z]+ ;
INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
