/*
 ============================================================================
 Name        : HellloWorld.c
 Author      : 
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

char* foo(int x) {
	char *hRet;
	if (x < 0) {
		hRet = "x is negativ\n";
	} else {
		hRet = "x is positiv\n";
	}
	return hRet;
}

int main(void) {
	printf("!!!Hello World!!!\n"); /* prints !!!Hello World!!! */
	for (int i = 0; i < 10; i++) {
		printf(foo(4));
	}
	return 0;
}
