#include <string>
#include <vector>
#include <algorithm> // sort
#include <cmath> // sqrt

using namespace std;

int solution(string numbers){
    int answer = 0;
    int len = numbers.length();
    sort(numbers.begin(), numbers.end());
    reverse(numbers.begin(), numbers.end());
    int num = stoi(numbers); // 가능한 가장 큰 수.
    int *sosu = new int[num + 1]; // 처음에는 0으로 초기화.

    for(int i = 2; i <= sqrt(num); ++i){ // 유클리드 호제법. 소수를 전부 다 찾아놓는다.
        if(sosu[i] == 0){ // 아직 소수(0)에만 소수의 배수를 다 소수아닌(1)처리.
            for(int j = 2*i; j <= num; j += i){
                sosu[j] = 1; // 소수아니면 1 저장.
            }
        }
    }

    for(int i = 2; i <= num; ++i){
        if(sosu[i] == 0){ // 소수인 경우
            int temp1 = num;
            int temp2 = i;
            vector <int> check;
            vector <int> soCheck;

            while(temp1){
                int k = temp1 % 10;
                check.push_back(k);
                temp1 /= 10;
            }
            while(temp2){
                int k = temp2 % 10;
                soCheck.push_back(k);
                temp2 /= 10;
            }

            int cnt = 0;
            for(int j = 0; j < soCheck.size(); ++j){
                for(int k = 0; k < check.size(); ++k){
                    if(soCheck[j] == check[k]){
                        check[k] = -1; // 중복 피하기 위함.
                        cnt++;  // 소수의 길이(글자수)와 cnt를 비교해서 나중에 같으면 numbers에서
                        break;  // 소수의 모든 글자를 포함하는 것. 따라서 answer++ 가능하다.
                    }
                }
            }
            if(cnt == soCheck.size())
                answer++;
        }
    }
    delete [] sosu;
    return answer;
}
