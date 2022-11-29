#include <stdio.h>
#include <string.h>

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

int main(int argc, char **argv) {

	int hStarIdx = 1;
	int hSpaceIdx = 2;
	char hRetStr[21] = "";

	for (int i = 0; i < 3; ++i) {

		addSpaces(hSpaceIdx, hRetStr);
		addStars(hStarIdx, hRetStr);
		addSpaces(hSpaceIdx, hRetStr);

		strcat(hRetStr, "\n");
		hStarIdx = hStarIdx + 2;
		hSpaceIdx = hSpaceIdx - 1;
	}

	printf("%s", hRetStr);
	return 0;
}
