def solution(today, terms, privacies):
    # 날짜를 28일 기준의 일수로 변환
    def to_days(date):
        y, m, d = map(int, date.split('.'))
        return (y * 12 + m) * 28 + d

    # 약관별 유효기간 저장
    s_term = {}
    for term in terms:
        t, tm = term.split()
        s_term[t] = int(tm)

    # 오늘 날짜를 28일 기준으로 변경
    today_days = to_days(today)

    answer = []

    for i, p in enumerate(privacies, start=1):
        # 날짜, 약관유형
        date, t = p.split()

        register_days = to_days(date)
        expire_days = register_days + s_term[t] * 28

        # 만료일 당일부터 파기
        if today_days >= expire_days:
            answer.append(i)

    return answer