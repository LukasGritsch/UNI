#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int isNumber(char *aChar, int alength) {
	for (int i = 0; i < alength; ++i) {
		int isNumberVar = (aChar[i] >= '0' && aChar[i] <= '9') || aChar[i] == '\n';
		if (isNumberVar != 1) {
			return 0;
		}
	}

	return 1;
}

int isExit(char *aChar) {
	int hComp = strcmp("exit\n", aChar);
	return hComp;
}

void resetAll(int *aNumber1, int *aNumber2, char aOperator[1]) {
	*aNumber1 = 0;
	*aNumber2 = 0;
	aOperator[0] = '\0';
}

void callError(int *aNumber1, int *aNumber2, char aOperator[1]) {
	fputs("Falsche Eingabe!\n", stderr);
	fflush(stderr);
	resetAll(aNumber1, aNumber2, aOperator);
}

int isValidOperator(char aChar[1]) {

	if (aChar[0] == '+') {
		return 1;
	} else if (aChar[0] == '*') {
		return 1;
	} else if (aChar[0] == '/') {
		return 1;
	} else if (aChar[0] == '-') {
		return 1;
	} else {
		return 0;
	}
}

int add(int a, int b) {
	return a + b;
}

int sub(int a, int b) {
	return a - b;
}

float division(int a, int b) {
	return (float)a / (float)b;
}

int mult(int a, int b) {
	return a * b;
}

int main(int argc, char **argv) {
	char buffer[255];
	int hNumber1 = 0;
	int hNumber2 = 0;
	char hOperation[1];
	hOperation[0] = '\0';

	while (1) {

		if (hNumber1 == 0) {
			printf("Geben Sie Zahl 1 ein:\n");
			fflush(stdout);
			fgets(buffer, 255, stdin);

			if (isExit(buffer) == 0) {
				printf("Rechner wird geschlossen\n");
				fflush(stdout);
				return 0;
			}

			if (isNumber(buffer, strlen(buffer))) {
				hNumber1 = atoi(buffer);
			} else {
				callError(&hNumber1, &hNumber2, hOperation);
			}
		} else if (hOperation[0] == '\0') {
			printf("Geben Sie die Operation ein:\n");
			fflush(stdout);
			fgets(buffer, 255, stdin);

			if (isExit(buffer) == 0) {
				printf("Rechner wird geschlossen\n");
				fflush(stdout);
				return 0;
			}

			if (isValidOperator(buffer)) {
				strncpy(hOperation, buffer, 1);
			} else {
				callError(&hNumber1, &hNumber2, hOperation);
			}
		} else if (hNumber2 == 0) {
			printf("Geben Sie Zahl 2 ein:\n");
			fflush(stdout);
			fgets(buffer, 255, stdin);

			if (isExit(buffer) == 0) {
				printf("Rechner wird geschlossen\n");
				fflush(stdout);
				return 0;
			}

			if (isNumber(buffer, strlen(buffer))) {
				hNumber2 = atoi(buffer);
			} else {
				callError(&hNumber1, &hNumber2, hOperation);
			}
		} else {
			switch (hOperation[0]) {
			case '+':
				printf("Ergebnis: %d\n", add(hNumber1, hNumber2));
				fflush(stdout);
				break;
			case '-':
				printf("Ergebnis: %d\n", sub(hNumber1, hNumber2));
				fflush(stdout);
				break;
			case '*':
				printf("Ergebnis: %d\n", mult(hNumber1, hNumber2));
				fflush(stdout);
				break;
			case '/':
				if (hNumber2 == 0) {
					callError(&hNumber1, &hNumber2, hOperation);
				}
				printf("Ergebnis: %.1f\n", division(hNumber1, hNumber2));
				fflush(stdout);
				break;
			}
			resetAll(&hNumber1, &hNumber2, hOperation);
		}
	}
}
