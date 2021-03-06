# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934

import ply.yacc as yacc
import sys
import memoria as memo
from lex import archivo
# Obtener la lista de tokens del lexer.
from lex import tokens
# import vars_table as master
import tabla_master as master
import quadruples as quad
import acciones as accion


idVector = None


# Leer archivo de prueba.
prueba = open(archivo, "r")
entrada = prueba.read()
idTemporal = None

varVector = {}
varMatriz = {}


# Declaración de funciones.
def p_programa(p):
    '''
    programa : BEGIN gotoMain globalfunc vars globalFuncFalse programa2 funcfalse MAIN mainfunc LKEY vars insertarParam programa3 RKEY END endprog
             | BEGIN gotoMain globalfunc vars globalFuncFalse MAIN mainfunc LKEY vars insertarParam programa3 RKEY END endprog
             | BEGIN gotoMain programa2 funcfalse MAIN mainfunc LKEY vars insertarParam programa3 RKEY END endprog
             | BEGIN gotoMain MAIN mainfunc LKEY vars insertarParam programa3 RKEY END endprog
    '''


def p_endprog(p):
    "endprog :"
    quad.endprog()


def p_gotoMain(p):
    "gotoMain :"
    quad.gotoMain()


# ############################# INICIAN FUNCIONES F ##########################
def p_globalfunc(p):
    '''
    globalfunc :
    '''
    master.insert("global", "void")
    master.funciones.append("global")
    master.esGlobal = True


def p_globalFuncFalse(p):
    '''
    globalFuncFalse :
    '''
    # memo.reiniciarDireccionesFunc()
    master.esGlobal = False
    # memo.reiniciarDireccionesFunc()
    # memo.limpiarDireUsadas()


# Funcion que declarar cuantas funciones puede haber
def p_programa2(p):
    '''
    programa2 : functrue modulo
              | functrue modulo programa2
    '''


def p_functrue(p):
    '''
    functrue :
    '''
    master.esFuncion = True


def p_funcfalse(p):
    '''
    funcfalse :
    '''
    master.esFuncion = False


def p_modulo(p):
    '''
    modulo : FUNC tipo ID seen_ID declararFunc LPAREN modulo1 RPAREN LKEY varsFunc insertarParam programa3 RKEY endproc
           | FUNC VOID tipoVoid ID seen_ID declararFunc LPAREN modulo1 RPAREN LKEY varsFunc insertarParam programa3 RKEY endproc
    '''
    master.contadorParam = 0


def p_tipoVoid(p):
    "tipoVoid :"
    master.miTipo = 'void'
    master.esVoid = True


def p_endproc(p):
    "endproc :"
    quad.endproc(master.miIdFunciones)
    master.esVoid = False


def p_varsFunc(p):
    '''
    varsFunc : vars
             | empty
    '''


def p_insertarParam(p):
    '''
    insertarParam :
    '''
    if master.esMain:
        master.insertIdToFunc("Cuadruplos", "int", "main", None)
        master.updateIdInFunc("Cuadruplos", "main", len(quad.Quad))
        quad.fill(0, len(quad.Quad))
    else:
        master.insertIdToFunc("Cuadruplos", "int", p[-7], None)
        master.updateIdInFunc("Cuadruplos", p[-7], len(quad.Quad))


def p_seen_ID(p):
    '''
    seen_ID :
    '''
    master.miIdFunciones = p[-1]
    p[0] = p[-1]
    master.miFuncType = p[-2]


def p_declararFunc(p):
    '''
    declararFunc :
    '''
    master.insert(master.miIdFunciones, master.miTipo)


# Modulo que declara los parametros de la funcion
def p_modulo1(p):
    '''
    modulo1 : modulo1Aux
            | empty
    '''
    master.insertIdToFunc("PARAMCANTI", "int", master.miIdFunciones, None)
    master.updateIdInFunc("PARAMCANTI", master.miIdFunciones, master.contadorParam)


