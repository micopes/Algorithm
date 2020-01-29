#include <iostream>
#define MAX 1000000
using namespace std;

int main(void){

    // 100만까지의 모든 수를 소수가 맞는지를 검사하고자 한다.
    bool isPrime[MAX+1] = { 0, }; //
    for(int i = 0; i <= MAX; ++i){
        isPrime[i] = true;  // 여기서는 true로 모두 바꿔준후 나중에 소수가아니면 0으로 만드는 작업을 할건데,
                            // 시간을 많이 줄여야된다면 이 작업을 반대로해서 원래 0으로 초기화된 값을 써도 된다.
    }
    isPrime[0] = isPrime[1] = false;
    for(int i = 2; i * i <= MAX; ++i){
        if(isPrime[i]){ // 소수일때만 조사를 해주면 되는데, 소수가 아닐때라면 이미 소수일때 조사가끝났기때문에 조사할필요가없다.
                        // ex) 2의 배수 조사를 끝마쳤는데 4의 배수를 조사할 필요가 없는 것.
            for(int j = i*i; j <= MAX; j +=i){  // i*i부터 조사를 하는것은 i*1부터 i*i-1까지는 이미 다 끝남.
                                                // 3*1, 3*2까지는 조사를 다했음(j = 2*2일때부터 2의 배수만큼 더해져서 2*3으로.), 3*3을 조사하면 됨.
                    isPrime[j] = false;
            }
        }
    }

    for(int i = 0; i <= MAX; ++i){
        if(isPrime[i])
            cout << 1 << " ";
        else
            cout << 0 << " ";
    }

    return 0;
}


