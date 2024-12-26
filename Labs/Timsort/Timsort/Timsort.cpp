#include "Timsort.h"

Vector Timsort::sort(Vector vec) {
	int n = vec.length();
	// Вычисление minrun
	int r = 0,m=n;           
	while (m >= 64) {
		r |= m & 1;
		m >>= 1;
	}
	int minrun = m + r;
	cout << "minrun = " << minrun << endl;

	// Деление на подмассивы и их сортировка
	int start, end = vec.length(), i = 0, j;
	bool flag1 = false;
	Vector store;
	Insert_sort insertion;
	while(i < n){
		start = i;
		i++;
		j = 2;
		if (i < n) {
			while (vec[start] == vec[i] and i<n-1) {
				i++;
				j++;
			}
			if (vec[start] > vec[i]) {
				flag1 = false;
			}
			else {
				flag1 = true;
			}
			if (flag1) {
				while ((j <= minrun || vec[i] >= vec[i - 1]) and i < n) {
					i++;
					j++;
				}
				end = i;
			}
			if (!flag1) {
				while ((j <= minrun || vec[i] <= vec[i - 1]) and i < n) {
					i++;
					j++;
				}
				end = i;
			}
		}
		store.push_back(start);
		store.push_back(end);
		vec = insertion.sort(vec, start, end);
	}
	// Cлияние подмассивов
	Stek stek;
	Merge_sort mer;
	int  count_stek=0,point,a1,b1;
	pair<int, int> tem, some, size_store;
	bool flag_izm;
	stek.push(store[0], store[1]);
	point = 2;
	count_stek=1;
	while (count_stek > 1 || point < store.length()) {
		
		if (point < store.length()) {
			a1 = store[point];
			b1 = store[point + 1];
			point+=2;
			if (count_stek == 1) {
			
				if (b1 - a1 >= stek.get().second - stek.get().first) {
					tem = mer.sort(vec, a1, b1, stek.get().first, stek.get().second);
					stek.pop();
					stek.push(tem.first, tem.second);
				}
				else {
					size_store.first = stek.get().first;
					size_store.second = stek.get().second ;
					stek.push(a1, b1);
					count_stek++;
				}
			}
			else {
				flag_izm = true;
				while (count_stek > 1 and flag_izm) {
					flag_izm = false;
					if (size_store.second - size_store.first <= stek.get().second - stek.get().first + b1 - a1) {
						if (size_store.second - size_store.first < b1 - a1) {
							flag_izm = true;
							tem = mer.sort(vec, size_store.first, size_store.second, stek.get().first, stek.get().second);
							stek.pop();
							stek.pop();
							if (stek.get().second != -1) {
								size_store.first = stek.get().first;
								size_store.second = stek.get().second;
							}
							stek.push(tem.first, tem.second);
							count_stek--;
						}
						else {
							tem = mer.sort(vec, a1, b1, stek.get().first, stek.get().second);
							a1 = tem.first;
							b1 = tem.second;
							
							stek.pop();
							if (stek.get().second != -1) {
								size_store.first = stek.get().first;
								size_store.second = stek.get().second;
							}
							count_stek--;
						}
					}
					if (stek.get().second - stek.get().first <= b1 - a1) {
						flag_izm = true;
						tem = mer.sort(vec, a1, b1, stek.get().first, stek.get().second);
						a1 = tem.first;
						b1 = tem.second;
						stek.pop();
						if (stek.get().second != -1) {
							size_store.first = stek.get().first;
							size_store.second = stek.get().second;
						}
						count_stek--;
					}
				}
				size_store.first = stek.get().first;
				size_store.second = stek.get().second;
				stek.push(a1, b1);
				count_stek++;
			}
		}
		else {
			while (count_stek > 1) {
				start = stek.get().first;
				end = stek.get().second;
				stek.pop();
				tem = mer.sort(vec, start, end, stek.get().first, stek.get().second);
				stek.pop();
				stek.push(tem.first, tem.second);
				count_stek--;
			}
		}
	}
	return vec;
}