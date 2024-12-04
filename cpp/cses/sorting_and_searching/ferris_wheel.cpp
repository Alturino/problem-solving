#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n, x;
  cin >> n;
  cin >> x;

  vector<int> p;
  for (int i = 0; i < n; i++) {
    int v;
    cin >> v;
    p.push_back(v);
  }

  sort(p.begin(), p.end());
  int res = 0, weight = 0, count = 0;
  for (int i = 0; i < n; i++) {
    if (weight >= x || count >= 2) {
      weight = 0, count = 0;
      res++;
    }
    weight += p[i];
    count++;
  }
  if (n % 2 != 0) {
    res++;
  }

  cout << res;
}
