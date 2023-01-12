# coding: utf-8
# pylint: disable=invalid-name
"""Base para desarrollo de modulos externos.

Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")

Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    pip install <package> -t .

"""
import configparser

global MOD_CONTROLL_INI #pylint: disable=global-at-module-level
# global config
# global configOpen
# global ruta

GetParams = GetParams #pylint: disable=undefined-variable,self-assigning-variable
SetVar = SetVar #pylint: disable=undefined-variable,self-assigning-variable
PrintException = PrintException #pylint: disable=undefined-variable,self-assigning-variable

try:
    if not MOD_CONTROLL_INI: #pylint: disable=used-before-assignment
        MOD_CONTROLL_INI = {}
except NameError:
    MOD_CONTROLL_INI = {}





#Obtengo el modulo que fueron invocados

module = GetParams("module")

"""
    Resuelvo catpcha tipo reCaptchav2
"""
if module == "leerIni":
    # Modulo Leer ini
    ruta = GetParams('content')
    variable = GetParams('variable')
    try:
        MOD_CONTROLL_INI["ruta"] = ruta
        MOD_CONTROLL_INI["config"] = configparser.ConfigParser()
        MOD_CONTROLL_INI["config"].read(ruta)
        SetVar(variable, True)
    except Exception as e:
        PrintException()
        SetVar(variable, False)
        raise e

if module == "obtenerDato":
    # Modulo Obtener Dato
    seccion = GetParams('idseccion')
    dato = GetParams('iddato')
    var = GetParams('idvar')

    config = MOD_CONTROLL_INI["config"]
    obtenido = config[seccion][dato]
    SetVar(var, obtenido)

if module == "anadirDato":
    # Modulo Añadir dato
    config = MOD_CONTROLL_INI["config"]
    ruta = MOD_CONTROLL_INI["ruta"]
    secciones = config.sections()

    seccion = GetParams('idseccion')
    dato = GetParams('iddato')
    contenido = GetParams('idcontent')

    if seccion == "DEFAULT":
        config.set(seccion, dato, contenido)
        with open(ruta, 'w', encoding='latin-1') as configfile:
            config.write(configfile)
    else:
        if seccion in secciones:
            # Tiene esta seccion
            config.set(seccion, dato, contenido)
            with open(ruta, 'w', encoding='latin-1') as configfile:
                config.write(configfile)
        else:
            # NO Tiene esta seccion, se va a crear
            config = configparser.RawConfigParser()
            config.add_section(seccion)
            config.set(seccion, dato, contenido)
            with open(ruta, 'a', encoding='latin-1') as configfile:
                config.write(configfile)

if module == "modificaDato":
    # Modulo que modifica un dato en la Varible del Ini
    seccion = GetParams('idseccion')
    dato = GetParams('iddato')
    contenido = GetParams('idcontent')

    config.set(seccion, dato, contenido)
    with open(ruta, 'w', encoding='latin-1') as configfile:
        config.write(configfile)

if module == "nuevoIni":
    # Modulo que crea un nuevo Ini
    nombreini = GetParams('idnombreini')
    ruta = GetParams('content')

    archivo = ruta+"\\"+ nombreini+".ini"

    config = configparser.ConfigParser()
    config['DEFAULT'] = {}
    with open(archivo, 'w', encoding='latin-1') as configfile:
        config.write(configfile)
