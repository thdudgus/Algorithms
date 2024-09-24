#include <string>
#include <cctype> 

using namespace std;

string solution(string s) {
    bool capitalize = true;  // 단어의 시작을 알리는 플래그
    bool digit = false; // 숫자인가?
    
    for (int i = 0; i < s.length(); i++) 
        s[i] = tolower(s[i]);
    
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ' ') {
            capitalize = true;  // 공백 다음 글자는 대문자로
        } 
        else if (capitalize && isdigit(s[i])) {  // 공백 다음에 숫자면 대문자로 x
            capitalize = false;
        }
        else if (capitalize && isalpha(s[i])) {
            s[i] = toupper(s[i]);
            capitalize = false;
            }
        else {
            s[i] = tolower(s[i]);  // 그 외의 경우는 소문자로 유지
        }
    }
    return s;
}
