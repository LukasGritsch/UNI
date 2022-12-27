#include "xmas_sort.h"

void xmas_sort(int* array, const int n){
	int hSortPlace = 1;
	while (hSortPlace < n){
		int hLeftItem = (int) *(array + (hSortPlace -1));
		int hRigthItem = (int) *(array + hSortPlace);

		if(hLeftItem <= hRigthItem){
			hSortPlace++;
		}else{
			*(array + (hSortPlace -1)) = hRigthItem;
			*(array + hSortPlace) = hLeftItem;

			if(hSortPlace > 1){
				hSortPlace--;
			}
		}
	}
}
