class WeightPath:
    def CreateWeightPath(nodeWeight):
        import numpy as np
        weight=[]
        for i in range(len(nodeWeight)-1):
            weight.append([])
            for j in range(len(nodeWeight[i])):
                weight[i].append([])
                for k in range(len(nodeWeight[i+1])-1):
                    weight[i][j].append(np.random.random())
                if i==(len(nodeWeight)-2):
                    weight[i][j].append(np.random.random())
        #print("\nWeights Of Paths Is Created!!!")
        return weight

class TryNetwork:
    def Try(nodeWeight,weight,printBool=False):
        print("aass ",nodeWeight)
        print("ssss ",weight)
        result=[]
        difference=[]
        if printBool:
            pass
        for i in range(1,len(nodeWeight)):
            if i==(len(nodeWeight)-1):
                for j in range(len(nodeWeight[i])):
                    result.append([])
                    difference.append([])
                    for k in range(len(nodeWeight[i-1])):
                        if k==0:
                            result[j]=weight[i-1][k][j]*nodeWeight[i-1][k]
                        else:
                            result[j]+=weight[i-1][k][j]*nodeWeight[i-1][k]
                    result[j]=Sigmoid.Sigmoid(result[j])
                    difference[j]=(nodeWeight[-1][j]-result[j])**2
            else:
                for j in range(len(nodeWeight[i])-1):
                    for k in range(len(nodeWeight[i-1])):
                        #print("i=",i," j=",j," k=",k)
                        if k==0:
                            nodeWeight[i][j]=weight[i-1][k][j]*nodeWeight[i-1][k]
                        else:
                            nodeWeight[i][j]+=weight[i-1][k][j]*nodeWeight[i-1][k]
                    nodeWeight[i][j]=Sigmoid.Sigmoid(nodeWeight[i][j])
        if printBool:
            #print("\nSuccessful Try!!!")
            pass
        return nodeWeight,result,difference

class Train:
    def Train(weight,delta):
        for i in range(len(delta)):
            for j in range(len(delta[i])):
                for k in range(len(delta[i][j])):
                    weight[i][j][k]+=delta[i][j][k]
        return weight
    
class Sigmoid:
    def Sigmoid(x):
        try:
            x=round(x,10)
            return round(1/((1+round((2.718281828459**(round(-x,10))),10))),10)
                  #number e ~= 2.718281828459
        except:
            pass

class Read:     
    def Read(value,outs,weight=""):
        biasValue=1
        inputs=[]
        outputs=[]
        lines=value
        for i in range(len(lines)):
            lines[i].append(biasValue)
            inputs.append(lines[i])
            outputs.append(outs[i])
        lines=[[]]
        lines[0].append(inputs[0])
        if weight=="":
            hiddenHeight= int(input('Please Enter Hiddesn Layers Height=\n'))
        else:
            hiddenHeight= (len(weight)-1)
        tempInput=[]
        for i in range(hiddenHeight):
            if weight=="":
                tempInput.append(int(input('Please Enter Hidden Layers Length=\n')))
            else:
                tempInput.append(len(weight[i][0]))
            tempLine=[0 for i in range(tempInput[i])]
            tempLine.append(1)
            tempInput[i]=tempLine        
            lines[0].append(tempLine)
        lines[0].append(outputs[0])
        for i in range(1,len(inputs)):
            lines.append([])
            lines[i].append(inputs[i])
            for j in range(hiddenHeight):
                lines[i].append(tempInput[j])
            lines[i].append(outputs[i])
        #print("L0",lines[0])
        #print("L1",lines[1])
        #print("\nRead Succesed!!!")
        return lines

class Random:
    def Random():
        import time
        return round((time.time()%1),12)
class CloneNode:
    def CloneNodeEmpty(node):
        newNode=[]
        try:
            for i in node:
                newNode.append(CloneNode.CloneNodeEmpty(i))
            return newNode
        except:
            return []
    
    def CloneNodeValue(node,value):
        newNode=[]
        try:
            for i in node:
                newNode.append(CloneNode.CloneNodeValue(i,value))
            return newNode
        except:
            return value


