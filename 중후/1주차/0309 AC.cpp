#include <iostream>
#include <deque>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		string cmd;
		cin >> cmd;

		int n;
		cin >> n;

		string arr;
		cin >> arr;

		deque<int> dq;
		string temp = "";
		for (auto num : arr)
		{
			if (num >= '0' and num <= '9')
			{
				temp += num;
			}
			else if (num == ']' or num == ',')
			{
				if (temp != "")
				{
					dq.push_back(stoi(temp));
					temp = "";
				}
			}
		}

		bool flag = true;
		bool error = false;
		for (auto c : cmd)
		{
			if (c == 'R') flag = !flag;
			else
			{
				if (!dq.empty())
				{
					if (flag) dq.pop_front();
					else dq.pop_back();
				}
				else
				{
					error = true;
					cout << "error\n";
					break;
				}
			}
		}

		if (!error)
		{
			cout << '[';
			if (flag)
			{
				while (!dq.empty())
				{
					cout << dq.front();
					dq.pop_front();
					if (!dq.empty()) cout << ',';
				}
			}
			else
			{
				while (!dq.empty())
				{
					cout << dq.back();
					dq.pop_back();
					if (!dq.empty()) cout << ',';
				}
			}
			cout << "]\n";
		}
	}
}