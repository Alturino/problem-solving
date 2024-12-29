#include <iostream>
#include <utility>
#include <vector>

using namespace std;

int main() {
  int n;
  cin >> n;

  vector<pair<int, int> > vi(n);
  for (int i = 0; i < n; i++) {
    int start, end;
    cin >> start >> end;
    vi[i] = pair<int, int>(start, end);
  }

  sort(vi.begin(), vi.end(), [](auto &left, auto &right) { return left.second < right.second; });
  int res = 0, timeElapsed = 0;
  for (int i = 0; i < n; i++) {
    pair<int, int> curr = vi[i];
    if (curr.first >= timeElapsed) {
      res++;
      timeElapsed = curr.second;
    }
  }

  cout << res << "\n";

  return 0;
}
