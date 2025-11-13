// NOTE: it is recommended to use this even if you don't understand the following code.

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAXP 1000000
#define MAXN 100000

int M, N, P, i, j, k;
int K[MAXN];
int S[MAXN][5];
int ans[MAXP][2];

int main() {
    // uncomment the two following lines if you want to read/write from files
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);

    assert(2 == scanf("%d%d", &N, &M));

    for (j = 0; j < N; ++j) {
        assert(1 == scanf("%d", &K[j]));
        for (i = 0; i < K[j]; ++i)
            assert(1 == scanf("%d", &S[j][i]));
    }


    // struttura dati: matrice MxM utilizzata solo nel triangolo i>j
    // inizialmente queste posizioni [i][j] con i>j vengono impostate tutte a 1
    // ad indicare che la coppia i,j per ora è ok
    char pairs[M][M];
    for (i=1;i<M;++i)
        for(j=0;j<i;++j)
            pairs[i][j]=1;
    int cont = M*(M-1)/2;

    
    // PROVA: stampa matrice MxM
    // printf("\ncont=%d",cont);
    // for (i=0;i<M;++i) {
    //     printf("\n");
    //     for (j=0;j<M;++j) {
    //         printf("%d\t",pairs[i][j]);
    //     }
    // }
    // printf("\n\n");
    // PROVA: stampa matrice MxM fine

    // Passo in rassegna tutte le N scelte (vettori di scelte) presenti in S
    // Per ogni coppia x,y ordinata x>y cancello da pairs l'elemento in posizione x,y, assegnando 0
    for (k=0;k<N;++k) {
        int lung = K[k];
        if (lung>=2) {
            for (i=0;i<lung-1;++i) {
                for(j=i+1;j<lung;++j) {
                    int a = S[k][i];
                    int b = S[k][j];
                    if (a<b) {
                        int temp = a;
                        a=b;
                        b=temp;
                    }
                    // printf("A:%d B:%d\n",a,b);
                    if (pairs[a-1][b-1] == 1) {
                        pairs[a-1][b-1] = 0;
                        cont--;
                    }
                }
            }
        }
    }


    // PROVA: stampa matrice MxM
    // printf("\ncont=%d",cont);
    // for (i=0;i<M;++i) {
    //     printf("\n");
    //     for (j=0;j<M;++j) {
    //         printf("%d\t",pairs[i][j]);
    //     }
    // }
    // printf("\n\n");
    // PROVA: stampa matrice MxM fine


    int index = 0;
    for (i=1;i<M;++i)
        for(j=0;j<i;++j)
            if (pairs[i][j]==1) {
                ans[index][0]=i;
                ans[index][1]=j;
                ++index;
            }


    printf("%d\n", cont);
    for (j = 0; j < cont; ++j) {
        for (i = 0; i < 2; ++i)
            printf("%d ", ans[j][i]+1);
        printf("\n");
    }

    return 0;
}
