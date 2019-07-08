#include <iostream>
using namespace std;

int main() {
	int n,m=0,i,flag=0;
	cin>>n;
	m=n/2;
	for(i=2;i<=m;i++)
	{
		if(n%i==0)
		{
			cout<<"no";
			flag=1;
			break;
		}
	}
	if(flag==0)
	{
		cout<<"yes";
	}
	return 0;
}