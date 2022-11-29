#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {

	if (argc <= 1) {
		return 0;
	}

	int hIdx = 1;
	int hSum = 2;

	while (hSum < atoi(argv[1])){
		hSum = hSum * 2;
		hIdx = hIdx + 1;
	}

	if(hSum == atoi(argv[1])){
		printf("%d\n",hIdx);
	}

}
