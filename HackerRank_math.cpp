#include <iostream>
#include <cmath>
#include <vector>
#include <string>
using namespace std;

/*
Author:         Ted Dang
Date created:   03/20/2020
Usage:          Returning if the sum of two halves of a number == itself
*/
// int checkHalvesSum(int n){
//     if countDigits(n % 2 == 0){
//
//     } else{
//
//     }
// }

/*
Author:         Ted Dang
Date created:   03/20/2020
Usage:          Returning the number of digits of a number
*/
bool coutDigits(int n){
    int count = 0;
    while (n > 0){
        count++;
        n /= 10;
    }
    return count;
}

/*
Author:         Ted Dang
Date created:   03/16/2020
Usage:          Returning power of a number
*/
double power(double num, int exp){
    if (exp == 0) return 1;
    double ans = num;
    for (int i = 2; i <= exp; i++){
        ans = ans * num;
    }
    return ans;
}

/*
Author:         Ted Dang
Date created:   03/16/2020
Usage:          Printing a vector
*/
void print(vector<int> v){
    for (int i = 0; i < v.size(); i++){
        cout << v[i] << endl;
    }
}

/*
Author:         Ted Dang
Date created:   03/16/2020
Usage:          Checking if the given number is prime
*/
bool isPrime(int n){
    for (int i = 2; i < sqrt(n); i++){
        if (n % i == 0) return false;
    }
    return true;
}

/*
Author:         Ted Dang
Date created:   03/16/2020
Usage:          Sum up all digits of a number
*/
int sumDigits(int n){
    int ans = 0;
    while (n > 0){
        int rem = n % 10;
        ans += rem;
        n /= 10;
    }
    return ans;
}

/*
Author:         Ted Dang
Date created:   03/16/2020
Usage:          Returning a vector of primes of the given number
*/
vector<int> findPrimes(int n){
    vector<int> primes;
    for (int i = 2; i < sqrt(n); i++){
        if (n % i == 0) primes.push_back(i);
        while (n % i == 0){
            n /= i;
        }
    }
    if (n != 1) primes.push_back(n);
    return primes;
}

/*
Author:         Ted Dang
Date created:   03/16/2020
Usage:          Summing up all digits of primes of a Smith number
*/
int sumSmith(int n){
    int ans = 0;
    for (int i = 2; i < sqrt(n); i++){
        while (n % i == 0){
            ans += sumDigits(i);
            n /= i;
        }
    }
    if (n != 1) ans += sumDigits(n);
    return ans;
}

/*
Author:         Ted Dang
Date created:   03/16/2020
Usage:          Checking if a number is a Smith number
*/
int isSmith(int n){
    return sumSmith(n) == sumDigits(n) && isPrime(n);
}

/*
Author:         Ted Dang
Date created:   03/16/2020
Usage:          Returning factorial of an interger mod m
*/
int fact(int n){
    int ans = 1;
    if (n == 0 || n == 1) return 1;
    else {
        for (int i = 2; i <= n; i++){
            ans *= i;
            cout << "i = " << i << endl;
            cout << "total = " << ans << endl;
            cout << endl;
            // cout << "n = " << i << endl;
            // cout << ans << endl;
        }
    }
    return ans;
}

/*
Author:         Ted Dang
Date created:   03/16/2020
Usage:          Returning permutation of n choose k mod m
*/
int permutation(int n, int k){
    int ans = 1;
	for (int i = n - k + 1; i <= n; i++){
        ans *= i;
    }
    return ans;
}
