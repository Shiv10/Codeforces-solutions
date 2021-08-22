#include <iostream>
using namespace std;

int main(){
    int n, t, i;
    cin>>n>>t;
    int start, end, sum;
    
    int a[n];
    for(i=0;i<n;i++){
        cin>>a[i];
    }
    start = -1;
    end = -1;
    int max = 0;
    sum = 0;

    if (n == 1 && a[0]>t){
        cout<<0;
        return 0;
    }

    for(i=0;i<n;i++){

        if (a[i]>=t){
            sum = 0;
            start = i+1;
            continue;
        }

        if (a[i]+sum <= t){
            sum += a[i];
            end = i+1;
            if (start ==-1) {
                start = i;
            }
        }
        else {
            while(sum+a[i]>t){
                sum -= a[start];
                start++;
            }
            end = i+1;
            sum += a[i];
        }

        if ((end - start)>max){
            max = end - start;
        }
    }

    cout<< max;

    return 0;
}