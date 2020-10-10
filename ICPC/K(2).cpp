#include <iostream>
#include <queue>
#include <bits/stdc++.h>
#define MAX 10000000

using namespace std;


int newTable[500][500] = { 0, };
struct cmp{
    bool operator()(pair <int, int> a, pair <int, int> b){
        int ax = a.first;
        int ay = a.second;
        int bx = b.first;
        int by = b.second;

        return newTable[ax][ay] < newTable[bx][by];
    }
};

int main(void){
    int n, m;
    cin >> n >> m;

    int table[500][500] = { 0, }; // 1001 로 변경 필요.
    bool visited[500][500] = { 0, };

    for(int i = 0; i < n; ++i){
        for(int j = 0; j < m; ++j){
            visited[i][j] = MAX;
        }
    }

    // 시작 점은 (0, 0) 이고, 끝 점은 (n-1, m-1)

    for(int i = 0; i < n; ++i){
        for(int j = 0; j < m; ++j){
            cin >> table[i][j];
        }
    }

    if(table[0][0] == -1){
        cout << -1;
        return 0;
    }

    priority_queue <pair <int, int>, vector <pair<int, int> >, cmp> pq;
    pq.push(pair<int, int>(0, 0));

    while(!pq.empty()){
        int x = pq.top().first;
        int y = pq.top().second;
        pq.pop();
        visited[x][y] = true;

        if(x >= 1 && y >= 1 && visited[x-1][y-1] == false && table[x-1][y-1] >= 0){
            pq.push(pair<int, int>(x-1, y-1));
            newTable[x-1][y-1] = newTable[x][y] + table[x-1][y-1];
        }
        if(x >= 1 && y < m-1 && visited[x-1][y+1] == false && table[x-1][y+1] >= 0){
            pq.push(pair<int, int>(x-1, y+1));
            newTable[x-1][y+1] = newTable[x][y] + table[x-1][y+1];
        }

        if(x < n-1 && y >= 1 && visited[x+1][y-1] == false && table[x+1][y-1] >= 0){
            pq.push(pair<int, int>(x+1, y-1));
            newTable[x+1][y-1] = newTable[x][y] + table[x+1][y-1];
        }

        if(x < n-1 && y < m-1 && visited[x+1][y+1] == false && table[x+1][y+1] >= 0){
            pq.push(pair<int, int>(x+1, y+1));
            newTable[x+1][y+1] = newTable[x][y] + table[x+1][y+1];
        }



    }

    if(newTable[n-1][m-1] == MAX)
        cout << -1;
    else{
        cout << newTable[n-1][m-1];
    }

    return 0;
}



