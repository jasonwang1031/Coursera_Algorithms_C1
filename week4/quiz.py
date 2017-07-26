import copy  
import random  


def ImportGraph(graph):
    # Import a graph through a text file of adjacency list
    v = open(graph,'r')  
    GraphDict = {}  
    for line in v.readlines():  
        vertex=[int(x) for x in line.split()]  
        GraphDict[vertex[0]]=set(vertex[1:])  
    v.close()  
    return GraphDict


def RandomContract(Graph,EdgeList):  
    # use Random Contract algorithm to find the minimum cut
    while len(Graph)>2:  
        [u,v]=EdgeList.pop(random.randrange(0,len(EdgeList)-1))  
        while([v,u] in EdgeList):  
            EdgeList.remove([v,u])  
        while([u,v] in EdgeList):  
            EdgeList.remove([u,v])  
        for ind in range(0,len(EdgeList)):  
            if EdgeList[ind][0]==v:
                EdgeList[ind][0]=u  
            if EdgeList[ind][1]==v:
                EdgeList[ind][1]=u  
        Graph[u]=Graph[u]-{v}  
        Graph[v]=Graph[v]-{u}  
        for [x,y] in Graph.items():  
            if v in y:  
                Graph[x]=(Graph[x]|{u})-{v}  
        Graph[u]=Graph[u]|Graph[v]  
        del Graph[v]    
    return (len(EdgeList)/2)
  


if __name__ == '__main__':

    Graph = ImportGraph("quiz.txt")

    EdgeList=[]  
    for [x,y] in Graph.items():  
        EdgeList.extend([[x,v] for v in y])  
      
    CountList=[]  
    for i in range(199):  
        GraphCopy=copy.deepcopy(Graph)  
        EdgeListCopy=copy.deepcopy(EdgeList)  
          
        #print cpmapDict  
        num=RandomContract(GraphCopy,EdgeListCopy)  
        CountList.append(num)  
        i+=1
    Minimum = min(CountList)  
    print ("the minimum cut is %d")%Minimum