# Modulo que declara los parametros de la funcion
def p_modulo1Aux(p):
    '''
    modulo1Aux : tipo ID modulo1Repe
    '''
    temp = memo.getVirtualDicLocal(p[1])
    master.insertIdToFunc(p[2], p[1], master.miIdFunciones, temp, True)
    if p[1] == 'int':
        master.updateIdInFunc(p[2], master.miIdFunciones, 0)
    elif p[1] == 'float':
        master.updateIdInFunc(p[2], master.miIdFunciones, 0.0)
    elif p[1] == 'string':
        master.updateIdInFunc(p[2], master.miIdFunciones, "")
    elif p[1] == 'bool':
        master.updateIdInFunc(p[2], master.miIdFunciones, 'false')


def p_modulo1Repe(p):
    '''
    modulo1Repe : COMMA modulo1Aux
               | empty
    '''
    master.contadorParam += 1


def p_modulo3(p):
    '''
    modulo3 : RETURN exp SEMICOLON insertReturn
    '''
    if master.esVoid:
        print("ERROR: return declarado en la funcion tipo void: ", master.miIdFunciones)
        sys.exit()
    if master.esMain:
        print("ERROR: el main no puede tener return")
        sys.exit()


def p_insertReturn(p):
    "insertReturn :"
    quad.miReturn()
# ########################### ACABA FUNCIONES  ##############################


# ############################ INICIA VARIABLES MAIN #########################
def p_mainfunc(p):
    '''
    mainfunc :
    '''
    master.esMain = True
    master.insert("main", "void")
    master.funciones.append("main")


def p_programa3(p):
    '''
    programa3 : bloque
              | bloque programa3
    '''


# ############################ CIERRA VARIABLES MAIN #########################
def p_vars(p):
    '''
    vars : tipo vars1 SEMICOLON
         | tipo vars1 SEMICOLON vars
    '''


# Inserta las variables en su tabla correspondiente con todos sus atributos,
# incluyendo el de la dimensión si es que son vectores.
def p_vars1(p):
    '''
    vars1 : ID
          | ID COMMA vars1
          | ID LCORCH variableDim CTE_I tamaVector RCORCH
          | ID LCORCH variableDim CTE_I tamaVector RCORCH COMMA vars1
          | ID LCORCH variableDim CTE_I COMMA CTE_I tamaMatriz RCORCH
          | ID LCORCH variableDim CTE_I COMMA CTE_I tamaMatriz RCORCH COMMA vars1
    '''
    global varVector
    global varMatriz
    if p[1] not in varVector.keys() and p[1] not in varMatriz.keys():
        if master.esFuncion:
            temp = memo.getVirtualDicLocal(master.miTipo)
            master.insertIdToFunc(p[1], master.miTipo, master.miIdFunciones, temp)
        elif master.esMain:
            dir = memo.getVirtualDicMain(master.miTipo)
            master.insertIdToFunc(p[1], master.miTipo, "main", dir)
            memo.insertLocalInMemory(master.miTipo, dir)
            memo.inicInMemory(p[1], master.miTipo, "main", dir)
        elif master.esGlobal:
            dir = memo.getVirtualDicGlobal(master.miTipo)
            master.insertIdToFunc(p[1], master.miTipo, "global", dir)
            memo.insertLocalInMemory(master.miTipo, dir)
            memo.inicInMemory(p[1], master.miTipo, "global", dir)
    elif p[1] in varVector.keys() and p[4] > 0:
        if master.esFuncion:
            dir = memo.getDirecVectorFunc(master.miTipo, varVector[p[1]])
            master.insertIdToFunc(p[1], master.miTipo, master.miIdFunciones, dir, None, varVector[p[1]])
        elif master.esMain:
            dir = memo.getDirecVectorMain(master.miTipo, varVector[p[1]])
            master.insertIdToFunc(p[1], master.miTipo, "main", dir, None, varVector[p[1]])
            memo.copyVectorToExe(dir, varVector[p[1]], master.miTipo)
        elif master.esGlobal:
            dir = memo.getDirecVecorGlobal(master.miTipo, varVector[p[1]])
            master.insertIdToFunc(p[1], master.miTipo, "global", dir, None, varVector[p[1]])
            memo.copyVectorToExe(dir, varVector[p[1]], master.miTipo)
        master.esVector = False
        varVector.pop(p[1], None)
    elif p[1] in varMatriz.keys() and p[4] > 0 and p[6] > 0:
        tama = varMatriz[p[1]][0] * varMatriz[p[1]][1]
        if master.esFuncion:
            dir = memo.getDirecVectorFunc(master.miTipo, tama)
            master.insertIdToFunc(p[1], master.miTipo, master.miIdFunciones, dir, None, varMatriz[p[1]][0], varMatriz[p[1]][1])
        elif master.esMain:
            dir = memo.getDirecVectorMain(master.miTipo, tama)
            master.insertIdToFunc(p[1], master.miTipo, "main", dir, None, varMatriz[p[1]][1], varMatriz[p[1]][0])
            memo.copyVectorToExe(dir, tama, master.miTipo)
        elif master.esGlobal:
            dir = memo.getDirecVecorGlobal(master.miTipo, tama)
            master.insertIdToFunc(p[1], master.miTipo, "global", dir, None, varMatriz[p[1]][1], varMatriz[p[1]][0])
            memo.copyVectorToExe(dir, tama, master.miTipo)
        varMatriz.pop(p[1], None)
    else:
        print("ERROR: No se puede declarar una matriz o vector con tamaño 0.")
        sys.exit()


