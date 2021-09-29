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
    day += stock;
    stock = 0;
    while(day < k){
        vector <pair <int, int> > temp;
        while(1){ // 밀가루가 바닥날 수 밖에 없는 경우는 없으므로 pq.empty()는 고려하지 않아도 된다.
            int d = pq.top().first;
            int supply = pq.top().second;
            pq.pop();
            if(d <= day){
                stock = supply;
                answer++;
                for(int i = 0; i < temp.size(); ++i){
                    pq.push(temp[i]);   // day범위 만족못하지만 supply높아 먼저나온것 저장한 것을 다시 pq에 넣는다.
                }
                break;
            }else{
                temp.push_back(pair<int, int>(d, supply)); // day범위 만족못하지만 supply높아 먼저나온것 저장.
            }
        }
        day += stock;
        stock = 0;
    }
    return answer;
}
