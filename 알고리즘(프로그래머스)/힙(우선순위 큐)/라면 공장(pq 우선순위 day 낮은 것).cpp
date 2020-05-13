#include <vector>
#include <string>
#include <queue>

using namespace std;

struct comp{
    bool operator()(pair <int, int> a, pair <int, int> b){ // first : dates, second : supplies
        if(a.first == b.first){ // dates같으면 supplies 높은 것이 출력.
            return a.second < b.second;
        }
        // dates 다른 보통의 경우는 dates가 낮은 순으로 먼저 출력.
        return a.first > b.first;
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
        int eff = 0; // day안에 supply가장 높은 효율적인 것을 저장할 것임.
        int effFirst = -1;
        while(pq.top().first <= day && !pq.empty()){
            temp.push_back(pair<int, int>(pq.top().first, pq.top().second));
            if(pq.top().second > eff){ // supply 가장 높은 것을 저장하기 위함.
                effFirst = pq.top().first;
                eff = pq.top().second;
            }
            pq.pop();
        }

        // day보다 낮은 것들 공급받을 수 있는 것중에 가장 supply높은 것을 제외하고는 다시 pq에 넣는다.
        for(int i = 0; i < temp.size(); ++i){
            if(temp[i].first != effFirst || temp[i].second != eff){ // 하나라도 다르면 eff 아님.
                pq.push(temp[i]);
            }
        }
        answer++;
        stock += eff;// += 나 = 나 상관없음
    }

    answer--;
    return answer;
}
