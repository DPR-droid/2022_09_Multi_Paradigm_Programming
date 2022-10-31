// Objectives
// Create Structs for the following 
    // • An employee (name, age, salary, years worked, job title)
    // • Manager (name, age, salary, an array of the employees they manage)
    // • A college module (module name, credits it is worth)
    // • Student (name, age, an array of their college modules)
    // The student structure should have internally an array of college modules. 
    //The same goes for the manager and their employees. In Listing 2 we have a partial solution for some of the above tasks. 
    // We have a Student structure which holds an array of 10 modules, this means that each student we create can have 10 modules. 
    // We add two modules to the student struct and we print them out. 
    // You can expand on this to add all the other information specified above such as name and age. 
    // It would be useful to keep track of how many modules have been added to each student, 
    // so that we know what index to place the next one. This can be done by storing an integer in the struct to keep track. 
    // For each struct type create a print method which outputs to the console all the information stored in the struct.


#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// An employee struct (name, age, salary, years worked, job title)
struct Employee {
    char* name;
    int age;
    int salary;
    int years;
    char jobtitle [20];
};

// Manager (name, age, salary, an array of the employees they manage)
struct Manager {
    char* name;
    int age;
    int salary;
    char jobtitle [20];
    struct Employee emp [10];
};

// A college module (module name, credits it is worth)
struct Module {
    char name [50];
    int credits;
    } m;  

// Student (name, age, an array of their college modules)
struct Student {
    char* name;
    int age;
    struct Module modules [10];
    } s;


// Print
void printModule ( struct Module module ){
    printf (" the module name is %s\n", module . name );
    };


// PrintStudent Modules
void printStudent ( struct Student student00 ){
    int i;
    printf(" Students name %s\n", student00.name);
    printf(" Age %d\n List of modules taken\n", student00.age);
    for (i = 0; i < 10; ++i) {
        i + 1;
        printf("%s\n", &student00.modules[i]);
        };
    };



// Main
int main ( void )
    {  
    //////////////////////////////////////////////////////////////////////
    // Set the modules
    // char name [50];
    // int credits;
    //////////////////////////////////////////////////////////////////////
    struct Module module00 = { " Programming_00 ", 5 };
    struct Module module01 = { " Programming_01 ", 10 };
    struct Module module02 = { " Programming_02 ", 5 };
    struct Module module03 = { " Programming_03 ", 5 };
    struct Module module04 = { " Programming_04 ", 5 };
    struct Module module05 = { " Programming_05 ", 20 };
    struct Module module06 = { " Programming_06 ", 10 };
    struct Module module07 = { " Programming_07 ", 5 };
    struct Module module08 = { " Programming_08 ", 15 };
    struct Module module09 = {  " Programming_09 ", 5 };

    //////////////////////////////////////////////////////////////////////
    // Student with age and modules 
    //////////////////////////////////////////////////////////////////////
    struct Student student00 = {"David", 23};
    student00 . modules [0] = module01 ;
    student00 . modules [1] = module02 ;
    student00 . modules [2] = module03 ;
    student00 . modules [3] = module04 ;
    student00 . modules [4] = module05 ;
    student00 . modules [5] = module06 ;
    student00 . modules [6] = module07 ;
    student00 . modules [7] = module08 ;
    student00 . modules [8] = module09 ;
    student00 . modules [9] = module00 ;

    //////////////////////////////////////////////////////////////////////
    // Second Student Test
    //////////////////////////////////////////////////////////////////////
    // struct Student student01 = {"Peter", 35, 102};
    // student01 . modules [0] = module08 ;
    // student01 . modules [1] = module09 ;
    // printf(" the module name is %s, age %d, module enrolled %s\n", student01.name, student01.age, student01.modules[0] );
    // printf(" the module name is %s, age %d, module enrolled %s\n", student01.name, student01.age, student01.modules[1] );

    //////////////////////////////////////////////////////////////////////
    // Printf 
    // testing of printf of structs for Student and modules 
    //////////////////////////////////////////////////////////////////////
    // printf(" the module name is %s, age %d, module enrolled %s\n", student00.name, student00.age, student00.modules[0] );
    // printf(" the module name is %s, age %d, module enrolled %s\n", student00.name, student00.age, student00.modules[1] );
    // printf(" the module name is %s, age %d, module enrolled %s\n", student00.name, student00.age, student00.modules[2] );
    // printf(" the module name is %s, age %d, module enrolled %s\n", student00.name, student00.age, student00.modules[3] );
    // printf(" the module name is %s, age %d, module enrolled %s\n", student00.name, student00.age, student00.modules[4] );
    // printf(" the module name is %s, age %d, module enrolled %s\n", student00.name, student00.age, student00.modules[5] );
    // printf(" the module name is %s, age %d, module enrolled %s\n", student00.name, student00.age, student00.modules[6] );
    // printf(" the module name is %s, age %d, module enrolled %s\n", student00.name, student00.age, student00.modules[7] );
    // printf(" the module name is %s, age %d, module enrolled %s\n", student00.name, student00.age, student00.modules[8] );
    // printf(" the module name is %s, age %d, module enrolled %s\n", student00.name, student00.age, student00.modules[9] );

    // int i;
    // printf(" Students name %s\n", student00.name);
    // printf(" Age %d\n List of modules taken\n", student00.age);
    // for (i = 0; i < 10; ++i) {
    //     i + 1;
    //     printf("%s\n", &student00.modules[i]);
    // };

    
    // printModule ( student . modules [0]) ;
    // printModule ( student . modules [1]) ;
    // Print Student00 
    printStudent ( student00 );

    //////////////////////////////////////////////////////////////////////
    // Employee
    // char* name;
    // int age;
    // int salary;
    // int years;
    // char jobtitle [20];
    //////////////////////////////////////////////////////////////////////
    struct Employee emp1 = { " Steven ", 30, 30000, 5, "Drone" } ;

    printf ( "\nAddress of Name = %s", emp1.name ) ;
    printf ( "\nAddress of Age = %d", emp1.age ) ;
    printf ( "\nAddress of Salary = %d", emp1.salary ) ;
    printf ( "\nAddress of Years of Service = %d", emp1.years ) ;
    printf ( "\nAddress of Job Title = %s", emp1.jobtitle ) ;

    //////////////////////////////////////////////////////////////////////
    // Manager
    // char* name;
    // int age;
    // int salary;
    // char jobtitle [20];
    // struct Employee emp [10];
    //////////////////////////////////////////////////////////////////////
    struct Manager man1 = {"Boss", 17, 102000, "Manager"};
    man1 . emp [0] = emp1 ;
    printf("\nThe manager name is %s, age %d, Staff assigned %s\n", man1.name, man1.age, man1.emp[0].name );

return 0;
}