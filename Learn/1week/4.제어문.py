# ============================================================
# if 응용문제 1: 놀이공원 입장료 계산기
# ============================================================
# 나이, 장애인 여부, 주말 여부를 입력받아 입장료를 계산하세요.
#
# 규칙:
# - 기본 요금: 성인(19세 이상) 15000원, 청소년(13~18세) 10000원, 어린이(3~12세) 7000원, 영유아(3세 미만) 무료
# - 장애인: 50% 할인
# - 주말: 20% 추가
# - 나이가 음수면 "잘못된 나이" 출력

age      = int(input("나이를 입력하세요: "))
disabled = input("장애인 여부 (Y/N): ").upper()
weekend  = input("주말 여부 (Y/N): ").upper()

if age < 0:
    print("잘못된 나이입니다.")
elif age < 3:
    print("입장료: 무료 (영유아)")
else:
    if age >= 19:
        fee = 15000
        category = "성인"
    elif age >= 13:
        fee = 10000
        category = "청소년"
    else:
        fee = 7000
        category = "어린이"

    if disabled == "Y":
        fee *= 0.5
    if weekend == "Y":
        fee *= 1.2

    print(f"분류: {category} / 최종 입장료: {int(fee):,}원")


# ============================================================
# if 응용문제 2: 택시 요금 계산기
# ============================================================
# 이동 거리(km), 시간대, 탑승 인원을 입력받아 요금을 계산하세요.
#
# 규칙:
# - 기본요금: 3800원 (기본 2km)
# - 2km 초과: 100m당 100원 추가
# - 심야(00시~04시): 20% 할증
# - 탑승 인원 4명 초과: "탑승 불가 (최대 4명)" 출력
# - 거리가 0 이하면 "잘못된 거리" 출력

print()
distance  = float(input("이동 거리를 입력하세요 (km): "))
hour      = int(input("현재 시간을 입력하세요 (0~23): "))
passenger = int(input("탑승 인원을 입력하세요: "))

if distance <= 0:
    print("잘못된 거리입니다.")
elif passenger > 4:
    print("탑승 불가 (최대 4명)")
else:
    fee = 3800
    if distance > 2:
        extra_100m = int((distance - 2) * 10)
        fee += extra_100m * 100

    if hour < 4:
        fee *= 1.2
        print(f"심야 할증 적용")

    print(f"이동 거리: {distance}km / 최종 요금: {int(fee):,}원")


# ============================================================
# if 응용문제 3: 환전 수수료 계산기
# ============================================================
# 환전 금액(원)과 등급(일반/우대/VIP)을 입력받아 수수료를 계산하세요.
#
# 규칙:
# - 일반: 수수료 1.5%
# - 우대: 100만원 미만 1.0%, 100만원 이상 0.7%
# - VIP:  100만원 미만 0.5%, 100만원 이상 수수료 없음
# - 환전 금액이 0 이하면 "잘못된 금액" 출력

print()
amount = int(input("환전 금액을 입력하세요 (원): "))
grade  = input("등급을 입력하세요 (일반/우대/VIP): ")

if amount <= 0:
    print("잘못된 금액입니다.")
elif grade == "일반":
    fee = amount * 0.015
    print(f"수수료: {int(fee):,}원 / 실수령액: {int(amount - fee):,}원")
elif grade == "우대":
    rate = 0.007 if amount >= 1000000 else 0.010
    fee  = amount * rate
    print(f"수수료율: {rate*100}% / 수수료: {int(fee):,}원 / 실수령액: {int(amount - fee):,}원")
elif grade == "VIP":
    if amount >= 1000000:
        print(f"수수료 없음 / 실수령액: {amount:,}원")
    else:
        fee = amount * 0.005
        print(f"수수료: {int(fee):,}원 / 실수령액: {int(amount - fee):,}원")
else:
    print("잘못된 등급입니다.")


# ============================================================
# for 응용문제 1: 로또 번호 통계 분석기
# ============================================================
# 여러 회차의 로또 당첨 번호를 입력받아 통계를 분석하세요.
#
# 규칙:
# - 각 회차마다 6개 번호 입력 (1~45)
# - 전체 번호 중 가장 많이 나온 번호 Top 3 출력
# - 번호 구간별 출현 횟수 출력 (1~15 / 16~30 / 31~45)
# - 범위 초과 번호는 "잘못된 번호"로 무시

print()
rounds     = int(input("회차 수를 입력하세요: "))
all_numbers = []

for i in range(rounds):
    print(f"\n[{i+1}회차] 번호 6개를 띄어쓰기로 입력하세요 (예: 3 12 24 35 41 45): ", end="")
    nums = input().split()
    for n in nums:
        num = int(n)
        if 1 <= num <= 45:
            all_numbers.append(num)
        else:
            print(f"  {num}: 잘못된 번호 (무시됨)")

count = []
for n in range(1, 46):
    count.append([n, 0])

for num in all_numbers:
    count[num - 1][1] += 1

count.sort(key=lambda x: x[1], reverse=True)

