#include <string>
#include <vector>
#include <queue>
using namespace std;

// 힙 정렬로 구현해주었다. 우선순위 큐의 우선순위를 어떻게 정할지가 중요하다.
// 하나하나 비교하는 식으로 이해하는 것이 중요!
struct cmp{
    bool operator()(int a, int b){
        string s1 = to_string(a) + to_string(b);
        string s2 = to_string(b) + to_string(a);
        if(s1 < s2){
            return true;
        }else{
            return false;
        }
    }
};
string solution(vector<int> numbers) {
    string answer = "";
    priority_queue <int, vector<int>, cmp> pq;
    for(int i = 0; i < numbers.size(); ++i){
        pq.push(numbers[i]);
    }
    while(!pq.empty()){
        answer += to_string(pq.top());
        pq.pop();
    }
    if(answer[0] == '0')
        answer = "0";
    return answer;
}
