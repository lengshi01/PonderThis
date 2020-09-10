#import numpy as np
dataset = [
    111100001110001101011101110111000000, 111100001011010110101001111011100101,
    111100001110010101101110110111100101, 111100001111000101011101110111100101,
    111100001110010011101010110111100101, 111100001010011110011011011110100010,
    111100001010011110101011101011001000, 111100001010101110011010111110001000,
    111100001010110110011101011111000101, 111100001010110110101100111111000101,
    111100001110100101011101110111000101, 111100001111000100111101110111000101,
    111100001010110110101010111011001000, 111100001010101110110010111011001000,
    111100001110001110011101111111000000
]

#print(dataset[1][1])

def generateRelationMap(data,dimension):
    dataStr=str(data)
    index=0
    RelationMap = [[0 for x in range(dimension)] for x in range(dimension)] 
    for i in range(dimension):
        for j in range(i+1,dimension):
            entry=int(dataStr[index])
            #print(index,entry)
            RelationMap[i][j]=entry
            RelationMap[j][i]=1-entry
            index+=1
    return RelationMap

def generate3cycleSet(RelationMap):
    dimension=len(RelationMap)
    cycleSet=[]
    for i in range(dimension):
        for j in range(i):
            for k in range(j):
                if RelationMap[i][j]==1 and RelationMap[j][k]==1 and RelationMap[k][i]==1:
                    cycleSet.append([i,j,k])
                if RelationMap[i][j]==0 and RelationMap[j][k]==0 and RelationMap[k][i]==0:
                    cycleSet.append([k,j,i])
    return cycleSet


def generateEdgeProfile(cycleSet,dimension):
    edgeProfile=[[0 for x in range(dimension)] for x in range(dimension)]
    for cycle in cycleSet:
        edgeProfile[cycle[1]][cycle[0]]+=1
        edgeProfile[cycle[2]][cycle[1]]+=1
        edgeProfile[cycle[2]][cycle[0]]+=1
        
        edgeProfile[cycle[0]][cycle[1]]+=1
        edgeProfile[cycle[1]][cycle[2]]+=1
        edgeProfile[cycle[0]][cycle[2]]+=1
    return edgeProfile

def generateProfile(cycleSet,edgeProfile):
    profile=[]
    dimension=len(edgeProfile)
    for i in range(dimension):
        profileOfVertice=[]
        for cycle in cycleSet:
            if i in cycle:
                ind=cycle.index(i)
                np=cycle[(ind+1)%3]
                pp=cycle[(ind+2)%3]
                profileOfVertice.append([edgeProfile[i][np],edgeProfile[np][pp],edgeProfile[pp][i]])
        profile.append(profileOfVertice)
    return profile

for i in range(15):
  RelationMap=generateRelationMap(dataset[i],9)
  cycleSet=generate3cycleSet(RelationMap)
  print(len(cycleSet))
  edgeProfile=generateEdgeProfile(cycleSet,len(RelationMap))
  #print(edgeProfile)
  profile=generateProfile(cycleSet,edgeProfile)

  for vertice in profile:
    print(vertice)
  print("next one")


