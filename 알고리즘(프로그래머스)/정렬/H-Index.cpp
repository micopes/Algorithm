#include <string>
#include <vector>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    int num[10001] = { 0, }; // 인용 횟수
    for(int i = 0; i < citations.size(); ++i){
        for(int j = 0; j <= citations[i]; ++j){
            num[j]++;
        }
    }
    for(int i = citations.size(); i >= 0; --i){ // 구하면 바로 나와서 바로 빠져나올 수 있다.
        if(num[i] >= i){
            answer = i;
            return answer;
        }
    }
    return answer;
}
