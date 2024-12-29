#include <iostream>
#include <set>

using namespace std;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n, m;
  cin >> n >> m;

  multiset<int> tickets;
  for (int i = 0; i < n; i++) {
    int v;
    cin >> v;
    tickets.insert(v);
  }

  for (int i = 0; i < m; i++) {
    int v;
    cin >> v;
    auto it = tickets.upper_bound(v);
    if (it == tickets.begin()) {
      cout << -1 << "\n";
    } else {
      cout << *(--it) << "\n";
      tickets.erase(it);
    }
  }
}
