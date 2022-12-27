#include <stdio.h>
#include <string.h>

// The command ./frequency Hallo Welt! has 3 parameters, which means there has to be 1 space between the given string
int evaluateSpace(int aAntParameter) {
	return aAntParameter - 2;
}

int evaluateLenOfReusltString(char **aArrayOfPointer, int aAnzParameter) {
	int hIdx = 1;
	int hRet = 0;
	while (hIdx < aAnzParameter) {
		char *hTmp = (char*) *(aArrayOfPointer + hIdx);
		hRet = hRet + strlen(hTmp);
		hIdx++;
	}
	return hRet;
}

char* createInputString(char **aArrayOfPointer, int aAnzParameter) {
	char hRet[evaluateLenOfReusltString(aArrayOfPointer, aAnzParameter)
			+ evaluateSpace(aAnzParameter)];
	int hIdx = 1;
	int hIdxResultArray = 0;

	while (hIdx < aAnzParameter) {
		char *hTmp = (char*) *(aArrayOfPointer + hIdx);
		int hLen = strlen(hTmp);

		int hArrayIdx = 0;

		if (hIdx != 1) {
			*(hRet + hIdxResultArray) = ' ';
			hIdxResultArray++;
		}

		while (hArrayIdx < hLen) {
			char hTmpChar = *(hTmp + hArrayIdx);
			*(hRet + hIdxResultArray) = hTmpChar;
			hArrayIdx++;
			hIdxResultArray++;
		}
		hIdx++;
	}
	*(hRet + hIdxResultArray) = '\0';
	char *hRet1 = (char*)hRet;
	return hRet1;
}

int countCharsInASCII(char *aArray, char aChar) {
	int hLen = strlen(aArray);
	int hIdx = 0;
	int hRet = 0;

	while (hIdx < hLen) {
		if (*(aArray + hIdx) == aChar) {
			hRet++;
		}
		hIdx++;
	}
	return hRet;
}

int doesCharExists(char *aArray, char aChar) {
	int hLen = strlen(aArray);
	int hIdx = 0;

	while (hIdx < hLen) {
		if (*(aArray + hIdx) == aChar) {
			return 1;
		}
		hIdx++;
	}
	return 0;
}

int getMaxASCII(char *aArray) {
	int hLen = strlen(aArray);
	int hIdx = 0;
	int hRet = 0;

	while (hIdx < hLen) {

		int hTmp = *(aArray + hIdx);

		if (hTmp > hRet) {
			hRet = hTmp;
		}

		hIdx++;
	}
	return hRet;
}

void checkASCIITable(char *aArray) {

	for(int i = 0; i <= getMaxASCII(aArray); i++){
		if(doesCharExists(aArray, i)){
			int hTmp = countCharsInASCII(aArray, i);
			printf("The character '%c' was found %d times\n",i,hTmp);
		}
	}
}

int main(int argc, char **argv) {

	if (argc < 1) {
		printf("Please enter a valid parameter!\n");
		return 1;
	}

	checkASCIITable(createInputString(argv, argc));
}
