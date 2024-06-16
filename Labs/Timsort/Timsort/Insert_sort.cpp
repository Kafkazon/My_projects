#include "Insert_sort.h"
#include "Vector.h"

Vector Insert_sort::sort(Vector vec, int start, int end) {
    for (int i = start + 1; i < end; i++) {
        int x = vec[i];
        int j = i;
        while (j > start and vec[j - 1] > x){
            vec[j] = vec[j - 1];
            j = j - 1;
        }
        vec[j] = x;
    }
	return vec;
}