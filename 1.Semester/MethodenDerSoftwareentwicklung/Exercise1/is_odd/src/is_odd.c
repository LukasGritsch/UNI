#include <stdio.h>
#include <stdlib.h>

int isOdd(int aNumber){
	return (aNumber % 2) != 0;
}

int main(int argc, char *argv[])
{

    if (argc <= 1) {
        printf("false\n");
        return 0;
    }

    int hNumber = atoi(argv[1]);
    if(!isOdd(hNumber)){
    	printf("false\n");
    	return 0;
    }

    printf("true\n");
    return 0;
}
