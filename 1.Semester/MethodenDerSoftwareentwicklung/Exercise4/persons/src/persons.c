#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Hobby {
	char name[20];
};

struct Person {
	char firstname[20];
	char lastname[20];
	int age;
	struct Hobby hobbies[5];
};

int is_number(char const *arg) {
	int n;
	return (sscanf(arg, "%d", &n) == 1);
}

void emptyArray(char *aArray, int aLength) {
	for (int i = 0; i < aLength; ++i) {
		*(aArray + i) = '\0';
	}
}

void loadIntoStruct(struct Person *aGroupOfPersons, char *aInputText,
		int aPersonIdx) {

	int hIdx = 0;
	int hLineFromIdx = 0;
	int hStructIdx = 0;
	int hLengthOfArray = strlen(aInputText);

	while (hIdx <= hLengthOfArray) {
		char hCurrentChar = *(aInputText + hIdx);
		if (hCurrentChar == ';' || hCurrentChar == '\n'
				|| hCurrentChar == '\0') {

			int hTmpIdx = (hIdx - hLineFromIdx);
			char hTmp[hTmpIdx];

			strncpy(hTmp, (aInputText + hLineFromIdx), hTmpIdx);
			hTmp[hTmpIdx] = '\0';

			int hHobbyIdx = 0;
			int hLastIdx = 0;

			switch (hStructIdx) {
			case 0:
				strncpy(aGroupOfPersons[aPersonIdx].firstname, hTmp, 20);
				break;
			case 1:
				strncpy(aGroupOfPersons[aPersonIdx].lastname, hTmp, 20);
				break;
			case 2:
				aGroupOfPersons[aPersonIdx].age = (int) atoi(hTmp);
				break;
			case 3:
				for (int i = 0; i <= hTmpIdx; ++i) {
					char hTmpChar = *(hTmp + i);
					if (hTmpChar == ',' || i == hTmpIdx) {

						int hHoppyTmpIdx = (i - hLastIdx);
						char hHoppyTmp[hHoppyTmpIdx];
						strncpy(hHoppyTmp, (hTmp + hLastIdx), hHoppyTmpIdx);
						hHoppyTmp[hHoppyTmpIdx] = '\0';

						strncpy(
								aGroupOfPersons[aPersonIdx].hobbies[hHobbyIdx].name,
								hHoppyTmp, 20);

						emptyArray(hHoppyTmp, hHoppyTmpIdx);

						hLastIdx = i + 1;
						hHobbyIdx++;
					}
				}

				//Fill remaining places of hobby array
				while (hHobbyIdx <= 5) {
					char hHoppyTmp[20];
					emptyArray(hHoppyTmp, 20);
					strncpy(aGroupOfPersons[aPersonIdx].hobbies[hHobbyIdx].name,
							hHoppyTmp, 20);
					hHobbyIdx++;
				}

				break;
			}

			emptyArray(hTmp, hTmpIdx);

			hLineFromIdx = hIdx + 1;
			hStructIdx++;
		}
		hIdx++;
	}
}

int isInOutputGrp(struct Person aPerson) {

	if (aPerson.age > 20 && aPerson.age <= 30) {
		for (int k = 0; k < 5; ++k) {
			int isTanzen = strcmp(aPerson.hobbies[k].name, "Tanzen");
			if (isTanzen == 0) {
				return 1;
			}
		}
	}
	return 0;
}

int main(int argc, char **argv) {

	FILE *hInput = fopen("persons_input.txt", "r");

	if (hInput == NULL) {
		perror("Fehler!");
		return 1;
	}
	char buffer[255];

	int hAnzLines = 0;
	while (fgets(buffer, 255, hInput)) {
		hAnzLines++;
	}

	fseek(hInput, 0L, SEEK_SET);

	struct Person hPersons[hAnzLines];

	int hIdx = 0;
	while (fgets(buffer, 255, hInput)) {
		loadIntoStruct(hPersons, buffer, hIdx);
		hIdx++;
	}

	for (int i = 0; i < hAnzLines; ++i) {

		if (isInOutputGrp(hPersons[i])) {
			printf("%s\n", (hPersons[i].lastname));
		}

//
//		printf("FirstName: %s\n", (hPersons[i].firstname));
//		printf("Lastname: %s\n", (hPersons[i].lastname));
//		printf("Age: %d\n", (hPersons[i].age));
//		printf("Hobbies: \n");
//		for (int k = 0; k < 5; ++k) {
//			if (hPersons[i].hobbies[k].name[0] != '\0') {
//				printf("%d: %s\n", (k + 1), hPersons[i].hobbies[k].name);
//			}
//		}
//		printf("\n\n");
	}

	fclose(hInput);

	return 0;
}
