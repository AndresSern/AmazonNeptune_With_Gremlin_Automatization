from __future__  import print_function  # Python 2/3 compatibility
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.traversal import T
import pandas as pd

graph = Graph()

neptuneEndpoint="your-neptune-endpoint"
remoteConn = DriverRemoteConnection(f'wss://{neptuneEndpoint}:8182/gremlin','g')
g = graph.traversal().withRemote(remoteConn)

namesHeader = ["nickname", "id", "name"]
fileXLSX = "./Matriz_de_adyacencia_data_team.xlsx"

checkFile= False

try:
    listaDeActores = pd.read_excel(fileXLSX, "Lista de actores", header=2, names=namesHeader)
    matrizDeAdyacencia = pd.read_excel(fileXLSX, "Matriz de adyacencia", header=1)
    
    checkFile = True
    
except FileNotFoundError:
    checkFile = False

if checkFile:
    checkUnion = (matrizDeAdyacencia.values > 0 ).tolist()

    g.V().drop().iterate()

    creatingVertex(listaDeActores)
    creatingEdge(checkUnion)

    print(g.V().limit(100).toList()) # Showing all Vertex with the Id
    print(g.V().count().next()) # Showing the number of vertices 
    print(g.V().outE().elementMap().toList()) # Showing all the edges

else:
    print(f"The File called {fileXLSX} Doen't Exist ")

remoteConn.close()