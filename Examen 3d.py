# Examen-3d
"""
Examen de recuperacion unidad 3.
"""

import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, radians, sqrt

plt.axis([0,150,100,0])

plt.axis('on')
plt.grid(True)
#———plano del sistema
x=[40,30,80,85] 
y=[60,10,60,40]
z=[0,0,0,0]
#____Plotear el sistema 
plt.plot([x[0],x[1]],[y[0],y[1]],color='k') 
plt.plot([x[1],x[2]],[y[1],y[2]],color='k')
plt.plot([x[2],x[0]],[y[2],y[0]],color='k')
plt.scatter(x[3],y[3],s=20,color='r')

plt.plot([x[0],x[3]],[y[0],y[3]],linestyle=':',color='r')
plt.plot([x[1],x[3]],[y[1],y[3]],linestyle=':',color='r')
plt.plot([x[2],x[3]],[y[2],y[3]],linestyle=':',color='r')

plt.text(35,63,'0') #——label corners
plt.text(25,10,'1')
plt.text(83,63,'2')
plt.text(x[3]+2,y[3],'3')
#Calculo de dimensiones.
a=x[1]-x[0] 
b=y[1]-y[0]
c=z[1]-z[0]
Q01=sqrt(a*a+b*b+c*c)

a=x[2]-x[1]
b=y[2]-y[1]
c=z[2]-z[1]
Q12=sqrt(a*a+b*b+c*c)

a=x[2]-x[0]
b=y[2]-y[0]
c=z[2]-z[0]
Q02=sqrt(a*a+b*b+c*c)

a=x[1]-x[3]
b=y[1]-y[3]
c=z[1]=z[3]
Q13=sqrt(a*a+b*b+c*c)

a=x[2]-x[3]
b=y[2]-y[3]
c=z[2]-z[3]
Q23=sqrt(a*a+b*b+c*c)

a=x[0]-x[3]
b=y[0]-y[3]
c=z[0]-z[3]
Q03=sqrt(a*a+b*b+c*c)
# —— calcular las áreas A, A1 y A2
s=(Q01+Q12+Q02)/2 
A=sqrt(s*(s-Q01)*(s-Q12)*(s-Q02))

s1=(Q01+Q03+Q13)/2
A1=sqrt(s1*(s1-Q01)*(s1-Q03)*(s1-Q13))

s2=(Q02+Q23+Q03)/2
A2=sqrt(s2*(s2-Q02 )*(s2-Q23)*(s2-Q03))
#Etiqueta del area A.
plt.arrow(70,55,10,15,linewidth=.5,color='grey')
plt.text(82,73,'A',color='k')

# —— salida del gráfico
plt.text(100,40,'A=') 
dle='%7.0f'% (A)
dls=str(dle)
plt.text(105,40,dls)

plt.text(100,45,'A1=',color='r')
dle='%7.0f'% (A1)
dls=str(dle)
plt.text(105,45,dls)

plt.text(100,50,'A2=',color='r')
dle='%7.0f'% (A2)
dls=str(dle)
plt.text(105,50,dls)

plt.text(91,55,'A1+A2=',color='r')
dle='%7.0f'% (A1+A2)
dls=str(dle)
plt.text(106,55,dls)

plt.text(100,40,'A=')
dle='%7.0f'% (A)
dls=str(dle)
plt.text(105,40,dls)

plt.text(100,45,'A1=',color='r')
dle='%7.0f'% (A1)
dls=str(dle)
plt.text(105,45,dls)

plt.text(100,50,'A2=',color='r')
dle='%7.0f'% (A2)
dls=str(dle)
plt.text(105,50,dls)

plt.text(91,55,'A1+A2=',color='r')
dle='%7.0f'% (A1+A2)
dls=str(dle)
plt.text(106,55,dls)
if A1+A2 > A:
    plt.text(100,63,'Esta afuera de los limites')
else:
    plt.text(100,63,'Esta adentro de los limites.')
    
plt.title ("Examen de recuperacion unidad 3")
plt.xlabel ("Eje x")
plt.ylabel ("Eje y")
plt.show()
while True:
    axis=input("Teclee Esc para salir ?:")
    if axis== 'Esc':
        break
