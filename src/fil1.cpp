#include<iostream>
#include<fstream>
class student
{
public:
int roll;
char name[15],f_name[20];
void put();
void get();
void switch_case();
};
void student::put()
{
clrscr();
fstream file;
cout<<"Enter the rollno:";
cin>roll;
cout<<"Enter the name:";
gets(name);
cout<<"Enter the father name:";
gets(f_name);
file.open("stu.txt",ios::out|ios::app);
file.write((char*)this,sizeof(student));
file.close()
getch();
s.switch_case();
}
void student get()
{
int temp;
clrscr();
cout<<"Enter the rollno:";
cin>>temp;
fstream file;
file.open("stu.txt",ios::in);
file.seekg(0,ios::beg);
while(file.read((char*)this,sizeof(student)));
{
if(roll==temp)
{
cout<<"roll no:"<<roll<<endl;
cout<<"student name:"<<nanme<<endl;
cout<<"Father name:"<<f_name;
}
}
file.close();
getch();
s.switch_case();
}
void student::switch_case()
{
int i;
cout<<"Enter your chooice:";
cin>>i;
switch(i)
{
case 1:s.put();
	break;
case 2:s.get();
	break;
case 3:exit(0);
default:
	cout<<"wrong code";
}
}
void main()
{
clrscr();
student.s;
s.put();
s.get()
s.switch_case();
}




