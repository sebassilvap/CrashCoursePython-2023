# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# PYTHON CRASH COURSE
# por @sebas.silva.p
# 11/2023
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 1) Comentarios
print('\n\n\n1) Comentarios\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - con símbolo de numeral # => comentario de 1 línea
# - entre 6 comillas simples o dobles => multilínea => string
# - no afectan al código

# comentario de 1 línea

"""
comentario
de varias
líneas
"""

# => este súper caracter ≡ es alt + 240 :)




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 2) print()
print('\n\n\n2) print()\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - función interna para imprimir en consola

print("Hola Mundo")
print('Hola Mundo') # comilla simple o doble
print('Hola a todos! Soy Sebas!') # cualquier mensaje
print(123) # números

# -------------
# Línea Vacía
# -------------
print('¿Cómo estás?')
print() # línea vacía
print('Estoy bien, y tú?')
print('') # línea vacía
print('Gracias')
print("") # línea vacía
print('De nada')




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 3) Variables
print('\n\n\n3) Variables\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - contenedor / espacio con memoria
# - para guardar un valor

a = 20
b = 10.5
c = 'Sebas'

print(a) # 20
print(b) # 10.5
print(c) # Sebas

# ----------------------------------------------------------------------
# Truco print => imprimir varios valores, separando con coma
# ¿por qué? => print es una función => recibe argumentos de función
# ----------------------------------------------------------------------
print(a, b, c) # 20 10.5 Sebas
print('hola', -50, -5.5)

# --------------------------------
# Redefinir / Reasignar variables
# --------------------------------
print(a) # 20
a = "I love Python"
print(a) # I love Python

# ---------------------
# Asignación Múltiple
# ---------------------
a, b, c = 100, -5.5, 'Hola'

print(a) # 100
print(b) # -5.5
print(c) # Hola

# -----------------------------------
# Asignación Múltiple a Valor Único
# -----------------------------------
a = b = c = 'Python'

print(a) # Python
print(b) # Python
print(c) # Python




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 4) Estándar en Nombres de Variables
print('\n\n\n4) Estándar en Nombres de Variables\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - En programación se maneja 2 estándares:
#   (a) cammelCase => nombreEstudiante
#   (b) separación  => nombre_estudiante (PYTHON)

# - REGLAS:
#   (a) no tildes
#   (b) no empezar con número
#   (c) no empezar con caracter de símbolo

nombre = 'Sebas'
apellido = 'Silva'
edad = 36
pais_origen = 'Ecuador'

print(nombre, apellido, edad, pais_origen) # Sebas Silva 36 Ecuador

# ------------------------
# print en varias líneas
# ------------------------

print(
    nombre,
    apellido,
    edad,
    pais_origen,
) # Sebas Silva 36 Ecuador

#123nombre = 'Sebas' # SyntaxError: invalid decimal literal
#%nombre = 'Sebas' # SyntaxError: invalid syntax




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 5) Tipos de Datos
print('\n\n\n5) Tipos de Datos\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ---------------
# Tipos Básicos
# ---------------

"""
Tipo de Dato     |  Denominación  |  Ej:
---------------------------------------------------------
Entero           |  int           |  -20, 0, 5
Punto Flotante   |  float         |  2.5, 0.669, -89.52
Cadena de Texto  |  str           |  'Hola', "Python"
Booleano         |  bool          |  True, False
"""

# --------------------------
# Todos los Tipos de Datos
# --------------------------

"""
Text Type:	     |    str
Numeric Types:   |    int, float, complex
Sequence Types:  |    list, tuple, range
Mapping Type:	 |    dict
Set Types:	     |    set, frozenset
Boolean Type:	 |    bool
Binary Types:	 |    bytes, bytearray, memoryview
None Type:	     |    NoneType
"""
# https://www.w3schools.com/python/python_datatypes.asp


# --------------------------------------
# type() => retorna tipo de dato
# --------------------------------------
# - función interna (built-in function)

nombre = 'Sebas'
edad = 36
nota = 18.5
es_profesor = True
es_estudiante = False

print( nombre, type(nombre) ) # Sebas <class 'str'>
print( edad, type(edad) ) # 36 <class 'int'>
print( nota, type(nota) ) # 18.5 <class 'float'>
print( es_profesor, type(es_profesor) ) # True <class 'bool'>
print( es_estudiante, type(es_estudiante) ) # False <class 'bool'>


# ----------------------------------------------------------------
# None => útil para crear una variable sin valor y asignar luego
# ----------------------------------------------------------------
x = None
print( x , type(x) ) # None <class 'NoneType'>

x = 100
print( x , type(x) ) # 100 <class 'int'>




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 6) Casting de Variables
print('\n\n6) Casting de Variables\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - cambiar el tipo de una variable a otro
# - se utilizan funciones-internas
# - con el mismo nombre que las variables, el nombre que utiliza python
# - int / float / str / bool
# - OJO: no todas las conversiones son posibles

# --------------------------
# Generalidades de Casting
# --------------------------
var_str = '100' # string numérico
print( var_str , type(var_str) ) # 100 <class 'str'>

var_int = int(var_str)
var_float = float(var_str)
var_bool = bool(var_str)

print( var_int , type(var_int) ) # 100 <class 'int'>
print( var_float , type(var_float) ) # 100.0 <class 'float'>
print( var_bool , type(var_bool) ) # True <class 'bool'>

# -------------------------
# Todo es CASTEABLE a bool
# -------------------------
str_1 = 'h'
str_2 = ' '
str_3 = ''
int_1 = 10
int_2 = -5
int_3 = 0
float_1 = 5.5
float_2 = 0
none_1 = None

print( str_1 , '=>' , bool(str_1) ) # h => True
print( str_2 , '=>' , bool(str_2) ) #   => True
print( str_3 , '=>' , bool(str_3) ) #  => False
print( int_1 , '=>' , bool(int_1) ) # 10 => True
print( int_2 , '=>' , bool(int_2) ) # -5 => True
print( int_3 , '=>' , bool(int_3) ) # 0 => False
print( float_1 , '=>' , bool(float_1) ) # 5.5 => True
print( float_2 , '=>' , bool(float_2) ) # 0 => False
print( none_1 , '=>' , bool(none_1) ) # None => False

# ------------
# Conclusión
# ------------
# - Número 0 / 0.0 => False
# - String vacío => False
# - Tipo None => False
# - Todo lo demás => True




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 7) función interna => isinstance()
print('\n\n7) función interna => isinstance()\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - función complemento de type()
# - verificar si una variable / dato es de un tipo

a = 'hola'
b = 100

print( a , type(a) ) # hola <class 'str'>
print( b , type(b) ) # 100 <class 'int'>

print( isinstance(a, str) ) # True
print( isinstance(a, int) ) # False
print( isinstance(b, str) ) # False
print( isinstance(b, int) ) # True




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 8) Función Internal - help()
print('\n\n8) Función Internal - help()\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - funciones internas de python (built-in functions)
# - no necesitan importación / instalación
# - están ahí desde que se instala python
# - ej: print() / type() / int() / float() / etc...
# - help() => biblioteca offline de Python
# - https://www.w3schools.com/python/python_ref_functions.asp


# -------------------------------------
# Averiguar sobre 1 tema en específico
# -------------------------------------
#help(print)
#help(str)
#help(type)

# ------------------
# Navegar en help()
# ------------------
# - help() + topics + seleccionar tema + enter
#help()




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 9) Aritmética en Python
print('\n\n\n9) Aritmética en Python\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ------------------------------
# Operaciones Básicas en Python
# ------------------------------

"""
    suma               =>   +
    resta              =>   -
    producto           =>   *
    división           =>   /
    potencia           =>   **
    módulo             =>   %
    división + floor   =>   //
"""

# ---------------------------------
# Aritmética con Valores Directos
# ---------------------------------
2 + 3
5 * 8
9 / 5
# más sentido imprimir para ver

print(2 + 3) # 5
print(5/6) # 0.8333333333333334
print(5  *8) # 40

# -------------------------
# Aritmética con variables
# -------------------------
x = 10
y = 3

print( x, '+', y, '=', x + y ) # 10 + 3 = 13
print( x, '-', y, '=', x - y ) # 10 - 3 = 7
print( x, '*', y, '=', x * y ) # 10 * 3 = 30
print( x, '/', y, '=', x / y ) # 10 / 3 = 3.3333333333333335
print( x, '**', y, '=', x ** y ) # 10 ** 3 = 1000
print( x, '%', y, '=', x % y ) # 10 % 3 = 1
print( x, '//', y, '=', x // y ) # 10 // 3 = 3

# -------
# Módulo
# -------
#    10 |___ 4
#    -8      2
#     2
print( 10 % 4 ) # 2

# --------------------
# División y Redondeo
# --------------------
# divide y devuelve la parte entera
print( 5/2 , 5//2 ) # 2 1
print( 9/5 , 9//5 ) # 2 1
print( type(9/5) , type(9//5) ) # <class 'float'> <class 'int'>
# la división convierte a punto flotante !

# ----------------------------------
# Las reglas matemáticas se cumplen
# ----------------------------------
x = 5
y = 2
resultado = x * (y + x) - y + x**y - x / (x- 2*y)
#           5 * (2 + 5) - 2 + 5**2 - 5 / (5- 2*2)
#           5 *    7    - 2 +  25  - 5 / (5 - 4)
#           35 - 2 + 25 - 5 / 1
#           35 - 2 + 25 - 5.0
#           53.0

print(resultado)




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 10) Secuencias de Escape
print('\n\n\n10) Secuencias de Escape\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - elementos que permiten dar un formato a string
# - se les antecede siempre el backslash => \

"""
SECUENCIA  NOMBRE           DEFINICIÓN
  \\       Backslash        Para insertar el caracter \ en un String
  \'       Comilla Simple   Para insertar la comilla simple en un String
  \"       Comilla doble    Para insertar la comilla doble en un String
  \b       Retroceso        Elimina un caracter del String al momento de aparecer en el output de la consola.
  \f       Formfeed         Imprime una nueva línea indentada al final de la línea anterior.
  \v       Tab Vertical     Realiza lo mismo que el Formfeed
  \t       Tab Horizontal   Inserta un espaciado de tabulación
  \r       Carriage return  Inserta los caracteres después de \r al inicio del String
  \n       Nueva Línea      Inserta un salto del línea en tabulación 0
"""
# - algunos no se visualizan en editores de código como VSCode
# - en Replit => se puede ver el funcionamiento de todos
# - aquí vamos a ver los más relevantes

print('hola mundo')
print('hola\nmundo\nhola sebas')
print('\tpython\t\tjava') # python 1 tab => 4 espacios
#print("Me gusta "Python", es chévere!") # Error de Sintaxis
print('Me gusta "Python", es chévere!')
print("Me gusta \"Python\", es chévere!")
print('Me gusta \'Python\', es chévere!')




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 11) String <str>
print('\n\n\n11) String <str>\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# --------------------------------
# formas de representar un string
# --------------------------------
cadena_1 = 'hola python'
cadena_2 = "hola java"
cadena_3 = '''hola ecuador'''
cadena_4 = """hola alemania"""
cadena_5 = """
hola este string
tiene varias
líneas
"""

print( cadena_1 , type(cadena_1) )
print( cadena_2 , type(cadena_2) )
print( cadena_3 , type(cadena_3) )
print( cadena_4 , type(cadena_4) )
print( cadena_5 , type(cadena_5) )

# -----------------
# concatenación +
# -----------------
nombre = 'Sebas'
apellido = 'Silva'

texto = nombre + apellido
print(texto)

nombre = 'Sebas'
apellido = ' Silva'

texto = nombre + apellido
print(texto)

nombre = 'Sebas'
apellido = 'Silva'

texto = nombre + ' ' + apellido
print(texto)
print( nombre + ' ' + apellido )

# ------------------
# multiplicación *
# ------------------
letra = 'A'
print( 5 * letra ) # AAAAA
print( letra * 5 ) # AAAAA

# ------------------------------
# índices [i] y tamaño => len()
# ------------------------------
palabra = 'hola'
# (+)      0123
# (-)      4321

print( palabra )
print()
print( palabra[0] )
print( palabra[1] )
print( palabra[2] )
print( palabra[3] )
print()
print( palabra[-4] )
print( palabra[-3] )
print( palabra[-2] )
print( palabra[-1] )
print()
print( len(palabra) , type(len(palabra)) )
#print( palabra[5] )  # IndexError: string index out of range

# ---------------------------
# slicing [start:end:step]
# end - exclusivo
# start, step - opcionales
# ---------------------------

palabra = 'programación'
#          012345678901


# EJ:
# pro
# gramación

print( palabra[0:2] ) # end => exclusivo!
print( palabra[0:3] )
print( palabra[3:11] ) # end => exclusivo, slicing no tiene index error!
print( palabra[3:12] )
print( palabra[3:100] )
print()
print( palabra[:3] )
print( palabra[3:] )


# EJ:
# grama
print( palabra[3:8] )
print( palabra[3:8:1] )
print( palabra[3:8:2] )


# EJ:
# usando => step
print( palabra[::1] )
print( palabra[::2] )
print( palabra[::3] )




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 12) Métodos de Formato Importantes de String <str>
print('\n\n\n12) Métodos de Formato Importantes de String <str>\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# --------------------------
# Para dar formato a texto
# --------------------------
texto = 'mE gusTA APRENDER pyTHON'
print( texto ) # mE gusTA APRENDER pyTHON
print( texto.capitalize() ) # Me gusta aprender python
print( texto.title() ) # Me Gusta Aprender Python
print( texto.upper() ) # ME GUSTA APRENDER PYTHON
print( texto.lower() ) # me gusta aprender python
print( texto.swapcase() ) # Me GUSta aprender PYthon

# ---------------------
# Alineación de texto
# ---------------------
nombre = 'Andy'

print('Hola', nombre, 'espero estés bien!') # Hola Andy espero estés bien!
print('Hola', nombre.center(10), 'espero estés bien!') # Hola    Andy    espero estés bien!
print('Hola', nombre.ljust(10), 'espero estés bien!') # Hola Andy       espero estés bien!
print('Hola', nombre.rjust(10), 'espero estés bien!') # Hola       Andy espero estés bien!

# ---------------------
# Contar Coincidencias
# ---------------------
cadena = 'esta vida es hermosa'
#         01234567890123456789

print( cadena.count('a') ) # 3
print( cadena.count('es') ) # 2
print( cadena.count('a' , 4) ) # 2
print( cadena.count('a' , 4 , 10) ) # 1
print( cadena.count('x') ) # 0

# --------------------------------
# Retornar índice de una búsqueda
# --------------------------------
lenguaje = 'javascript'
#           0123456789

print( lenguaje.index('a') , lenguaje.find('a') ) # izquierda a derecha
print( lenguaje.rindex('a') , lenguaje.rfind('a') ) # derecha a izquierda
print( lenguaje.index('asc') , lenguaje.find('asc') ) 
print( lenguaje.index('c',3,8) , lenguaje.find('c',3,8) ) 
#print( lenguaje.index('x') ) # ValueError: substring not found
print( lenguaje.find('x') ) # -1

# ------------------------------
# Eliminar espacios / caracter
# ------------------------------
c1 = '    python'
c2 = 'python   '
c3 = '      python   '
c4 = '***python**'

print(c1)
print(c2)
print(c3)
print(c4)

print( c1.lstrip() )
print( c2.rstrip() )
print( c3.strip() )
print( c4.strip('*') )

# -------------------------------------------
# Unir un caracter a un string en secuencia
# -------------------------------------------
char_1 = '-'
char_2 = '#'

palabra = 'youtube'

print( char_1.join(palabra) ) # y-o-u-t-u-b-e
print( char_2.join(palabra) ) # y#o#u#t#u#b#e
print( '.'.join(palabra) ) # y.o.u.t.u.b.e

# ---------------------------------------------
# Separar un string en elementos de una lista
# (* tema lista ya lo vemos a continuación)
# ---------------------------------------------
lenguajes_1 = 'java python c++ basic'
lenguajes_2 = 'java,python,c++,basic'

lista_1 = lenguajes_1.split()
lista_2 = lenguajes_2.split(',')

print( lista_1 , type(lista_1) , len(lista_1) ) # ['java', 'python', 'c++', 'basic'] <class 'list'> 4
print( lista_2 , type(lista_2) , len(lista_2) ) # ['java', 'python', 'c++', 'basic'] <class 'list'> 4

# --------------------------
# Líneas de string a lista
# --------------------------
texto = 'Yo programo en Python.\nEl en Java.\nElla en C++.'
lista_1 = texto.splitlines()
lista_2 = texto.splitlines(keepends=True) # conserva los saltos de línea como secuencia de escape

print(texto)
print(lista_1)
print(lista_2)

texto = """hola
mundo
hola python"""

lista = texto.splitlines()
print(lista)

# --------------------------
# Cambiar espaciado de tabs
# --------------------------
saludo = 'hola\tamigo'

print( saludo )               # hola    amigo
print( saludo.expandtabs() )  # hola    amigo
print( saludo.expandtabs(1) ) # hola amigo
print( saludo.expandtabs(2) ) # hola  amigo
print( saludo.expandtabs(4) ) # hola    amigo

# -----------------------------------------------
# IMPORTANTE: reemplazar un caracter del string
# -----------------------------------------------
secreto = 'pXlabrX secreXtX pXlabrX ocultX'

print( secreto.replace('X' , '***') ) # p***labr*** secre***t*** p***labr*** ocult***       
print( secreto.replace('pXl' , 'zzzzzz') ) # zzzzzzabrX secreXtX zzzzzzabrX ocultX
print( secreto.replace(' ' , 'yyy') ) # pXlabrXyyysecreXtXyyypXlabrXyyyocultX




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 13) Métodos de String con Retorno Booleano (averiguar algo en el String)
print('\n\n\n13) Métodos de String con Retorno Booleano (averiguar algo en el String)\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ----------------------------------------------------
# .isalpha() => True si todos son letras (A-Z / a-z)
# ----------------------------------------------------
c_1 = 'abcXYZ'
c_2 = 'abc XYZ'
c_3 = '1abcXYZ'

print( c_1 , c_1.isalpha() ) # abcXYZ True
print( c_2 , c_2.isalpha() ) # abc XYZ False
print( c_3 , c_3.isalpha() ) # 1abcXYZ False

# -------------------------------------------
# .isalnum() => True si son letras y números
# -------------------------------------------
print( c_1 , c_1.isalnum() ) # abcXYZ True
print( c_2 , c_2.isalnum() ) # abc XYZ False
print( c_3 , c_3.isalnum() ) # 1abcXYZ True

# --------------------------------------------
# .isdigit() => True si es un sting numérico
# --------------------------------------------
c_1 = '12345'
c_2 = '123 45'
c_3 = '12.345'
c_4 = 'a12345'

print( c_1 , c_1.isdigit() ) # 12345 True
print( c_2 , c_2.isdigit() ) # 123 45 False
print( c_3 , c_3.isdigit() ) # 12.345 False
print( c_4 , c_4.isdigit() ) # a12345 False

# --------------------------
# Verificadores de formato
# .islower()
# .isupper()
# .istitle()
# --------------------------
c_1 = 'Hola Amigo' # title
c_2 = 'Hola amigo'
c_3 = 'HOLA AMIGO' # upper
c_4 = 'hola amigo' # lower

print('string|.islower()|.isupper()|.istitle()')             # string|.islower()|.isupper()|.istitle()
print( c_1 , c_1.islower() , c_1.isupper() , c_1.istitle() ) # Hola Amigo False False True
print( c_2 , c_2.islower() , c_2.isupper() , c_2.istitle() ) # Hola amigo False False False
print( c_3 , c_3.islower() , c_3.isupper() , c_3.istitle() ) # HOLA AMIGO False True False
print( c_4 , c_4.islower() , c_4.isupper() , c_4.istitle() ) # hola amigo True False False

# ----------------------------
# .startswith() / .endswith()
# ----------------------------
c_1 = 'súper python!'
c_2 = ' Hola mundo...'

print( c_1.startswith('s') ) # True
print( c_1.startswith('sú') ) # True
print( c_2.startswith(' ') ) # True
print( c_2.startswith(' H') ) # True
print( c_2.startswith(' h') ) # False
print()
print( c_1.endswith('!') ) # True
print( c_1.endswith('n!') ) # True
print( c_1.endswith('On!') ) # False




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 14) Métodos para Números + Librería Math
print('\n\n\n14) Métodos para Números + Librería Math\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ==> funciones internas para números

# ---------------------------------
# round() / inmediato superior
# ---------------------------------
num_1 = 3.2
num_2 = 3.5
num_3 = 3.9

print( num_1, '|' , round(num_1) ) # 3.2 | 3
print( num_2, '|' , round(num_2) ) # 3.5 | 4
print( num_3, '|' , round(num_3) ) # 3.9 | 4


# ---------------------------
# abs() / valor absoluto
# ---------------------------
num_1 = -9
num_2 = -10.5

# ---------------------
# pow() / exponencial
# ---------------------
print( pow(2,3) ) # 8
print( pow(5,2) ) # 25
print( pow(25,1/2) ) # 5.0
print( pow(25,0.5) ) # 5.0

print( abs(num_1) , abs(num_2) ) # 9 10.5

# -----------------------------------
# sum() / max() / min() / En Listas
# -----------------------------------
lista_1 = [-5, 20, 5, 8.6, -1.2]

print( sum(lista_1), max(lista_1), min(lista_1) ) # 27.400000000000002 20 -5


# ==> librería math
# https://www.w3schools.com/python/python_math.asp


# --------------------------
# Importación de un módulo
# --------------------------
import math

# ------------
# Constantes
# ------------
print( math.e ) # 2.718281828459045
print( math.pi ) # 3.141592653589793


# ------------------------
# Representación numérica
# ------------------------
print( math.ceil(4.8) ) # techo / número arriba => 5
print( math.floor(4.8) ) # piso / número abajo => 4

# ------------------
# Raíces y Potencia
# ------------------
print( math.pow(2,3) ) # potencia => 8.0
print( math.sqrt(25) ) # raíz cuadrada => 5.0
print( math.cbrt(8) ) # raiz cúbica => 2.0

# -----------
# Logaritmos
# -----------
print( math.log(2.71 ** 5) ) # logaritmo natural => 4.984743174458048
print( math.log10(10000) ) # logatirmo base 10 => 4.0

# ---------------------------
# Ángulos
# 360 grados == 2*pi radianes
# ---------------------------
print( math.degrees( math.pi / 3 ) ) # pasar de rad a grados => 59.99999999999999
print( math.radians(180) ) # pasar de grados a rad => 3.141592653589793
print( math.sin( math.pi / 6 ) ) # seno de 30 grados => 0.49999999999999994
print( math.cos( math.pi / 3 ) ) # coseno de 60 grados => 0.5000000000000001
print( math.tan( math.pi / 4 ) ) # tangente de 45 grados => 1
print( math.asin(0.5) ) # arcoseno => 0.5235987755982989
print( math.acos(0.5) ) # arcocoseno => 1.0471975511965979
print( math.atan(1) ) # arcotangente => 0.7853981633974483
print( math.degrees( math.asin(0.5) ) ) # 30.000000000000004
print( math.degrees( math.acos(0.5) ) ) # 60.00000000000001
print( math.degrees( math.atan(1) ) ) # 45.0

# ----------------------------
# Otras funciones importantes
# ----------------------------
print( math.factorial(4) ) # 24

lista_1 = [-5, 20, 5, 8.6, -1.2]
print( math.fsum(lista_1) ) # 27.4

num_1 = -55.66
print( math.fabs(num_1) ) # 55.66




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 15) Encadenamiento / Chaining - Funciones & Métodos
print('\n\n\n15) Encadenamiento / Chaining - Funciones & Métodos\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ------------------------
# Métodos
# => izquierda a derecha
# ------------------------
str_1 = '   hOla MundO  '
print( str_1 ) #    hOla MundO
print( str_1.title().strip(' ') ) # Hola Mundo


# -------------------------
# Funciones
# => de dentro hacia fuera
# -------------------------
print( type( len(str_1) ) ) # <class 'int'>




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 16) Función Internal => eval()
print('\n\n\n16) Función Internal => eval()\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - evaluar una expresión matemática
# - expresada a manera de string 

expr_1 = '2*5 - (10 + 3)/2 - 2**3'
expr_2 = '2*5 - (10 + 3)/2 - 2**3 - pow(3,2) + sum([1,2,3])'

print( eval(expr_1) ) # -4.5
print( eval(expr_2) ) # -7.5




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 17) input => entrada de datos
print('\n\n\n17) input => entrada de datos\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# -----------
# SIN input
# -----------
"""
nombre = 'Sebas'
edad = 36

print('Su nombre es', nombre)
print('Usted tiene', edad, 'años')
print('El próximo año tendrá', edad + 1, 'años!')
"""

# -----------------
# Utilizando input
# -----------------
"""
nombre = input('¿Cual es su nombre? : ')
edad = input('Qué edad tiene? : ')

print('Su nombre es', nombre)
print('Usted tiene', edad, 'años')
#print('El próximo año tendrá', edad + 1, 'años!')

# => todo lo que viene del input es string
print( type(nombre) )
print( type(edad) )
"""

# -------------------
# Utilizando casting
# -------------------
"""
nombre = input('¿Cual es su nombre? : ')
edad = input('Qué edad tiene? : ')

print('Su nombre es', nombre)
print('Usted tiene', edad, 'años')
print('El próximo año tendrá', int(edad) + 1, 'años!')
"""




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 18) Operadores de Comparación
print('\n\n\n18) Operadores de Comparación\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - al usarlos nos devuelve un valor booleano

# -----------------------------------
# Tabla de Operadores de Comparación
# -----------------------------------
'''
Operador |  Definición
-------------------------------
   >     |  Mayor que
   <     |  Menor que
   >=    |  Mayor o igual que
   <=    |  Menor o igual que
   ==    |  Igual que
   !=    |  Diferente de
'''

# ------------
# Con Números
# ------------
print( 5 > 2 ) # True
print( 2 < 5 ) # True
print( 2 >= 2 ) # True
print( 3 <= 4 ) # True
print( 3 <= 3 ) # True
print( 8 == 8 ) # True
print( 8 == 9 ) # False
print( 8 != 9 ) # True
print( 10 != 10 ) # False

# ------------
# Con Strings
# ------------
print( 'a' > 'z' ) # False
print( '&' > '@' ) # False

# https://elcodigoascii.com.ar/
# @ => alt + 64
# & => alt + 38




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 19) Operadores Lógicos
print('\n\n\n19) Operadores Lógicos\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ----------------------------
# Tabla de Operadores Lógicos
# ----------------------------

'''
Operador |  Ejemplo  |  Descripción
----------------------------------------------------------------
not      |  X and Y  |  True si todos son True
and      |  X or Y   |  Basta que 1 sea True, resultado es True
or       |  not X    |  Niega al booleano
'''

print('\nTabla AND')
# => basta que tengamos 1 False, resultado es False
print( True and False ) # False
print( False and True ) # False
print( False and False ) # False
print( True and True ) # True
print( True and True and True and True ) # True
print( True and True and False and True ) # False

print('\nTabla OR')
print( True or False ) # True
print( False or True ) # True
print( False or False ) # False
print( True or True ) # True
print( True or True or True or True ) # True
print( True or True or False or True ) # True

print('\nTabla NOT')
print( not True ) # False
print( not False ) # True

print('\nCombinando!')
print( True and False or (True and not False) ) # True




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 20) Listas en Python
print('\n\n\n20) Listas en Python\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - la colección de datos MÁS IMPORTANTE

# ----------------
# Creación Básica
# ----------------
# - corchetes y separando elementos con coma
# - con len() => tamaño de lista / número de elementos
lista = [True, -100, 'ABC', 8.5, None, [1,2,3]] # True
print(lista , type(lista) , len(lista)) # [True, -100, 'ABC', 8.5, None, [1, 2, 3]] <class 'list'> 6

# ----------------------------
# Creación con Función list()
# ----------------------------
lista = list([1,2,'A']) # [1, 2, 'A'] <class 'list'> 3
print(lista , type(lista) , len(lista)) # [1, 2, 'A'] <class 'list'> 3

# ------------
# Lista Vacía
# ------------
lista_vacia_1 = []
lista_vacia_2 = list()

print( lista_vacia_1 , len(lista_vacia_1) ) # [] 0
print( lista_vacia_2 , len(lista_vacia_2) ) # [] 0

# ---------------------------
# Palabra Clave / Keyword in
# ---------------------------
lista = [True, -100, 'ABC', 8.5, None, [1,2,3]]

print( 'ABC' in lista ) # True
print( -100 in lista ) # True
print( '-100' in lista ) # False

# ---------------------------
# Concatenación y Operador *
# ---------------------------
lista_1 = [10, 20]
lista_2 = ['A', 'B']

r1 = lista_1 + lista_2
r2 = lista_2 + lista_1
r3 = 2 * lista_1
r4 = lista_2 * 3

print( r1 ) # [10, 20, 'A', 'B']
print( r2 ) # ['A', 'B', 10, 20]
print( r3 ) # [10, 20, 10, 20]
print( r4 ) # ['A', 'B', 'A', 'B', 'A', 'B']

# -------------------
# Indexing & Slicing
# -------------------
lista = [10,20,30,40]

print( lista[0] ) # 10
print( lista[-1] ) # 40
print( lista[1:3] ) # [20, 30]
print( lista[:3] ) # [10, 20, 30]
print( lista[3:] ) # [40]
print( lista[::2] ) # [10, 30]


# ==> Métodos Importantes

# -----------
# .append()
# -----------
lista = [1,2,3]
print(lista) # [1, 2, 3]
lista.append('a')
print(lista) # [1, 2, 3, 'a']
lista.append([10,20])
print( lista , len(lista) ) # [1, 2, 3, 'a', [10, 20]] 5

# -----------
# .insert()
# -----------
lista = ['A', 'B', 'C']
#         0    1    2

lista.insert( 1 , 'Sebas' )
print( lista )

lista.insert( -1 , 100 )
print( lista )


# -------------------------------------------
# métodos / funciones para borrar elementos

# del lista[indice]
# .pop()
# .remove()
# .clear()
# -------------------------------------------

lista = ['A', 'B', 'C', 10, 20, 30, -100.5, -200.5]
#         0    1    2   3   4   5     6       7
print(lista) # ['A', 'B', 'C', 10, 20, 30, -100.5, -200.5]

del lista[4]
print( lista, len(lista) ) # ['A', 'B', 'C', 10, 30, -100.5, -200.5] 7

lista.pop()
print( lista, len(lista) ) # ['A', 'B', 'C', 10, 30, -100.5] 6

lista.pop()
print( lista, len(lista) ) # ['A', 'B', 'C', 10, 30] 5

lista.pop(2)
print( lista, len(lista) ) # ['A', 'B', 10, 30] 4

lista = ['A', 'B', 'C', 10, 20, 30, -100.5, -200.5]
#         0    1    2   3   4   5     6       7

elemento_pop = lista.pop()
print( lista ) # ['A', 'B', 'C', 10, 20, 30, -100.5]
print( elemento_pop ) # -200.5

lista.remove('A')
print( lista ) # ['B', 'C', 10, 20, 30, -100.5]

lista.remove(30)
print( lista ) # ['B', 'C', 10, 20, -100.5]


# ==> ERROR cuando trato de eliminar algo que no existe

lista = ['A', 'B', 'C', 10, 20, 30, -100.5, -200.5]
#         0    1    2   3   4   5     6       7

#del lista[10] # IndexError: list assignment index out of range
#lista.pop(10) # IndexError: pop index out of range
#lista.remove('AA') # ValueError: list.remove(x): x not in list

lista.clear()
print( lista ) # []

# ---------
# .count()
# ---------
lista = [1,2,3,10,20,30,1,5,9,-1,-2,-3,1]
print( lista.count(1) )

# -----------
# .reverse()
# -----------
lista = ['A', 'B', 'C', 10, 20, 30, -100.5, -200.5]
print( lista ) # ['A', 'B', 'C', 10, 20, 30, -100.5, -200.5]
lista.reverse()
print( lista ) # [-200.5, -100.5, 30, 20, 10, 'C', 'B', 'A']

# --------
# .sort()
# --------
l1 = [20, 5, 2, 15]
l2 = ['a', 'x', 'm', 'h']
l3 = ['sol', 'hola', 'palabra']

l1.sort() # números => menor a mayor
l2.sort() # strings => a-z

print( l1 ) # [2, 5, 15, 20]
print( l2 ) # ['a', 'h', 'm', 'x']

l1.sort(reverse=True) # números => mayor a menor
l3.sort(reverse=True) # strings => z-a

print( l1 ) # [20, 15, 5, 2]
print( l2 ) # ['a', 'h', 'm', 'x']

l3.sort( reverse=True, key=len )
print(l3) # ['palabra', 'hola', 'sol']
l3.sort( reverse=False, key=len )
print(l3) # ['sol', 'hola', 'palabra']
l3.sort( key=len )
print(l3) # ['sol', 'hola', 'palabra']

# --------
# .copy()
# --------
lista = [1,2,3]
print( lista, len(lista) ) # [1, 2, 3] 3
lista.append('A')
print( lista, len(lista) ) # [1, 2, 3, 'A'] 4

lista = [1,2,3]
lista_2 = lista
lista_2.append('Z')
print(lista, lista_2) # [1, 2, 3, 'Z'] [1, 2, 3, 'Z']

lista = [1,2,3]
lista_copy = lista.copy()
lista.append('X')
lista_copy.append('Y')
print(lista, lista_copy) # [1, 2, 3, 'X'] [1, 2, 3, 'Y']




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 21) Condicional IF
print('\n\n\n21) Condicional IF\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# -----
# EJ 1
# -----
nota = 14

if nota >= 15 and nota < 20:
    print('Usted ha pasado la materia')
elif nota < 15 and nota >= 0:
    print('Usted ha perdido la materia')
else:
    print('Error - Nota debe ser de 0 a 20')
# end if


# -----
# EJ 2
# -----
"""
nota = input('¿Cuál fue su nota? : ')
nota = int(nota)

if nota >= 15 and nota < 20:
    print('Usted ha pasado la materia')
elif nota < 15 and nota >= 0:
    print('Usted ha perdido la materia')
else:
    print('Error - Nota debe ser de 0 a 20')
# end if
"""

# -----
# EJ 3
# -----
temp = 20

if temp < 5 or temp > 35:
    print('Clima muy malo!')
else:
    print('Qué buen clima!')
# end if




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 22) Condicional Match-Case
print('\n\n\n22) Condicional Match-Case\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - a partir de python 3.10 >
# - simula el switch...case de otros lenguajes

opcion = '5'

match opcion:
    case '1':
        print('Opción 1 - Guardar Archivo')
    case '2':
        print('Opción 2 - Eliminar Archivo')
    case '3':
        print('Opción 3 - Salir del Programa')
    case _ :
        print('ERROR - Opción no existe')
# end match-case




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 23) Operador Ternario
print('\n\n\n23) Operador Ternario\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - una manera corta / sencilla de expresar una condición
# - aconsejable usarla para algo sencillo

# --------------------
# Con condicional IF
# --------------------
edad = 14

if edad >= 18:
    print('Usted es mayor de edad')
else:
    print('Usted es menor de edad!!')
# end if

# ----------------------
# Con Operador Ternario
# ----------------------
resultado = 'Mayor de edad' if edad >= 18 else 'Menor de Edad'
print(resultado)




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 24) Bucle For
print('\n\n\n24) Bucle For\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

lista = ['Sebas', 'Carlos', 'Ana', 'Ramón', 'Julia']
nombre = 'Ximena'

# --------------------
# recorrido de listas
# --------------------
for cada_elemento in lista:
    print(cada_elemento)
# end for

# --------------------------------------------
# la variable usada para el recorrido se crea
# --------------------------------------------
print()
print( cada_elemento ) # Julia

# ----------------------
# recorrido de Strings
# ----------------------
print()
for letra in nombre:
    print(letra)
# end for

# ----------------------------
# función interna range + for
# range (start, end, step)
# end => EXCLUSIVO
# ----------------------------
print()

rango_1_10 = range(1,11)
rango_1_10_2 = range(1,11,2)

print( rango_1_10 ) # range(1, 11)
print( rango_1_10_2 ) # range(1, 11, 2)

for x in range(1,11):
    print(x, x*2, x**2)
# print

# -----------------------
# for + contador externo
# -----------------------
print()
lista = ['Sebas', 'Carlos', 'Ana', 'Ramón', 'Julia']

contador = 1

for nombre in lista:
    print('Estudiante #', contador, '=>', nombre)
    contador += 1 # importante incremento!
# end for

# ----------------
# for + enumerate
# ----------------
print()

for index, nombre in enumerate(lista):
    print('Estudiante #', index, '==>', nombre)
# end for

# -----------
# for + else
# -----------
# - se ejecuta 1 vez al final de la iteración
print()

for nombre in lista:
    print('Estudiante: ' + nombre + ' => PRESENTE!')
else:
    print('Fin de tomar lista')
# end for

# -------------
# for + break
# -------------
# - para romper / terminar la iteración por completo
print()

for x in range(1, 21):
    print(x)
    if x == 10:
        print('fin del bucle for')
        break
    # end if
# end for

# ---------------
# for + continue
# ---------------
# - para saltar una iteración
print()

for x in range(1, 21):
    print(x)
    if x == 10 or x == 15:
        print('Salto en iteración cuando x =', x)
        continue
    # end if
# end for

# -----------
# for + pass
# -----------
# - en este caso pass funciona como continue
print()

for x in range(1, 21):
    print(x)
    if x == 10 or x == 15:
        print('Salto en iteración cuando x =', x)
        pass
    # end if
# end for

# -----------------------------------
# aplicación for => cálculo numérico
# -----------------------------------
print()

sumatoria = 0
producto = 1

for x in range(1,11):
    sumatoria += x
# end for

for x in range(1,11):
    producto *= x
# end for

print('sumatoria =', sumatoria)
print('producto =', producto)




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 25) Bucle while
print('\n\n\n25) Bucle while\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - nunca olvidar el contador + incremento / decremento
# - cuidado con loop infinito

# ----------------------
# ERROR: bucle infinito
# ----------------------

"""
x = 1

while x <= 10:
    print('x =', x)
# end while
"""

# ---------------------------------------
# Incremento / Decremento indispensable
# ---------------------------------------
print()

x = 1

while x <= 10:
    print('x =', x)
    x += 1
# end while


# ----------------------------------
# Recorrido de Elementos Iterables
# ----------------------------------
# - también puede recorrer strings, listas, tange, etc...
# - pero para hacer eso se debe usar mejor el bucle for

lista = ['Sebas', 'Carlos', 'Ana', 'Ramón', 'Julia']
nombre = 'Ximena'
rango_1_10 = range(1,11)

# -- recorrido de lista + while
print()

i = 0

while i < len(lista):
    print(lista[i])
    i += 1
# end while

# -- recorrido de string + while
print()

i = 0

while i < len(nombre):
    print(nombre[i])
    i += 1
# end while

# -- recorriendo range + while
print()

i = 0

while i < len(rango_1_10):
    print(rango_1_10[i])
    i += 1
# end while


# --------------
# while + else
# --------------
# - se ejecuta una vez al final
# - así se cumpla la condición o no
print()

x = 5

while x > 10:
    print('hola')
# end while

print()

while x > 10:
    print('hola')
else:
    print('else en while')
# end while

print()

while x <= 10:
    print('x =', x)
    x += 1
else:
    print('Fin de bucle, x al final =', x)
# end while

# ---------------
# while + break
# ---------------
# - romper / terminar el bucle
print()

x = 0

while x <= 5:
    if x == 3:
        break
    print('Contador x =', x)
    x += 1
# end while

# -------------------------
# while + continue / pass
# -------------------------
# - saltarse iteraciones
print()

x = 0

while x <= 5:
    if x == 2 or x == 4:
        x += 1
        continue
    print('El valor de x =', x)
    x += 1
# end while

# ------------
# while True
# ------------
# - técnica de bucle para ejecutar un programa
# - siempre entramos al bucle
# - CUIDADO: obliga el uso de un break para terminar el bucle en algún momento
print()

"""
while True:
    print('Bienvenido al Programa')
    print('Opciones:')
    print('(A) Comprar')
    print('(B) Vender')
    print('(C) Salir (s/q)\n')
    opcion = input('Elija su opción : ')
    opcion = opcion.upper().strip(' ')
    print()
    
    if opcion == 'A':
        print('Usted a seleccionado la opción de COMPRAR !')
    elif opcion == 'B':
        print('Usted a seleccionado la opción de VENDER !')
    elif opcion == 'C' or opcion == 'S' or opcion == 'Q':
        print('Gracias por utilizar el programa!')
        break
    else:
        print('ERROR - Opción no existe! :(')
# end while
"""




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 26) pares / impares / múltiplos
print('\n\n26) pares / impares / múltiplos\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 27) print avanzado + string format
print('\n\n\n27) print avanzado + string format\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ------------------------
# print básico aprendido
# ------------------------
print('hola mundo')
print('hola python')

# --------------------------
# parámetro opcional (end)
# --------------------------
print('hola mundo' , end=' ')
print('hola python')

print('hola mundo' , end='****')
print('hola python')

# -----------------
# string.format()
# -----------------
nombre = 'Sebas'
edad = 36
nota_final = 15.5
es_estudiante = False

print( nombre, edad, nota_final, es_estudiante ) # print con parámetros
print( nombre + ' ' + str(edad) + ' ' + str(nota_final) + ' ' + str(es_estudiante) ) # print + concatenación str
print( '{} / {} / {} / {}'.format(nombre, edad, nota_final, es_estudiante) ) # print + str.format()
print( '\nNombre: {}\nEdad:{}\nNota Final: {}\n¿Es estudiante?: {}\n'.format(nombre, edad, nota_final, es_estudiante) )

print( '\nNombre: {}\nEdad:{}\nNota Final: {}\n¿Es estudiante?: {}\n'.format
      (nombre.upper(),
       edad,
       nota_final,
       es_estudiante)
     )

# -----------
# f'String'
# -----------
print( f'Nombre: {nombre} | Edad: {edad} | Nota Final: {nota_final} | ¿Es Estudiante?: {es_estudiante}' )


# ---------------------------------------
# str.format() + argumentos posicionales
# ---------------------------------------
n1 = 'Andy'
n2 = 'Paola'
n3 = 'Ximena'

print( '{} es increíble! {} es inteligente! {} es una gran persona!'.format(
    n1, n2, n3
) )

print( '{2} es increíble! {1} es inteligente! {0} es una gran persona!'.format(
    n1, n2, n3
) )

# IndexError
"""
print( '{5} es increíble! {1} es inteligente! {0} es una gran persona!'.format(
    n1, n2, n3
) )
"""

# ---------------------------------------
# str.format() + argumentos con keyword
# ---------------------------------------
print('Me gusta el pastel de {comida} con una {bebida}'.format(
    comida = 'chocolate',
    bebida = 'cola'
))




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 28) String Format + Números
print('\n\n28) String Format + Números\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ------------------------------
# Número de dígitos & decimales
# ------------------------------
PI = 3.14159265358979323846

print( 'PI = {}'.format(PI) )
print( 'PI = {:.2}'.format(PI) )
print( 'PI = {:.4}'.format(PI) )
print( 'PI = {:.2f}'.format(PI) )
print( 'PI = {:.4f}'.format(PI) )

# -----------
# Alineación
# -----------
num = 1.234
print( 'Valor = {} | Es un Número Flotante'.format(num) )
print( 'Valor = {:10} | Es un Número Flotante'.format(num) ) # alineación derecha
print( 'Valor = {:>10} | Es un Número Flotante'.format(num) ) # alineación derecha
print( 'Valor = {:<10} | Es un Número Flotante'.format(num) ) # alineación izquierda
print( 'Valor = {:^10} | Es un Número Flotante'.format(num) ) # alineación en centro

# -------------------
# Relleno de ceros 
# -------------------
# - OJO: Toma en cuenta todos los caracteres
num = 1.23
print( 'Número = {:05}'.format(num) )
print( 'Número = {:08}'.format(num) )

# -------------------
# Separador de miles
# -------------------
num = 12345678
print( '{}'.format(num) )
print( '{:,}'.format(num) )

# --------------------
# Notación Científica
# --------------------
print( '{:E}'.format(num) )
print( '{:e}'.format(num) )
print( '{:.3e}'.format(num) ) # notación científica con decimales

# ----------------
# Combinando todo
# ----------------
num = 1.23456
print( 'El valor = {} | Es un flotante.'.format(num) )
print( 'El valor = {:15.2f} | Es un flotante.'.format(num) )
print( 'El valor = {:<15.2f} | Es un flotante.'.format(num) )

# --------------
# CON f'String'
# --------------
print( f'El valor = {num:<15.2f} | Es un flotante.' )




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 29) String Format + Texto
print('\n\n\n29) String Format + Texto\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

pais = 'ECUADOR'

print( 'Mi país {}, es un país muy hermoso'.format(pais) ) # sin formato
print( 'Mi país {:<15}, es un país muy hermoso'.format(pais) ) # alineación a izquierda
print( 'Mi país {:>15}, es un país muy hermoso'.format(pais) ) # alineación a derecha
print( 'Mi país {:^15}, es un país muy hermoso'.format(pais) ) # alineación a centro
print( 'Mi país {:.3}, es un país muy hermoso'.format(pais) ) # truncamiento
print( 'Mi país {:^10.3}, es un país muy hermoso'.format(pais) ) # alineación + truncamiento
print( f'Mi país {pais:^10.3}, es un país muy hermoso' ) # con f'String'




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 30) Librería / Módulo random
print('\n\n\n30) Librería / Módulo random\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# -------------------
# importación módulo
# -------------------
import random

# ----------
# .random()
# ----------
# - número al azar entre 0 y 1
# - sin incluir el 1

x = random.random()
print(x)

# ---------------
# .random() * N
# ---------------
# - para generar números aleatorios de 0 a N
# - sin incluir N
print()

lista_numeros = []

for i in range(1,21):
    lista_numeros.append( random.random() * 100 )
# end for

print(lista_numeros)

# -----------------------------------------
# Truco str.format() para reducir decimales
# -----------------------------------------
print()

lista_numeros = []

for i in range(1,21):
    x = random.random() * 100
    x = '{:.2f}'.format(x)
    x = float(x)
    lista_numeros.append(x)
# end for

print(lista_numeros)

# --------------
# .randint(x,y)
# --------------
# - número entero aleatorio entre x, y
print()

lista_numeros = []

for i in range(1,21):
    lista_numeros.append( random.randint(1000,2000) )
# end for

print(lista_numeros)

# ----------
# .choice()
# ----------
# - aplicado en lista !!
heroes = ['goku', 'gohan', 'krilin', 'yamcha', 'vegeta']

print( heroes )
print( random.choice(heroes) )
print( random.choice(heroes) )

# -----------
# .shuffle()
# -----------
# - aplicado en lista !!
heroes = ['goku', 'gohan', 'krilin', 'yamcha', 'vegeta']
print( heroes )

random.shuffle(heroes)
print( heroes )

# sin cambiar la lista original
heroes = ['goku', 'gohan', 'krilin', 'yamcha', 'vegeta']
heroes_copy = heroes.copy()
random.shuffle( heroes_copy )

print( heroes )
print( heroes_copy )



# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 31) Condicional Anidado
print('\n\n\n31) Condicional Anidado\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

"""
opciones_juego = ['Piedra', 'Papel', 'Tijera']

opcion_player = ''
opcion_cpu = ''

while True:
    print('Juego Piedra / Papel / Tijera')
    print('(A) Piedra')
    print('(B) Papel')
    print('(C) Tijera')
    print('(D) Salir (s/q)\n')
    
    opcion_player = input('Elija su opción : ')
    opcion_player = opcion_player.title().strip(' ')
    
    opcion_cpu = random.choice(opciones_juego)
    
    print( 'Player ha elegido => {}'.format(opcion_player.upper()) )
    print( 'Computadora ha elegido => {}'.format(opcion_cpu.upper()) )
    
    if opcion_player == 'A' or opcion_player == 'Piedra':
        opcion_player = 'Piedra'
        if opcion_cpu == 'Piedra':
            print('EMPATE !')
        elif opcion_cpu == 'Papel':
            print( '{} le gana a {} - Computadora gana!!'.format(opcion_cpu.upper(), opcion_player.upper()) )
        elif opcion_cpu == 'Tijera':
            print( '{} le gana a {} - Player gana!!'.format(opcion_player.upper(), opcion_cpu.upper()) )
    
    elif opcion_player == 'B' or opcion_player == 'Papel':
        opcion_player = 'Papel'
        if opcion_cpu == 'Papel':
            print('EMPATE !')
        elif opcion_cpu == 'Tijera':
            print( '{} le gana a {} - Computadora gana!!'.format(opcion_cpu.upper(), opcion_player.upper()) )
        elif opcion_cpu == 'Piedra':
            print( '{} le gana a {} - Player gana!!'.format(opcion_player.upper(), opcion_cpu.upper()) )
    
    elif opcion_player == 'C' or opcion_player == 'Tijera':
        opcion_player = 'Tijera'
        if opcion_cpu == 'Tijera':
            print('EMPATE !')
        elif opcion_cpu == 'Piedra':
            print( '{} le gana a {} - Computadora gana!!'.format(opcion_cpu.upper(), opcion_player.upper()) )
        elif opcion_cpu == 'Papel':
            print( '{} le gana a {} - Player gana!!'.format(opcion_player.upper(), opcion_cpu.upper()) )
    
    elif opcion_player == 'D' or opcion_player == 'S' or opcion_player == 'Q':
        print('Gracias por Jugar! :)')
        break
    
    else:
        print('ERROR - Opción Equivocada! :(')
    # end if
# end while
"""



# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 32) Listas Multidimensionales
print('\n\n\n32) Listas Multidimensionales\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - Una lista puede contener otras listas

# ---------------------------------------------
# Representación de una lista multidimensional
# ---------------------------------------------
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matriz)

# --------------------
# Acceso de elementos
# --------------------
print( len(matriz) )
print( matriz[0] )
print( matriz[1] )
print( matriz[2] )
# ej acceder al 6
print( matriz[1][2] ) # 6
# ej acceder al 8
print( matriz[2][1] ) # 8




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 33) Bucles Anidados
print('\n\n\n33) Bucles Anidados\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ---------------------------
# Recorrido básico con while
# ---------------------------
# - NO OLVIDAR: while obliga tener un contador

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

i = 0 # filas
j = 0 # columnas


# ==> recorrido básico
print()
while i < len(matriz):
    while j < len( matriz[i] ):
        print( matriz[i][j] )
        j += 1
    i += 1
    j = 0
# end while

i = 0
j = 0

# ==> recorrido + print => forma de matriz
print()
while i < len(matriz):
    while j < len( matriz[i] ):
        print( matriz[i][j] , end='\t' )
        j += 1
    i += 1
    j = 0
    print()
# end while


# -------------------------
# Recorrido básico con for
# -------------------------

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# i => filas
# j => columnas


# ==> recorrido básico
print()

for i in matriz:
    for j in i:
        print(j)
# end for


# ==> recorrido + print en forma de matriz
print()

for i in matriz:
    for j in i:
        print(j , end='\t')
    print()
# end for




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 34) Mutabilidad / Inmutabilidad
print('\n\n34) Mutabilidad / Inmutabilidad\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - Mutabilidad => que puede cambiar
# - Inmutabilidad => que no puede cambiar

# --------------------------------
# funciones internas id() & hex()
# --------------------------------
# id()  => dirección en la memoria de una variable
# hex() => transforma un entero a valor hexadecimal

numero = 10
string = 'python'
lista = [1,2,3]

print( id(numero) )
print( id(string) )
print( id(lista) )

print( hex(id(numero)) )
print( hex(id(string)) )
print( hex(id(lista)) )

# ----------------------
# concepto de INMUTABLE
# ----------------------
# - cualquier tipo básico

string = 'python'
print( string[0] ) # p
#string[0] = 'P' # TypeError: 'str' object does not support item assignment

print( hex(id(string)) )

string = string[0].upper() + string[1:] # no es modificar / reasignar una variable
print(string)
print( hex(id(string)) )

string_1 = 'java'
string_2 = 'java'

print( hex(id(string_1)) )
print( hex(id(string_2)) )


# ---------------------
# concepto de MUTABLE
# ---------------------
# - típico ejemplo son las listas

lista_1 = [1,2,3]
lista_2 = [1,2,3]

print( hex(id(lista_1)) )
print( hex(id(lista_2)) ) # son distintos

lista_3 = lista_1

print( hex(id(lista_1)) )
print( hex(id(lista_3)) ) # son los mismos

lista_3.append('A') # método que modifica la variable, la cambia!!

print( lista_1, hex(id(lista_1)) )
print( lista_3, hex(id(lista_3)) )

# => solución
lista_1 = [1,2,3]
lista_3 = lista_1.copy()

print( hex(id(lista_1)) )
print( hex(id(lista_3)) ) # son diferentes

lista_1.append('Z')
lista_3.pop()

print( lista_1, hex(id(lista_1)) )
print( lista_3, hex(id(lista_3)) )



# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 35) keyword is
print('\n\n35) keyword is\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
#   ==  | True: si 2 variables tienen el mismo valor
#   is  | True: mismo valor y dirección en la memoria

#   RECORDAR: hex(id()) => dirección en la memoria en valor hexadecimal !!

lista_1 = [1,2,3]
lista_2 = [1,2,3]

print( lista_1 == lista_2 ) # True
print( lista_1 is lista_2 ) # False
print( 'lista_1', hex(id(lista_1)) ) # lista_1 0x1acc3447bc0
print( 'lista_2', hex(id(lista_2)) ) # lista_2 0x1acc3387c80

lista_3 = lista_1

print( lista_1 == lista_3 ) # True
print( lista_1 is lista_3 ) # True
print( 'lista_1', hex(id(lista_3)) ) # lista_1 0x1acc3447bc0
print( 'lista_3', hex(id(lista_3)) ) # lista_3 0x1acc3447bc0




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 36) Tuplas
print('\n\n36) Tuplas\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - parecidos a las listas
# - son ordenadas
# - son inmutables / no se pueden modificar
# - se declaran con () / listas con []

# -----------------------
# Creación de una Tupla
# -----------------------
# - también tiene la función len()

t1 = (100, 'sebas', False, -5.8)
t2 = tuple( (100, 'sebas', False, -5.8) )

print( t1, type(t1), len(t1) ) # (100, 'sebas', False, -5.8) <class 'tuple'> 4
print( t2, type(t2), len(t2) ) # (100, 'sebas', False, -5.8) <class 'tuple'> 4

# => creando tupla vacía
tupla_vacia_1 = ()
tupla_vacia_2 = tuple()

print( tupla_vacia_1, type(tupla_vacia_1), len(tupla_vacia_1) ) # () <class 'tuple'> 0
print( tupla_vacia_2, type(tupla_vacia_2), len(tupla_vacia_2) ) # () <class 'tuple'> 0


# -------------------
# Indexing & Slicing
# -------------------
print( t1[0] ) # 100
print( t1[1] ) # sebas
print( t1[-1] ) # -5.8
print( t1[1:3] ) # ('sebas', False)

# -----------
# keyword in
# -----------
print( 100 in t1 ) # True
print( -200 in t1 ) # False

# ---------------
# Son INMUTABLES
# ---------------
lista = [100, 'sebas', False, -5.8]
tupla = (100, 'sebas', False, -5.8)

lista[1] = 'Python'
#tupla[1] = 'Java' # TypeError: 'tuple' object does not support item assignment

print(lista) # [100, 'Python', False, -5.8]
print(tupla) # (100, 'sebas', False, -5.8)

# ---------------------
# Truco para Modificar
# ---------------------
tupla = (100, 'sebas', False, -5.8)
lista = list(tupla)
lista[1] = 'Python'
tupla = tuple(lista)
print(tupla) # (100, 'Python', False, -5.8)

# ---------------
# Concatenación
# ---------------
t1 = (10, 20, 30)
t2 = ('a', 'b', 'c')

r1 = t1 + t2
r2 = t2 + t1

print( r1, r2 ) # (10, 20, 30, 'a', 'b', 'c') ('a', 'b', 'c', 10, 20, 30)

# -------------------------------
# Métodos => .count() / .index()
# -------------------------------
tupla = (10, 50, 'A', 10, '10', 'A', 'A')

print( tupla.count('A') ) # 3
print( tupla.count(10) ) # 2
print( tupla.count(100) ) # 0

print( tupla.index('A') ) # 2
print( tupla.index(10) ) # 0 => búsqueda de index de izq a der

# --------------------
# Recorrido de tuplas
# --------------------
print()
for elemento in tupla:
    print(elemento)
# end for




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 37) Sets / Conjuntos
print('\n\n37) Sets / Conjuntos\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - elementos únicos / conjuntos
# - colección desordenada
# - no se pueden alterar sus elementos, pero el set si
# - se crean con {}

# -------------------
# Creación de un Set
# -------------------
# - también tiene la función len()

conjunto_1 = {10, 'ABC', -8.5}
conjunto_2 = set( (10, 'ABC', -8.5) )

print( conjunto_1, type(conjunto_1), len(conjunto_1) ) # {-8.5, 10, 'ABC'} <class 'set'> 3
print( conjunto_2, type(conjunto_2), len(conjunto_2) ) # {-8.5, 10, 'ABC'} <class 'set'> 3

# => creando conjunto vacío
set_vacio_1 = {} # MANERA INCORRECTA => DICCIONARIO VACÍO
set_vacio_2 =set()

print( set_vacio_1, type(set_vacio_1), len(set_vacio_1) ) # {} <class 'dict'> 0
print( set_vacio_2, type(set_vacio_2), len(set_vacio_2) ) # set() <class 'set'> 0

# -------------------------------------
# No existe Indexing & Slicing en Sets
# -------------------------------------
# - ¿por qué? => los sets son colecciones desordenadas

s1 = {'A', 'B', 'C'}
#s1[0]    # TypeError: 'set' object is not subscriptable
#s1[0:2]  # TypeError: 'set' object is not subscriptable

# -------------------------------
# Elementos repetidos se eliminan
# -------------------------------
# - los elementos de un set son ÚNICOS
s1 = {'A', 'B', 'C', 'A', 'A', 'B'}
print(s1)

# -----------------------------------------
# No existe concatenación & producto (+ *)
# -----------------------------------------
s1 = {'A', 'B', 'C'}
s2 = {10, 20, 30}

#r1 = s1 + s2  # TypeError: unsupported operand type(s) for +: 'set' and 'set'
#r2 = 2 * s1   # TypeError: unsupported operand type(s) for *: 'int' and 'set'

# -----------------
# Recorrido de Set
# -----------------
s1 = {'A', 'B', 'C'}

for elem in s1:
    print(elem) # impresión en desorden
# end for


# => Métodos Importantes para SET
# - no es posible modificar elementos de un set
# - pero es posible modificar el set como tal

# -------
# .add()
# -------
s1 = {'A', 'B', 'C'}
s1.add(10)
s1.add(False)
s1.add('B')

print(s1, len(s1))


"""
Métodos para eliminar / borrar
    .remove()
    .discard()
    .pop()
    .clear()
    del set
"""

# ----------
# .remove()
# ----------
print()
s1 = {'A', 'B', 'C'}
s1.remove('A')
print(s1)
#s1.remove('Z') # KeyError: 'Z'

# -----------
# .discard() 
# -----------
# - igual que remove pero no me da error
print()
s1 = {'A', 'B', 'C'}
s1.discard('A')
print(s1)
s1.discard('Z')
print(s1)

# -------
# .pop()
# -------
# - elimina elemento al azar
print()
s1 = {'A', 'B', 'C'}
s1.pop()
print(s1)

# ---------
# .clear()
# ---------
# - deja un set vacío
print()
s1 = {'A', 'B', 'C'}
s1.clear()
print(s1) # set()

# ---------
# del set
# ---------
# elimina la variable por completo
print()
s1 = {'A', 'B', 'C'}
del s1
#print(s1) # NameError: name 's1' is not defined.


"""
Métodos de Operaciones de Conjuntos

    .union()         /  .update()
    .intersection()  /  .intersection_update()
    .difference()    /  .difference_update()

==> los update son para modificar un set existente
"""
# https://www.w3schools.com/python/python_ref_set.asp


# ------------------------
# .union()   /  .update()
# ------------------------
# - unión de conjuntos
# - se excluye elementos repetidos
s1 = {'A', 'B', 'C', 'D'}
s2 = {10, 'B', 20, 'A'}

union = s1.union(s2)
print(union)

s1.update(s2)
print(s1)

# ---------------------------------------------
# .intersection()   /  .intersection_update()
# ---------------------------------------------
# - RETORNA elementos en común entre 2 conjuntos
s1 = {'A', 'B', 'C', 'D'}
s2 = {10, 'B', 20, 'A'}

intersection_1 = s1.intersection(s2)
print(intersection_1)

s1.intersection_update(s2)
print(s1)
print(s2)

# ----------------------------------------
# .difference()   /  .difference_update()
# ----------------------------------------
# - ELIMINA elementos en común entre 2 conjuntos
s1 = {'A', 'B', 'C', 'D'}
s2 = {10, 'B', 20, 'A'}

diff_1 = s1.difference(s2)
diff_2 = s2.difference(s1)
print(diff_1)
print(diff_2)

s1.difference_update(s2)
print(s1)
print(s2)

# --------
# .copy()
# --------
# - igual que en listas
s1 = {'A', 'B', 'C'}
s2 = s1
s1.add(100)
s2.add(200)
print(s1)
print(s2)

# => evitando esto con copy
s1 = {'A', 'B', 'C'}
s2 = s1.copy()
s1.add(100)
s2.add(200)
print(s1)
print(s2)




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 38) Diccionarios
print('\n\n38) Diccionarios\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - estructura de clave y valor (key-value pair)
# - python 3.6 < -- DESORDENADOS
# - python 3.6 > -- ORDENADOS

# -------------------------------
# Creación Básica de Diccionario
# -------------------------------
# - también funciona el len (tamaño de diccionario)

#   clave : valor
dict_1 = {
    'A' : 100,
    'B' : 200,
    'C' : 300,
}

dict_2 = dict( A=100 , B=200, C=300 )

print( dict_1, type(dict_1), len(dict_1) ) # {'A': 100, 'B': 200, 'C': 300} <class 'dict'> 3
print( dict_2, type(dict_2), len(dict_2) ) # {'A': 100, 'B': 200, 'C': 300} <class 'dict'> 3

# claves => pueden ser números enteros
dict_3 = {
    100 : 'Ecuador',
    200 : 'USA',
    300 : 'Alemania'
}

print( dict_3, type(dict_3), len(dict_3) ) # {100: 'Ecuador', 200: 'USA', 300: 'Alemania'} <class 'dict'> 3

# ------------------
# Diccionario Vacío
# ------------------
dict_vacio_1 = {}
dict_vacio_2 = dict()

print( dict_vacio_1, type(dict_vacio_1), len(dict_vacio_1) ) # {} <class 'dict'> 0
print( dict_vacio_2, type(dict_vacio_2), len(dict_vacio_2) ) # {} <class 'dict'> 0

# ------------------------------
# NO existe Indexing y Slicing
# ------------------------------
dict_1 = {
    'A' : 100,
    'B' : 200,
    'C' : 300,
}

#dict_1[0]   # KeyError: 0
#dict_1[0:2] # TypeError: unhashable type: 'slice'


# -----------------
# Acceso con Clave
# -----------------
print( dict_1['A'] ) # 100
print( dict_1['C'] ) # 300

# --------------------------------------------
# Creación / Modificación con Acceso de Clave
# --------------------------------------------
dict_1['B'] = 555
dict_1['Z'] = 'python'
print( dict_1 ) # {'A': 100, 'B': 555, 'C': 300, 'Z': 'python'}

# -----------------------------------------------
# 2 valores iguales es posible pero no 2 claves
# -----------------------------------------------
# - se sobrescribe el último valor ingresado

dict_1 = {
    'Carlos' : 15,
    'Sebas' : 14,
    'Ana' : 18,
    'Ximena' : 15
}

print(dict_1) # {'Carlos': 15, 'Sebas': 14, 'Ana': 18, 'Ximena': 15}  

dict_2 = {
    'Carlos' : 15,
    'Sebas' : 14,
    'Ana' : 18,
    'Sebas' : 15
}

print(dict_2) # {'Carlos': 15, 'Sebas': 15, 'Ana': 18}

# ----------------------------------
# keyword in => averiguar una clave
# ----------------------------------
# - True si existe la clave, False si no

print( 'Carlos' in dict_1 ) # True
print( 18 in dict_1 ) # False


"""
MÉTODOS IMPORTANTES DE DICCIONARIOS
Métodos de Acceso => .get / .keys / .values / .items
Métodos de Modificación => .update / .setdefault
Métodos de Eliminación => .pop / .popitem / .clear / del
"""

# -------
# .get()
# -------
heroes = {
    'dbz' : 'goku',
    'dc' : 'superman',
    'marvel' : 'spiderman',
    'starwars' : 'obi-wan',
}

print( heroes.get('dbz') ) # goku
print( heroes['dbz'] ) # goku => con acceso por clave

# --------
# .keys()
# --------
claves = heroes.keys()
print( claves , type(claves) ) # dict_keys(['dbz', 'dc', 'marvel', 'starwars']) <class 'dict_keys'>

# ----------
# .values()
# ----------
values = heroes.values()
print( values , type(values) ) # dict_values(['goku', 'superman', 'spiderman', 'obi-wan']) <class 'dict_values'>

# ---------
# .items()
# ---------
# - retorna tupla de (clave, valor)
items = heroes.items()
print( items, type(items) ) # dict_items([('dbz', 'goku'), ('dc', 'superman'), ('marvel', 'spiderman'), ('starwars', 'obi-wan')]) <class 'dict_items'>

# ----------
# .update()
# ----------
# modifica / crea clave - valor

mod_heroes = {
    'dc' : 'wonderwoman',
    'tortugas ninja' : 'donatello'
}

heroes.update( mod_heroes )

print( heroes, len(heroes) )
# {'dbz': 'goku', 'dc': 'wonderwoman', 'marvel': 'spiderman', 'starwars': 'obi-wan', 'tortugas ninja': 'donatello'} 5


# => Con acceso a clave
heroes['dbz'] = 'gohan'
heroes['power rangers'] = 'zordon'
print( heroes, len(heroes) )
# {'dbz': 'gohan', 'dc': 'wonderwoman', 'marvel': 'spiderman', 'starwars': 'obi-wan', 'tortugas ninja': 'donatello', 'power rangers': 'zordon'} 6


# => Pasar directamente un diccionario
heroes = {
    'dbz' : 'goku',
    'dc' : 'superman',
    'marvel' : 'spiderman',
    'starwars' : 'obi-wan',
}

heroes.update( {'dbz' : 'piccolo'} )
print( heroes, len(heroes) )
# {'dbz': 'piccolo', 'dc': 'superman', 'marvel': 'spiderman', 'starwars': 'obi-wan'} 4

# --------------
# .setdefault()
# --------------
# - recibe como argumentos clave & valor
# - .setdefault(clave, valor)
# - si existe la clave => no la modifica
# - si no existe => la crea

persona = {
    'nombre' : 'Andy',
    'edad' : 32,
    'nota' : 15.8,
    'es_estudiante' : True
}

persona.setdefault( 'apellido' , 'Pérez' )
print(persona)
# {'nombre': 'Andy', 'edad': 32, 'nota': 15.8, 'es_estudiante': True, 'apellido': 'Pérez'}

persona.setdefault( 'nombre' , 'Carlos' )
print(persona)
# {'nombre': 'Andy', 'edad': 32, 'nota': 15.8, 'es_estudiante': True, 'apellido': 'Pérez'}

# -------
# .pop()
# -------
# - hay que pasar la clave como argumento
# - caso contrario da error
# - devuelve VALOR de elemento eliminado

heroes = {
    'dbz' : 'goku',
    'dc' : 'superman',
    'marvel' : 'spiderman',
    'starwars' : 'obi-wan',
}

heroes.pop('dbz')
print( heroes ) # {'dc': 'superman', 'marvel': 'spiderman', 'starwars': 'obi-wan'}
elemento = heroes.pop('marvel')
print( elemento ) # spiderman
#heroes.pop() # TypeError: pop expected at least 1 argument, got 0 

# -----------
# .popitem()
# -----------
# - python 3.7 > -- borra último elemento
# - python 3.6 < -- borra elemento al azar
# - devuelve tupla de clave valor del elemento eliminado

heroes = {
    'dbz' : 'goku',
    'dc' : 'superman',
    'marvel' : 'spiderman',
    'starwars' : 'obi-wan',
}

print( heroes.popitem() ) # ('starwars', 'obi-wan')
print( heroes ) # {'dbz': 'goku', 'dc': 'superman', 'marvel': 'spiderman'} 

# ----------
# .clear()
# ----------
# - deja un diccionario vacío

heroes = {
    'dbz' : 'goku',
    'dc' : 'superman',
    'marvel' : 'spiderman',
    'starwars' : 'obi-wan',
}

print( heroes ) # {'dbz': 'goku', 'dc': 'superman', 'marvel': 'spiderman', 'starwars': 'obi-wan'}
heroes.clear()
print( heroes ) # {}

# -------------------
# del dict['clave']
# -------------------
# - elimina par de clave/valor pasando la clave
# - también elimina toda la variable de diccionario

heroes = {
    'dbz' : 'goku',
    'dc' : 'superman',
    'marvel' : 'spiderman',
    'starwars' : 'obi-wan',
}

del heroes['marvel']
print( heroes ) # {'dbz': 'goku', 'dc': 'superman', 'starwars': 'obi-wan'}
del heroes
#print( heroes ) # NameError: name 'heroes' is not defined

# ---------------------------
# Recorrido de diccionarios
# ---------------------------
# - la mejor manera es con for + .items()

heroes = {
    'dbz' : 'goku',
    'dc' : 'superman',
    'marvel' : 'spiderman',
    'starwars' : 'obi-wan',
}

for k, v in heroes.items():
    print( 'Clave: {} - Valor: {}'.format(k,v) )
# end for




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 39) Casting entre Colecciones
print('\n\n39) Casting entre Colecciones\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# --------------
# lista a tupla
# --------------
# - para dar mayor seguridad
# - recordar, las tuplas no son modificables

lista = [1,2,3,4]
tupla = tuple(lista)

print( lista , type(lista) ) # [1, 2, 3, 4] <class 'list'>
print( tupla , type(tupla) ) # (1, 2, 3, 4) <class 'tuple'>

# ----------------------
# lista / tuplas a sets
# ----------------------
# - manera fácil de eliminar elementos repetidos

lista = [10, -5, 20, 10, 30, 25, 20]
tupla = [10, -5, 20, 10, 30, 25, 20]

set_1 = set(lista)
set_2 = set(tupla)

print(set_1) # {10, 20, 25, -5, 30}
print(set_2) # {10, 20, 25, -5, 30}


# ---------------------------------
# Casting a Diccionario => CUIDADO
# ---------------------------------
# - la colección debe tener sentido
# - con la estructura del diccionario
# - debe ser una colección de colecciones de 2 elementos (clave/valor)


# ==> Esto es ERROR
lista = [1,2,3]
#dict_1 = dict(lista) # TypeError: cannot convert dictionary update sequence element #0 to a sequence


# ==> Esto es POSIBLE!
lista = [
    ['A', 10],
    ['B', 20],
    ['C', 30],
]

tupla = (
    ('X' , -10),
    ('Y' , -20),
    ('Z' , -30),
)

lista_tuplas = [
    ('M' , 1.5),
    ('N' , 2.5),
    ('O' , 3.5),
]

dict_1 = dict(lista)
dict_2 = dict(tupla)
dict_3 = dict(lista_tuplas)

print(dict_1) # {'A': 10, 'B': 20, 'C': 30}
print(dict_2) # {'X': -10, 'Y': -20, 'Z': -30}
print(dict_3) # {'M': 1.5, 'N': 2.5, 'O': 3.5}




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 40) Funciones
print('\n\n40) Funciones\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ----------------
# Función Básica
# ----------------

nombre = 'Sebas'
edad = 36
nota = 18.5

print('{} tiene {} años y su nota final es {}'.format(
    nombre, edad, nota
))
# Sebas tiene 36 años y su nota final es 18.5

def presentar_estudiante(a, b, c): # PARÁMETROS
    print('{} tiene {}. Su nota final es = {}'.format(
        a, b, c
    ))
# end def

# => invocar la función
# ARGUMENTOS
presentar_estudiante(nombre, edad, nota) # Sebas tiene 36. Su nota final es = 18.5
presentar_estudiante('Carlos', 15, 19.5) # Carlos tiene 15. Su nota final es = 19.5

# ---------------------
# Parámetros y Retorno
# ---------------------
# - Un función puede o no tener parámetros
# - y puede o no retornar algún valor => keyword 'return'

# ==> sin parámetros / sin retorno
def saludar():
    print('hola')
# end def

saludar() # hola

# ==> con parámetros / sin retorno
def despedirse(nombre):
    print( 'Charo {} !!'.format(nombre) )
# end def

despedirse('Mateo') # Charo Mateo !!


# ==> con parámetros / con retorno
def sumar(a, b):
    return a + b
# end def

sumar(5,6)
print( sumar(5,6) ) # 11
r = sumar(5,6)
print( r ) # 11

# ==> sin parámetros / con retorno
# (no tiene mucho sentido, pero no es error)

def devolver_10():
    return 10
# end def

print( devolver_10() ) # 10


# ---------------------------
# Pueden Redefinirse N veces
# ---------------------------
def sumar(a,b):
    return a + b
# end def

print( sumar(10,15) ) # 25

def sumar(a,b):
    print( a + b + 100 )
# end def

sumar( 1,2 ) # 103


# --------------------------------------------
# Parámetros => Existen solo en las funciones
# --------------------------------------------
# - pueden repetirse
# - pueden tener el mismo nombre que variables creadas afuera
# - no afecta la función

a = 10
b = 20

def multiplicar(a,b):
    return a * b
# end def

def restar(a,b):
    return a-b
# end def


print( a , b ) # 0 20
print( multiplicar(a, b) ) # 200
print( multiplicar(7, 2) ) # 14
print( restar(a, b) ) # -10
print( restar(7, 2) ) # 5


# ---------------------------------------
# pass => definir función y trabar luego
# ---------------------------------------
def calcular_algo(a,b,c,d,e):
    pass
# end def

# -------
# return
# -------
# - marca el fin de la función
# - pueden haber varios, con un condicional

def saludar(nombre, edad):
    return 'Hola {}, tienes {} años!'.format(nombre, edad)
    print('hola de nuevo')
# end def

print( saludar('Dani',20) ) # Hola Dani, tienes 20 años!


def saludar(idioma):
    if idioma.lower() == 'esp':
        return 'buenos días'
    elif idioma.lower() == 'eng':
        return 'good morning'
    else:
        return 'hola!'
# end def

print( saludar('a') ) # hola!
print( saludar('esp') ) # buenos días
print( saludar('ENG') ) # good morning
#print( saludar() ) # TypeError: saludar() missing 1 required positional argument: 'idioma'

# --------------------
# función en función
# --------------------

def doblar_numero(x):
    return x * 2
# end def

def triplicar_numero(x):
    return x * 3
# end def

def presentar_resultados(x):
    print( 'El número doblado es =', doblar_numero(x) )
    print( 'El número triplicado es =', triplicar_numero(x) )
# end def

presentar_resultados(3)

# -----------------------
# parámetros por defecto
# -----------------------

# ==> recordar print + end
# - este end es un parámetro por defecto '\n'
print('Hola')
print('Sebas')
print('Hola', end='-----')
print('Dani')

# ==> podemos definir las nuestras
def que_aprendemos(lenguaje='Python'):
    print('Nosotros aprendemos', lenguaje)
# end def

que_aprendemos() # Nosotros aprendemos Python
que_aprendemos('Física') # Nosotros aprendemos Física

# ==> SIEMPRE al final
def ingredientes_pasta(tipo_pasta, salsa, carne='carne molida', condimento='oregano'):
    print('La pasta tiene: {}, {} y {}'.format(
        tipo_pasta,
        salsa,
        carne,
        condimento
    ))
# end def

ingredientes_pasta('spagethi', 'pesto') # La pasta tiene: spagethi, pesto y carne molida
ingredientes_pasta('spagethi', 'pesto', 'pollo') # La pasta tiene: spagethi, pesto y pollo
ingredientes_pasta('spagethi', 'pesto', 'pollo bbq', 'ajo molido') # La pasta tiene: spagethi, pesto y pollo bbq
ingredientes_pasta('spagethi', 'pesto', condimento='pimienta', carne='bolitas de res') # La pasta tiene: spagethi, pesto y bolitas de res




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 41) Funciones Recursivas
print('\n\n41) Funciones Recurvivas\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - función que se llama a sí misma
# - cualquier cosa que se pueda hacer con una función recursiva
# - se puede hacer con función normal / bucle / condicional
# - CUIDADO: de caer en una función que nunca termina

# -----
# EJ 1
# -----
def conteo_atras(x):
    if x > 0:
        print( '{} segundos para año nuevo!'.format(x) )
        conteo_atras(x-1)
# end def

conteo_atras(5)

# -----
# EJ 2
# -----
# sumatorio(5) = 1+2+3+4+5 = 15

def sumatorio(x):
    if x > 0:
        return x + sumatorio(x-1)
    else:
        return 0
# end def

print( sumatorio(5) ) # 15
print( sumatorio(3) ) # 6

# -----
# EJ 3
# -----
# factorial(5) = 5*4*3*2*1 = 120

def factorial(x):
    if x > 0:
        return x * factorial(x-1)
    else:
        return 1
# end def

print( factorial(5) ) # 120
print( factorial(3) ) # 6

# ==> factorial con funcion normal

def factorial_2(x):
    resultado = 1
    while x > 0:
        resultado *= x
        x -= 1
    # end while
    return resultado
# end def

print( factorial_2(5) ) # 120
print( factorial_2(3) ) # 6




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 42) Scope de Variables
print('\n\n42) Scope de Variables\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# ---------------
# Global y Local
# ---------------
# - global => todo en el código con indentación 0
# - local  => todo lo que está dentro de las funciones
# - 1 sólo ámbito GLOBAL / N ámbitos LOCALES

variable_a = 10 # GLOBAL

def hacer_algo():
    variable_b = 20
    print(variable_b) # LOCAL
# end def

print( variable_a )
#print( variable_b ) # NameError: name 'variable_b' is not defined.

"""
def hacer_algo_mas():
    #print(variable_b) # NameError: name 'variable_b' is not defined.
# end def

#hacer_algo_mas()
"""

# ---------------
# Keyword global
# ---------------

# ==> podemos mostrar una variable global dentro de local
a = 20

def mostrar():
    a
    print(a)
    print(a * 5)
# end def

mostrar()

# ==> NO se puede modificar directamente la variable global dentro de local
# - en el siguiente ejemplo
# - ambas se llaman a
# - pero son distintas, una es global / otra es local

a = 20

def intento_modificar():
    a = 100
    return a
# end def

print(a) # 20
print( intento_modificar() ) # 100

def intento_2(a):
    a = 150
    print(a)
# end def

intento_2(2) # 150
print(a) # 20
intento_2(a) # 150
print(a) # 20


# ==> Se puede modificar con keyword global
a = 30

def cambiar_variable():
    global a
    a += 20
    print('Se cambió el valor a {}'.format(a))
# end def

print(a) # 30
cambiar_variable() # Se cambió el valor a 50
print(a) # 50



# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 43) Funciones *args
print('\n\n43) Funciones *args\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - función con argumentos arbitrarios
# - número indefinido de parámetros
# - que se guardan como tupla

# ----------------
# ¿qué son *args?
# ----------------
def que_son_args(*args):
    print( args , type(args) )
# end def

que_son_args(1,2,3,4) # (1, 2, 3, 4) <class 'tuple'>
    
# ---------------------
# aplicación con *args
# ---------------------
def sumatoria(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    # end for
    return resultado
# end def

print( sumatoria(1,5,6) ) # 12
print( sumatoria(1,2,3,4,5) ) # 15


# ----------------------------------------------
# el nombre args => no es relevante, pero si *
# ----------------------------------------------
def promedio(*numeros):
    resultado = 0
    for valor in numeros:
        resultado += valor
    # end for
    resultado = resultado / len(numeros)
    return resultado
# end def

print( promedio(10,18,15,20) ) # 15.75




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 44) Funciones **kwargs
print('\n\n44) Funciones **kwargs\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - función con argumentos arbitrarios asociados a clave
# - número indeterminado de parámetros
# - asociados a una clave
# - se los puede empacar en un diccionario

# --------------------
# ¿qué son **kwargs?
# --------------------

def que_son_kwargs(**kwargs):
    print( kwargs , type(kwargs) )
# end def

que_son_kwargs(nombre='sebas', edad=36, nota=18.5)
# {'nombre': 'sebas', 'edad': 36, 'nota': 18.5} <class 'dict'>


# ------------------------
# aplicación con **kwargs
# ------------------------
def calculo_nota_final(**kwargs):
    nota_final = kwargs['nota_deberes'] * 0.3 + kwargs['nota_examen'] * 0.7
    print( 'La nota final es de =', nota_final )
# end def

calculo_nota_final( nota_deberes=18, nota_examen=14 ) # La nota final es de = 15.2
calculo_nota_final( nota_deberes=20, nota_examen=11 ) # La nota final es de = 13.7
#calculo_nota_final( nota_deberes=20, nota_examn=11 ) # KeyError: 'nota_examen'

# ------------------------------------------------
# el nombre kwargs => no es relevante, pero si **
# ------------------------------------------------

def describir_persona(**caracteristicas):
    print('Características de Persona:')
    for clave, valor in caracteristicas.items():
        print( '{} : {}'.format(clave, valor) )
    # end for
# end def

describir_persona(
    nombre='Sebas',
    apellido='Silva',
    edad=36,
    profesion='Ing. Mecánico',
    pais='Alemania'
)




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 45) Función Lambda
print('\n\n45) Función Lambda\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - función anónima
# - N argumentos => 1 sola expresión
# - como un "shortcut" => lo usamos luego lo descartamos

# ---------------------------
# Función Normal vs. Lambda
# ---------------------------

# ==> función normal
def suma_normal(a,b):
    return a + b
# end def

# ==> función lambda
suma_lambda = lambda a,b : a + b

print( suma_normal(4,5) ) # 9
print( suma_lambda(2,6) ) # 8


# --------------------------
# Lambda con valores String
# --------------------------
saludar = lambda nombre, edad : 'Hola soy {}, tengo {} años'.format(nombre, edad)

print( saludar('Diego',20) ) # Hola soy Diego, tengo 20 años
print( saludar('Andrea',34) ) # Hola soy Andrea, tengo 34 años


# ------------------------------
# Lambda con Operador Ternario
# ------------------------------

# ==> Recordar: Operador Ternario
edad = 12
mensaje = 'mayor de edad' if edad >= 18 else 'menor de edad'
print(mensaje) # menor de edad

# ==> Lambda + Operador Ternario
check_temperatura = lambda temp : 'Frío' if temp < 10 else 'Buen Clima'
print( check_temperatura(10) ) # Buen Clima
print( check_temperatura(15) ) # Buen Clima
print( check_temperatura(8) ) # Frío


# --------------------------
# Lambda => Función Anónima
# --------------------------
# - lambda puede ser el retorno de una función por ej.

def multiplicador(x):
    return lambda numero : numero * x
# end def

mult_5 = multiplicador(5)
print(mult_5) # <function multiplicador.<locals>.<lambda> at 0x000001A8C8A0A200>

print( mult_5(20) ) # 100

# ==> en 1 sola línea
mult_5_20 = multiplicador(5)(20)
print(mult_5_20) # 100



# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 46) Funciones como Variables
print('\n\n46) Funciones como Variables\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - todo en Python puede ser variable
# - en Python todo es un objeto (POO)

# --------------------
# Función a Variable
# --------------------
def resta(x,y):
    return x - y
# end def

print( resta , type(resta) ) # <function resta at 0x00000235CB5BA2A0> <class 'function'>
print( hex(id(resta)) ) # 0x235cb5ba2a0


# -------------------------------
# Funciones Internas a Variables
# -------------------------------
print('hola mundo')
print( print , type(print) ) # built-in function print> <class 'builtin_function_or_method'>

# ==> puedo asignarle "un nuevo nombre"
imprimir = print

imprimir('hola mundo') # hola mundo




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 47) sorted / map / filter / reduce
print('\n\n47) sorted / map / filter / reduce\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - Funciones muy muy útiles para tratamiento de datos
# - Su fundamento se aplica en otros lenguajes de programación
# - ej: en javascript (programación web)

"""
    sorted => establecer ordenamiento
    map    => transformar una colección por medio de un cálculo
    filter => filtrado de datos de colección
    reduce => reducir grupo de datos a 1 sólo valor
"""



# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 48) sorted()
print('\n\n48) sorted()\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - las mismas nociones que .sort() de listas
# - la diferencia es que no modifica la lista

# -----
# EJ 1
# -----
lista = [20, 15, 8, 90, -5, -50, 20.2]

lista_menor_mayor = sorted(lista)
lista_mayor_menor = sorted(lista, reverse=True)

print( 'lista =', lista ) # lista = [20, 15, 8, 90, -5, -50, 20.2]
print( 'lista_mayor_menor =', lista_mayor_menor ) # lista_mayor_menor = [90, 20.2, 20, 15, 8, -5, -50]       
print( 'lista_menor_mayor =', lista_menor_mayor ) # lista_menor_mayor = [-50, -5, 8, 15, 20, 20.2, 90] 

# -----
# EJ 2
# -----
palabras = ['sol', 'planeta', 'investigacion']

orden_menos_mas = sorted(palabras, key=len)
orden_mas_menos = sorted(palabras, key=len, reverse=True)

print( 'palabras =', palabras ) # palabras = ['sol', 'planeta', 'investigacion']
print( 'orden_menos_mas =', orden_menos_mas ) # orden_menos_mas = ['sol', 'planeta', 'investigacion']    
print( 'orden_mas_menos =', orden_mas_menos ) # orden_mas_menos = ['investigacion', 'planeta', 'sol'] 




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 49) map()
print('\n\n49) map()\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - map( funcion , elementos_iterables )
# - transforma una colección por medio de una función
# - "elementos_iterables" => puede ser más de 1 !!
# - retorna un objeto de tipo map

# ----------------------------------
# Ejemplo Básico con Función Normal
# ----------------------------------
def funcion(x):
    return 3*x - 5
# end def

valores = [-20, 5, 16, -8, 12]
resultado_map = map( funcion , valores )
print( resultado_map , type(resultado_map) ) # <map object at 0x0000025580522590> <class 'map'>

# ==> conveniente hacer casting a lista u otro iterable
resultado = list(resultado_map)
print( resultado , type(resultado) ) # [-65, 10, 43, -29, 31] <class 'list'>

# ----------------------------------
# Ejemplo Básico con Función Lambda
# ----------------------------------
# - ej: notas de 3 alumnos ordenadas en lista
# - nota_final = 0.2*deberes + 0.3*proyecto + 0.5*examen

nota_deberes = [15, 18, 14]
nota_proyecto = [18, 16, 20]
nota_examen = [16, 17, 15]

nota_final_map = map(
    lambda deberes, proyecto, examen : 0.2*deberes + 0.3*proyecto + 0.5*examen,
    nota_deberes,
    nota_proyecto,
    nota_examen
)

nota_final = list(nota_final_map)
print(nota_final) # [16.4, 16.9, 16.3]

# ==> con función normal
def calcular_nota_final(deberes, proyecto, examen):
    return 0.2*deberes + 0.3*proyecto + 0.5*examen
# end def

"""
nota_final_map_2 = map(
    calcular_nota_final,
    nota_deberes,
    nota_proyecto,
    nota_examen
)
nota_final_2 = list(nota_final_map_2)
"""

# ==> se puede hacer todo de 1 sola!!

nota_final_2 = list(map(
    calcular_nota_final,
    nota_deberes,
    nota_proyecto,
    nota_examen
))

print(nota_final_2) # [16.4, 16.9, 16.3]




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 50) filter()
print('\n\n50) filter()\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - filter( funcion , elemento_iterable )
# - la función debe retornar True / False => de acuerdo al criterio de filtrado
# - la función puede ser normal / lambda
# - filter => retorna un objeto de tipo dilter

# ----------------------------------
# Ejemplo Básico con Función Normal
# ----------------------------------
calificaciones = [13, 14, 18, 10, 20, 15, 16, 14, 19, 11]

def notas_altas(nota):
    if nota > 14:
        return True
    else:
        return False
# end def

calificaciones_altas_filter = filter( notas_altas , calificaciones )
print( calificaciones_altas_filter , type(calificaciones_altas_filter) )
# <filter object at 0x000001C8F96E26E0> <class 'filter'> 

# ==> muy conveniente castearlo a un iterable, ej: lista
calificaciones_altas = list(calificaciones_altas_filter)
print(calificaciones_altas) # [18, 20, 15, 16, 19]

# ----------------------------------
# Ejemplo Básico con Función Lambda
# ----------------------------------

calificaciones_bajas = list(filter(
    lambda nota : True if nota <= 14 else False,
    calificaciones
))

print(calificaciones_bajas) # [13, 14, 10, 14, 11]




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 51) reduce()
print('\n\n51) reduce()\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - reduce ( función , elemento_iterable )
# - OJO: para usarlo hay que importar la librería functools !!!
# - reduce los valores de una colección a 1 sólo !
# - puede considerar un valor inicial

# -------------------------------------
# importar módulo / librería functools
# -------------------------------------
import functools

# ----------------
# Ejemplo Básico
# ----------------
compras_usd = [100.50, 200, 85, 15, 20.99]
suma_compras = lambda x , y : x + y
valor_a_pagar = functools.reduce( suma_compras , compras_usd )
print( valor_a_pagar ) # 421.49
# sería lo mismo que:
valor_total_2 = sum(compras_usd)
print(valor_total_2) # 421.49

# ------------------
# Ejemplo Complejo
# ------------------
gastos = [
    ['Empleado','gastos_administrativos' , 'gastos_combustible'],
    ['Sebastián', 20.54 , 15.85],
    ['Ximena', 18.24 , 17.98],
    ['Eduardo', 42.65 , 31.23],
    ['Carlos', 18.78 , 14.36],
    ['Andrea', 50.48 , 16.87],
]

gastos_administrativos_totales = functools.reduce(
    lambda x , y : x + y, # función de suma reduce
    
    list(map( # lista con solo gastos administrativos
        lambda x : x[1],
        gastos[1:]
    ))
)
#print(list(map( lambda x : x[1] , gastos[1:] )))
print(gastos_administrativos_totales, 'USD') # 150.69 USD

gastos_combustible_totales = functools.reduce(
    lambda x , y : x + y, # función de suma reduce
    
    list(map( # lista con solo gastos administrativos
        lambda x : x[2],
        gastos[1:]
    ))
)
print(gastos_combustible_totales, 'USD') # 96.29 USD




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 52) List Comprehension
print('\n\n52) List Comprehension\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - manera corta/dinámica/inteligente de crear una lista
# - se lo puede realizar por medio de 3 sintaxis:

"""
    A) lista = [ expresión + bucle FOR en un iterable ]
    B) lista = [ expresión + bucle FOR en un iterable + condicional IF ]
    C) lista = [ expresión + condicional IF/ELSE + bucle FOR en un ITERABLE ]
"""

# ----------------------------------------------------
# A) lista = [ expresión + bucle FOR en un iterable ]
# ----------------------------------------------------
valores = [10, -50, 62, -5, 22, 15, -9]
resultado_1 = [ 2*x - 5 for x in valores ]
print(resultado_1) # [15, -105, 119, -15, 39, 25, -23] => también se podría usar map

resultado_2 = [ math.sqrt(x) for x in range(1,11) ]
print(resultado_2) # [1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979, 2.449489742783178, 2.6457513110645907, 2.8284271247461903, 3.0, 3.1622776601683795]


# ---------------------------------------------------------------------
# B) lista = [ expresión + bucle FOR en un iterable + condicional IF ]
# ---------------------------------------------------------------------
valores = [10, -50, 62, -5, 22, 15, -9]
resultado = [ 2.5*y - 5/y for y in valores if y > 0 ]
print(resultado) # [24.5, 154.91935483870967, 54.77272727272727, 37.166666666666664]


# --------------------------------------------------------------------------
# C) lista = [ expresión + condicional IF/ELSE + bucle FOR en un ITERABLE ]
# --------------------------------------------------------------------------
valores = [10, -50, 62, -5, 22, 15, -9]
resultado = [ 'positivo' if z > 0 else 'negativo' for z in valores ]
print(resultado) # ['positivo', 'negativo', 'positivo', 'negativo', 'positivo', 'positivo', 'negativo']




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 53) Dictionary Comprehension
print('\n\n53) Dictionary Comprehension\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - manera corta/dinámica/inteligente de crear un diccionario
# - a partir de otro diccionario
# - se lo puede realizar por medio de 4 sintaxis:

"""
    A) dict = {KEY: expresión + bucle FOR (KEY, VALUE) + in + ITERABLE}
    B) dict = {KEY: expresión + bucle FOR (KEY, VALUE) + in + ITERABLE + condicional IF}
    C) dict = {KEY: condicional IF/ELSE + bucle FOR (KEY, VALUE) + in + ITERABLE}
    D) dict = {KEY: función(VALOR) + bucle FOR (KEY, VALUE) + in + ITERABLE}
"""

notas = {
    'Daniel' : 16,
    'Pedro' : 14,
    'Sebastián' : 13,
    'Santiago' : 19,
    'Eduardo' : 11,
    'Rodrigo' : 20,
    'Francisco' : 12,
    'María' : 14,
}

# --------------------------------------------------------------------
# A) dict = {KEY: expresión + bucle FOR (KEY, VALUE) + in + ITERABLE}
# --------------------------------------------------------------------
notas_100 = { key : (value / 20 * 100) for (key, value) in notas.items() }
print(notas_100)
# {'Daniel': 80.0, 'Pedro': 70.0, 'Sebastián': 65.0, 'Santiago': 95.0, 'Eduardo': 55.00000000000001, 'Rodrigo': 100.0, 'Francisco': 60.0, 'María': 70.0}

# ==> key / value, no es importante el nombre!, pero si el orden!
notas_100 = { clave : float('{:.2f}'.format(valor / 20 * 100)) for (clave, valor) in notas.items() }
print(notas_100)
# {'Daniel': 80.0, 'Pedro': 70.0, 'Sebastián': 65.0, 'Santiago': 95.0, 'Eduardo': 55.0, 'Rodrigo': 100.0, 'Francisco': 60.0, 'María': 70.0}


# -------------------------------------------------------------------------------------
# B) dict = {KEY: expresión + bucle FOR (KEY, VALUE) + in + ITERABLE + condicional IF}
# -------------------------------------------------------------------------------------
estudiantes_aprobados = { clave : valor for (clave, valor) in notas.items() if valor > 14 }
estudiantes_no_aprobados = { clave : valor for (clave, valor) in notas.items() if valor <= 14 }

print(estudiantes_aprobados) # {'Daniel': 16, 'Santiago': 19, 'Rodrigo': 20}
print(estudiantes_no_aprobados) # {'Pedro': 14, 'Sebastián': 13, 'Eduardo': 11, 'Francisco': 12, 'María': 14}


# ------------------------------------------------------------------------------
# C) dict = {KEY: condicional IF/ELSE + bucle FOR (KEY, VALUE) + in + ITERABLE}
# ------------------------------------------------------------------------------
aprobado_reprobado = { clave : ('aprobado' if valor > 14 else 'reprobado') for (clave, valor) in notas.items() }
print(aprobado_reprobado)
# {'Daniel': 'aprobado', 'Pedro': 'reprobado', 'Sebastián': 'reprobado', 'Santiago': 'aprobado', 'Eduardo': 'reprobado', 'Rodrigo': 'aprobado', 'Francisco': 'reprobado', 'María': 'reprobado'}


# -------------------------------------------------------------------------
# D) dict = {KEY: función(VALOR) + bucle FOR (KEY, VALUE) + in + ITERABLE}
# -------------------------------------------------------------------------
def check_estudiante(nota):
    if nota > 14 and nota <= 20:
        return 'Aprobado'
    elif nota == 14:
        return 'Supletorio'
    elif nota >= 12 and nota < 14:
        return 'Pierde el Cupo'
    elif nota >= 0 and nota < 12:
        return 'Pierde el Año'
    else:
        return 'ERROR - Nota'
# end def

analisis_estudiante = { clave : check_estudiante(valor) for(clave, valor) in notas.items() }

print(analisis_estudiante)
# {'Daniel': 'Aprobado', 'Pedro': 'Supletorio', 'Sebastián': 'Pierde el Cupo', 'Santiago': 'Aprobado', 'Eduardo': 'Pierde el Año', 'Rodrigo': 'Aprobado', 'Francisco': 'Pierde el Cupo', 'María': 'Supletorio'}




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 54) Función Interna - zip
print('\n\n54) Función Interna - zip\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - empaca 2 o + iterables en un objeto tipo zip
# - el iterable de menor tamaño decide el tamaño del zip
# - básicamente se unen los valores en una tupla

# ---------------
# Ejemplo Básico
# ---------------
l1 = ['A', 'B', 'C']
l2 = [100, 200, 300]

zip_l1_l2 = zip(l1, l2)
print(zip_l1_l2) # <zip object at 0x0000017728147440>

# ==> más sentido transformarlo a un iterable conocido
resultado_zip = list(zip_l1_l2)
print(resultado_zip) # [('A', 100), ('B', 200), ('C', 300)]

# --------------------------------------------------------
# N iterables / el de menor tamaño decide el tamaño final
# --------------------------------------------------------
iter_1 = ['A', 'B', 'C']
iter_2 = [100, 200, 300]
iter_3 = ('USA', 'ECU', 'DEU', 'JPN')

resultado_zip = zip(iter_1, iter_2, iter_3)
resultado_final = tuple( resultado_zip )

print( resultado_final ) # (('A', 100, 'USA'), ('B', 200, 'ECU'), ('C', 300, 'DEU'))




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 55) Librería Time
print('\n\n55) Librería Time\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - una opción para trabajar fecha y hora en Python => PERO no la más recomendable
# - crea fechas en función de la hora cero (EPOCH)
# - la hora cero (EPOCH) de la computadora se considera el 1 de enero de 1970
# - útil para crear estampas de tiempo y sleep !!!
# - para fechas / horas => veremos la librería datetime !!!

# ------------------------------
# importación de librería time
# ------------------------------
import time

# -----------
# punto cero
# -----------
print( time.ctime(0) ) # Thu Jan  1 01:00:00 1970

# ------------------------------------
# milisegundos a partir del tiempo 0
# ------------------------------------
# - desde el punto 0
# - hasta el preciso momento de ejecución de este script
print( time.time() ) # 1701018544.838476

# -------------
# fecha actual
# -------------
# - en el preciso momento de ejecución del script
print( time.ctime( time.time() ) ) # Sun Nov 26 18:10:21 2023

# ---------------------------------------
# aplicación útil => estampas de tiempo
# ---------------------------------------
# - crear una identificación única para algún dato
lista_estudiantes = [
    'Carlos', 'Ana', 'Diego', 'Ximena', 'Adri', 'Sebas', 'Marcelo'
]

identificacion_unica = []

for estudiante in lista_estudiantes:
    identificacion_unica.append( round(time.time() * random.random()) )
# end for

#print(identificacion_unica)

id_estudiante = zip(identificacion_unica , lista_estudiantes)
tupla_id_estudiante = tuple(id_estudiante)

for elemento in tupla_id_estudiante:
    print(elemento)
# end for

# -------------
# time.sleep()
# -------------
"""
contador = 5

while contador > 0:
    print( 'Quedan {} segundos para año nuevo!'.format(contador) )
    contador -= 1
    time.sleep(1)
else:
    print('Feliz año nuevo!!!')
# end while
"""


# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 56) Librería datetime
print('\n\n56) Librería datetime\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - la librería / módulo adecuado para trabajar hora y fecha

# ---------------------------------------------
# importación de la librería / módulo datetime
# ---------------------------------------------
import datetime

# -------------
# fecha actual
# -------------
# - al momento de ejecución del script !!
# - retorna un objeto del tipo "datetime.datetime"
fecha_actual = datetime.datetime.now()
print( fecha_actual , type(fecha_actual) ) # 2023-11-26 19:42:44.708292 <class 'datetime.datetime'>

# -----------------------------------
# acceso a los elementos de datetime
# -----------------------------------
# - OJO: no son métodos
# - son atributos / propiedades del objeto (teoría de POO)
# - en pocas palabras => no usar los paréntesis al final

"""
Elemento de Acceso          |  Manera de Acceder
-----------------------------------------------------------
acceder al año              |  fecha_datetime.year 
acceder al mes              |  fecha_datetime.month 
acceder al día              |  fecha_datetime.day 
acceder a la hora           |  fecha_datetime.hour
acceder a los minutos       |  fecha_datetime.minute
acceder a los segundos      |  fecha_datetime.second
acceder a los microsegundos |  fecha_datetime.microsecond
"""

print(fecha_actual.year) # 2023
print(fecha_actual.month) # 11
print(fecha_actual.hour) # 19

# ------------------------------
# creando fechas personalizadas
# ------------------------------
# - de 2 maneras
#   a) tupla de 3 valores (año, mes, día)
#   b) tupla de 6 valores (año, mes, día, hora, minutos, segundos)

fecha_1 = datetime.datetime(2001,7,20)
fecha_2 = datetime.datetime(2025,12,19,19,51,25)

print(fecha_1) # 2001-07-20 00:00:00
print(fecha_2) # 2025-12-19 19:51:25

# -----------------------------
# formato personalizado fácil
# -----------------------------
# - hay muchas maneras de complicarse aquí
# - pero como breve introducción aprenderemos una manera muy fácil

fecha_actual = datetime.datetime.now()
print(fecha_actual)

formato_personalizado = '{}/{}/{} - {}h:{}m:{}s'.format(
    fecha_actual.year,
    fecha_actual.month,
    fecha_actual.day,
    fecha_actual.hour,
    fecha_actual.minute,
    fecha_actual.second
)

print(formato_personalizado) # 2023/11/26 - 19h:53m:39s

# ---------------------
# reloj en tiempo real
# ---------------------
"""
def imprimir_reloj_tiempo_real():
    hoy = datetime.datetime.now()
    print('{}/{}/{} - {}h:{}m:{}s'.format(
        hoy.year,
        hoy.month,
        hoy.day,
        hoy.hour,
        hoy.minute,
        hoy.second
    ))
# end def

while True:
    imprimir_reloj_tiempo_real()
    time.sleep(1)
# end while
"""




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 57) keywords as / from
print('\n\n57) keyword as / from\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - as   ==> para redefinir el nombre de una librería módulo
# - from ==> para importar algo específico de un módulo

"""
import random as r
import datetime as dt

print( r.random() ) # 0.7889372068450233
print( dt.datetime.now() ) # 2023-11-26 20:03:57.858369

from math import cos
print( cos(3.1416 / 3) ) # 0.4999978792725457

from math import pi as constante_pi, sin as seno, cos as coseno
print( coseno( constante_pi / 6 ) ) # 0.8660254037844387
print( seno( constante_pi / 6 ) ) # 0.49999999999999994
"""




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 58) Operador Walrus :=
print('\n\n58) Operador Walrus :=\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - a partir de python 3.8 >
# - asignador de expresión
# - asignar variables dentro de alguna función / expresión

# ---------------
# Ejemplo Básico
# ---------------
nombre = 'Sebas'
print( nombre ) # Sebas

print( nombre_completo := 'Sebas Silva' )
print( nombre_completo )

# ---------------------
# Ejemplo más complejo
# ---------------------

# ==> sin walrus :=
"""
ingredientes = []
opcion_user = ''

print('Lista de Ingredientes para una Receta:')
while opcion_user != 'salir':
    opcion_user = input('Ingrese un Ingrediente : ')
    ingredientes.append(opcion_user)
else:
    ingredientes.pop()

print( ingredientes )
"""

# ==> con walrus :=
"""
ingredientes = []

print('Lista de Ingredientes para una Receta:')
while ( opcion_user := input('Ingrese un Ingrediente : ') ) != 'salir':
    ingredientes.append(opcion_user)
# end while

print(ingredientes)
"""




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 59) Gestión de Errores => try-except
print('\n\n59) Gestión de Errores => try-except\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# - errores en programación hay básicamente 2
#   a) errores de sintaxis => algo escribimos mal (lo detecta el editor de código)
#   b) errores de ejecución => todo bien escrito, pero algo usamos mal
# - ambos paran la ejecución del programa
# - try-except => para capturar el error y gestionarlo
# - raise => para definir un error personalizado

# ------------------
# Error de Sintaxis
# ------------------
print('hola')
#pint('hola') # NameError: name 'pint' is not defined. Did you mean: 'print'?

# -------------------
# Error de Ejecución
# -------------------
lista = ['a','b','c']
print( lista[0] )
#print( lista[5] ) # IndexError: list index out of range

#resultado = 5/0 # ZeroDivisionError: division by zero

print('si llego aquí no hay error')

# ------------------
# try-except Básico
# ------------------
# - try => alberga el código peligroso que puede causar error
# - except => presenta el error sin parar la ejecución del programa
print()

try:
    print( 5/0 )
except:
    print('ERROR - algo salió mal')
# end try-except

print('si llego aquí el error no ha parado el programa')

# ------------------
# Mostrando el error
# ------------------
# - usando Exception y un alias
print()

try:
    print( 5/0 )
except Exception as e:
    print('ERROR - algo salió mal |', e)
# end try-except

print('si llego aquí el error no ha parado el programa')

# ---------------------------------------------
# Estructura Completa: try-except-else-finally
# ---------------------------------------------
"""
try:     aquí va el código que tiene el riesgo de producir error
except:  bloque que se ejecuta en caso de error sin interrumpir el flujo del programa
else:    bloque que se ejecuta cuando no se da error
finally: bloque que se ejecuta SIEMPRE, haya error o no
"""

def dividir(a,b):
    try:
        resultado = a/b
    except Exception as e:
        print( 'ERROR | Lo siento, pero algo salió mal |', e )
    else:
        print( 'Operación con ÉXITO | RESULTADO => {}/{} = {:.2f}'.format(a,b,resultado) )
    finally:
        print( 'FIN DEL MÉTODO DIVIDIR' )
    # end try-except
# end def

print('\nTEST')
dividir(5,0)
dividir(5,2)
dividir(5,'a')

# -----------------
# type(e).__name__
# -----------------
# - devuelve el tipo del error

def dividir(a,b):
    try:
        resultado = a/b
    except Exception as e:
        print( 'ERROR | Lo siento, pero algo salió mal |', e, '|', type(e).__name__ )
    else:
        print( 'Operación con ÉXITO | RESULTADO => {}/{} = {:.2f}'.format(a,b,resultado) )
    finally:
        print( 'FIN DEL MÉTODO DIVIDIR' )
    # end try-except
# end def

print('\nTEST')
dividir(5,0) # ZeroDivisionError
dividir(5,2)
dividir(5,'a') # TypeError

# ---------------------------------
# Capturar Excepciones Específicas
# ---------------------------------

def dividir(a,b):
    try:
        resultado = a/b
    except TypeError as e:
        print( type(e).__name__ , '||' , e  )
        print('ERROR - Por favor ingrese un número !')
    except ZeroDivisionError as e:
        print( type(e).__name__ , '||' , e  )
        print('ERROR - La división para CERO no existe !')
    except Exception as e: # de manera general
        print( type(e).__name__ , '||' , e  )
        print('ERROR - La división no es posible...')
    else:
        print( 'Operación con ÉXITO | RESULTADO => {}/{} = {:.2f}'.format(a,b,resultado) )
    finally:
        print( 'FIN DEL MÉTODO DIVIDIR' )
    # end try-except
# end def

print('\nTEST')
dividir(5,0) # ZeroDivisionError
dividir(5,2)
dividir(5,'a') # TypeError

# --------------------------------
# Generar Errores Personalizados
# --------------------------------
# - raise => invocamos un error
# - OJO: debemos capturarlo, caso contrario, se para la ejecución del programa


# ==> definición de una función sencilla
def saludar(nombre):
    print('Hola', nombre)
# end def

saludar('Carlos') # Hola Carlos
saludar('123') # Hola 123


# ==> prohibiendo al usuario poner números en el nombre
def saludar(nombre):
    if nombre.isalpha():
        print('Hola', nombre)
    else:
        print('ERROR')
# end def

print('\nTEST')
saludar('Carlos') # Hola Carlos
saludar('123') # ERROR
saludar('') # ERROR


# ==> utilizando raise
def saludar(nombre):
    if nombre.isalpha():
        print('Hola', nombre)
    else:
        raise Exception('ERROR - El nombre solo puede contener letras')
# end def

saludar('Carlos') # Hola Carlos
#saludar('123') # Exception: ERROR - El nombre solo puede contener letras 
#saludar('') # ERROR


# ==> raise + try-except
def saludar(nombre):
    try:
        if nombre.isalpha():
            print('Hola', nombre)
        else:
            raise Exception('ERROR - El nombre solo puede contener letras')
    except Exception as e: # el mensaje que definimos arriba !
        print( type(e).__name__, '||', e )
# end def

print('\nTEST')
saludar('Carlos') # Hola Carlos
saludar('123') # Exception || ERROR - El nombre solo puede contener letras
saludar('') # Exception || ERROR - El nombre solo puede contener letra




# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 60) Breve Introducción a numpy
print('\n\n60) Breve Introducción a numpy\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

# -----------------
# ¿Por qué numpy?
# -----------------
lista_1 = [10, 20, 30]
lista_2 = [5, 6, 7]

resultado = lista_1 + lista_2
print(resultado) # [10, 20, 30, 5, 6, 7]





# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
# 61) Breve Introducción a Matplot
print('\n\n61) Breve Introducción a Matplot\n')
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