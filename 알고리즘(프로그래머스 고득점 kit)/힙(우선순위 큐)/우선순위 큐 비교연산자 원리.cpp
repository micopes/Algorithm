#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct comp{
    bool operator()(int a, int b){
        //return a < b; // 이러면 값이 큰거부터 먼저 나온다.
        return a > b; // 이러면 값이 작은 것부터 먼저 나온다.
    }
};

int main(void){
    priority_queue <int, vector <int>, comp> pq;
    int n;
    cin >> n;

    for(int i = 0; i < n; ++i){
        int x;
        cin >> x;
        pq.push(x);
    }

    while(!pq.empty()){
        cout << pq.top() << endl;
        pq.pop();
    }

    return 0;
}
