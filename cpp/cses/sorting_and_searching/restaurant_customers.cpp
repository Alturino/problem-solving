#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n;
  cin >> n;
  vector<pair<int, int> > vi;
  for (int i = 0; i < n; i++) {
    int start, end;
    cin >> start >> end;
    vi.push_back(pair<int, int>(start, 1));
    vi.push_back(pair<int, int>(end, -1));
  }
  sort(vi.begin(), vi.end());

  int res = 0, curr = 0;
  for (int i = 0; i < vi.size(); i++) {
    curr += vi[i].second;
    res = max(res, curr);
  }
  cout << res << "\n";
}
