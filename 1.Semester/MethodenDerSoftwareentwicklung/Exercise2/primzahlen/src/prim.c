#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int isPrim(int aNumber) {
	if (aNumber < 2) {
		return 0;
	} else if (aNumber == 2) {
		return 1;
	} else {
		for (int i = 1; i < (aNumber / 2) + 1; ++i) {
			if (i != 1 && i != aNumber && (aNumber % i) == 0) {
				return 0;
			}
		}
		return 1;
	}
}

int main(int argc, char **argv) {

	if (argc <= 1) {
		printf("Please enter a valid number. (e.g. .\\prim 100)\n");
		return 1;
	}

	int hInput = atoi(argv[1]);
	int hOutputCounter = 0;

	for (int i = 0; i < hInput; ++i) {
		if (isPrim(i) == 1) {
			if (hOutputCounter == 9) {
				printf("\t%d\n", i);
				fflush(stdout);
				hOutputCounter = 0;
				continue;
			} else if (hOutputCounter == 0) {
				printf("%d", i);
				fflush(stdout);
			} else {
				printf("\t%d", i);
				fflush(stdout);
			}
			hOutputCounter = hOutputCounter +1;
		}
	}
	return 0;
}
