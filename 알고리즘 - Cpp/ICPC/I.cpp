#include <iostream>
#include <algorithm>
#include <deque>
#define MAX 1000000

using namespace std;

int main(void){

    int n;
    cin >> n;

    deque <int> dq;
    int x, y;
    for(int i = 0; i < n*2; ++i){
        cin >> x;
        dq.push_back(x);
    }

    sort(dq.begin(), dq.end());

    int m = MAX;
    while(!dq.empty()){
        x = dq.front();
        y = dq.back();

        dq.pop_back();
        dq.pop_front();

        if(m > x + y)
            m = x + y;
    }

    cout << m;

    return 0;
}
