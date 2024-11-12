#include <iostream>
#include <string.h>
#define N 1000001
#define inf 0x7f7f7f7f
using namespace std;
#define mp(x, y) ( (x - 1) * m + y - 1)
int n, m, maxr, maxc, minr, minc;
char a[N];
int r0[N], c0[N], R[N], C[N], ans, sz;
int dirs[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
void dfs(int x, int y)
{
	int ii = mp(x, y);
	if ('#' == a[ii])
	{
		a[ii] = '.';
		sz++;
		maxr = max(maxr, x);
		maxc = max(maxc, y);
		minr = min(minr, x);
		minc = min(minc, y);
		for (auto d : dirs)
		{
			int u = d[0] + x, v = d[1] + y;
			if ( u == 0 || u > n || v  == 0 || v > m || '#'!=a[mp(u, v)]) continue;
			dfs(u, v);
		}
	}
}
int main()
{
	int tc;
	cin >> tc;
	// int cnt = 0;
	while (tc --)
	{
		cin >> n >> m;
		// cnt += 1;
		// cout << tc << "tc  -=== "<< endl;
		ans = -0x7f7f7f7f;
		memset(r0, 0, sizeof r0);
		memset(c0, 0, sizeof c0);
		memset(R, 0, sizeof R);
		memset(C, 0, sizeof C);
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
			{
				// int ii = (i - 1) * m + j -1;
				int ii = mp(i, j);
				cin >> a[ii];
				if ('.' == a[ii])
				{
					r0[i]++;
					c0[j]++;
				}
			}
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
			{
				int ii = mp(i, j);
				if ('#' == a[ii])
				{
					maxr = -inf;
					minr = inf;
					maxc = -inf;
					minc = inf;
					sz = 0;
					dfs(i, j);
					maxr = min(maxr + 1, n);
					maxc = min(maxc + 1, m);
					minr = max(minr - 1, 1);
					minc = max(minc - 1, 1);
					R[minr]+= sz;
					R[maxr + 1]-= sz;
					C[minc]+= sz;
					C[maxc + 1]-= sz;

				}
			}
		// continue;

		for (int i = 1; i <= n; i++)
		{
			R[i]+= R[i -1];
			ans = max(ans, R[i] + r0[i]);
		}
		for (int j = 1; j <= m; j++)
		{
			C[j]+= C[j - 1];
			ans = max(ans, C[j] + c0[j]);
		}
		cout << ans << endl;

	}
}