def p_tamaVector(p):
    "tamaVector :"
    global varVector
    varVector[master.esVector] = p[-1]
    master.tamaVec = p[-1]


def p_tamaMatriz(p):
    "tamaMatriz :"
    global varMatriz
    tama = [p[-1], p[-3]]
    varMatriz[master.esVector] = tama
    master.tamaVec = p[-1] * p[-3]


def p_variableDim(p):
    "variableDim :"
    master.esVector = p[-2]


def p_tipo(p):
    '''
    tipo : INT
         | FLOAT
         | STRING
         | BOOL
    '''
    master.miTipo = p[1]
    p[0] = p[1]


def p_bloque(p):
    '''
    bloque : asignacion
           | condicion
           | lectura
           | escritura
           | loop
           | funcion SEMICOLON
           | modulo3
    '''


def p_asignacion(p):
    '''
    asignacion : ID push_id EQUAL push_poper logico pop_assign SEMICOLON
               | ID push_id EQUAL push_poper array pop_assign SEMICOLON
               | ID push_id EQUAL push_poper funcion pop_assignFunc SEMICOLON
               | array EQUAL push_poper logico pop_assign SEMICOLON
               | array EQUAL push_poper array pop_assign SEMICOLON
               | array EQUAL push_poper funcion pop_assignFunc SEMICOLON
    '''


def p_pop_assign(p):
    "pop_assign :"
    master.miValor = quad.popAssign()
    if p[-4] is None:
        if master.isVarGlobal(p[-5]):
            master.updateIdInFunc(p[-5], "global", master.miValor)
            dir = master.getDireccion(p[-5], "global")
            type = master.getType(p[-5], "global")
        elif master.esFuncion:
            master.updateIdInFunc(p[-5], master.miIdFunciones, master.miValor)
            type = master.getType(p[-5], master.miIdFunciones)
        elif master.esMain:
            master.updateIdInFunc(p[-5], "main", master.miValor)
            dir = master.getDireccion(p[-5], "main")
            type = master.getType(p[-5], "main")
    else:
        if master.isVarGlobal(p[-4]):
            master.updateIdInFunc(p[-4], "global", master.miValor)
            dir = master.getDireccion(p[-4], "global")
            type = master.getType(p[-4], "global")
        elif master.esFuncion:
            master.updateIdInFunc(p[-4], master.miIdFunciones, master.miValor)
            type = master.getType(p[-4], master.miIdFunciones)
        elif master.esMain:
            master.updateIdInFunc(p[-4], "main", master.miValor)
            dir = master.getDireccion(p[-4], "main")
            type = master.getType(p[-4], "main")


