#include <iostream>
#include <fstream>
#include <queue>
#include <cstring>
#include <stack>
using namespace std;

// 1. 모든 가는 경로 다 구해서 나열한 다음에 나열한 모든 것에 대해 공통으로 포함하고 있는 [i][j]를 적어주면 된다.
// 나열한 모든 것에 대해 공통으로 포함하고 있는 [i][j]가 없다면 0을 출력하면 된다.
// 2. _로 처리되어 있는 것들을 하나씩 막아서 bfs로 도달할 수 없으면 막은 해당 [i][j]를 출력하면 된다.
// 2번의 방법으로 풀었다.

ifstream in("lock.inp");
ofstream out("lock.out");
int n, m;
int startX, startY; // S의 위치를 나타냄.
int resultX, resultY; // T 의 위치를 나타냄.
char ar[31][31] = { 0, };
int order[31][31] = { 0, }; //  방문 순서
bool visited[31][31] = { 0, }; // 해당 i, j가 방문된 횟수.
bool isCut[31][31] = { 0, }; // 해당하는 vertex가 cut vertex인지 여부.
int cnt; // 방문순서 count.
bool result = false; // T 에 도달한 경우 -> true;
void input();
int dfs(int x, int y, int root);
void solution();
int main(void){
    ios_base::sync_with_stdio(false);
    in.tie(nullptr);
    input();

    // cut vertex 구하기.
    for(int i = 1; i <= m; ++i){
        for(int j = 1; j <= n; ++j){
            if(visited[i][j] == false)
                dfs(i, j, true);
        }
    }

    // 해답 구하는 과정.
    vector <pair <int, int> > v;
    stack <pair <int, int> > st;
    queue <pair <int, int> > q;

    int prevX[31] = { 0, }; // 이전에 방문한 것. 나중에 result와 같은 값을 구한 뒤에 역추적 할것임.
    int prevY[31] = { 0, };
    pair <int, int> prev[31][31];
    // 처음부터 단절되어 있는 경우인지를 조사.
    q.push(pair<int, int>(startX, startY));
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        visited[x][y] = true; // 해당 [i][j]가 방문됨.
        q.pop();
        if(x == resultX && y == resultY){
            result = true; // 시작 -> 도착의 경우가 있다는 것만 찾았다면 더이상 안해도 된다.
            break;
        }
        if(visited[x+1][y] == false && ar[x+1][y] != '#' && x < m){
            q.push(pair<int, int>(x+1, y));
            prev[x+1][y].first = x;
            prev[x+1][y].second = y;

        }
        if(visited[x][y+1] == false && ar[x][y+1] != '#' && y < n){
            q.push(pair<int, int>(x, y+1));
            prev[x][y+1].first = x;
            prev[x][y+1].second = y;
        }
        if(visited[x-1][y] == false && ar[x-1][y] != '#' && x > 1){
            q.push(pair<int, int>(x-1, y));
            prev[x-1][y].first = x;
            prev[x-1][y].second = y;
        }
        if(visited[x][y-1] == false && ar[x][y-1] != '#' && y > 1){
            q.push(pair<int, int>(x, y-1));
            prev[x][y-1].first = x;
            prev[x][y-1].second = y;
        }
    }
    if(result == false){ // 처음부터 단절되어 잇는 경우.
        out << 0;
        return 0;
    }
    // 처음부터 단절되어 있지 않은 경우. 초기화 작업.
    result = false;
    memset(visited, false, sizeof(visited));
