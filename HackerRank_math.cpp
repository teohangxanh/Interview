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

/* This function returns cosine of the angle to x-axis*/
double findCos(double slope){
    double c = sqrt(1 + slope*slope);
    return slope / c;
}

/* This function returns sine of the angle to x-axis*/
double findSin(double slope){
    double c = sqrt(1 + slope*slope);
    return 1 / c;
}

/* This class store location of a point in 2D*/
class Location{
    public:
        double cord_x;
        double cord_y;

        // Constructor
        Location(){
            cord_x = 0;
            cord_y = 0;
        }
        Location(double x, double y){
            cord_x = x;
            cord_y = y;
        }
};

/* This class represents a square */
class Square{
    public:
        Location bl;
        Location br;
        Location tl;
        Location tr;

        //Constructor
        Square(double x, double y, double lengthSide){
            bl.cord_x = x;
            bl.cord_y = y;
            br.cord_x = x + lengthSide;
            br.cord_y = y;
            tl.cord_x = x;
            tl.cord_y = y+ lengthSide;
            tr.cord_x = x + lengthSide;
            tr.cord_y = y + lengthSide;
        }

        void shiftH(double magnitude){
            bl.cord_x += magnitude;
            br.cord_x += magnitude;
            tl.cord_x += magnitude;
            tr.cord_x += magnitude;
        }

        void shiftV(double magnitude){
            bl.cord_y += magnitude;
            br.cord_y += magnitude;
            tl.cord_y += magnitude;
            tr.cord_y += magnitude;
        }

        void shiftVelo(double slope, double velo){
            bl.cord_x =
        }
};