def p_pop_assignFunc(p):
    "pop_assignFunc :"
    quad.assignFunc(p[-1])


def p_logico(p):
    '''
    logico : expresion pop_log
           | expresion pop_log logico1
    '''


def p_pop_log(p):
    "pop_log :"
    if master.esMain:
        quad.popLog(True)
    elif master.esFuncion:
        quad.popLog(False)


def p_logico1(p):
    '''
    logico1 : AND push_poper logico
            | OR push_poper logico
    '''


def p_expresion(p):
    '''expresion : exp
                 | exp relop exp pop_relop
    '''


def p_pop_relop(p):
    "pop_relop :"
    if master.esMain:
        quad.popRelop(True)
    elif master.esFuncion:
        quad.popRelop(False)


def p_relop(p):
    '''relop : GT
             | LT
             | GTE
             | LTE
             | DOUBLEEQUAL
             | NE
             | AND
             | OR
    '''
    quad.pushPoper(p[1])


def p_exp(p):
    '''
    exp : termino pop_term
        | termino pop_term exp1
    '''


def p_pop_term(p):
    "pop_term :"
    if master.esMain:
        quad.popTerm(True)
    elif master.esFuncion:
        quad.popTerm(False)


def p_exp1(p):
    '''
    exp1 : PLUS push_poper exp
         | MINUS push_poper exp
    '''


def p_termino(p):
    '''
    termino : factor pop_fact
            | factor pop_fact termino1
    '''


def p_pop_fact(p):
    "pop_fact :"
    if master.esMain:
        quad.popFact(True)
    elif master.esFuncion:
        quad.popFact(False)


def p_termino1(p):
    '''
    termino1 : MULT push_poper termino
             | DIV push_poper termino
    '''


def p_push_poper(p):
    "push_poper :"
    quad.pushPoper(p[-1])


def p_pop_poper(p):
    "pop_poper :"
    quad.popPoper()


def p_factor(p):
    '''
    factor : LPAREN push_poper logico RPAREN pop_poper
           | var_cte
    '''


def p_var_cte(p):
    '''
    var_cte : ID push_id
            | CTE_I push_cte
            | CTE_F push_cte
            | CTE_S push_cte
            | TRUE push_cte
            | FALSE push_cte
            | array
            | funcion
    '''
    master.returnValor = p[1]
    if len(p) == 2:
        master.miValor = p[1]


def p_push_id(p):
    "push_id :"
    if master.esFuncion:
        quad.pushID(p[-1], master.miIdFunciones)
    elif master.esMain:
        quad.pushID(p[-1], 'main')
    else:
        quad.pushID(p[-1], 'global')
    # if para pasar los valores a los parametros de la funcion llamada desde el main


def p_push_cte(p):
    "push_cte :"
    tipo = memo.getTipo(p[-1])
    if not memo.verificarValorCte(p[-1]):
        dir = memo.getVirtualCte(tipo)
        memo.updateCteInMemory(p[-1], dir, tipo)
    direccion = memo.getDireCte(p[-1])
    quad.pushCte(p[-1], direccion, tipo)


def p_condicion(p):
    '''
    condicion : IF LPAREN logico RPAREN ifelse1 LKEY programa3 RKEY ifelse2
              | IF LPAREN logico RPAREN ifelse1 LKEY programa3 RKEY ELSE ifelse3 LKEY programa3 RKEY ifelse2
    '''


def p_ifelse1(p):
    "ifelse1 :"
    quad.ifelseUno()


def p_ifelse2(p):
    "ifelse2 :"
    quad.ifelseDos()


def p_ifelse3(p):
    "ifelse3 :"
    quad.ifelseTres()


