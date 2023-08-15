#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
#include <iomanip>
#include <cassert>
#include <numeric>
#include <deque>
//#include <atcoder/modint>
#define rep(i,n) for(int i=0;i<n;i++)
#define prep(i,m,n) for(int i=m;i<n;i++)
#define rrep(i,n) for(int i=n-1;i>=0;i--)
#define fore(i,v) for(auto& i:v)
using namespace std;
//using namespace atcoder;
//using mint = modint998244353;
typedef long long ll;
/*template<class T>T tousa_sum(T a, T d, ll n) {
	return (a * 2 + d * (n - 1)) * n / 2;
}
const ll mod=1000000007;
using Graph=vector<vector<int> >;
map<ll,ll> prime_factor(ll n){
    map<ll,ll> ret;
    for(ll i=2;i*i<=n;i++){
        ll tmp=0;
        while(n%i==0){
            tmp++;
            n/=i;
        }
        ret[i]=tmp;
    }
    if(n!=1)ret[n]=1;
    return ret;
}
ll divisor_num(ll n){
    map<ll,ll> pf=prime_factor(n);
    ll ret=1;
    for(auto p:pf){
        ret*=(p.second+1);
    }
    return ret;
}

bool IsPrime(ll num)
{
    if (num < 2) return false;
    else if (num == 2) return true;
    else if (num % 2 == 0) return false; // 偶数はあらかじめ除く

    double sqrtNum = sqrt(num);
    for (ll i = 3; i <= sqrtNum; i += 2)
    {
        if (num % i == 0)
        {
            // 素数ではない
            return false;
        }
    }

    // 素数である
    return true;
}
/*struct UnionFind {
    vector<int> par; // par[i]:iの親の番号　(例) par[3] = 2 : 3の親が2

    UnionFind(int N) : par(N) { //最初は全てが根であるとして初期化
        for(int i = 0; i < N; i++) par[i] = i;
    }

    int root(int x) { // データxが属する木の根を再帰で得る：root(x) = {xの木の根}
        if (par[x] == x) return x;
        return par[x] = root(par[x]);
    }

    void unite(int x, int y) { // xとyの木を併合
        int rx = root(x); //xの根をrx
        int ry = root(y); //yの根をry
        if (rx == ry) return; //xとyの根が同じ(=同じ木にある)時はそのまま
        par[rx] = ry; //xとyの根が同じでない(=同じ木にない)時：xの根rxをyの根ryにつける
    }

    bool same(int x, int y) { // 2つのデータx, yが属する木が同じならtrueを返す
        int rx = root(x);
        int ry = root(y);
        return rx == ry;
    }
};*/
//*/
int main(){
    string S;
    S= "fsdz{Fdhvdu_flskhu_lv_fodvvlfdo_flskhu}";
    int l = S.size();
    rep(i,l){
        if((int)(S[i])>=(int)('a') && (int)(S[i])<=(int)('z')){
            cout << (char)((int)(S[i])-3);
        }
        else cout << S[i];
    }
}