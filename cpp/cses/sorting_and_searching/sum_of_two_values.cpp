#include <iostream>
#include <map>

using namespace std;

int main() {
  int n, x;
  cin >> n >> x;

  map<int, int> mp;
  for (int i = 0; i < n; i++) {
    int v;
    cin >> v;
    if (mp.find(x - v) != mp.end()) {
      cout << mp[x - v] + 1 << " " << i + 1 << "\n";
      return 0;
    }
    mp[v] = i;
  }

  cout << "IMPOSSIBLE"
       << "\n";

  return 0;
}
