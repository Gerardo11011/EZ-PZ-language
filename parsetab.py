
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BEGIN BOOL COMMA CTE_F CTE_I CTE_S DIV DOUBLEEQUAL ELSE END EQUAL FALSE FLOAT FUNC GT GTE ID IF INPUT INT LCORCH LKEY LOOP LPAREN LT LTE MAIN MINUS MULT NE OR OUTPUT PLUS RCORCH RETURN RKEY RPAREN SEMICOLON STRING TRUE\n    programa : BEGIN vars programa2 MAIN LKEY vars programa3 RKEY END\n             | BEGIN vars MAIN LKEY vars programa3 RKEY END\n             | BEGIN programa2 MAIN LKEY vars programa3 RKEY END\n             | BEGIN MAIN LKEY vars programa3 RKEY END\n    \n    programa2 : modulo\n              | modulo programa2\n    \n    programa3 : bloque\n              | bloque programa3\n    \n    vars : tipo vars1 SEMICOLON\n         | tipo vars1 SEMICOLON vars\n    \n    vars1 : ID\n          | ID COMMA vars1\n    \n    tipo : INT\n         | FLOAT\n         | STRING\n         | BOOL\n    \n    bloque : asignacion\n           | condicion\n           | lectura\n           | escritura\n           | loop\n           | funcion\n    \n    asignacion : ID EQUAL expresion SEMICOLON\n               | ID EQUAL array SEMICOLON\n               | ID EQUAL funcion SEMICOLON\n               | ID LCORCH exp RCORCH EQUAL expresion SEMICOLON\n    expresion : exp\n                 | exp relop exp expresion1\n    expresion1 : relop exp\n                  | empty\n    relop : GT\n             | LT\n             | GTE\n             | LTE\n             | DOUBLEEQUAL\n             | NE\n             | AND\n             | OR\n    \n    exp : termino\n        | termino exp1\n    \n    exp1 : PLUS exp\n         | MINUS exp\n    \n    termino : factor\n            | factor termino1\n    \n    termino1 : MULT termino\n             | DIV termino\n    \n    factor : LPAREN expresion RPAREN\n           | PLUS var_cte\n           | MINUS var_cte\n           | var_cte\n    \n    var_cte : ID\n            | CTE_I\n            | CTE_F\n            | CTE_S\n            | TRUE\n            | FALSE\n    \n    condicion : IF LPAREN expresion RPAREN LKEY bloque RKEY\n              | IF LPAREN expresion RPAREN LKEY bloque RKEY ELSE LKEY bloque RKEY\n    \n    lectura : INPUT LPAREN ID RPAREN SEMICOLON\n    \n    escritura : OUTPUT LPAREN exp RPAREN SEMICOLON\n    \n    array : LCORCH array1 RCORCH\n    \n    array1 : exp\n           | exp COMMA array1\n    \n    loop : LOOP LPAREN expresion RPAREN LKEY bloque RKEY\n    \n    funcion : ID LPAREN funcion1 RPAREN\n    \n    funcion1 : exp\n             | exp COMMA funcion1\n    \n    modulo : FUNC ID LPAREN modulo1 RPAREN LKEY vars modulo2 modulo3\n    \n    modulo1 : tipo ID\n            | tipo ID COMMA modulo1\n    \n    modulo2 : bloque\n            | bloque modulo2\n    \n    modulo3 : RETURN exp SEMICOLON RKEY\n            | RKEY\n    empty :'
    
