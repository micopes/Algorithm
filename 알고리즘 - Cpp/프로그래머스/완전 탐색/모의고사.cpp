#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector <int> v1, v2, v3;
    while(v1.size() <= 10000){
        for(int i = 1; i <= 5; ++i){
            v1.push_back(i);
        }
    }
    while(v2.size() <= 10000){
        v2.push_back(2);
        v2.push_back(1);
        for(int i = 3; i <= 5; ++i){
            v2.push_back(2);
            v2.push_back(i);
        }
    }
    while(v3.size() <= 10000){
        for(int i = 0; i < 2; ++i)
            v3.push_back(3);
        for(int i = 0; i < 2; ++i)
            v3.push_back(1);
        for(int i = 0; i < 2; ++i)
            v3.push_back(2);
        for(int i = 0; i < 2; ++i)
            v3.push_back(4);
        for(int i = 0; i < 2; ++i)
            v3.push_back(5);

    }
    int score[3] = { 0, };
    for(int i = 0; i < answers.size(); ++i){
        if(v1[i] == answers[i])
            score[0]++; // 1¹ø
        if(v2[i] == answers[i])
            score[1]++; // 2¹ø
        if(v3[i] == answers[i])
            score[2]++; // 3¹ø
    }
    int maxnum = max(max(score[0], score[1]), score[2]);
    for(int i = 0; i < 3; ++i){
        if(maxnum == score[i])
            answer.push_back(i+1);
    }
    return answer;
}