/*
    for(int i = 1; i <= m; ++i){
        for(int j = 1; j <= n; ++j){
            if(isCut[i][j])
                cout << i << " " << j << "\n";
        }
    }
*/
    bool isCutST[31][31] = { 0, };
    int i = resultX;
    int j = resultY;
    while(startX != i || startY != j){
        int x = prev[i][j].first;
        int y = prev[i][j].second;
        isCutST[x][y] = true;
        i = x;
        j = y;
    }

    for(int i = 1; i <= m; ++i){
        for(int j = 1; j <= n; ++j){
            if(isCut[i][j] && !isCutST[i][j])
                isCut[i][j] = false;
        }
    }

    for(int i = 1; i <= m; ++i){
        for(int j = 1; j <= n; ++j){
            if(isCut[i][j] == true && ar[i][j] == '_'){ //
                ar[i][j] = '#'; // 임시로 바꾼다.
                queue <pair <int, int> > q2;
                q2.push(pair<int, int>(startX, startY));

                while(!q2.empty()){
                    int x = q2.front().first;
                    int y = q2.front().second;
                    visited[x][y] = true; // 해당 [i][j]가 방문됨.
                    q2.pop();
                    if(x == resultX && y == resultY){
                        result = true; // 시작 -> 도착의 경우가 있다는 것만 찾았다면 더이상 안해도 된다.
                        break;
                    }
                    if(visited[x+1][y] == false && ar[x+1][y] != '#' && x < m)
                        q2.push(pair<int, int>(x+1, y));
                    if(visited[x][y+1] == false && ar[x][y+1] != '#' && y < n)
                        q2.push(pair<int, int>(x, y+1));
                    if(visited[x-1][y] == false && ar[x-1][y] != '#' && x > 1)
                        q2.push(pair<int, int>(x-1, y));
                    if(visited[x][y-1] == false && ar[x][y-1] != '#' && y > 1)
                        q2.push(pair<int, int>(x, y-1));
                }
                if(result == false){ // 답을 구할 수 없는 경우. 즉, lockdown인 경우.
                    v.push_back(pair<int, int>(i, j));
                }
                // 초기화작업
                result = false;
                ar[i][j] = '_'; // 다시 원상태로.
                memset(visited, false, sizeof(visited));
            }
        }
    }

    if(v.size() == 0){ // lockdown하는 셀이 없을 경우.
        out << 0;
    }else{ // 답이 존재하는 경우.
        out << v.size() << endl;
        for(int i = 0; i < v.size(); ++i){
            out << v[i].first << " " << v[i].second << endl;
        }
    }

	return 0;
}

void input(){
    in >> n >> m;
    for(int j = 1; j <= n; ++j){ // 인덱스 위치가 좀 다른데 이것은 뺄셈을 통해서 해당하는 것 찾아주자.
        for(int i = 1; i <= m; ++i){
            in >> ar[i][n+1-j];
            //cout << i << " " << n+1-j;
            if(ar[i][n+1-j] == 'S'){
                startX = i;
                startY = n+1-j;
            }else if(ar[i][n+1-j] == 'T'){
                resultX = i;
                resultY = n+1-j;
            }
        }
    }
}

int dfs(int x, int y, int root){
    order[x][y] = ++cnt;
    int ret = order[x][y];
    int childNum = 0;

    if(order[x+1][y] == true)
        ret = min(ret, order[x+1][y]);
    else if(order[x+1][y] == false && ar[x+1][y] != '#' && x < m){
        childNum++;
        int val = dfs(x+1, y, false);
        if(root == false && val >= order[x][y]){
            isCut[x][y] = true;
        }

        ret = min(ret, val);
    }
    if(order[x][y+1] == true)
        ret = min(ret, order[x][y+1]);
    else if(order[x][y+1] == false && ar[x][y+1] != '#' && y < n){
        childNum++;
        int val = dfs(x, y+1, false);
        if(root == false && val >= order[x][y])
            isCut[x][y] = true;

        ret = min(ret, val);
    }
    if(order[x-1][y] == true)
        ret = min(ret, order[x-1][y]);
    else if(order[x-1][y] == false && ar[x-1][y] != '#' && x > 1){
        childNum++;
        int val = dfs(x-1, y, false);
        if(root == false && val >= order[x][y])
            isCut[x][y] = true;

        ret = min(ret, val);
    }
    if(order[x][y-1] == true)
        ret = min(ret, order[x][y-1]);
    else if(order[x][y-1] == false && ar[x][y-1] != '#' && y > 1){
        childNum++;
        int val = dfs(x, y-1, false);
        if(root == false && val >= order[x][y])
            isCut[x][y] = true;

        ret = min(ret, val);
    }

    if(root == true && childNum >= 2){
        isCut[x][y] = true;
    }
    return ret;
}
