# Control Ini
  
Control de Archivos .ini  
  

  
![banner](imgs/Banner_ControlIni.png)

## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



## Descripción de los comandos

### Nuevo Ini
  
Crea un archivo ini.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta donde se ubicará el archivo|Ruta donde se ubicará el archivo ini creado.|C:/Users/usuario/Desktop|
|Nombre del archivo ini|Nombre del archivo ini que se creará.|Nombre del archivo ini|

### Leer Ini
  
Abre y lee el archivo ini.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo ini|Ruta del archivo ini que se leerá|C:/Users/User/Desktop/archivo.ini|
|Variable|Variable donde se almacenará el resultado de la operación|resultado|

### Obtener Dato
  
Obtiene el dato segun la seccion y lo envia a la variable.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Seccion|Seccion donde se encuentra el dato que deseamos obtener|Seccion donde se encutra el dato. Por ejemplo: [SECTION]|
|Variable|Variable donde se almacenará el resultado de la operación|resultado|

### Modificar Dato
  
Modifica un dato y una seccion indicada.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Seccion|Seccion donde se encuentra el dato a modificar.|Seccion donde se encutra el dato. Por ejemplo: [SECTION]|
|Dato|Nombre del dato a modificar.|Nombre de el dato en el Ini. Por ejemplo: nombre=|
|Contenido|Contenido nuevo que tendrá el dato del ini.|Contenido de la variable.|

### Añadir Dato
  
Añade un dato en una seccion indicada.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Seccion|Seccion donde se encuentra el dato en el archivo ini.|Seccion donde se encuentra el dato. Por ejemplo: [SECTION]|
|Dato|Nombre del dato en el archivo ini.|Nombre del dato en el Ini. Por ejemplo: nombre=|
|Contenido|Contenido de la variable que se agregará al archivo ini.|Contenido de la variable.|
