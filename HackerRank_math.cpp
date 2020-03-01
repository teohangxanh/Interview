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