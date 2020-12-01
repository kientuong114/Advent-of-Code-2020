#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    FILE *f = fopen("1.in", "r");
    char* line;
    size_t len = 0;
    ssize_t read;
    char lines[200][5];
    int i, j, n1, n2;
    char* endptr;

    i = 0;

    while ((read = getline(&line, &len, f)) != -1){
        strcpy(lines[i++], line);
    }

    fclose(f);

    for(i = 0; i < 200; i++){
        n1 = strtol(lines[i], &endptr, 10);
        for(j = i; j < 200; j++){
            n2 = strtol(lines[j], &endptr, 10);
            if(n1 + n2 == 2020){
                printf("%d\n", n1*n2);
                return 0;
            }
        }
    }
}
