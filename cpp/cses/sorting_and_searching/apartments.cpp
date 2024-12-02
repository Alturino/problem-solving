#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

bool inRange(int low, int high, int v) { return v >= low && v <= high; }

int main() {
  int applicant, apartment, allowed;
  cin >> applicant;
  cin >> apartment;
  cin >> allowed;

  vector<int> applicants;
  vector<int> apartments;

  for (int i = 0; i < applicant; i++) {
    int v;
    cin >> v;
    applicants.push_back(v);
  }

  for (int i = 0; i < apartment; i++) {
    int v;
    cin >> v;
    apartments.push_back(v);
  }

  sort(applicants.begin(), applicants.end());
  sort(apartments.begin(), apartments.end());

  int res = 0;
  for (int i = 0; i < applicants.size(); i++) {
    for (int j = i; j < apartments.size(); j++) {
      bool isInRange = inRange(applicants[i] - allowed, applicants[i] + allowed,
                               apartments[j]);
      if (isInRange) {
        res++;
      }
    }
  }

  cout << res;

  return 0;
}
