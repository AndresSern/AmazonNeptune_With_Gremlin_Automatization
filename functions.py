def creatingVertex(data):
    for index,row in data.iterrows():
        g.addV('PERSONA').\
        property(T.id,str(row["id"])).\
        property("name",row["name"]).\
        property("nickname", row["nickname"]).next()

def creatingEdge(checkUnion):
    for indexRow, row in enumerate(checkUnion):
        if not True in row:
            continue
        for indexColumn, column in enumerate(row):
            if column == True:
                client= g.V(str(int(indexRow + 1))).toList()[0]
                finalClient = g.V(str(int(indexColumn + 1))).toList()[0]
                
                g.V(client).addE('PERSONA').to(finalClient).property('weight',0.75).iterate()