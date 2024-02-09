effort_list=[
    [6,6,8],
    [3,3,8],
    [2,1,2]
]

def findmin_enum(lst,priv_index):
    i=0
    min_value= -1; 
    print(lst)
    
    for index, value in enumerate(lst):           
        if index == priv_index:
            continue
        if min_value == -1:
            min_value=value
            min_index=index
        elif min_value > value:
            min_value=value
            min_index=index
  
    return(min_value,min_index)



def findmin(lst,priv_index):
    i=0
    min_value= -1; 
    print(lst)
    for i in range(len(lst)):        
        if i == priv_index:
            continue
        if min_value == -1:
            min_value=lst[i]
            min_index=i
        elif min_value > lst[i]:
            min_value=lst[i]
            min_index=i
  
    return(min_value,min_index)

def findmin1(lst,c):
    i=0
    count=0
    min_value= -1; 

    print(lst)
    for a in lst:
        if count == c:
            count=count+1
            continue

        if min_value == -1:
            min_index=count
            min_value=a
        elif min_value > a:
            min_value=a
            min_index=count

        count=count+1
        
    return(min_value,min_index)    


m_index=4
sum=0
for effort in effort_list:
    #m_val,m_index=findmin(effort,m_index)
    m_val,m_index=findmin_enum(effort,m_index)
    print(m_val,m_index)
    sum=sum+m_val

print(sum)
