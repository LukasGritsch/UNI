#include<stdio.h>

//Funktion prototype
int add(int num1,int num2);

//Main funktion call
void main()
{
printf("Hello World!\n");
int hSum; 
hSum = add(5,88);
 printf("If you add 5 to 88 you will get: %d", hSum);
}

//Funktion decleration
int add(int num1,int num2){
    return num1+num2;
}