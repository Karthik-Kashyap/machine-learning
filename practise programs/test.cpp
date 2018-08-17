#include<iostream>

using namespace std;

void sortit(string &str)
{
	qsort(str.begin(),str.end());
	cout<<str;
	return;
}

int main()
{
	string str="karthik";
	sortit(str);
	//qsort(str.begin(),str.end());
	//cout<<str;
	return 0;
}