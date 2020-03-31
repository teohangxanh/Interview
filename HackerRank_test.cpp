#include <iostream>
#include <cmath>
#include <vector>
// #include "HackerRank_math.cpp"
using namespace std;

int workbook(int n, int k, vector<int> arr) {
    int i = 0;
    vector<vector<int>> v;
    for (int num: arr){
        int mul = num / k;
        if (num % k > 0) mul++;
        int count = 1;
        vector<int> a;
        for (int j = 1; j <= num; j++){
            a.push_back(j);
            count++;
            if (count == 3){
                v.push_back(a);
                vector<int> a;
                count = 1;
            }
            
        }
    }
    // for (int i = 0; i < v.size(); i++){
    //     for (int j = 0; j < v[i].size(); j++){
    //         cout << v[i][j] << " ";
    //     }
    //     cout << endl;
    // }
    return 0;
}

void print(vector<vector<int>> v){
    for (int i = 0; i < v.size(); i++){
        for (int j = 0; j < v[i].size(); j++){
            cout << v[i][j] << " ";
        }
        cout << endl;
    }
}

int main(){
    int n = 5, k = 3;
    vector <int> arr = {4, 2, 6, 1, 10};
    cout << workbook(n, k, arr);
    return 0;
}
