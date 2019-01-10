#include <stdlib.h>
#include <stdio.h>


main() {
	
char nome;
 
  double salario,vendas,x;
 
  scanf("%s %lf %lf", &nome, &salario, &vendas);
 
  x = salario + (15*vendas)/100;
 
   printf("TOTAL = R$ %.2f\n",x);
   
   system("pause");
	
	
	

	
}
