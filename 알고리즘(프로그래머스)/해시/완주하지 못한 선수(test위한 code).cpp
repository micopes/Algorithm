#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector <string> v1; // parti
vector <string> v2; // complet

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";

    bool flag = false;
    int pre;
    for(int i = 0; i < completion.size(); ++i){
        if(participant[i] != completion[i]){
            if(flag == false){ // 차이 처음 발생한 곳 pre에 저장.
                pre = i;
                flag = true;
            }else{ // 차이 2번째 발생.
                return participant[pre];
            }
            /*
            // 맨 앞이 다른 경우
            [0]과 [1]이 다를 것.
            // 중간이 다른 경우3sdfj
            [0]부터 같다가 n부터 차이가 발생할 것. 그러면 participant[n]을 출력.
            */
        }
    }
    if(flag == true){
        answer = participant[pre];
    }else{
        // 다른 것 발견하지 못할경우 맨 마지막에 숨어있는 것.
        answer = participant[participant.size()-1];
    }


    return answer;
}

int main(void){
    int n;
    cin >> n;
    for(int i = 0; i < n; ++i){
        string s;
        cin >> s;
        v1.push_back(s);
    }
    for(int i = 0; i < n-1; ++i){
        string s;
        cin >> s;
        v2.push_back(s);
    }
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());
    for(int i = 0; i < v1.size(); ++i){
        cout << v1[i] << " ";
    }
    cout << endl;

    for(int i = 0; i < v2.size(); ++i){
        cout << v2[i] << " ";
    }
    cout << endl;
    cout << solution(v1, v2);

    return 0;
}
