import csv
import matplotlib.pyplot as plt
import math
import sys
from collections import defaultdict
tau = defaultdict(defaultdict)
myDictionary={}
cities=[]
xx=[]
homeCity=[]
yy=[]
def euclidean(xa,xb,ya,yb):
    dist = math.sqrt((xa-xb)**2 + (ya-yb)**2)
    return dist

if (len(sys.argv) == 2):
        print"t\OK You entered correct input"
        myfileprefix = str(sys.argv[1])
else:
    print 'Error:you passed',len(sys.argv)-1,"input parameters."
    quit()
    
myCSVfile = "%s.csv"%(myfileprefix)


with open (myCSVfile, 'rb ') as csvfile :
    filex = csv.reader (csvfile , delimiter =',' , quotechar ='|')
    for row in filex:
        if ( row[0][0]!='%'):
            Id = int(row[0])
            isHome = int(row[1])
            x = float(row[2])
            y = float(row[3])
            if(isHome==1):
                homeCity=Id
            cities.append(Id)
            myDictionary[Id]={'isHome':isHome,'x':x,'y':y}
            xx.append(x)
            yy.append(y)

#print homeCity
myTour=[]    
for i in range(homeCity,len(cities)+1):
    myTour.append(i)
for i in range(1,homeCity+1):
    myTour.append(i)
# print myTour

tau=myDictionary
d=[]
z=myDictionary
for i in range(1,len(myTour)-1):
    for j in range (2,len(myTour)):
    
        
        tau[i][j]=euclidean(myDictionary[i]['x'],myDictionary[i]['y'],myDictionary[j]['x'],myDictionary[j]['y'])
        

                
    # d.append(tau[i][i+1])
###############################################
    
    
    
 ########Calculating the Cost Function #######   
for i in range(1,len(myTour)-1):
    
    z[i]['distance'] = euclidean(myDictionary[i]['x'],myDictionary[i]['y'],myDictionary[i+1]['x'],myDictionary[i+1]['y'])
    d.append(z[i]['distance'])
z[len(myTour)-1]['distance']=euclidean(myDictionary[1]['x'],myDictionary[1]['y'],myDictionary[len(myTour)-1]['x'],myDictionary[len(myTour)-1]['y'] )    
d.append(z[len(myTour)-1]['distance'])


 



cost = sum(d[i] for i in range(0,len(d)))

# print "The value of Cost Function is ",cost
g=[]
col=[]
for i in range(1,len(xx)+1):
    if myDictionary[i]['isHome'] == 1 :
        col.append('g') 
        
    else:
        col.append('r') 
        

 
difx=[]
dify=[]


for j in range(0,len(xx)-1):
    difx.append((xx[j]-xx[j+1]))
    dify.append((yy[j]-yy[j+1]))


difx.append((xx[len(xx)-1]-xx[0]))
dify.append((yy[len(yy)-1]-yy[0]))

#print homeCity
#print difx
#print dify
# =============================================================================
# for i in range (0, len( city )):
#     myx = x[i]
#     myy = y[i]
#     mycity = city [i]
# plt. text (myx , myy , mycity , color ="red", fontsize =12)
# 

# =============================================================================
print 'Cost Function Value is ',cost
print tau
plt.axis ([ min(xx) -15, max(xx)+15, min(yy) -15 , max(yy) + 15])
                
for i in range(0,len(xx)):
    plt.scatter(xx[i],yy[i],c=col[i], s=250)
    plt.text(xx[i],yy[i],i+1, fontsize=10,color ="yellow", horizontalalignment ='center', verticalalignment ='center' )
    plt.arrow(xx[i],yy[i],-difx[i],-dify[i] , head_width =2 , head_length=5 , ls='--', ec='k')
plt.axis ([ min(xx) -15, max(xx)+15, min(yy) -15 , max(yy) + 15])
plt.text(xx[homeCity-1],yy[homeCity-1],'Home', color='white',horizontalalignment='center',verticalalignment='center',bbox={'facecolor':'green', 'alpha':0.9, 'pad':5})
plt.xlabel('x [miles]')
plt.ylabel('y [miles]')
plt.title('TSP Tour using Lexicographic Algorithm')
plt.axis()

plt.savefig("%s.png"%(myfileprefix))



