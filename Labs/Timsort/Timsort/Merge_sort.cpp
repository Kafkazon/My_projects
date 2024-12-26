#include "Merge_sort.h"
pair<int,int> Merge_sort::sort(Vector vec, int start1, int end1, int start2, int end2){
    Vector ans;
    //cout << start1 << " " << end1 << " " << start2 << " " << end2 << endl;
    int a = start1, b = start2,countera = 0, counterb = 0,galop = 0;
    //int gal_a = 0, gal_b = 0;
    while (a < end1 || b < end2){
        if (a < end1) {
            if (vec[a] <= vec[b])
            {
                ans.push_back(vec[a]);
                a++;
                countera++;
                counterb = 0;
            }
        }
        else {
            while (b < end2) {
                ans.push_back(vec[b]);
                b++;
            }
        }
        if (b < end2) {
            if (vec[a] > vec[b])
            {
                counterb++;
                countera = 0;
                ans.push_back(vec[b]);
                b++;
            }
        }
        else {
            while (a < end1) {
                ans.push_back(vec[a]);
                a++;
            }
        }
        /*
        if (countera > 5) {
            galop = 1;
            gal_a = a;
            while (gal_a < end1 and vec[a] <= vec[b]) {
                gal_a+= galop;
                galop *= 2;
            }
            if (gal_a > end1) {
                gal_a = end1-1;
            }
            while (vec[gal_a] > vec[b]) {
                gal_a--;
            }
            for (int i = a; i <= gal_a; i++) {
                ans.push_back(vec[i]);
            }
            countera = 0;
            a = gal_a+1;
        }

        if (counterb > 5) {
            galop = 1;
            gal_b = b;
            while (gal_b < end2 and vec[a] > vec[b]) {
                gal_b += galop;
                galop *= 2;
            }
            if (gal_b > end2) {
                gal_b = end2 - 1;
            }
            while (vec[gal_b] > vec[a]) {
                gal_b--;
            }
            for (int i = b; i <= gal_b; i++) {
                ans.push_back(vec[i]);
            }
            counterb = 0;
            b = gal_b+1;
        }
        */
    }
    //cout << ans.length() << "\n\n";
   // ans.print();
    for (int i = min(start1, start2); i < max(end1, end2); i++) {
        //cout << ans[i - min(start1, start2)] << endl;

        vec[i] = ans[i - min(start1, start2)];
    }
    return make_pair(min(start1, start2), max(end1, end2));
}