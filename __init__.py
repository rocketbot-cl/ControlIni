# coding: utf-8
"""
Base para desarrollo de modulos externos.
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
global config
global configOpen
global ruta

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

"""
    Resuelvo catpcha tipo reCaptchav2
"""
if module == "leerIni":
    # Modulo Leer ini
    ruta = GetParams('content')
    variable = GetParams('variable')
    try:
        config = configparser.ConfigParser()
        configOpen = config.read(ruta)
        SetVar(variable, True)
    except:
        PrintException()
        SetVar(variable, False)
        raise Exception("Error al leer el archivo")

if module == "obtenerDato":
    # Modulo Obtener Dato
    seccion = GetParams('idseccion')
    dato = GetParams('iddato')
    var = GetParams('idvar')

    print(config)
    obtenido = config[seccion][dato]
    SetVar(var, obtenido)

if module == "anadirDato":
    # Modulo Añadir dato
    secciones = config.sections()
    seccion = GetParams('idseccion')
    dato = GetParams('iddato')
    contenido = GetParams('idcontent')

    print(secciones)

    if seccion == "DEFAULT":
        config.set(seccion, dato, contenido)
        with open(ruta, 'w') as configfile:
            config.write(configfile)
    else:
        if seccion in secciones:
            # Tiene esta seccion
            config.set(seccion, dato, contenido)
            with open(ruta, 'w') as configfile:
                config.write(configfile)
        else:
            # NO Tiene esta seccion, se va a crear
            config = configparser.RawConfigParser()
            config.add_section(seccion)
            config.set(seccion, dato, contenido)
            with open(ruta, 'a') as configfile:
                config.write(configfile)

if module == "modificaDato":
    # Modulo que modifica un dato en la Varible del Ini
    seccion = GetParams('idseccion')
    dato = GetParams('iddato')
    contenido = GetParams('idcontent')

    config.set(seccion, dato, contenido)
    with open(ruta, 'w') as configfile:
        config.write(configfile)

if module == "nuevoIni":
    # Modulo que crea un nuevo Ini
    nombreini = GetParams('idnombreini')
    ruta = GetParams('content')

    archivo = ruta+"\\"+ nombreini+".ini"

    config = configparser.ConfigParser()
    config['DEFAULT'] = {}
    with open(archivo, 'w') as configfile:
        config.write(configfile)