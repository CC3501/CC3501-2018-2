function [ u] = auxiliar2( h )
%Definir el tamaño de la matriz con el paso
x=floor(5/h);
y=floor(5/h);
%Definir una matriz de ceros
%Recordar que en matlab las matrices se definen como M[Fila, Columna] (y,x)
u=zeros(y,x);
%Condiciones de borde
for i=1:x
    u(1,i)=180;
end
 for j=1:y
     u(j,1)=80;
 end
 %Calculo de w
parte1=cos(pi/((y)-1));
parte2= cos(pi/((x)-1));
parte3= (parte1 + parte2)^2;
parte4= sqrt(4- parte3);
parte5=2+parte4;

w= 4/parte5;
iter=0;
r=100000;
while iter<100 || r>0.0001 
     for i=2:y-1;
          for j= 2:x-1;
    %Condiciones tipo dirichlet
            r= (u(i+1,j)+u(i-1,j)+u(i,j+1)+u(i,j-1)-4*u(i,j))/4;
            u(i,j)= u(i,j) + w*r;
    %Condiciones tipo Neumann
           u(x,j)= u(x,j)+w*((u(x,j+1)+u(i,j-1)+(2*u(x,(j-1)))-4*u(x,j))/4);
    %Uso de promedio en esquinas
            u(1,1)=(u(1,2)+u(2,1))/2;
            u(1,y)=(u(1,y-1)+u(2,y))/2;
            
          end
     end
     iter=iter+1;
end
  
  
disp(u);
end