def p_lectura(p):
    '''
    lectura : INPUT push_poper LPAREN ID push_id RPAREN pop_io SEMICOLON
    '''


def p_escritura(p):
    '''
    escritura : OUTPUT push_poper LPAREN exp RPAREN pop_io SEMICOLON
    '''


def p_pop_io(p):
    "pop_io :"
    quad.popIO()


def p_array(p):
    '''
    array : ID LCORCH arrayDos exp arrayTres array1
    '''
    p[0] = p[1]


def p_array1(p):
    '''
    array1 : RCORCH arrayCinco
           | COMMA exp matrizDos RCORCH arrayCinco
    '''


def p_arrayDos(p):
    "arrayDos :"
    global idVector
    quad.arregloDos()
    idVector = p[-2]


def p_arrayTres(p):
    "arrayTres :"
    global idVector
    if 'global' in master.simbolos:
        if idVector in master.simbolos['global'].value:
            if master.simbolos['global'].value[idVector].matriz == 0:
                tam = master.simbolos['global'].value[idVector].dimensionada
                quad.arregloTres(tam)
            else:
                tam = master.simbolos['global'].value[idVector].dimensionada
                tam2 = master.simbolos['global'].value[idVector].matriz
                quad.matrizUno(True, tam, tam2)
    if master.miIdFunciones in master.simbolos:
        if idVector in master.simbolos[master.miIdFunciones].value:
            if master.simbolos[master.miIdFunciones].value[idVector].matriz == 0:
                tam = master.simbolos[master.miIdFunciones].value[idVector].dimensionada
                quad.arregloTres(tam)
            else:
                tam = master.simbolos[master.miIdFunciones].value[idVector].dimensionada
                tam2 = master.simbolos[master.miIdFunciones].value[idVector].matriz
                quad.matrizUno(True, tam, tam2)
    if 'main' in master.simbolos:
        if idVector in master.simbolos['main'].value:
            if master.simbolos['main'].value[idVector].matriz == 0:
                tam = master.simbolos['main'].value[idVector].dimensionada
                quad.arregloTres(tam)
            else:
                tam = master.simbolos['main'].value[idVector].dimensionada
                tam2 = master.simbolos['main'].value[idVector].matriz
                quad.matrizUno(True, tam, tam2)


def p_arrayCinco(p):
    "arrayCinco :"
    if 'global' in master.simbolos:
        if idVector in master.simbolos['global'].value:
            base = master.simbolos['global'].value[idVector].direccion
            tipo = master.simbolos['global'].value[idVector].type_data
            quad.arregloCinco(True, base, tipo)
    if 'main' in master.simbolos:
        if idVector in master.simbolos['main'].value:
            base = master.simbolos['main'].value[idVector].direccion
            tipo = master.simbolos['main'].value[idVector].type_data
            quad.arregloCinco(True, base, tipo)
    if master.miIdFunciones in master.simbolos:
        if idVector in master.simbolos[master.miIdFunciones].value:
            base = master.simbolos[master.miIdFunciones].value[idVector].direccion
            tipo = master.simbolos[master.miIdFunciones].value[idVector].type_data
            quad.arregloCinco(False, base, tipo)


def p_matrizDos(p):
    "matrizDos :"
    if 'global' in master.simbolos:
        if idVector in master.simbolos['global'].value:
            tam2 = master.simbolos['global'].value[idVector].matriz
            quad.matrizDos(True, tam2)
    if master.miIdFunciones in master.simbolos:
        if idVector in master.simbolos[master.miIdFunciones].value:
            tam2 = master.simbolos[master.miIdFunciones].value[idVector].matriz
            quad.matrizDos(False, tam2)
    if 'main' in master.simbolos:
        if idVector in master.simbolos['main'].value:
            tam2 = master.simbolos['main'].value[idVector].matriz
            quad.matrizDos(True, tam2)


def p_loop(p):
    '''
    loop : LOOP loop1 LPAREN logico RPAREN loop2 LKEY programa3 RKEY loop3
    '''


