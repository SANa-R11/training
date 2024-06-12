#include <stdio.h>

int N, Arr[20], i, j, temp;

int main() {
    printf("Enter the size N of the array:\n");
    scanf("%d", &N);
    
    if (N > 20) {
        printf("Array size should not exceed 20.\n");
        return 1;
    }

    printf("Enter the array elements:\n");
    for (i = 0; i < N; i++) {
        scanf("%d", &Arr[i]);
    }

    for (i = 0; i < N - 1; i++) {
        for (j = 0; j < N - i - 1; j++) {
            if (Arr[j] < Arr[j + 1]) {  
                temp = Arr[j];
                Arr[j] = Arr[j + 1];
                Arr[j + 1] = temp;
            }
        }
    }

    printf("The greatest element is: %d\n", Arr[0]);
    printf("The second greatest element is: %d\n", Arr[1]);

    return 0;
}
