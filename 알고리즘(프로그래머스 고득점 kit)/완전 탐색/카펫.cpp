#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    // x : 가로, y : 세로.
    // xy-(x-2)(y-2) = brown
    // (x-2)(y-2) = yellow
    // xy = sum = brown + yellow
    int sum = brown + yellow;
    // 가로의 길이 최대 2500이하. 2500이면 다 포함 감싸는 거 최대가 5000이니까.
    // 감싸야 하니 둘다 가로 세로 3부터 시작.
    int x = 0, y = 0;
    for(int i = 3; i <= 2500; ++i){
        // 세로
        for(int j = 3; j <= i; ++j){
            if(i*j == sum && (i-2)*(j-2) == yellow){
                x = i;
                y = j;
                break;
            }
        }
        if(x > 0 && y > 0)
            break;
    }
    answer.push_back(x);
    answer.push_back(y);
    return answer;
}
