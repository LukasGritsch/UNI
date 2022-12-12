#include <stdio.h>
#include <string.h>
//Wert berechnen, welcher vom Uppercase subtrahiert werden muss
const char ASCII_SPACE = 'a' - 'A';

// Herausfinden, ob der übergebene Buchstabe ein Kleinbuchstabe ist
int isLower(char ch){
	if (ch >= 'a' && ch <= 'z') {
		return 1;
	}else{
		return 0;
	}
}

// Kleinbuchstabe in Großbuchstabe umwandeln
void toUpperCase(char* c){
	*c -= ASCII_SPACE;
}

int main(int argc, char **argv) {
	char input[50];


	printf("Enter a string : ");
	scanf("%[^\n]", input);

	if(strlen(input) > 0 && strlen(input) < 50){
		for (int i = 0; i < strlen(input);  i++) {
			if(isLower(input[i]) == 1){
				toUpperCase(&input[i]);
			}
			printf("%c",input[i]);
		}
	}else{
		printf("The input must be less than 50 characters!\n");
	}

	return (0);
}
