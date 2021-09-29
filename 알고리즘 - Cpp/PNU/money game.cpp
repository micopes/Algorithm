#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int opResult(int a, char c, int b);
int main(void){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    ifstream in("mgame.inp");
    ofstream out("mgame.out");

    int dp[31][31] = { 0, }; // 필요없을듯?
    int num[31] = { 0, }; // 숫자.
    char op[30] = { 0, }; // 연산자.
    int maxdp[31][31] = { 0, };
    int mindp[31][31] = { 0, };

    string s;
    in >> s;

    int n = s.length()/2 + 1; // 숫자의 개수.
    int m = s.length()/2; // 연산자의 개수.

    for(int i = 0, j = 0; i < n; i++, j=j+2){
        num[i] = s[j]-'0';
        cout << num[i] << endl;
    }
    for(int i = 0, j = 1; i < m; i++, j=j+2){
        op[i] = s[j];
        cout << op[i] << endl;
    }
    /*
    num[0], num[1]을 op[0]의 연산을 통해서 연산한 것을 dp[0][0]에 넣자.
    num[1], num[2]을 op[1]의 연산을 통해서 연산한 것을 dp[1][1]에 넣자.
    num[2], num[3]을 op[2]의 연산을 통해서 연산한 것을 dp[2][2]에 넣자.
    num[3], num[4]을 op[3]의 연산을 통해서 연산한 것을 dp[3][3]에 넣자.
    num[4], num[5]을 op[4]의 연산을 통해서 연산한 것을 dp[4][4]에 넣자.
    */
    // 1. 초기값 설정.
    int p = n-1; // 헷갈리지않기위해 p는 dp의 개수.
    for(int i = 0; i < p; ++i){
        maxdp[i][i] = opResult(num[i], op[i], num[i+1]);
        mindp[i][i] = opResult(num[i], op[i], num[i+1]);
    }

    for(int gap = 1; gap < p; ++gap){ // -999 끼리 곱해서 엄청큰값이될수도. 그럼?
        for(int i = 0; i < p; ++i){
            int j = i + gap;
            maxdp[i][j] = max(opResult(num[i], op[i], maxdp[i+1][j]), opResult(num[i], op[i], mindp[i+1][j])); // 초기화.
            mindp[i][j] = min(opResult(num[i], op[i], maxdp[i+1][j]), opResult(num[i], op[i], mindp[i+1][j]));
            for(int k = i; k < j; ++k){
                int tempmax;
                int tempmin;
                if(k == j-1){ // 마지막것. 여기가 문제.
                    tempmax = max(opResult(maxdp[i][k], op[k+1], num[k+2]), opResult(mindp[i][k], op[k+1], num[k+2]));
                    tempmin = min(opResult(maxdp[i][k], op[k+1], num[k+2]), opResult(mindp[i][k], op[k+1], num[k+2]));
                }
                else{
                    int temp1 = max(opResult(mindp[i][k], op[k+1], mindp[k+2][j]), opResult(mindp[i][k], op[k+1], maxdp[k+2][j]));
                    int temp2 = max(opResult(maxdp[i][k], op[k+1], mindp[k+2][j]), opResult(maxdp[i][k], op[k+1], maxdp[k+2][j]));
                    tempmax = max(temp1, temp2);

                    temp1 = min(opResult(mindp[i][k], op[k+1], mindp[k+2][j]), opResult(mindp[i][k], op[k+1], maxdp[k+2][j]));
                    temp2 = min(opResult(maxdp[i][k], op[k+1], mindp[k+2][j]), opResult(maxdp[i][k], op[k+1], maxdp[k+2][j]));
                    tempmin = min(temp1, temp2);


                }
                mindp[i][j] = min(mindp[i][j], tempmin);
                maxdp[i][j] = max(maxdp[i][j], tempmax);
            }
        }
    }
    // 결과 확인
    for(int i = 0; i < p; ++i){
        for(int j = 0; j < p; ++j){
            cout << mindp[i][j] << " " << maxdp[i][j] << '\t';
        }
        cout << endl;
    }

    // 최종적으로 구해야 하는 것은 dp[0][n-1];
    out << maxdp[0][p-1];

    in.close();
    out.close();
    return 0;
}

int opResult(int a, char c, int b){
    int ret;
    if(c == '*'){
        ret = a * b;
    }else if(c == '+'){
        ret = a + b;
    }else if(c == '-'){
        ret = a - b;
    }
    return ret;
}
