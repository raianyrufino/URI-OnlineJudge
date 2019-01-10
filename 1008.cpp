#include <stdlib.h>
#include <stdio.h>
main()

{   int func, horas;
    float salario, salariomes;
    
    scanf("%i", &func);
    scanf("%i", &horas);
    scanf("%f", &salario);
    
    salariomes = horas * salario;
    
    printf("NUMBER = %i\nSALARY = U$ %.2f\n", func, salariomes);
    
    
    system("PAUSE"); }
