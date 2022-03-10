#include <iostream>
#include <vector>
using namespace std;

int n,m,t;
bool True_People[51];
vector<int> Party[51];

int main()
{
	cin >> n >> m;
	cin >> t;
	
	for(int i=1;i<t+1;i++)
	{
		int True_People_Number;
		cin >> True_People_Number;
		True_People[True_People_Number] = true;
	}
	
	for(int i=1;i<m+1;i++)
	{
		int Party_People_Count;
		cin >> Party_People_Count;
		for(int j=0;j<Party_People_Count;j++)
		{
			int Party_People_Number;
			cin >> Party_People_Number;
			Party[i].push_back(Party_People_Number);
		}
	}
	
	for(int i=0;i<50;i++)
	{
		for(int j=1;j<m+1;j++)
		{
			for(auto Party_People : Party[j])
			{
				if(True_People[Party_People])
				{
					for(auto True_Number : Party[j]) True_People[True_Number] = true;
					break;
				}
			}
		}
	}
	
	int Lie_Count = 0; 
	for(int i=1;i<m+1;i++)
	{
		bool flag = true;
		for(auto Party_People : Party[i])
		{
			if(True_People[Party_People]) 
			{
				flag = false;
				break;
			}	
		}
		if(flag) Lie_Count++;
	}
	
	cout << Lie_Count;
}
