#include <string>
#include <algorithm> // sort
#include <vector>

using namespace std;
// 접두어면 false, 접두어가 아니면 true

bool solution(vector<string> phone_book) {
    bool answer = true;
    sort(phone_book.begin(), phone_book.end());
    // 정렬하고 v[i] 이 비교하는 대상(i+1, i+2 ...)와 처음부터 끝까지 같으면 접두어.
    // v[i]가 끝까지 안갔는데 다른 부분 찾으면 i++, j = i+1;
    int i = 0, j = i+1;
    while(i < phone_book.size()-1){
        for(int k = 0; k < phone_book[i].size(); ++k){
            if(phone_book[i][k] == phone_book[j][k]){
                if(k == phone_book[i].length()-1){ // 마지막 자리
                    answer = false;
                    return answer;
                }
            }else{
                i++;
                j = i+1;
                break;
            }
        }

    }
    return answer;
}
