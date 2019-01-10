#include <stdlib.h>
#include <stdio.h>
main () 

{   double raio, pi = 3.14159, volume;
 
    scanf ("%lf", &raio);
    
    volume = 4 * pi * raio * raio *raio/3;
    
    printf("VOLUME = %.3lf\n", volume);
    
	
	system ("PAUSE");
}
