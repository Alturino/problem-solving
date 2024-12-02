#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n, m, k;
  cin >> n;
  cin >> m;
  cin >> k;

  vector<int> A;
  vector<int> B;

  for (int i = 0; i < n; i++) {
    int v;
    cin >> v;
    A.push_back(v);
  }

  for (int i = 0; i < m; i++) {
    int v;
    cin >> v;
    B.push_back(v);
  }

  sort(A.begin(), A.end());
  sort(B.begin(), B.end());

  int a = 0, b = 0, res = 0;
  while (a < n && b < m) {
    int currentApplicant = A[a];
    int currentApartment = B[b];
    bool isInRange = abs(currentApartment - currentApplicant) <= k;
    if (isInRange) {
      a++;
      b++;
      res++;
    } else if (currentApplicant < currentApartment) {
      a++;
    } else {
      b++;
    }
  }

  cout << res;

  return 0;
}
