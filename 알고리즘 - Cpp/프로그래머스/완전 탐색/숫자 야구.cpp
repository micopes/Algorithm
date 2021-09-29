#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> baseball) {
    int answer = 0;
    int sz = baseball.size();

    bool imposs[1000] = { false, }; // 초기화번거로우니 true(1)이 되면 불가능인걸로.
    for(int i = 123; i <= 987; ++i){ // 0포함된거는 버려야함. 서로 같은 수도 버려야 함. 미리 버린다.
        int checknum[4] = { 0, };
        checknum[1] = i / 100;
        checknum[2] = (i / 10) % 10;
        checknum[3] = i % 10;
        if(checknum[1] == 0 || checknum[2] == 0 || checknum[3] == 0){
            imposs[i] = true;
        }else if(checknum[1] == checknum[2] || checknum[2] == checknum[3] || checknum[3] == checknum[1])
            imposs[i] = true;
    }
    for(int i = 0; i < sz; ++i){
        int num[4] = { 0, };
        num[1] = baseball[i][0] / 100;
        num[2] = (baseball[i][0] / 10) % 10;
        num[3] = baseball[i][0] % 10;
        int st = baseball[i][1];
        int ball = baseball[i][2];
        for(int j = 123; j <= 987; ++j){
            if(imposs[j] == true)
                continue;
            int checknum[4] = { 0, };
            checknum[1] = j / 100;
            checknum[2] = (j / 10) % 10;
            checknum[3] = j % 10;
            int checkst = 0;
            int checkball = 0;
            if(num[1] == checknum[1])
                checkst++;
            else if(num[1] == checknum[2] || num[1] == checknum[3])
                checkball++;
            if(num[2] == checknum[2])
                checkst++;
            else if(num[2] == checknum[1] || num[2] == checknum[3])
                checkball++;
            if(num[3] == checknum[3])
                checkst++;
            else if(num[3] == checknum[1] || num[3] == checknum[2])
                checkball++;

            if(checkst != st || checkball != ball)
                imposs[j] = true;
        }
    }
    for(int i = 123; i <= 987; ++i){
        if(!imposs[i])
            answer++;
    }
    return answer;
}
