#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n;
  cin >> n;

  vector<int> vi(n);
  for (int i = 0; i < n; i++) {
    cin >> vi[i];
  }

  sort(vi.begin(), vi.end());
  int median = vi[n / 2], ans = 0;
  for (int i = 0; i < n; i++) {
    ans += abs(vi[i] - median);
  }

  cout << ans;

  return 0;
}
