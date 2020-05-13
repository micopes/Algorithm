#include <vector>
#include <string>
#include <queue>

using namespace std;

struct comp{
    bool operator()(pair <int, int> a, pair <int, int> b){ // first : dates, second : supplies
        if(a.second == b.second){ // supplies 같으면 dates 낮은 것이 출력
            return a.first > b.first;
        }
        // supplies 보통의 경우는 supplies 높은 것 순서대로 먼저 출력.
        return a.second < b.second;
    }
};

int solution(int stock, vector <int> dates, vector <int> supplies, int k){
    int answer = 0;
    int day = 0;
    int sz = dates.size();
    priority_queue <pair <int, int>, vector <pair <int, int> >, comp> pq;

    for(int i = 0; i < sz; ++i){
        pq.push(pair<int, int>(dates[i], supplies[i]));
    }

    while(day < k){
        day += stock;
        stock = 0;
        vector <pair <int, int> > temp;
        // supply높은 순으로 뽑는데 day 범위를 만족하는 것이 나오면 그것을 pq에서 제거하고 stock에 추가해준다.
        while(1){
            int d = pq.top().first;
            int supply = pq.top().second;
            pq.pop();
            if(d <= day){
                stock = supply;
                answer++;
                for(int i = 0; i < temp.size(); ++i){
                    pq.push(temp[i]);
                }
                break;
            }else{
                temp.push_back(pair<int, int>(d, supply)); // day범위 만족못하지만 supply높아 먼저나온것 저장.
            }
        }
    }
    answer--;
    return answer;
}
