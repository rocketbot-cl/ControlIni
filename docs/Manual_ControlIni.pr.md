# Control Ini
  
Controle de arquivos .ini  
  
*Read this in other languages: [English](Manual_ControlIni.md.md), [Portugues](Manual_ControlIni.pr.md), [Español](Manual_ControlIni.es.md).*
  
![banner](imgs/Banner_ControlIni.png)

## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot  



## Descrição do comando

### Novo Ini
  
Cria um arquivo ini.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho onde o arquivo será localizado|Caminho onde o arquivo ini criado será localizado.|C:/Users/usuario/Desktop|
|Nome do arquivo ini|Nome do arquivo ini que será criado.|Nome do arquivo ini|

### Ler Ini
  
Abre e lê o arquivo ini.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho do arquivo ini|Caminho do arquivo ini que será lido|C:/Users/User/Desktop/arquivo.ini|
|Variável|Variável onde o resultado da operação será armazenado|resultado|

### Obter Dado
  
Obter o dado de acordo com a seção e enviá-lo para a variável.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Seção|Seção onde os dados que desejamos obter estão localizados|Seção onde os dados são inseridos. Por exemplo: [SECTION]|
|Variável|Variável onde o resultado da operação será armazenado|resultado|

### Editar Dado
  
Edita um dado e uma seção indicada.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Seção|Seção onde os dados a serem modificados estão localizados.|Seção onde os dados são inseridos. Por exemplo: [SECTION]|
|Dado|Nome dos dados a serem modificados.|Nome do dado no Ini. Por exemplo: nome=|
|Conteúdo|Novo conteúdo que o dado do ini terá.|Conteúdo da variável.|

### Adicionar Dado
  
Adiciona um dado em uma seção indicada.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Seção|Seção onde o dado está no arquivo ini.|Seção onde o dado está. Por exemplo: [SECTION]|
|Dado|Nome do dado no arquivo ini.|Nome do dado no Ini. Por exemplo: nome=|
|Conteúdo|Conteúdo da variável que será adicionada ao arquivo ini.|Conteúdo da variável.|
