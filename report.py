def tabbs(n:int)->str:
    s=""
    for nn in range(n):
        s=s+"    "
    return s
a:int=0
styles=True
scripts=True
triggers=False
filename="/tmp/my.html"
filename2="/tmp/my2.html"
tabsx=0
outputss:str=""
print("\x1bc\x1b[41;30m")
f1=open(filename,"r")

files=f1.read()
f1.close()
splits=files.split(">")
counter=0
counter2=0
tabsx=0
for n in splits:
    n=n.replace("\n","")
    n=n.replace("\r","")
    tags=n.split("<")
    triggers=False
    counter=0
    if len(tags)==2 and len(tags[0])>0:
        triggers=True
    counter2=0
    for ta in tags:
        
        ta=ta.strip()
        
        if counter==0 and len(tags)==1:
            if counter==0 and len(ta)>0:
                   
               if ta[0]!="/":
                    tabsx=tabsx+1
            if counter==0 and len(ta)>0:
                   
               if ta[0]=="/":
                    tabsx=tabsx-1

            if len(ta)>0:
               if ta=="style" or ta=="STYLE":
                   styles=False
               if ta=="script" or ta=="SCRIPT":
                   scripts=False
               if styles and scripts:
                    if triggers:
                       
                        outputss=outputss+"\t"
                   
                    outputss=outputss+str(tabbs(tabsx))+"<"+str(tags)+">\n"
               if ta=="/style" or ta=="/STYLE":
                   styles=True
               if ta=="/script" or ta=="/SCRIPT":
                   scripts=True
            
        else:
            
            if counter==1 and len(ta)>0:
                   
               if ta[0]!="/":
                    tabsx=tabsx+1
            if counter==1 and len(ta)>0:
                   
               if ta[0]=="/":
                    tabsx=tabsx-1

            if len(ta)>0 and counter==1:
               if ta=="style" or ta=="STYLE":
                   styles=False
               if ta=="script" or ta=="SCRIPT":
                   scripts=False
               if styles and scripts:
                   if triggers:
                       
                       outputss=outputss+"\t"
                   
                   outputss=outputss+tabbs(tabsx)+str(tags[0])+"\n"+str(tabbs(tabsx))+"<"+str(tags[1])+">\n"
               if ta=="/style" or ta=="/STYLE":
                   styles=True
               if ta=="/script" or ta=="/SCRIPT":
                   scripts=True

            
                        

               
        counter+=1

f2=open(filename2,"w")
f2.write(outputss)
f2.close  
    
