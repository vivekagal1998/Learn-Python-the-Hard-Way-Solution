/******************************************
*    AUTHOR         :   VIVEK SHAH        *
*    INSTITUTION    :   NIT SURAT         *
******************************************/

#include <bits/stdc++.h>
#define boost ios_base::sync_with_stdio(false);cin.tie(NULL)
#define ll long long int
#define mod 1000000007
#define rep(i,a,b) for (ll i = a; i<b; ++i)

using namespace std;

int main()
{
	boost;
	ll n;
	cin>>n;
	ll a[n];
	rep(i,0,n)cin>>a[i];
	ll ans = 0;
	rep(i,0,n){
		ans = ans^a[i];
	}
	cout<<ans<<"\n";
	return 0;
}