#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

// 이중 우선순위큐를 이용해서 구현하고자 하면 -를 이용하면 된다.

vector<int> solution(vector<string> operations) {
    deque <int> dq;

    int sz = operations.size();
    for(int i = 0; i < sz; ++i){
        if(operations[i][0] == 'I'){
            int k = stoi(operations[i].substr(2));
            dq.push_back(k);
            sort(dq.begin(), dq.end());
        }else if(operations[i] == "D 1"){
            if(!dq.empty()){
                dq.pop_back(); // 최댓값 제거.
            }
        }else if(operations[i] == "D -1"){
            if(!dq.empty()){
                dq.pop_front(); // 최솟값 제거
            }
        }
    }

    vector<int> answer;
    if(!dq.empty()){
        answer.push_back(dq.back());
        answer.push_back(dq.front());
    }else{
        answer.push_back(0);
        answer.push_back(0);
    }
    return answer;
}
