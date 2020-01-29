#include <iostream>
#define MAX 1000

using namespace std;

int main(void){
    bool isPrime[MAX] = { 0, };

    for(int i = 2; i < MAX; ++i){
        isPrime[i] = true;
    }

    for(int i = 2; i*i < MAX; ++i){ //루트MAX 보다 작은 수의 배수만 조사해서 다 없애면 된다.
        if(isPrime[i]){
            for(int j = i*i; j < MAX; j += i)
                isPrime[j] = false;
        }
    }

    for(int i = 0; i < MAX; ++i){
        if(isPrime[i])
            cout << 1 << " ";
        else
            cout << 0 << " ";
    }

    return 0;
}
