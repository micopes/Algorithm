#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int stock, vector<int> dates, vector<int> supplies, int k) {
    int answer = 0;
    for(int day = 1; day < k; ++day){ // if(day == k) // 종료.
        stock--;
        if(stock == 0){
            int eff = 0;
            int effIndex = -1;
            for(int i = 0; i < dates.size(); ++i){
                if(dates[i] <= day && eff < supplies[i]){
                    eff = supplies[i];
                    effIndex = i;
                }
            }
            cout << dates[effIndex] << " " << supplies[effIndex] << endl;
            stock += supplies[effIndex]; // =나 +=나 같음 어차피 stock == 0 일때 조사하는 거라
            supplies[effIndex] = 0;
            answer++;
            // 범위 안 최대 공급받는 거 공급받고 0으로 만들기.
            // 여기서 루프로 최솟값을 찾으면 시간복잡도 커진다. 여기서 힙 사용해야 함
            // 1) <= day에 해당하면서 2) supply 가장 높은 index를 찾아서
            // pq에서 pop()해줘야 한다.

            // 달리 말하면 supply[i] 최대부터 찾는데, date[i] <= day
            // priority_queue인데 pair <int, int> 로 넣어주고. 우선순위는 supply 가장 높은 걸로 설정해줘야 한다.
        }
    }
    return answer;
}
