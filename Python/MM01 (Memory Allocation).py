# from js import FillMemory, UpdateOutput, TerminalOutput

# Initializing array
MM = [0 for i in range(101)]
for i in range(12, 19, 1):
    MM[i] = 1
for i in range(53, 59, 1):
    MM[i] = 1
for i in range(93, 96, 1):
    MM[i] = 1


def ApplyBestFit():
    MyDiv = Element("ProcessSize")
        
    flag = 1
    start = 0
    end = 0
    preStart=[]
    preEnd=[]

    if MyDiv.value != '':
        if int(MyDiv.value) > 0 and int(MyDiv.value) < 101:
            i = 0   
            j = 0   
            while (i < 101 and flag):
                if MM[i] == 0:
                    j=i
                    while(j < 101):
                        if MM[j] == 1:
                            preStart.append(i)
                            preEnd.append(j-1)
                            i = j
                            break
                        if j == 100:
                            preStart.append(i)
                            preEnd.append(j)
                            flag=0
                            break
                        j+=1
                i+=1
            
            if len(preStart) != 0:
                flag = 0 # Now it being used as whether we can allocated the memory or not.
                end = 2000
                start = 1000
            
                for i in range(len(preStart)):
                    if  preEnd[i] - preStart[i] + 1 <= end-start+1 and preEnd[i] - preStart[i] + 1 >= int(MyDiv.value): 
                        start = preStart[i]
                        end = preEnd[i]
                        flag = 1
                if flag == 1:
                    FillMemory(start, start+int(MyDiv.value)-1)
                    for j in range(start, start+int(MyDiv.value), 1):
                        MM[j] = 1
                    UpdateOutput(int(MyDiv.value), 1, 2)
                    TerminalOutput(int(MyDiv.value), 1)
        else:
            TerminalOutput(int(MyDiv.value), 0)

def ApplyWorstFit():
    MyDiv = Element("ProcessSize");
    
    flag = 1
    start = 0
    end = 0
    preStart=[]
    preEnd=[]

    if MyDiv.value != '':
        if int(MyDiv.value) > 0 and int(MyDiv.value) < 101:
            i = 0   
            j = 0   
            while (i < 101 and flag):
                if MM[i] == 0:
                    j=i
                    while(j < 101):
                        if MM[j] == 1:
                            preStart.append(i)
                            preEnd.append(j-1)
                            i = j
                            break
                        if j == 100:
                            preStart.append(i)
                            preEnd.append(j)
                            flag=0
                            break
                        j+=1
                i+=1
            
            if len(preStart) != 0:
                flag = 0 # Now it being used as whether we can allocated the memory or not.
                end = -1
                start = 0
            
                for i in range(len(preStart)):
                    if  preEnd[i] - preStart[i] + 1 >= end-start+1 and preEnd[i] - preStart[i] + 1 >= int(MyDiv.value): 
                        start = preStart[i]
                        end = preEnd[i]
                        flag = 1
                if flag == 1:
                    FillMemory(start, start+int(MyDiv.value)-1)  # JavaScript Function
                    for j in range(start, start+int(MyDiv.value), 1):
                        MM[j] = 1
                    UpdateOutput(int(MyDiv.value), 1, 3)
                    TerminalOutput(int(MyDiv.value), 1)
        else:
                TerminalOutput(int(MyDiv.value), 0)
        
def ApplyFirstFit():
    MyDiv = Element("ProcessSize");
    
    flag = 0
    start = 0
    end = 0

    if MyDiv.value != '':
        if int(MyDiv.value) > 0 and int(MyDiv.value) < 101:
            MyDivValue = int(MyDiv.value)
            for i in range(101):
                if MM[i] == 0:
                    temp = MyDivValue
                    if i + temp <= 101:
                        for j in range(i, i + MyDivValue, 1):
                            if MM[j] == 0:
                                temp=temp-1
                                if temp == 0:
                                    start = i
                                    end = j
                                    flag = 1
                                    break
                            else:
                                i = j
                                break
                if flag == 1:
                    FillMemory(start, end)  # JavaScript Function
                    UpdateOutput(MyDivValue, 1, 1)
                    TerminalOutput(MyDiv.value, 1)
                    for j in range(start, end+1, 1):
                        MM[j] = 1
                    break
        else:
            TerminalOutput(MyDiv.value, 0)