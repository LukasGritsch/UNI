#include <stdio.h>
#include <string.h>

char* extractNumbersFromLine(char *aString) {

	char hRetStr[strlen(aString)];

	int hIdx = 0;

	if (*aString == '\n') {
		return " ";
	} else {

		for (int i = 0; i < strlen(aString); ++i) {
			if (aString[i] >= '0' && aString[i] <= '9') {
				hRetStr[hIdx] = aString[i];
				hIdx++;
			} else if (hIdx != 0 && hRetStr[hIdx - 1] != ' ') {
				hRetStr[hIdx] = ' ';
				hIdx++;
			}
		}

		if (hRetStr[0] >= '0' && hRetStr[0] <= '9') {
			hRetStr[hIdx] = '\0';
			char *hToRet = (char*) hRetStr;
			return hToRet;
		} else {
			return " ";
		}
	}
}

int main(int argc, char **argv) {

	char hInput[255];
	char *hPointer = "init";
	char hOutput[254] = "";

	printf("Geben Sie einen Text ein!\n");
	while (*hPointer != '\n') {
		hPointer = fgets(hInput, 255, stdin);
		char *hNumbersInLine = extractNumbersFromLine(hInput);
		strcat(hOutput, hNumbersInLine);
		strcat(hOutput, "\n");
	}
	printf("Ende der Eingabe");

	FILE *hOutputFile = fopen("integers_output.txt", "w");

	if (hOutputFile == NULL) {
		perror("Fehler!");
		return 1;
	}

	fprintf(hOutputFile,"%s", hOutput);
	fflush(hOutputFile);
	fclose(hOutputFile);

	return 0;
}
