#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void addSpaces(int aAnz, char *aVarToAdd) {
	for (int l = 0; l < aAnz; ++l) {
		strcat(aVarToAdd, " ");
	}
}

void addStars(int aAnz, char *aVarToAdd) {
	for (int k = 0; k < aAnz; ++k) {
		strcat(aVarToAdd, "*");
	}
}

int getAnzChar(int aIdx){
	int hRet = 1;
	for (int i = 0; i < aIdx; ++i) {
		hRet = hRet + aIdx + 4;
	}
	return hRet;
}

int main(int argc, char **argv) {

	if (argc <= 1) {
		printf("Please enter a number\n");
		return 1;
	}

	int hInput = atoi(argv[1]);
	int hStarIdx = 1;
	int hSpaceIdx = hInput -1 ;

	int hAnzChar = getAnzChar(hInput);

	char hRetStr[hAnzChar];
	memset(hRetStr, 0, sizeof hRetStr);

	for (int i = 0; i < (hInput -1 ); ++i) {

		addSpaces(hSpaceIdx, hRetStr);
		addStars(hStarIdx, hRetStr);
		addSpaces(hSpaceIdx, hRetStr);

		strcat(hRetStr, "\n");
		hStarIdx = hStarIdx + 2;
		hSpaceIdx = hSpaceIdx - 1;
	}

	printf("%s", hRetStr);
	fflush(stdout);
	return 0;
}