print(f"\n{'='*30}")
print("  번호 출현 Top 3")
for i in range(3):
    print(f"  {i+1}위: {count[i][0]}번 ({count[i][1]}회)")

zones = [[0, "1~15"], [0, "16~30"], [0, "31~45"]]
for num in all_numbers:
    if num <= 15:
        zones[0][0] += 1
    elif num <= 30:
        zones[1][0] += 1
    else:
        zones[2][0] += 1

print(f"\n  구간별 출현 횟수")
for zone in zones:
    print(f"  {zone[1]}: {zone[0]}회")
print(f"{'='*30}")


# ============================================================
# for 응용문제 2: 주식 수익률 계산기
# ============================================================
# 여러 종목의 매수가, 매도가, 수량을 입력받아 수익을 분석하세요.
#
# 규칙:
# - 종목별 수익금, 수익률 계산
# - 수익률이 양수면 "수익", 음수면 "손실", 0이면 "본전" 표시
# - 전체 수익금 합산, 수익 종목 수 / 손실 종목 수 출력
# - 수익률이 가장 높은 종목과 가장 낮은 종목 출력

print()
stock_count = int(input("종목 수를 입력하세요: "))
stocks = [None] * stock_count

for i in range(stock_count):
    print(f"\n[종목 {i+1}]")
    name      = input("  종목명: ")
    buy_price = int(input("  매수가 (원): "))
    sell_price= int(input("  매도가 (원): "))
    quantity  = int(input("  수량 (주): "))
    stocks[i] = [name, buy_price, sell_price, quantity]

print(f"\n{'='*45}")
total_profit  = 0
win_count     = 0
lose_count    = 0
best  = None
worst = None

for stock in stocks:
    name, buy, sell, qty = stock
    profit = (sell - buy) * qty
    rate   = (sell - buy) / buy * 100

    if rate > 0:
        result = "수익"
        win_count += 1
    elif rate < 0:
        result = "손실"
        lose_count += 1
    else:
        result = "본전"

    print(f"  {name} | 수익금: {profit:+,}원 | 수익률: {rate:+.2f}% | {result}")
    total_profit += profit

    if best is None or rate > best[1]:
        best = [name, rate]
    if worst is None or rate < worst[1]:
        worst = [name, rate]

print(f"{'─'*45}")
print(f"  총 수익금: {total_profit:+,}원")
print(f"  수익 종목: {win_count}개 / 손실 종목: {lose_count}개")
print(f"  최고 수익률: {best[0]} ({best[1]:+.2f}%)")
print(f"  최저 수익률: {worst[0]} ({worst[1]:+.2f}%)")
print(f"{'='*45}")


# ============================================================
# for 응용문제 3: 계단식 요금 전기 요금 계산기
# ============================================================
# 여러 가구의 월 전력 사용량을 입력받아 전기 요금을 계산하세요.

# 규칙 (주택용 저압 누진제):
# - 200kWh 이하: kWh당 93.3원
# - 201~400kWh:  기본 18,660원 + 초과분 kWh당 187.9원
# - 400kWh 초과: 기본 56,240원 + 초과분 kWh당 280.6원
# - 부가세 10% 추가
# - 전체 가구 평균 사용량과 최대/최소 요금 가구 출력

print()
household_count = int(input("가구 수를 입력하세요: "))
households = []

for i in range(household_count):
    name  = input(f"\n[가구 {i+1}] 이름: ")
    usage = int(input("  이번 달 사용량 (kWh): "))
    households.append([name, usage])

print(f"\n{'='*45}")
total_usage = 0
max_household = None
min_household = None

for household in households:
    name, usage = household

    if usage <= 200:
        fee = usage * 93.3
    elif usage <= 400:
        fee = 18660 + (usage - 200) * 187.9
    else:
        fee = 56240 + (usage - 400) * 280.6

    fee_with_tax = fee * 1.1
    print(f"  {name} | {usage}kWh | 요금: {int(fee_with_tax):,}원 (부가세 포함)")

    total_usage += usage
    if max_household is None or fee_with_tax > max_household[1]:
        max_household = [name, fee_with_tax]
    if min_household is None or fee_with_tax < min_household[1]:
        min_household = [name, fee_with_tax]

print(f"{'─'*45}")
print(f"  평균 사용량: {total_usage / household_count:.1f}kWh")
print(f"  최고 요금: {max_household[0]} ({int(max_household[1]):,}원)")
print(f"  최저 요금: {min_household[0]} ({int(min_household[1]):,}원)")
print(f"{'='*45}")


# ============================================================
# while 응용문제 1: 자판기 시뮬레이터
# ============================================================
# 금액을 투입하고 음료를 선택하는 자판기를 구현하세요.
#
# 규칙:
# - 음료 목록: 콜라(1200원), 사이다(1100원), 물(600원), 커피(1500원)
# - 투입 금액이 부족하면 "금액 부족" 출력
# - "반환" 입력 시 잔액 반환 후 종료
# - "종료" 입력 시 즉시 종료
# - 재고가 0이 되면 "품절" 표시

