#include<bits/stdc++.h>
using namespace std;
#include "Solution.cpp"


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    cin >> n;
    vector<string> trainName(n), timeOfArrival(n), timeOfDeparture(n), timeToDepart(n);
    vector<int> trainNum(n);

    for(int i = 0 ; i < n ; ++i) {
        cin >> trainName[i] >> trainNum[i] >> timeOfArrival[i] >> timeOfDeparture[i] >> timeToDepart[i];

    }

    pair<int, vector<int> > result = assignPlatformToTrain(trainName, timeOfArrival, timeOfDeparture, timeToDepart, trainNum);

    int platformsRequired = result.first;
    vector<int> platformAssigned = result.second;

    cout << platformsRequired << "\n";
    for(int i = 0 ; i < n ; ++i) {
        cout << trainName[i] << " " << trainNum[i] << " " << platformAssigned[i] << "\n";
    }
}
