#include <iostream>

using namespace std;

int n,m;
int in[500000][2];
int inchk[500000];

int find(int pos, int init, int now, int next)
{
    inchk[pos] = 1;
    if(init == now) return 1;

    for(int i=0;i<m;i++) {
        if(in[i][0]==now && in[i][1]==next) {
            find(i,init,in[i][0],in[i][1]);
        }

        else if(in[i][1]==now && in[i][0]==next) {
            find(i,init,in[i][1],in[i][0]);
        }
    }

    inchk[pos] = 0;
    return 0;
}

int main(void){
    int i, j;

    cin >> n >> m;

    for(i=0; i<n; i++)
        inchk[i] = 0;

    for(i=0; i<m; i++)
        cin >> in[i][0] >> in[i][1];

    int chk = 0;
    for(i=0; i<m; i++)
    {
        if(find(i,in[i][0],in[i][0],in[i][1])) {
            chk = 1;
            break;
        }
    }

    if (chk!=0)
    {
        int dab;
        for(i=m-1;i>=0;i--) {
            if(inchk[i]==1) {
                dab = i;
                break;
            }
        }

        cout<<dab;
    }

    else
        cout<<"0";

    return 0;
}
