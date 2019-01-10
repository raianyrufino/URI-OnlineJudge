#include <stdlib.h>
#include <stdio.h>
main() 

{      int codigoum, numeroum, codigodois, numerodois;
       float valorum, valordois, total;

       scanf("%i %i %f", &codigoum, &numeroum, &valorum);
       scanf("%i %i %f", &codigoum, &numerodois, &valordois);
       
       total = (valorum * numeroum) + (valordois * numerodois);
       
       printf("VALOR A PAGAR: R$ %.2f\n", total);
       
      
    
    
    
    system ("PAUSE"); }
