#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	int a[10],i,limit,j;
	float suma, division;	
	
	
	printf("\ncuantos alumnos van a consultar ");scanf("%i",&limit);
	
	for(j=1;j<=limit;j++)
	{
		system("cls");
		printf("\nEl alumno %i\n",j);
		suma=0;
		division=0;
		
		for(i=1;i<=10;i++)
		{
			printf("\nIngresa el dato del array en la posicion %i: ",i);scanf("%i",&a[i]);
			suma = suma + a[i];
			
			if(i==10)
			{
				division = suma/10;
				printf("\nel promedio del alumno %i es: ",j);
				printf("\nel promedio es %f",division);	
				if(division>=6){ 
				printf("\nes aprovatoria :D\n");
				getch();
				}
				else{
					printf("\nes reprovatoria :C\n");
					getch();
				}
			}
		}
	}
	
}