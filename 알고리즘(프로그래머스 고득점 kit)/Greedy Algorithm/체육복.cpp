#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    int stu[31] = { 0, };
    for(int i = 1; i <= n; ++i){
        stu[i] = 1; // 1로 초기화.
    }
    for(int i = 0; i < lost.size(); ++i){
        stu[lost[i]]--; // 없으면 0.
    }
    for(int i = 0; i < reserve.size(); ++i){
        stu[reserve[i]]++; // 여분 있으면 2로. lost, reserve둘다 포함되어 있으면 1로.
    }

    stu[0] = 1; // 아래 계산시 오류 방지.
    // reserve로 따져주게 되면 2가 아닌 것이 있어서 잘못된 값이 나올 수 있다.
    for(int i = 1; i <= n; ++i){
        if(stu[i] == 2 && stu[i-1] == 0){
            stu[i-1] += 1;
            stu[i] -= 1;
        }else if(stu[i] == 2 && stu[i+1] == 0){
            stu[i+1] += 1;
            stu[i] -= 1;
        }
    }

    for(int i = 1; i <= n; ++i){
        if(stu[i] >= 1){
            answer++;
        }
    }
    return answer;
}