class Calculate:
    def CalculateDelta(nodeWeight,weight,result,delta,learningRate=0.25,momentum=0.1):
        nodeS=CloneNode.CloneNodeEmpty(nodeWeight)
        for i in reversed(range(1,len(nodeWeight))):
            if i==len(nodeWeight)-1:
                for j in range(len(nodeWeight[i])):
                    nodeS[i][j]=(nodeWeight[i][j]-result[j])\
                        *result[j]*(1-result[j])
                for j in range(len(nodeWeight[i-1])):
                    for k in range(len(weight[i-1][j])):
                        delta[i-1][j][k]=learningRate*nodeS[i][k]\
                            *nodeWeight[i-1][j]+momentum*delta[i-1][j][k]
            else:
                for j in range(len(nodeWeight[i])):
                    for k in range(len(weight[i][j])):
                        if k==0:
                            nodeS[i][j]=nodeS[i+1][k]*weight[i][j][k]\
                                *nodeWeight[i][j]*(1-nodeWeight[i][j])
                        else:
                            nodeS[i][j]+=nodeS[i+1][k]*weight[i][j][k]\
                                *nodeWeight[i][j]*(1-nodeWeight[i][j])
                for j in range(len(nodeWeight[i-1])):
                    for k in range(len(weight[i-1][j])):
                        delta[i-1][j][k]=learningRate*nodeS[i][k]\
                            *nodeWeight[i-1][j]+momentum*delta[i-1][j][k]
        #print("\nDelta Calculate Successed!!!")
        return delta,nodeS

def WriteWeight(weight):
    file=open("weight.txt","w")
    for i in range(len(weight)):
        for j in range(len(weight[i])):
            for k in range(len(weight[i][j])):
                if not k==len(weight[i][j])-1:
                    file.write((str(weight[i][j][k])+"&"))
                else:
                    file.write((str(weight[i][j][k])))
            file.write("/")
        file.write("%")
    file.close()
    print("Write Complate")
    
def ReadWeight():
    file=open("weight.txt","r")
    file=file.read()
    weight=file.split('%')
    weight.pop()
    temp=[]
    for i in weight:
        temp.append(i.split('/'))
        temp[-1].pop()
        values=[]
        for j in range(len(temp)):
            values.append([])
            for k in range(len(temp[j])):
                val=temp[j][k].split('&')
                values[j].append([])
                for v in val:
                    values[j][k].append(float(v))
    print("Read Complate")
    return values

def main(value="",outs="",read=True,learningRate=0.5):
    import time
    errorRate=0.0001
    if read==False:
        allNodes=Read.Read(value,outs)
        weight=WeightPath.CreateWeightPath(allNodes[0])
    else:
        weight=ReadWeight()
        allNodes=Read.Read(value,outs,weight)
    allNodes[0],result,difference=TryNetwork.Try(allNodes[0],weight,True)
    delta=CloneNode.CloneNodeValue(weight,0)#first delta must 0
    delta,nodeS=Calculate.CalculateDelta\
        (allNodes[0],weight,result,delta)
    end=False
    iteration=0
    mainIter=0
    d=[]
    learningCounter=48*(0.26/learningRate)
    try:
        while not end:
            best=True
            for nodeWeight in allNodes:
                weight=Train.Train(weight,delta)
                nodeWeight,result,difference=\
                TryNetwork.Try(nodeWeight,weight,False)
                delta,nodeS=Calculate.CalculateDelta\
                    (nodeWeight,weight,result,delta,learningRate)
                iteration+=1
                d.append(difference)
            if iteration>10000:
                iteration-=10000
                mainIter+=1
                learningRate=round(0.01+(12/(learningCounter+mainIter/4)),3)
                print("\ndiff ",d,"  lr=",learningRate)
            for i in range(len(d)):
                if d[i][0] >= errorRate:
                    best=False
            d=[]
            if best:
                end=True
                print("\n\nTraining Successed!!!\n")
                break 
    except:
        pass
    print("iter ",iteration+(10000*(mainIter)))
    temp=input("If you want save,press 'e'")
    if temp == "e":
        WriteWeight(weight)
        print("\n\nTraining Saved!!!")        
    return nodeWeight,weight

def train_interface():
    inputVal=input();#"1&1&1,1,1,1,1,1,1&1,1"
    inputVal=inputVal.split('&')
    isRead=bool(inputVal[0])
    isWrite=bool(inputVal[1])
    values=list(map(float,inputVal[2].split(',')))
    outs=list(map(float,inputVal[3].split(',')))
    values=[values]
    outs=[outs]
    '''
    print(type(isRead),isRead)
    print(isWrite,values,outs)
    print(type(values[0]))
    '''
    nodeWeight,weight=main(values,outs,True)
    nodeWeight[0]=values[0]
    nodeWeight[-1]=outs[0]
    nodeWeight,result,difference=TryNetwork.Try(nodeWeight,weight)
    #print("Result ",result," Diff",difference)
    print(result)

train_interface()



