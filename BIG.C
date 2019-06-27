#include<stdio.h>
#include<conio.h>
void main()
{
int a,b;
clr scr()
printf("enter the values :");
scanf("%d%d",&a,&b);
if(a>b)
printf("a is greater:",a);
else
printf("b is greater:",b);
getch();
}