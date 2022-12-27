#include <stdio.h>
#include <string.h>

struct {
	int id;
	char name[9];
} test;

int main(int argc, char **argv) {
	test.id = 256;
	strncpy(test.name,"test\0",9);

	printf("Size of struct:  %ld\n",sizeof(test));
	printf("Size of id:  %ld\n",sizeof(test.id));
	printf("Size of name:  %ld\n",sizeof(test.name));
	printf("Size of Pointer %ld:  %ld\n",strlen(test.name),sizeof(test.id));
	fprintf(stderr,"This is an error");
}

