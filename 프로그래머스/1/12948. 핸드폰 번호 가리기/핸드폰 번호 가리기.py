def solution(phone_number):
    hidden = list(phone_number)
    for i in range(len(hidden)):
        if  len(hidden) - hidden.count("*") == 4:
            break
        hidden[i] = "*"
    return ''.join(hidden)