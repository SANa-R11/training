#include <stdio.h>

int N, Arr[20], i, X;

int main() {
    int count = 0;
    
    printf("Enter the size N of the array:\n");
    scanf("%d", &N);
    


    printf("Enter the array elements:\n");
    for (i = 0; i < N; i++) {
        scanf("%d", &Arr[i]);
    }
    
    printf("Enter the number X:\n");
    scanf("%d", &X);

    for (i = 0; i < N; i++) {
        if (Arr[i] == X) {
            count++;
        }
    }

    printf("The occurrence of X is %d times\n", count);

    return 0;
}
