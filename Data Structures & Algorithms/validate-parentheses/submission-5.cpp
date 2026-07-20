#include <stack>
#include <vector>
class Solution {
public:
    bool isValid(string s) {
        if (s.size() % 2 != 0) return false;

        std::stack<char> chars;

        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {
                chars.push(c);
            } else {
                if (chars.empty()) return false;

                char top = chars.top();
                chars.pop();

                if (c == ')' && top != '(') return false;
                if (c == '}' && top != '{') return false;
                if (c == ']' && top != '[') return false;
            }
        }

        return chars.empty();
    }    
};
