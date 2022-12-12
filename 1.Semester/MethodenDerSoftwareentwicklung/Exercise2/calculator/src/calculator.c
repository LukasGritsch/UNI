#include <stdio.h>
#include "operations.h"
#include <string.h>
#include <stdlib.h>

int main(int argc, char **argv) {

	if (argc != 4) {
		printf("Please enter a valid Opertaion eg 5 + 5\n");
		return 1;
	}

	char operator = argv[2][0];
	int hOne = atoi(argv[1]);
	int hTwo = atoi(argv[3]);
	int hErg = 0;

	switch (operator) {
	case '+':
		hErg = add(hOne, hTwo);
		break;
	case '-':
		hErg = sub(hOne, hTwo);
		break;
	case '*':
		hErg = mult(hOne, hTwo);
		break;
	case '/':
		if (hTwo == 0) {
			printf("Div througth 0 \n");
			return 1;
		}
		hErg = division(hOne, hTwo);
		break;
	default:
		printf("No valid operator (+,-,*,/)\n");
		return 1;
		break;
	}

	printf("%d\n", hErg);
	return 0;
}
