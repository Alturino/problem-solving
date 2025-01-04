#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n;
  cin >> n;

  long long res = -1e18, currSum = -1e18;
  for (int i = 0; i < n; i++) {
    long long v;
    cin >> v;
    currSum = max(currSum + v, v);
    res = max(res, currSum);
  }

  cout << res;

  return 0;
}
