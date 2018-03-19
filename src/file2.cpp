#include<iostream>
#include<fstream>
using namespace std;
int main()
{
char line[100];
fstream file;
file.open("file.txt",ios::out|ios::app);
if(file.fail())
{
cout<<"the file was open error";
}
else
{
cout<<"Enter a line:";
cin.getline(line,100);
file<<line<<endl;
cout<<"line written into a file"<<endl;
}
return 0;
}
