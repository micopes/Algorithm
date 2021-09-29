#include <string>
#include <vector>
#include <queue>

using namespace std;

string solution(string number, int k) {
    string answer = "";
    priority_queue <int, vector<int>, greater<int> > pq;
    int x;
    for(int i = 0; i < number.length(); ++i){
        x = int(number[i]);
        pq.push(x);
    }
    string temp = "";

    for(int i = 0; i < number.length()-k; ++i){
        temp += char(pq.top());
        pq.pop();
    }

    for(int i = 0; i < temp.length(); ++i){

        for(int j = 0; j < number.length(); ++j){
            if(temp[i] == number[j]){
                answer += temp[i];
                break;
            }
        }
    }
    return answer;
}
