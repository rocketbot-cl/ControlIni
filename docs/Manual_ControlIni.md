# Control Ini
  
Controle de arquivos .ini 

*Read this in other languages: [English](Manual_ControlIni.md.md), [Portugues](Manual_ControlIni.pr.md), [Español](Manual_ControlIni.es.md).*
  
![banner](imgs/Banner_ControlIni.png)

## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



## Description of the commands

### New Ini
  
create the ini file.
|Parameters|Description|example|
| --- | --- | --- |
|Path where the file will be located|Path where the created ini file will be located.|C:/Users/user/Desktop|
|Name Ini file|Name of the ini file that will be created.|Ini file name|

### Read Ini
  
Open and read the ini file.
|Parameters|Description|example|
| --- | --- | --- |
|Path of the ini file|Path of the ini file that will be read|C:/Users/User/Desktop/file.ini|
|Variable|Variable where the result of the operation will be stored|result|

### Get Data
  
Get Data. Get the data according to the section and send it to the variable.
|Parameters|Description|example|
| --- | --- | --- |
|Section|Section where the data we want to obtain is located|Section where the data is entered. For example: [SECTION]|
|Variable|Variable where the result of the operation will be stored|result|

### Edit Data
  
Edit a data and a section indicated.
|Parameters|Description|example|
| --- | --- | --- |
|Section|Section where the data to be modified is located.|Section where the data is entered. For example: [SECTION]|
|Data|Name of the data to modify.|Name of the data in the Ini. For example: name=|
|Content|New content that the ini data will have.|Content of the variable.|

### Add Data
  
Add a data in a section indicated.
|Parameters|Description|example|
| --- | --- | --- |
|Section|Section where the data is in the ini file.|Section where the data is. For example: [SECTION]|
|Data|Name of the data in the ini file.|Name of the data in the Ini. For example: name=|
|Content|Content of the variable that will be added to the ini file.|Content of the variable.|
