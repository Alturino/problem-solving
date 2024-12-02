#include <iostream>
#include <set>

using namespace std;

int main() {
  int n;
  cin >> n;

  set<int> set;
  for (int i = 0; i < n; i++) {
    int v;
    cin >> v;

    set.insert(v);
  }

  cout << set.size();

  return 0;
}
