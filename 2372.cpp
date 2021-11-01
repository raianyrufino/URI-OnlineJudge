#include <stdio.h>
#include <string.h>
#include <algorithm>

#define MAX 112
#define INF 1000000007

using namespace std;


void floydWarshall(int num, int aux[MAX][MAX]){
	for(int k = 0; k <= num; k++)
		for(int i = 0; i <= num; i++)
			for(int j = 0; j <= num; j++)
				aux[i][j] = min(aux[i][j], aux[i][k] + aux[k][j]);
}

int main(){
	
	int nodes, edges, p, k, peso;
	
	int aux[MAX][MAX];
	
	int atual, saida;
	
	while(scanf("%d %d", &nodes, &edges) != EOF){
	   
		memset(aux, INF, sizeof aux);
		
		while(edges--){
			scanf("%d %d %d", &p, &k, &peso);
			aux[p][k] = aux[k][p] = peso;
		}
		
		floydWarshall(nodes, aux);
		saida = INF;
		
		for(p = 0; p < nodes; p++){
			
			atual = -INF;
			
			for(k = 0; k < nodes; k++)
				if(aux[k][p] != INF)
					atual = max(atual, aux[k][p]);
					
			saida = min(saida, atual);
		}
		printf("%d\n", saida);
	}
	return 0;
}

