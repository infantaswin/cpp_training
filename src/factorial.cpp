#include<iostream>
using namespace std;
int main()
{
long int fact(int)
int x,n;
std::cout<<"Enter any integer number"<endl;
std::cin>>n;
x=fact(n);
std::cout<<"value="<<n<<"and its factorial=";
std::cout<<x<<endl;
return 0;
}
long int fact(int n)
{
int value=1;
if(n==1)
{
return (value);
}
else
{
for(int i=1;i<=n;i++)
{
value=value*i;
return(value);
}
}
}



