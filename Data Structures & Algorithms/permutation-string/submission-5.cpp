class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) return false;

        unordered_map<char, int> target;
        for (char c : s1) {
            target[c]++;
        }

        unordered_map<char, int> window;
        for (int i = 0; i < s1.size(); i++) {
            window[s2[i]]++;
        }

        int l = 0;
        int r = s1.size();

        while (r < s2.size()) {
            if (window == target) return true;

            window[s2[l]]--;
            if (window[s2[l]] == 0)
                window.erase(s2[l]);
            l++;

            window[s2[r]]++;
            r++;
        }

        return window == target;
    }
};
