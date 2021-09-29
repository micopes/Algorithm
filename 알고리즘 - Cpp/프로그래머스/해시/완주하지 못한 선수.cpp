#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    bool flag = false;
    int pre;
    for(int i = 0; i < completion.size(); ++i){
        if(participant[i] != completion[i]){
            if(flag == false){ // 차이 처음 발생한 곳 pre에 저장. 1)
                pre = i;
                flag = true;
            }else{ // 차이 2번째 발생. 2)
                return participant[pre];
            }
            /*
            // 맨 앞이 다른 경우
            [0]과 [1]이 다를 것.
            // 중간이 다른 경우
            [0]부터 같다가 n부터 차이가 발생할 것. 그러면 participant[n]을 출력.
            */
        }
    }
    if(flag == true){ // 1) 은 발생했는데 2)가 없음 이전에 틀린 것 출력
        answer = participant[pre];
    }else{
        // 다른 것 발견하지 못할경우 맨 마지막에 숨어있는 것.
        answer = participant[participant.size()-1];
    }

    return answer;
}
