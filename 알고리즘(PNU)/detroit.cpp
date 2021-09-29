#include <iostream>
#include <fstream>
#include <vector>
#include <stack>

using namespace std;

void backtracking(int x, int y, int val);
bool checkCorrect(int x, int y);
int n;
int ar[10][10] = { 0, };
int result;
vector < pair <int, int> > v; // x y 기존에 차있지 않은 것들을 다 넣음.
stack < pair< pair <int, int>, int> > st; // x y n
int main(void){
    ifstream in("detroit.inp");
    ofstream out("detroit.out");
    ios_base::sync_with_stdio(false);
    in.tie(nullptr);
    in >> n;

    int index = 0;
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < n; ++j){
            in >> ar[i][j];
            if(ar[i][j] == 0){ // 기존에 뭔가 차있지 않으면 (= 0이면) vector에 넣는다.
                v.push_back(make_pair(i, j));
            }
        }
    }
    if(v.size() == 0){ // 기존에 완성되어 있으면
        out << 1; // 1을 출력하고 종료. // sampledata 4번.
        return 0;
    }
    // 처음 시작할 값.
    int x = v[0].first;
    int y = v[0].second;
    for(int i = 1; i <= n; ++i){
        //st.push(make_pair(make_pair(x, y), i)); // st.push(make_pair(v[0], i));
        st.push(make_pair(v[0], i)); // ex) n = 4 이면 4개를 스택에 넣는것.
    }
    //cout << v.size();
    while(!st.empty()){
        auto a = st.top();
        x = a.first.first;
        y = a.first.second;
        int val = a.second;
        ar[x][y] = val;
/*
        cout << x << " " << y << " " << val << " " << index << endl; //특이점 : n == 4면 val = 4를 첫번재로 진행.
        //cout << st.size() << endl;
        cout << endl;
/*

        for(int i = 0; i < n; ++i){
            for(int j = 0; j < n; ++j){
                cout << ar[i][j] << " ";
            }
            cout << endl;
        }
        cout << endl;
*/
        if(checkCorrect(x, y)){ // 가로 세로 모두 조사해서 그 자리에 넣는게 가능할 경우.
            // st.push(make_pair(v[index], i);를 할지 for문으롲 전체관리를 할지 결정해줘야한다.
            if(v.size()-1 == index){
/*
                for(int i = 0; i < n; ++i){
                    for(int j = 0; j < n; ++j){
                        cout << ar[i][j] << " ";
                    }
                    cout << endl;
                }
                cout << endl;
*/
                result++;
                ar[x][y] = 0; // 기존의 것을 0으로 바꾸고
                st.pop(); // 빼낸다.

                //index--;
            }else{
                index = index + 1;
                st.pop();
                for(int i = 1; i <= n; ++i){
                    st.push(make_pair(v[index], i)); // v[index]에 x, y 정보가 있다.
                }
            }
        }else{

            if(ar[x][y] == 1){
                if(st.size() == 1) // 끝
                    break;
                index--;
            // 여기가 매우 조잡하기는 함.
            // 3개면 되지않을까.. -> 근거 : 원래 비어있던 것(벡터 앞의 순서가 1이어서 스택에 아무것도 남아있지 않는경우 한번 더 앞으로가주는 작업. 11111 이렇게 3개이상겹쳐지면안되는데 어차피 많아도 2개 11는 불가능하고 [1][5]에 1, [2][1]에 1인경우 이런경우만 고려해주면 된다.
                if(ar[v[index].first][v[index].second] == 1){
                    ar[v[index].first][v[index].second] = 0;
                    index--;
                }
                if(ar[v[index].first][v[index].second] == 1){
                    ar[v[index].first][v[index].second] = 0;
                    index--;
                }
                if(ar[v[index].first][v[index].second] == 1){
                    ar[v[index].first][v[index].second] = 0;
                    index--;
                }
            }
            ar[x][y] = 0;
            st.pop();
            //index--;
        }

        /*
        // 찾은 경우
        if(v.size() == index){
            result++;
            st.pop();
        }
        */
    }

    //backtracking(x, y, 1); // recursion으로 들어가지 않고 풀기.
    // ar[0][0] = 0이면 하려고했는데 원래 값이 여기들어있을 수 있으니까.

    out << result;

    in.close();
    out.close();
    return 0;
}
/*
void backtracking(int x, int y, int n){
    if(checkCorrect(x, y)){ // 적합한 수인 경우.
        //backtracking();
    }else{
        backtracking(x, y, n+1);
    }

}
*/

bool checkCorrect(int x, int y){ // 0이상일때만 체크.
    for(int i = 0; i < n; ++i){
        if(x != i){
            if(ar[x][y] == ar[i][y])
                return false;
        }
    }
    for(int i = 0; i < n; ++i){
        if(y != i){
            if(ar[x][y] == ar[x][i])
                return false;
        }
    }
	return true;
}
