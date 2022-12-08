#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// week 3 Q1
int calcAbsoluteDifference(int n){
    if (n>51){
        return 3 * abs(n-51);
    }
    return abs(n-51);
}

// week 3 Q2
bool isThirty(int a, int b){
    
    if (a == 30 || b == 30){
        return true;
    } else if ((a+b) == 30){
        return true;
    } else {
        return false;
    }
}

// week 3 Q3
int computeSum(int a, int b){
    int sum = a+b;
    if (sum>9 && sum<=20){
        return 30;
    }
    return sum;
}

// week 3 Q4
bool ifItsFive(int a, int b){
    int sum = a+b;
    int diff = a-b;
    
    if (sum == 5 || diff == 5 || a == 5 || b == 5){
        return true;
    }
    return false;
}

// week 3 Q5
void isGreater(int x, int y, int z){
    
    if (y>x){
        printf("\ny > x");
    } 
    if (z>y){
        printf("\nz > y");
    }
}

int reduce(int a){
    while (a>10){
        a = a % 10;
    }
    return a;
}

// Week 3 Q6
bool sameRightmost(int a, int b){
    a = reduce(a);
    b = reduce(b);
    printf("\na reduced to %d. and b reduced to %d", a, b);
    if (a==b){
        return true;
    }
    return false;
}

// week 4
struct Employee {
    char name[50];
    int age;
    double salary;
    int years;
    char title[50];
};

struct Module {
    char name[50];
    int credits;
};

struct Student {
    char name[50];
    int age;    
    struct Module modules[10];
    int index;
};

struct Manager {
    char name[50];
    int age;
    double salary;
    struct Employee employees[100];
    int index;
};

void printModule(struct Module m){
    printf("\nNAME:%s, CREDITS:%d", m.name, m.credits);
}

void printStudent(struct Student s){
    printf("\nNAME:%s, AGE:%d", s.name, s.age);
    printf("\nMODULES:");
    for(int i =0; i<s.index; i++){
        printModule(s.modules[i]);
    }
}

int main()
{
    
    int n = 20;
    printf("result was %d", calcAbsoluteDifference(n));
    
    bool res = isThirty(10, 20);
    printf("\nresult was %s ", res ? "true" : "false");

    printf("\nresult was %d ", computeSum(9,10));
    
    res = ifItsFive(9,4);
    printf("\nresult was %s ", res ? "true" : "false");
    
    isGreater(2, 10, 100);
    
    res = sameRightmost(96,46);
    printf("\nresult was %s ", res ? "true" : "false");
    
    
    // week 4
    
    struct Module m1 = { "Introduction to Python", 5 };
    struct Module m2 = { "Databases", 5 };
    struct Student john = { "john", 20 };
    
    john.modules[john.index++] = m1;
    john.modules[john.index++] = m2;
    printStudent(john);
    // do the same for the Manager and the Employee
    
    return 0;
}