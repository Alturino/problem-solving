#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n, x;
  cin >> n >> x;

  vector<int> vi(n);
  for (int i = 0; i < n; i++)
    cin >> vi[i];

  sort(vi.begin(), vi.end());
  int res = 0, left = 0, right = n - 1;
  while (left <= right) {
    if (vi[left] + vi[right] <= x) {
      res++;
      left++;
      right--;
    } else {
      res++;
      right--;
    }
  }
  cout << res;
}
