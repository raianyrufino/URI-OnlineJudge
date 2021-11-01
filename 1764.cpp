#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
 
using namespace std;

vector <int> set;

void initSet(int num)
{
    set.assign(num, 0);
    
    for (int i=0; i<num; i++) set[i] = i;
}
int findSet (int i)
{
    return ((set[i]==i)?i : set[i] = findSet(set[i]));
}
bool equalsSet (int i, int j)
{
    return findSet(i) == findSet(j);
}
void unionSet(int i, int j)
{
    set[findSet(i)] = findSet(j);
}
int main ()
{
    int m, n, origem, destino, peso, custo2;
    pair<int, pair<int,int> > pares;
    
    vector<pair<int, pair<int,int>>> arestas ;
    
    while (true) {
        scanf("%d %d", &m, &n);
        
        if (m == 0 && n == 0) return 0;
        
        for (int i =0; i<n; i++)
        {
			scanf("%d %d %d", &origem, &destino, &peso);
			
			arestas.push_back(make_pair(peso, pair<int, int>(origem,destino)));
        }
        
        sort(arestas.begin(), arestas.end());
        
        
        custo2 = 0;
        
        initSet(m);
        
        for (int i=0; i<n; i++)
        {
            pares = arestas[i];
            
            if (!equalsSet(pares.second.first, pares.second.second))
            {
                unionSet(pares.second.first, pares.second.second);
            	custo2 += pares.first;
            }
        }
        cout<<custo2<<endl;        
        arestas.clear();
    }
}
