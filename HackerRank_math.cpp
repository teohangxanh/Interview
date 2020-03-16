#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

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
        while (n % i == 0){
            primes.push_back(i);
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


/* This function returns factorial of an interger*/
int fact(int n){
    int ans = 1;
    if (n < 2) return 1;
    else {
        for (int i = n; i > 1; i--){
            ans *= i;
        }
    }
    return ans;
}

/* This function returns a combination of n choose k*/
int combination(int n, int k){
	return fact(n) / (fact(n-k) * fact(k));
}
