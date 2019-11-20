def polygonArea(X, Y, n): 
    area = 0.0
  
    j = n - 1
    for i in range(0,n): 
        area += (X[j] + X[i]) * (Y[j] - Y[i]) 
        j = i         
  
    return int(abs(area / 2.0)) 

area=[]
centroid=[]
inertia=[]
X=[]
Y=[]
Cx=0.0
Cy=0.0
Ix=0.0
Iy=0.0
n = int(input("Enter the number of sides of the polygon : "))
print("")
print("Note the maximum length is 256 units")
print("Also note to enter the vertices in counter-clockwise direction")
print("Make sure to ensure that the coordinates are entered w.r.t your origin of choice")
print("")
X=input("Enter the x co-ordinates: ")
Y=input("Enter the y co-ordinates: ")
area=polygonArea(X, Y, len(X))
for i in range(0,n):
    k=i+1
    if k>=n:
        k=0
    #Calculating centroid using formula
    Cx+=(X[i]+X[k])*(X[i]*Y[k]-X[k]*Y[i])
    Cy+=(Y[i]+Y[k])*(X[i]*Y[k]-X[k]*Y[i])
    #Calculating moment of inertia about x and y axes
    Ix+=(X[i]*Y[k]-X[k]*Y[i])*(Y[i]*Y[i]+Y[i]*Y[k]+Y[k]*Y[k])
    Iy+=(X[i]*Y[k]-X[k]*Y[i])*(X[i]*X[i]+X[i]*X[k]+X[k]*X[k])
#Finding centroid of polygon using formula
Cx=1/(6*area)*Cx
Cy=1/(6*area)*Cy
#Finding moment of inertia of polygon about x and y axes    
Ix=(1/12)*Ix
Iy=(1/12)*Iy
#Calculating moment of inertia of polygon about centroid of polygon (using parallel axis theorem)
IxMain=Ix-(area)*Cy*Cy
IyMain=Iy-(area)*Cx*Cx
tempList1=[]
tempList1.append(Cx)
tempList1.append(Cy)
centroid=tempList1
tempList2=[]
tempList2.append(IxMain)
tempList2.append(IyMain)
inertia=tempList2

print("The centroid of the polygon is "+str(centroid))
print("The moment of inertia of the polygon about its centroid is "+str(inertia))
print("The area of the polygon is "+str(area))

Cx1=0.0
Cy1=0.0
Ix1=0.0
Iy1=0.0
X1=[]
Y1=[]
n = int(input("Enter the number of sides of the cutout : "))
print("")
print("Note the maximum length is 256 units")
print("Also note to enter the vertices in counter-clockwise direction")
print("Make sure to ensure that the coordinates are entered w.r.t your origin of choice")
print("")
X1=input("Enter the x co-ordinates: ")
Y1=input("Enter the y co-ordinates: ")
area1=polygonArea(X1, Y1, len(X1))
#Negating cutout area
area1=-1*area1
for i in range(0,n):
    k=i+1
    if k>=n:
        k=0
    #Calculating centroid using formula
    Cx1+=(X1[i]+X1[k])*(X1[i]*Y1[k]-X1[k]*Y1[i])
    Cy1+=(Y1[i]+Y1[k])*(X1[i]*Y1[k]-X1[k]*Y1[i])
    #Calculating moment of inertia about x and y axes
    Ix1+=(X1[i]*Y1[k]-X1[k]*Y1[i])*(Y1[i]*Y1[i]+Y1[i]*Y1[k]+Y1[k]*Y1[k])
    Iy1+=(X1[i]*Y1[k]-X1[k]*Y1[i])*(X1[i]*X1[i]+X1[i]*X1[k]+X1[k]*X1[k])
#Finding centroid of cutout using formula
Cx1=1/(-6*area1)*Cx1
Cy1=1/(-6*area1)*Cy1
#Finding moment of inertia of cutout about x and y axes
Ix1=(1/12)*Ix1
Iy1=(1/12)*Iy1
#Finding centroid of polygon - cutout shape
Cx1=(Cx*area+Cx1*area1)/(area1+area)
Cy1=(Cy*area+Cy1*area1)/(area1+area)
tempList1=[]
tempList1.append(Cx1)
tempList1.append(Cy1)
centroid=tempList1
#Calculating moment of inertia of polygon about centroid of polygon - cutout (using parallel axis theorem)
IxMain=Ix-(area)*Cy1*Cy1
IyMain=Iy-(area)*Cx1*Cx1
#Calculating moment of inertia of composite shape about centroid of polygon - cutout (using parallel axis theorem)
Ix1=Ix1-(area1)*Cy1*Cy1
Iy1=Iy1-(area1)*Cx1*Cx1
#Adding both the above moments of inertia to find the overall moment of inertia
IxMain=IxMain+Ix1
IyMain=IxMain+Ix1
tempList2=[]
tempList2.append(IxMain)
tempList2.append(IyMain)
inertia=tempList2
print("The centroid of the polygon - cutout is "+str(centroid))
print("The moment of inertia of the polygon - cutout about its centroid is "+str(inertia))
print("The area of the polygon - cutout shape is "+str(area+area1))