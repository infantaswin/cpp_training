#include<iostream>
#include<fstream>
using namespace std;
int main()
{
int student[3];
fstream file;
int i;
file.open("objects.txt",ios::out);
cout<<"Enter your number what do u want?:-"<<endl;
cin>>i;
switch(i)
{
case 1:cout<<"\nName=Aswin";
	cout<<"\nRoll no=1";
	cout<<"\nMark=99";
break;
case 2:cout<<"\nName=vikey";
	cout<<"\nRoll no=2";
	cout<<"\nMark=98";
break;
case 3:cout<<"\nName=karthi";
	cout<<"\nRoll no=3";
	cout<<"\nMark=97";
break;
default : cout<<"enter 1-3";
file.close();
}
return 0;
}

