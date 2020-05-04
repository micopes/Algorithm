#include <iostream>
#include <fstream>
#include <stack>
#define MAX 100000

using namespace std;

int L; // 하수관의 길이.
int k; // 기본 튜브의 종류.
int type[11] = { 0, }; // l1 ..
int sum; // 총 튜브의 길이 (subtubelength)
int num; // 사용 튜브의 개수.
int output = MAX; // default = 0, 전역변수는 자동으로 default값이 0으로 초기화된다.
int eachsum[11] = { 0, };
stack< pair <int, int> > st;
int main(void){
    ifstream in("tube.inp");
    ofstream out("tube.out");

    in >> L;
    in >> k;

    for(int i = 0; i < k; ++i){
        in >> type[i];
    }
    st.push(make_pair(0, 0));

    while(!st.empty()){
        auto x = st.top();
        sum = x.first;
        num = x.second + 1;
        st.pop();
        for(int i = 0; i < k; ++i){
            eachsum[i] = sum + type[i];
            if(eachsum[i] == L){
                if(num < output){
                    output = num;
                    break;
                }
            }else if(eachsum[i] < L){
                st.push(make_pair(eachsum[i], num));
            }else if(eachsum[i] > L){
                break; // i1 < i2 이므로 뒤의 것은 당연히 eachsum[i] > L 이므로 체크할필요없이 break.
            }
        }
        if(output != MAX){
            out << output;
            return 0;
        }
    }

    if(output == MAX) // 튜브의 수를 적절하게 조합해서 L미터의 하수관의 길이를 맞출 수 없다면 0으로.
        output = 0;

    out << output;

    in.close();
    out.close();

    return 0;
}
