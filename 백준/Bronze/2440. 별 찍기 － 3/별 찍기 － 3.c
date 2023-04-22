#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    for (int i = n; i >= 1; i--) { // 5 4 3 2 1
        for (int j = 1; j <= i; j++) printf("*");
        printf("\n");
    }

    return 0;
}