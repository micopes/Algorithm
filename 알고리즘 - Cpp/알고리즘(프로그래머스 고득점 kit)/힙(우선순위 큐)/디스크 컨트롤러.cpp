#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#define MAX 100000000

using namespace std;
// 작업시간 적게걸리는것부터 다 수행이 되어야지 나중에 평균값이 가장 적을듯. 아닐수가 있나?
struct comp{
    // 우선순위 : 대기 시작시간 작은거부터, 대기 시작시간이 같으면 작업소요시간 적은것이 나오는걸로.
    bool operator()(pair <int, int> a, pair<int, int> b){ // first : 대기 시작 시간 second : 작업 소요 시간.
        if(a.first == b.first){
            a.second > b.second;
        }
        return a.first > b.first;
    }
};
int solution(vector<vector<int>> jobs) {
    int now = 0; // 현재 시간
    int answer = 0;
    priority_queue <pair <int, int>, vector< pair <int, int> >, comp> pq;
    int sz = jobs.size();

    for(int i = 0; i < sz; ++i){
        int x = jobs[i][0];
        int y = jobs[i][1];
        pq.push(make_pair(x, y));
    }

    int request; // request time 대기 시작 시간
    int elapsed; // elapsed time 소요 시간
    while(!pq.empty()){ // } && temp.size() != 0){
        vector < pair <int, int> > temp;
        request = pq.top().first;
        elapsed = pq.top().second;
        if(request > now){ // 현재 할 수 있는게 아무것도 없을경우 그냥 시간이 흐르는것.
            now++;
            continue;
        }
        while(request <= now && !pq.empty()){ // request <= now인동안 계속 vector 에 넣어주고. 끝나면 시간이 제일 적은 것부터.
            temp.push_back(pair<int, int>(request, elapsed));
            pq.pop();
            request = pq.top().first;
            elapsed = pq.top().second;
        }
        int minVal = MAX; // request <= now 만족하는 것중에서 소요시간 최소인 것을 찾는다.
        int minIndex = -1;
        for(int i = 0; i < temp.size(); ++i){
            int requestToEnd = now + temp[i].second - temp[i].first;
            if(requestToEnd < minVal){
                minVal = requestToEnd;
                minIndex = i;
            }
        }
        for(int i = 0; i < temp.size(); ++i){
            if(i != minIndex){
                pq.push(temp[i]);
            }
        }
        answer += minVal;
        now += temp[minIndex].second;
    }
    answer /= sz;
    return answer;
}