_lr_action_items = {'BEGIN':([0,],[2,]),'$end':([1,65,94,95,128,],[0,-4,-2,-3,-1,]),'MAIN':([2,3,4,7,13,19,25,44,152,154,164,],[5,14,15,-5,21,-6,-9,-10,-68,-74,-73,]),'INT':([2,16,22,23,25,27,28,91,92,],[8,8,8,8,8,8,8,8,8,]),'FLOAT':([2,16,22,23,25,27,28,91,92,],[9,9,9,9,9,9,9,9,9,]),'STRING':([2,16,22,23,25,27,28,91,92,],[10,10,10,10,10,10,10,10,10,]),'BOOL':([2,16,22,23,25,27,28,91,92,],[11,11,11,11,11,11,11,11,11,]),'FUNC':([2,3,7,25,44,152,154,164,],[12,12,12,-9,-10,-68,-74,-73,]),'LKEY':([5,14,15,21,60,122,125,161,],[16,22,23,28,91,139,142,163,]),'ID':([6,8,9,10,11,12,24,25,26,29,30,32,33,34,35,36,37,38,44,47,48,53,54,55,56,57,58,59,71,72,75,77,96,97,98,99,100,101,102,103,104,105,106,107,112,113,115,116,120,121,126,131,137,139,140,141,142,144,145,153,157,158,159,163,166,],[18,-13,-14,-15,-16,20,39,-9,18,39,39,39,-17,-18,-19,-20,-21,-22,-10,61,39,66,83,83,83,88,83,83,83,83,83,83,-23,-24,-25,83,-31,-32,-33,-34,-35,-36,-37,-38,83,83,83,83,-65,83,39,83,83,39,-59,-60,39,39,83,83,-26,-57,-64,39,-58,]),'SEMICOLON':([17,18,45,66,67,68,69,70,73,74,76,78,79,80,81,82,83,111,114,117,118,120,123,124,129,130,132,133,134,135,136,146,147,149,156,160,],[25,-11,-12,-51,96,97,98,-27,-39,-43,-50,-52,-53,-54,-55,-56,-51,-40,-44,-48,-49,-65,140,141,-75,-61,-47,-41,-42,-45,-46,-28,-30,157,-29,162,]),'COMMA':([18,61,73,74,76,78,79,80,81,82,83,86,109,111,114,117,118,132,133,134,135,136,],[26,92,-39,-43,-50,-52,-53,-54,-55,-56,-51,121,131,-40,-44,-48,-49,-47,-41,-42,-45,-46,]),'LPAREN':([20,39,40,41,42,43,53,54,55,56,58,59,66,71,72,99,100,101,102,103,104,105,106,107,112,113,115,116,121,131,137,145,153,],[27,55,56,57,58,59,72,72,72,72,72,72,55,72,72,72,-31,-32,-33,-34,-35,-36,-37,-38,72,72,72,72,72,72,72,72,72,]),'IF':([24,25,29,30,32,33,34,35,36,37,38,44,48,96,97,98,120,126,139,140,141,142,144,157,158,159,163,166,],[40,-9,40,40,40,-17,-18,-19,-20,-21,-22,-10,40,-23,-24,-25,-65,40,40,-59,-60,40,40,-26,-57,-64,40,-58,]),'INPUT':([24,25,29,30,32,33,34,35,36,37,38,44,48,96,97,98,120,126,139,140,141,142,144,157,158,159,163,166,],[41,-9,41,41,41,-17,-18,-19,-20,-21,-22,-10,41,-23,-24,-25,-65,41,41,-59,-60,41,41,-26,-57,-64,41,-58,]),'OUTPUT':([24,25,29,30,32,33,34,35,36,37,38,44,48,96,97,98,120,126,139,140,141,142,144,157,158,159,163,166,],[42,-9,42,42,42,-17,-18,-19,-20,-21,-22,-10,42,-23,-24,-25,-65,42,42,-59,-60,42,42,-26,-57,-64,42,-58,]),'LOOP':([24,25,29,30,32,33,34,35,36,37,38,44,48,96,97,98,120,126,139,140,141,142,144,157,158,159,163,166,],[43,-9,43,43,43,-17,-18,-19,-20,-21,-22,-10,43,-23,-24,-25,-65,43,43,-59,-60,43,43,-26,-57,-64,43,-58,]),'RKEY':([31,32,33,34,35,36,37,38,49,50,52,62,96,97,98,120,140,141,143,144,150,151,155,157,158,159,162,165,166,],[51,-7,-17,-18,-19,-20,-21,-22,63,64,-8,93,-23,-24,-25,-65,-59,-60,154,-71,158,159,-72,-26,-57,-64,164,166,-58,]),'RETURN':([33,34,35,36,37,38,96,97,98,120,140,141,143,144,155,157,158,159,166,],[-17,-18,-19,-20,-21,-22,-23,-24,-25,-65,-59,-60,153,-71,-72,-26,-57,-64,-58,]),'EQUAL':([39,119,],[53,137,]),'LCORCH':([39,53,],[54,71,]),'RPAREN':([46,61,70,73,74,76,78,79,80,81,82,83,85,86,87,88,89,90,110,111,114,117,118,127,129,132,133,134,135,136,138,146,147,156,],[60,-69,-27,-39,-43,-50,-52,-53,-54,-55,-56,-51,120,-66,122,123,124,125,132,-40,-44,-48,-49,-70,-75,-47,-41,-42,-45,-46,-67,-28,-30,-29,]),'END':([51,63,64,93,],[65,94,95,128,]),'PLUS':([53,54,55,56,58,59,66,71,72,73,74,76,78,79,80,81,82,83,99,100,101,102,103,104,105,106,107,112,113,114,115,116,117,118,121,131,132,135,136,137,145,153,],[75,75,75,75,75,75,-51,75,75,112,-43,-50,-52,-53,-54,-55,-56,-51,75,-31,-32,-33,-34,-35,-36,-37,-38,75,75,-44,75,75,-48,-49,75,75,-47,-45,-46,75,75,75,]),'MINUS':([53,54,55,56,58,59,66,71,72,73,74,76,78,79,80,81,82,83,99,100,101,102,103,104,105,106,107,112,113,114,115,116,117,118,121,131,132,135,136,137,145,153,],[77,77,77,77,77,77,-51,77,77,113,-43,-50,-52,-53,-54,-55,-56,-51,77,-31,-32,-33,-34,-35,-36,-37,-38,77,77,-44,77,77,-48,-49,77,77,-47,-45,-46,77,77,77,]),'CTE_I':([53,54,55,56,58,59,71,72,75,77,99,100,101,102,103,104,105,106,107,112,113,115,116,121,131,137,145,153,],[78,78,78,78,78,78,78,78,78,78,78,-31,-32,-33,-34,-35,-36,-37,-38,78,78,78,78,78,78,78,78,78,]),'CTE_F':([53,54,55,56,58,59,71,72,75,77,99,100,101,102,103,104,105,106,107,112,113,115,116,121,131,137,145,153,],[79,79,79,79,79,79,79,79,79,79,79,-31,-32,-33,-34,-35,-36,-37,-38,79,79,79,79,79,79,79,79,79,]),'CTE_S':([53,54,55,56,58,59,71,72,75,77,99,100,101,102,103,104,105,106,107,112,113,115,116,121,131,137,145,153,],[80,80,80,80,80,80,80,80,80,80,80,-31,-32,-33,-34,-35,-36,-37,-38,80,80,80,80,80,80,80,80,80,]),'TRUE':([53,54,55,56,58,59,71,72,75,77,99,100,101,102,103,104,105,106,107,112,113,115,116,121,131,137,145,153,],[81,81,81,81,81,81,81,81,81,81,81,-31,-32,-33,-34,-35,-36,-37,-38,81,81,81,81,81,81,81,81,81,]),'FALSE':([53,54,55,56,58,59,71,72,75,77,99,100,101,102,103,104,105,106,107,112,113,115,116,121,131,137,145,153,],[82,82,82,82,82,82,82,82,82,82,82,-31,-32,-33,-34,-35,-36,-37,-38,82,82,82,82,82,82,82,82,82,]),'MULT':([66,74,76,78,79,80,81,82,83,117,118,132,],[-51,115,-50,-52,-53,-54,-55,-56,-51,-48,-49,-47,]),'DIV':([66,74,76,78,79,80,81,82,83,117,118,132,],[-51,116,-50,-52,-53,-54,-55,-56,-51,-48,-49,-47,]),'GT':([66,70,73,74,76,78,79,80,81,82,83,111,114,117,118,129,132,133,134,135,136,],[-51,100,-39,-43,-50,-52,-53,-54,-55,-56,-51,-40,-44,-48,-49,100,-47,-41,-42,-45,-46,]),'LT':([66,70,73,74,76,78,79,80,81,82,83,111,114,117,118,129,132,133,134,135,136,],[-51,101,-39,-43,-50,-52,-53,-54,-55,-56,-51,-40,-44,-48,-49,101,-47,-41,-42,-45,-46,]),'GTE':([66,70,73,74,76,78,79,80,81,82,83,111,114,117,118,129,132,133,134,135,136,],[-51,102,-39,-43,-50,-52,-53,-54,-55,-56,-51,-40,-44,-48,-49,102,-47,-41,-42,-45,-46,]),'LTE':([66,70,73,74,76,78,79,80,81,82,83,111,114,117,118,129,132,133,134,135,136,],[-51,103,-39,-43,-50,-52,-53,-54,-55,-56,-51,-40,-44,-48,-49,103,-47,-41,-42,-45,-46,]),'DOUBLEEQUAL':([66,70,73,74,76,78,79,80,81,82,83,111,114,117,118,129,132,133,134,135,136,],[-51,104,-39,-43,-50,-52,-53,-54,-55,-56,-51,-40,-44,-48,-49,104,-47,-41,-42,-45,-46,]),'NE':([66,70,73,74,76,78,79,80,81,82,83,111,114,117,118,129,132,133,134,135,136,],[-51,105,-39,-43,-50,-52,-53,-54,-55,-56,-51,-40,-44,-48,-49,105,-47,-41,-42,-45,-46,]),'AND':([66,70,73,74,76,78,79,80,81,82,83,111,114,117,118,129,132,133,134,135,136,],[-51,106,-39,-43,-50,-52,-53,-54,-55,-56,-51,-40,-44,-48,-49,106,-47,-41,-42,-45,-46,]),'OR':([66,70,73,74,76,78,79,80,81,82,83,111,114,117,118,129,132,133,134,135,136,],[-51,107,-39,-43,-50,-52,-53,-54,-55,-56,-51,-40,-44,-48,-49,107,-47,-41,-42,-45,-46,]),'RCORCH':([73,74,76,78,79,80,81,82,83,84,108,109,111,114,117,118,132,133,134,135,136,148,],[-39,-43,-50,-52,-53,-54,-55,-56,-51,119,130,-62,-40,-44,-48,-49,-47,-41,-42,-45,-46,-63,]),'ELSE':([158,],[161,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'vars':([2,16,22,23,25,28,91,],[3,24,29,30,44,48,126,]),'programa2':([2,3,7,],[4,13,19,]),'tipo':([2,16,22,23,25,27,28,91,92,],[6,6,6,6,6,47,6,6,47,]),'modulo':([2,3,7,],[7,7,7,]),'vars1':([6,26,],[17,45,]),'programa3':([24,29,30,32,48,],[31,49,50,52,62,]),'bloque':([24,29,30,32,48,126,139,142,144,163,],[32,32,32,32,32,144,150,151,144,165,]),'asignacion':([24,29,30,32,48,126,139,142,144,163,],[33,33,33,33,33,33,33,33,33,33,]),'condicion':([24,29,30,32,48,126,139,142,144,163,],[34,34,34,34,34,34,34,34,34,34,]),'lectura':([24,29,30,32,48,126,139,142,144,163,],[35,35,35,35,35,35,35,35,35,35,]),'escritura':([24,29,30,32,48,126,139,142,144,163,],[36,36,36,36,36,36,36,36,36,36,]),'loop':([24,29,30,32,48,126,139,142,144,163,],[37,37,37,37,37,37,37,37,37,37,]),'funcion':([24,29,30,32,48,53,126,139,142,144,163,],[38,38,38,38,38,69,38,38,38,38,38,]),'modulo1':([27,92,],[46,127,]),'expresion':([53,56,59,72,137,],[67,87,90,110,149,]),'array':([53,],[68,]),'exp':([53,54,55,56,58,59,71,72,99,112,113,121,131,137,145,153,],[70,84,86,70,89,70,109,70,129,133,134,86,109,70,156,160,]),'termino':([53,54,55,56,58,59,71,72,99,112,113,115,116,121,131,137,145,153,],[73,73,73,73,73,73,73,73,73,73,73,135,136,73,73,73,73,73,]),'factor':([53,54,55,56,58,59,71,72,99,112,113,115,116,121,131,137,145,153,],[74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),'var_cte':([53,54,55,56,58,59,71,72,75,77,99,112,113,115,116,121,131,137,145,153,],[76,76,76,76,76,76,76,76,117,118,76,76,76,76,76,76,76,76,76,76,]),'funcion1':([55,121,],[85,138,]),'relop':([70,129,],[99,145,]),'array1':([71,131,],[108,148,]),'exp1':([73,],[111,]),'termino1':([74,],[114,]),'modulo2':([126,144,],[143,155,]),'expresion1':([129,],[146,]),'empty':([129,],[147,]),'modulo3':([143,],[152,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> BEGIN vars programa2 MAIN LKEY vars programa3 RKEY END','programa',9,'p_programa','yacc.py',18),
  ('programa -> BEGIN vars MAIN LKEY vars programa3 RKEY END','programa',8,'p_programa','yacc.py',19),
  ('programa -> BEGIN programa2 MAIN LKEY vars programa3 RKEY END','programa',8,'p_programa','yacc.py',20),
  ('programa -> BEGIN MAIN LKEY vars programa3 RKEY END','programa',7,'p_programa','yacc.py',21),
  ('programa2 -> modulo','programa2',1,'p_programa2','yacc.py',26),
  ('programa2 -> modulo programa2','programa2',2,'p_programa2','yacc.py',27),
  ('programa3 -> bloque','programa3',1,'p_programa3','yacc.py',32),
  ('programa3 -> bloque programa3','programa3',2,'p_programa3','yacc.py',33),
  ('vars -> tipo vars1 SEMICOLON','vars',3,'p_vars','yacc.py',38),
  ('vars -> tipo vars1 SEMICOLON vars','vars',4,'p_vars','yacc.py',39),
  ('vars1 -> ID','vars1',1,'p_vars1','yacc.py',44),
  ('vars1 -> ID COMMA vars1','vars1',3,'p_vars1','yacc.py',45),
  ('tipo -> INT','tipo',1,'p_tipo','yacc.py',50),
  ('tipo -> FLOAT','tipo',1,'p_tipo','yacc.py',51),
  ('tipo -> STRING','tipo',1,'p_tipo','yacc.py',52),
  ('tipo -> BOOL','tipo',1,'p_tipo','yacc.py',53),
  ('bloque -> asignacion','bloque',1,'p_bloque','yacc.py',58),
  ('bloque -> condicion','bloque',1,'p_bloque','yacc.py',59),
  ('bloque -> lectura','bloque',1,'p_bloque','yacc.py',60),
  ('bloque -> escritura','bloque',1,'p_bloque','yacc.py',61),
  ('bloque -> loop','bloque',1,'p_bloque','yacc.py',62),
  ('bloque -> funcion','bloque',1,'p_bloque','yacc.py',63),
  ('asignacion -> ID EQUAL expresion SEMICOLON','asignacion',4,'p_asignacion','yacc.py',68),
  ('asignacion -> ID EQUAL array SEMICOLON','asignacion',4,'p_asignacion','yacc.py',69),
  ('asignacion -> ID EQUAL funcion SEMICOLON','asignacion',4,'p_asignacion','yacc.py',70),
  ('asignacion -> ID LCORCH exp RCORCH EQUAL expresion SEMICOLON','asignacion',7,'p_asignacion','yacc.py',71),
  ('expresion -> exp','expresion',1,'p_expresion','yacc.py',75),
  ('expresion -> exp relop exp expresion1','expresion',4,'p_expresion','yacc.py',76),
  ('expresion1 -> relop exp','expresion1',2,'p_expresion1','yacc.py',80),
  ('expresion1 -> empty','expresion1',1,'p_expresion1','yacc.py',81),
  ('relop -> GT','relop',1,'p_relop','yacc.py',85),
  ('relop -> LT','relop',1,'p_relop','yacc.py',86),
  ('relop -> GTE','relop',1,'p_relop','yacc.py',87),
  ('relop -> LTE','relop',1,'p_relop','yacc.py',88),
  ('relop -> DOUBLEEQUAL','relop',1,'p_relop','yacc.py',89),
  ('relop -> NE','relop',1,'p_relop','yacc.py',90),
  ('relop -> AND','relop',1,'p_relop','yacc.py',91),
  ('relop -> OR','relop',1,'p_relop','yacc.py',92),
  ('exp -> termino','exp',1,'p_exp','yacc.py',97),
  ('exp -> termino exp1','exp',2,'p_exp','yacc.py',98),
  ('exp1 -> PLUS exp','exp1',2,'p_exp1','yacc.py',103),
  ('exp1 -> MINUS exp','exp1',2,'p_exp1','yacc.py',104),
  ('termino -> factor','termino',1,'p_termino','yacc.py',109),
  ('termino -> factor termino1','termino',2,'p_termino','yacc.py',110),
  ('termino1 -> MULT termino','termino1',2,'p_termino1','yacc.py',115),
  ('termino1 -> DIV termino','termino1',2,'p_termino1','yacc.py',116),
  ('factor -> LPAREN expresion RPAREN','factor',3,'p_factor','yacc.py',121),
  ('factor -> PLUS var_cte','factor',2,'p_factor','yacc.py',122),
  ('factor -> MINUS var_cte','factor',2,'p_factor','yacc.py',123),
  ('factor -> var_cte','factor',1,'p_factor','yacc.py',124),
  ('var_cte -> ID','var_cte',1,'p_var_cte','yacc.py',129),
  ('var_cte -> CTE_I','var_cte',1,'p_var_cte','yacc.py',130),
  ('var_cte -> CTE_F','var_cte',1,'p_var_cte','yacc.py',131),
  ('var_cte -> CTE_S','var_cte',1,'p_var_cte','yacc.py',132),
  ('var_cte -> TRUE','var_cte',1,'p_var_cte','yacc.py',133),
  ('var_cte -> FALSE','var_cte',1,'p_var_cte','yacc.py',134),
  ('condicion -> IF LPAREN expresion RPAREN LKEY bloque RKEY','condicion',7,'p_condicion','yacc.py',139),
  ('condicion -> IF LPAREN expresion RPAREN LKEY bloque RKEY ELSE LKEY bloque RKEY','condicion',11,'p_condicion','yacc.py',140),
  ('lectura -> INPUT LPAREN ID RPAREN SEMICOLON','lectura',5,'p_lectura','yacc.py',145),
  ('escritura -> OUTPUT LPAREN exp RPAREN SEMICOLON','escritura',5,'p_escritura','yacc.py',150),
  ('array -> LCORCH array1 RCORCH','array',3,'p_array','yacc.py',155),
  ('array1 -> exp','array1',1,'p_array1','yacc.py',160),
  ('array1 -> exp COMMA array1','array1',3,'p_array1','yacc.py',161),
  ('loop -> LOOP LPAREN expresion RPAREN LKEY bloque RKEY','loop',7,'p_loop','yacc.py',166),
  ('funcion -> ID LPAREN funcion1 RPAREN','funcion',4,'p_funcion','yacc.py',171),
  ('funcion1 -> exp','funcion1',1,'p_funcion1','yacc.py',176),
  ('funcion1 -> exp COMMA funcion1','funcion1',3,'p_funcion1','yacc.py',177),
  ('modulo -> FUNC ID LPAREN modulo1 RPAREN LKEY vars modulo2 modulo3','modulo',9,'p_modulo','yacc.py',182),
  ('modulo1 -> tipo ID','modulo1',2,'p_modulo1','yacc.py',187),
  ('modulo1 -> tipo ID COMMA modulo1','modulo1',4,'p_modulo1','yacc.py',188),
  ('modulo2 -> bloque','modulo2',1,'p_modulo2','yacc.py',193),
  ('modulo2 -> bloque modulo2','modulo2',2,'p_modulo2','yacc.py',194),
  ('modulo3 -> RETURN exp SEMICOLON RKEY','modulo3',4,'p_modulo3','yacc.py',198),
  ('modulo3 -> RKEY','modulo3',1,'p_modulo3','yacc.py',199),
  ('empty -> <empty>','empty',0,'p_empty','yacc.py',203),
]
