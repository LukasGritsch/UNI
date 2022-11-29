#include <stdio.h>

int main(int argc, char **argv) {
	int hSum = 0;
	int hIdx = 2;
	while (hIdx < 1000) {
		hSum = hSum + hIdx;
		hIdx += 8;
	}
	printf("%d\n", hSum);
}
