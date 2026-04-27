# 전화번호를 담은 배열 phone_book
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false, 그렇지 않으면 true
import statistics
def solution(phone_book):
    # phone_book.sort(key=lambda x: len(x), reverse=False)
    phone_book.sort()
    answer = True
    for i in range(len(phone_book)):
        # for j in range(i+1, len(phone_book)):
        #     if phone_book[i] in phone_book[j] and phone_book[j].index(phone_book[i]) == 0:
        if i+1<len(phone_book):
            if phone_book[i+1].startswith(phone_book[i]):
                return False
    return answer