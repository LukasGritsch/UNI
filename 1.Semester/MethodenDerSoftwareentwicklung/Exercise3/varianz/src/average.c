#include <stdio.h>

float getAverageAndVarianz(int *aArray, float *aVarainzPointer, int hSize) {

	//MIttelwert berechenen
	float hAvg = 0;

	for (int i = 0; i < hSize; ++i) {
		hAvg = hAvg + aArray[i];
	}

	hAvg = (float) hAvg / (float) hSize;

	//Varainaz berechnen
	float hVarianz = 0;
	for (int i = 0; i < hSize; ++i) {
		hVarianz = hVarianz + ((aArray[i] - hAvg) * (aArray[i] - hAvg));
	}

	int hSizeOfPointer = sizeof(aArray);
	int hSizeOfInt = sizeof(int);

	float hElements = hSizeOfPointer / hSizeOfInt;

	// Wert via Call by Value zuweisen
	*aVarainzPointer = hVarianz / hElements;

	return hAvg;
}

int main(int argc, char **argv) {
	int hAnzArray = 0;
	printf("Enter the size of the array :");
	scanf("%d", &hAnzArray);

	int hArray[hAnzArray];
	for (int i = 0; i < hAnzArray; ++i) {
		int hPlaceholder = 0;
		printf("Enter value #%d: ", i + 1);
		scanf("%d", &hPlaceholder);
		hArray[i] = hPlaceholder;
	}

	float hVarianz = 0;
	float hAVG = getAverageAndVarianz(hArray, &hVarianz, hAnzArray);

	printf("> Average: %.1f > Varianz: %.1f\n",hAVG,hVarianz);

	return 0;
}
