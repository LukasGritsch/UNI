#include "my_string.h"
#include <stdio.h>
//Counts the steps until \0 is reached
unsigned int string_len(const char *str) {

	int hCount = 0;

	while (*(str + hCount) != '\0') {
		hCount++;
	}

	return hCount;
}

int string_cmp(const char *str1, const char *str2) {

	int hLen1 = string_len(str1);
	int hLen2 = string_len(str2);

	if (hLen1 != hLen2) {
		return 0;
	}

	for (int i = 0; i < hLen1; ++i) {
		if (str1[i] != str2[i]) {
			return 0;
		}
	}
	return 1;
}

void string_rev(unsigned char *str) {

	int hLenStr = 0;

	while (*(str + hLenStr) != '\0') {
		hLenStr++;
	}

	if (hLenStr < 1) {
		return;
	}

	int temp = 0;

	for (int i = 0; i < hLenStr / 2; i++) {
		temp = str[i];
		str[i] = str[hLenStr - i - 1];
		str[hLenStr - i - 1] = temp;
	}
}


char* string_chr(const char *str, const char c) {

	int hLen = string_len(str);

	for (int i = 0; i < hLen; ++i) {
		if (str[i] == c) {
			return (char*) str + i;
		}
	}

	return NULL;
}
