#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0; // 섞은 횟수

    priority_queue < int, vector<int>, greater<int> > pq;
    int sz = scoville.size();
    for(int i = 0; i < sz; ++i){
        pq.push(scoville[i]);
    }
    while(1){ // 다 K이상이 되었거나 1개 이하여서 섞을 것이 없는 경우 종료.
        if(pq.top() >= K || pq.size() <= 1)
            break;
        int x = pq.top();
        cout << x << " ";
        pq.pop();
        int y = pq.top();
        cout << y << " " << endl;
        pq.pop();
        int z = x + 2*y;
        answer++;
        pq.push(z);
    }
    // 종료 한 후 나오는게 K보다 작으면 -1을 리턴.
    if(pq.top() < K)
        answer = -1;
    return answer;
}

int main(void){
    vector <int> v;
    int n;
    cin >> n;
    for(int i = 0; i < n; ++i){
        int x;
        cin >> x;
        v.push_back(x);
    }
    cout << solution(v, 7);
    return 0;
}