def p_loop1(p):
    "loop1 :"
    quad.loopUno()


def p_loop2(p):
    "loop2 :"
    quad.loopDos()


def p_loop3(p):
    "loop3 :"
    quad.loopTres()


def p_funcion(p):
    '''
    funcion : ID getParamId LPAREN funcionDos funcion1 RPAREN paramFalse funcionSeis push_funcion
    '''
    # Condiciones que verifican si la recursividad cumple con los requisitos y desde donde es llamada la funcion
    if master.contadorDatosPasados < master.simbolos[p[2]].value["PARAMCANTI"].value and master.esFuncion:
        print("Faltan parametros en la funcion", master.miParamFunc, "En el ", master.miIdFunciones)
        sys.exit()
    if master.contadorDatosPasados < master.simbolos[p[2]].value["PARAMCANTI"].value and master.esMain:
        print("Faltan parametros en la funcion", master.miParamFunc, "en el MAIN")
        sys.exit()
    master.contadorDatosPasados = 0
    p[0] = p[1]


def p_push_funcion(p):
    "push_funcion :"
    quad.pushFunc(p[-8])


def p_getParamId(p):
    '''
    getParamId :
    '''
    master.miParamFunc = p[-1]

    if master.miParamFunc in master.simbolos.keys():
        master.esParam = True
        master.arrParam = master.getidParam(p[-1])
    else:
        print("ERROR: Función no declarada.")
        sys.exit()
    p[0] = p[-1]


def p_funcionDos(p):
    "funcionDos :"
    quad.moduloDos(p[-3])


def p_funcion1(p):
    '''
    funcion1 : exp funcionTres
             | exp funcionTres COMMA funcionCuatro funcion1
             | empty
    '''


def p_funcionTres(p):
    "funcionTres :"
    valor = quad.moduloTres()

    if master.esParam:
        # IF para checar si la llamada a funcion es dentro del main o de una funcion
        if master.esMain:
            master.contadorDatosPasados += 1
            if master.contadorDatosPasados > master.simbolos[master.miParamFunc].value["PARAMCANTI"].value:
                print("Sobran parametros en la funcion", master.miParamFunc, ".")
                sys.exit()
            master.updateIdInFunc(master.arrParam[-1], master.miParamFunc, valor)
            del(master.arrParam[-1])
        if master.esFuncion:
            master.contadorDatosPasados += 1
            if master.contadorDatosPasados > master.simbolos[master.miParamFunc].value["PARAMCANTI"].value:
                print("Sobran parametros en la funcion", master.miParamFunc, "en", master.miIdFunciones)
                sys.exit()
            master.updateIdInFunc(master.arrParam[-1], master.miIdFunciones, valor)
            del(master.arrParam[-1])


def p_funcionCuatro(p):
    "funcionCuatro :"
    quad.moduloCuatro()


def p_paramFalse(p):
    '''
    paramFalse :
    '''
    master.esParam = False


def p_funcionSeis(p):
    "funcionSeis :"
    quadNo = master.simbolos[p[-7]].value['Cuadruplos'].value
    quad.moduloSeis(p[-7], quadNo)


def p_empty(p):
    'empty :'
    pass


# Regla de error para errores de sintaxis.
def p_error(p):
    print(p)
    print("Error de sintaxis en '%s'" % p.value)
    sys.exit()


# construir el parser.
# print("Parsing . . . \n")
parser = yacc.yacc()
result = parser.parse(entrada)
# print(result)
#
# print("")
# print("CUADRUPLOS")
# print("")
# quad.show()
# print("VARS TABLE")
# print("")
# master.show()
# print("")
# # print("MEMORIA")
# # print("")
# # memo.show()

# print("\n",)
print("*************************************")
print("EJECUCION")
print("*************************************", "\n")
accion.inicio()
# print("")
# print("MEMORIA DESPUES DE LIMPIAR EN EJECUCION")
# print("")
# memo.show()
