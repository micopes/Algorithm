#include <iostream>
#include <string>
using namespace std;

int main() {
    int num;
    int pos = 0;
    int i,j;
    int x,y;
    string M;
    string SS;
    string T;
    string S;
    cin >> num;
    cin >> SS;
    cin >> T;
    cin >> x >> y;

    for(i=0; i<num; i++) {
        if(i == x || i == y) {
            M += SS[i];
            continue;
        }
        S += SS[i];
    }


    for(i=0; i<num; i++) {
        if(T[i] == S[pos]) {
            pos++;
        }

        else
        {
            if(M[0] != T[i]) {
                cout << "NO";
                break;
            }
        }
    }


    if(pos == num-2)
        cout<<"YES";

    return 0;
}
