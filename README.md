#  REQUIREMENTS TO RUN THIS SCRIPT

<ol>
1. Run the first cell where the code <b><code>pip install xlrd==1.2.0</code></b> is located to install the module called xlrd with version 1.2.0, and restart the Jupyter notebook kernel<br></li><br> <li>Run the second cell to run the functions <b>creatingVertex and creatingEdge</b> </li><br> <li>CreatingVertex and creatingEdge</b> </li><br>.
    
2. Run the second cell to run the <b>creatingVertex and creatingEdge</b> </li><br> functions.
    
3. In the third cell locate the variable "neptuneEndpoint" and initialize it with the url of your Neptune database, as in this example <code>"database-andres-instance-1.cayvc4hmpdyd.us-east-1.neptune.amazonaws.com"</code>(must be in quotes the url of your database), you must ensure that your database instance has write permission </li><br>.

3. You must be the file called <b>"Matriz_de_adyacencia_data_team.xlsx"</b>, this must be located in the <b>root of your Jupyter notebook</b>, as must be this script</li><br>.

4. If you completed the two previous steps you can run the third cell of this script to create the <b>vertex and edges</b>, these are created with <b>Gremlin query with python</b></b></li><br>.

5. In the fourth cell where is located <code>"your-neptune-enpoint"</code> must be replaced but the url of your Neptune database, (must be in quotes the url of your database), make sure it is the same url that you inserted in the first step</li><br>.

6. If you completed the previous step you can run the fourth cell for the configuration, if <b>an error appeared running this cell</b>, save the changes you have made, close the file and re-enter, this happens because you must turn on the file in notebook to run the gremlin commands</li><br>.

7. If you completed all the above steps correctly, run the last cell to display the graph with the data that has been entered into the database</li><br>.
</ol>
