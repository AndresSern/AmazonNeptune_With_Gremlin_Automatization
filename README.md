# REQUIREMENTS TO RUN THIS SCRIPT

### REQUIRIMIENTOS PARA CORRER ESTA SCRIPT

<ol>
<li >Ejecutar la primera celda donde se encuentra el codigo <b><code>pip install xlrd==1.2.0</code></b> para instalar el modulo llamado xlrd con la version 1.2.0, y reiniciar el Kernel de notebook Jupyter <br></li><br>
    
<li> Ejecutar la segunda celda para correr las funciones <b>creatingVertex y creatingEdge</b> </li><br>
    
<li> En la tercera celda ubicar la variable "neptuneEndpoint" e inizializarla con la url de tu base de datos Neptune, como en este ejemplo <code>"database-andres-instance-1.cayvc4hmpdyd.us-east-1.neptune.amazonaws.com"</code>(debe ir entre comillas la url de tu base de datos), debes asegurarte que la instancia de tu base de datos tengo el permiso de escritura </li><br>

<li> Debe estar el archivo llamado <b>"Matriz_de_adyacencia_data_team.xlsx"</b>, este debe estar ubicado en el <b>root de tu notebook Jupyter</b>, al igual que debe estar esta script</li><br>

<li> Si cumpliste los dos pasos anterios puedes ejecutar la tercera celda de esta script para crear los <b>vertex y los edges</b>, estos se crean con <b>query de Gremlin con python</b></li><br>

<li> En la cuarta celda donde esta ubicada <code>"your-neptune-enpoint"</code> debe ser remplazado pero el url de tu base de datos Neptune,(debe ir entre comillas la url de tu base de datos), asegurate que sea la misma url que insertaste en el primer paso</li><br>

<li> Si cumpliste el paso anterior puedes ejecutar la cuarta celda para la configuración, si aparecio <b>un error ejecutando esta celda</b>, guarda los cambios que has hecho, cierra el archivo y vuelve a ingresar, esto pasa porque se debe encender el archivo en notebook para poder ejecutar los comandos de gremlin</li><br>

<li> Si cumpliste todos los pasos anteriores correctamente, ejecuta la ultima celda para visualizar el grafico con los datos que han sido ingresados en la base de datos</li><br>
</ol>