print()
menu = [
    ["콜라",   1200, 3],
    ["사이다", 1100, 3],
    ["물",      600, 3],
    ["커피",   1500, 3],
]
balance = 0

while True:
    print(f"\n[잔액: {balance}원]")
    print("  메뉴: ", end="")
    for item in menu:
        name, price, stock = item
        status = f"{price}원" if stock > 0 else "품절"
        print(f"{name}({status}) ", end="")
    print()

    action = input("  투입 금액 또는 음료명 입력 ('반환'/'종료'): ")

    if action == "종료":
        print("  자판기를 종료합니다.")
        break
    elif action == "반환":
        print(f"  {balance}원을 반환합니다.")
        balance = 0
        break
    elif action.isdigit():
        balance += int(action)
        print(f"  {action}원 투입 완료. 잔액: {balance}원")
    else:
        found = False
        for item in menu:
            name, price, stock = item
            if action == name:
                found = True
                if stock == 0:
                    print(f"  {name}: 품절")
                elif balance < price:
                    print(f"  금액 부족 (필요: {price}원 / 잔액: {balance}원)")
                else:
                    balance -= price
                    item[2] -= 1
                    print(f"  {name} 나왔습니다! 잔액: {balance}원")
                break
        if not found:
            print("  없는 메뉴입니다.")


# ============================================================
# while 응용문제 2: 숫자 맞추기 게임
# ============================================================
# 1~100 사이의 숫자를 맞추는 게임을 구현하세요.

# 규칙:
# - 정답 숫자를 직접 입력 (랜덤 없이 미리 지정)
# - 최대 7번 안에 맞춰야 함
# - 틀릴 때마다 "더 높게" / "더 낮게" 힌트 제공
# - 남은 기회도 함께 출력
# - 7번 안에 못 맞추면 정답 공개

print()
print("[숫자 맞추기 게임]")
answer  = int(input("출제자: 정답 숫자를 입력하세요 (1~100, 상대방 안 보이게): "))
print("\n" * 3)

max_try = 7
attempts = 0
solved   = False

while attempts < max_try:
    remain = max_try - attempts
    guess  = int(input(f"  숫자를 입력하세요 (남은 기회: {remain}번): "))
    attempts += 1

    if guess == answer:
        print(f"  정답! {attempts}번 만에 맞췄습니다!")
        solved = True
        break
    elif guess < answer:
        print(f"  더 높게!")
    else:
        print(f"  더 낮게!")

if not solved:
    print(f"  실패! 정답은 {answer}이었습니다.")


# ============================================================
# while 응용문제 3: ATM 시뮬레이터
# ============================================================
# ATM 기능을 구현하세요.

# 규칙:
# - 초기 잔액 입력
# - 메뉴: 1.잔액조회  2.입금  3.출금  4.이체  5.거래내역  0.종료
# - 출금/이체 시 잔액 부족이면 "잔액 부족" 출력
# - 출금/이체는 1만원 단위만 가능
# - 모든 거래는 내역 list에 기록 후 조회 가능

print()
balance  = int(input("초기 잔액을 입력하세요 (원): "))
history  = []

while True:
    print(f"\n{'─'*30}")
    print("  1.잔액조회  2.입금  3.출금  4.이체  5.거래내역  0.종료")
    menu_choice = input("  선택: ")

    if menu_choice == "0":
        print("  이용해 주셔서 감사합니다.")
        break

    elif menu_choice == "1":
        print(f"  현재 잔액: {balance:,}원")

    elif menu_choice == "2":
        amount = int(input("  입금액: "))
        balance += amount
        history.append(f"입금 +{amount:,}원 (잔액: {balance:,}원)")
        print(f"  입금 완료. 잔액: {balance:,}원")

    elif menu_choice == "3":
        amount = int(input("  출금액: "))
        if amount % 10000 != 0:
            print("  출금은 1만원 단위만 가능합니다.")
        elif amount > balance:
            print(f"  잔액 부족 (현재 잔액: {balance:,}원)")
        else:
            balance -= amount
            history.append(f"출금 -{amount:,}원 (잔액: {balance:,}원)")
            print(f"  출금 완료. 잔액: {balance:,}원")

    elif menu_choice == "4":
        target = input("  이체 대상 계좌: ")
        amount = int(input("  이체 금액: "))
        if amount % 10000 != 0:
            print("  이체는 1만원 단위만 가능합니다.")
        elif amount > balance:
            print(f"  잔액 부족 (현재 잔액: {balance:,}원)")
        else:
            balance -= amount
            history.append(f"이체 -{amount:,}원 -> {target} (잔액: {balance:,}원)")
            print(f"  {target}에게 {amount:,}원 이체 완료.")

    elif menu_choice == "5":
        if not history:
            print("  거래 내역이 없습니다.")
        else:
            print(f"  {'─'*28}")
            for i, record in enumerate(history):
                print(f"  {i+1}. {record}")
    else:
        print("  잘못된 메뉴입니다.")
