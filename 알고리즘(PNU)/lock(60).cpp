#include <iostream>
#include <fstream>
#include <queue>
#include <cstring>
using namespace std;

// 1. 모든 가는 경로 다 구해서 나열한 다음에 나열한 모든 것에 대해 공통으로 포함하고 있는 [i][j]를 적어주면 된다.
// 나열한 모든 것에 대해 공통으로 포함하고 있는 [i][j]가 없다면 0을 출력하면 된다.
// 2. _로 처리되어 있는 것들을 하나씩 막아서 bfs로 도달할 수 없으면 막은 해당 [i][j]를 출력하면 된다.
// 2번의 방법으로 풀었다.

ifstream in("lock.inp");
ofstream out("lock.out");
int n, m;
int resultX, resultY; // T 의 위치를 나타냄.
int startX, startY; // S의 위치를 나타냄.
char ar[31][31] = { 0, };
bool visited[31][31] = { 0, }; // 해당 i, j가 방문된 횟수.
int result = -1; // T 에 도달한 횟수.

// result 와 visited[i][j] 가 같은 숫자이면 그것이 답이된다. 모든 답에서 꼭 거쳐야 하는 경로라는 뜻이기때문
void input();

int main(void){
    ios_base::sync_with_stdio(false);
    in.tie(nullptr);

    input();
    queue <pair <int, int> > q;
    vector <pair <int, int> > v;
    // 해답 구하는 과정.
    for(int i = 1; i <= m; ++i){
        for(int j = 1; j <= n; ++j){
            if(ar[i][j] == '_'){
                ar[i][j] = '#'; // 임시로 바꾼다.
                q.push(pair<int, int>(startX, startY));

                while(!q.empty()){
                    int x = q.front().first;
                    int y = q.front().second;
                    visited[x][y] = true; // 해당 [i][j]가 방문됨.
                    q.pop();
                    if(x == resultX && y == resultY)
                        result++;
                    if(visited[x+1][y] == false && ar[x+1][y] != '#' && x < m)
                        q.push(pair<int, int>(x+1, y));
                    if(visited[x][y+1] == false && ar[x][y+1] != '#' && y < n)
                        q.push(pair<int, int>(x, y+1));
                    if(visited[x-1][y] == false && ar[x-1][y] != '#' && x > 1)
                        q.push(pair<int, int>(x-1, y));
                    if(visited[x][y-1] == false && ar[x][y-1] != '#' && y > 1)
                        q.push(pair<int, int>(x, y-1));

                }
                if(result == -1){ // 답을 구할 수 없는 경우. 즉, lockdown인 경우.
                    v.push_back(pair<int, int>(i, j));
                }
                // 초기화작업
                result = -1;
                ar[i][j] = '_'; // 다시 원상태로.
                memset(visited, 0, sizeof(visited));
            }else{
                continue;
            }
        }
    }

    if(v.size() == 0){ // lockdown하는 셀이 없을 경우.
        out << 0;
        return 0;
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
