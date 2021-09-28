#include <stdio.h>
int main() {
    int numberofinputs;
    printf("Enter the number of inputs: ");
    scanf("%d", &numberofinputs);
    int list[numberofinputs];
    int i;
    printf("Enter the %d numbers: \n", numberofinputs);
    for (i = 0; i<numberofinputs; ++i) {
        scanf("%d", &list[i]);
    }
    size_t listlength = sizeof(list)/sizeof(list[0]);
    int x;
    for (size_t x = 0; x<listlength; ++x) {
        printf("%d ", list[x]);
    }
    printf("\n");
    size_t listlength1 = sizeof(list)/sizeof(list[0]);
    int y;
    int z;
    int a;
    for (size_t y = 0; y<listlength1; ++y) {
        for (z = 0; z<listlength1 - y - 1; ++z) {
            if (list[z]>list[z + 1]) {
                a = list[z];
                list[z] = list[z + 1];
                list[z + 1] = a;
            }
            else if (list[z]<list[z + 1]) {
                ;
            }
        }
    }
    size_t listlength2 = sizeof(list)/sizeof(list[0]);
    int b;
    for (size_t b = 0; b<listlength2; ++b) {
        printf("%d ", list[b]);
    }
    return 0;
}