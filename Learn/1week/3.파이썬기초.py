# ============================================================
# 고난이도 문제 1: 택배 요금 계산기
# ============================================================
# 무게(kg), 부피(가로x세로x높이 cm), 배송지(국내/해외), 특급여부(Y/N)를 입력받아
# 최종 요금을 계산하세요.

# 규칙:
# - 실제 무게와 부피 무게(가로*세로*높이/6000) 중 큰 값을 기준 무게로 사용
# - 국내 기본요금: 3000원 (5kg 초과 시 kg당 800원 추가)
# - 해외 기본요금: 15000원 (3kg 초과 시 kg당 3000원 추가)
# - 특급배송: 요금의 50% 추가
# - 기준 무게가 30kg 초과면 "배송 불가" 출력
# - 여러 박스를 입력받아 총 요금 합산 출력

box_count = int(input("박스 개수를 입력하세요: "))
boxes = []

for i in range(box_count):
    print(f"\n[박스 {i+1}]")
    weight = float(input("  무게 (kg): "))
    width  = float(input("  가로 (cm): "))
    depth  = float(input("  세로 (cm): "))
    height = float(input("  높이 (cm): "))
    boxes.append([weight, width, depth, height])

region  = input("\n배송지 (국내/해외): ")
express = input("특급배송 여부 (Y/N): ").upper()

print()
total_fee = 0
failed_boxes = []

for i, box in enumerate(boxes):
    weight, width, depth, height = box
    volume_weight   = (width * depth * height) / 6000
    standard_weight = max(weight, volume_weight)

    print(f"[박스 {i+1}] 기준 무게: {standard_weight:.2f}kg", end=" -> ")

    if standard_weight > 30:
        print("배송 불가")
        failed_boxes.append(i + 1)
        continue

    if region == "국내":
        fee = 3000 + (max(0, standard_weight - 5) * 800)
    elif region == "해외":
        fee = 15000 + (max(0, standard_weight - 3) * 3000)
    else:
        print("잘못된 배송지")
        break

    if express == "Y":
        fee *= 1.5

    print(f"{fee:,.0f}원")
    total_fee += fee

print(f"\n총 요금: {total_fee:,.0f}원")
if failed_boxes:
    print(f"배송 불가 박스: {failed_boxes}")


# ============================================================
# 고난이도 문제 2: 편의점 재고 관리 시스템
# ============================================================
# 상품명, 가격, 재고 수량을 여러 개 입력받아 재고를 관리하세요.

# 규칙:
# - 상품 정보를 list에 저장 [상품명, 가격, 수량]
# - 전체 재고 목록 출력
# - 재고 5개 이하인 상품은 "⚠ 재고 부족" 표시
# - 판매할 상품명과 수량을 입력받아 재고 차감
#   - 재고 부족 시 "재고 부족 (현재 재고: N개)" 출력
#   - 판매 성공 시 매출액 누적
# - 최종 재고 현황과 총 매출액 출력

print()
product_count = int(input("상품 수를 입력하세요: "))
products = []

for i in range(product_count):
    print(f"\n[상품 {i+1}]")
    name  = input("  상품명: ")
    price = int(input("  가격 (원): "))
    stock = int(input("  재고 수량: "))
    products.append([name, price, stock])

print(f"\n{'='*40}")
print("  현재 재고 목록")
print(f"  {'─'*36}")
for product in products:
    name, price, stock = product
    warning = "  ⚠ 재고 부족" if stock <= 5 else ""
    print(f"  {name} | {price:,}원 | {stock}개{warning}")
print(f"{'='*40}")

sale_count = int(input("\n판매할 항목 수를 입력하세요: "))
total_sales = 0

for i in range(sale_count):
    print(f"\n[판매 {i+1}]")
    target = input("  상품명: ")
    qty    = int(input("  수량: "))

    found = False
    for product in products:
        name, price, stock = product
        if name == target:
            found = True
            if stock < qty:
                print(f"  재고 부족 (현재 재고: {stock}개)")
            else:
                product[2] -= qty
                revenue = price * qty
                total_sales += revenue
                print(f"  판매 완료 | 매출: {revenue:,}원 | 남은 재고: {product[2]}개")
            break

    if not found:
        print(f"  '{target}' 상품을 찾을 수 없습니다.")

print(f"\n{'='*40}")
print("  최종 재고 현황")
print(f"  {'─'*36}")
for product in products:
    name, price, stock = product
    warning = "  ⚠ 재고 부족" if stock <= 5 else ""
    print(f"  {name} | {stock}개{warning}")
print(f"{'─'*40}")
print(f"  총 매출액: {total_sales:,}원")
print(f"{'='*40}")


# ============================================================
# 고난이도 문제 3: 영화관 좌석 예매 시스템
# ============================================================
# 상영관 좌석(행 x 열)을 초기화하고, 예매/취소/현황 조회를 처리하세요.

# 규칙:
# - 행(A~E), 열(1~8) 구조의 40석 좌석을 list로 관리
# - 예매할 좌석 목록을 입력받아 처리 (예: A3, B7)
#   - 이미 예매된 좌석이면 "이미 예매된 좌석" 출력
#   - 존재하지 않는 좌석이면 "잘못된 좌석" 출력
# - 예매 완료 후 현재 좌석 현황 출력 (O: 빈자리, X: 예매됨)
# - 남은 좌석 수와 예매율 출력

print()
rows    = ["A", "B", "C", "D", "E"]
cols    = [1, 2, 3, 4, 5, 6, 7, 8]
tickets = int(input("예매할 좌석 수를 입력하세요: "))

seats = []
for row in rows:
    seat_row = []
    for col in cols:
        seat_row.append("O")
    seats.append(seat_row)

booked = []

for i in range(tickets):
    seat = input(f"  좌석 입력 ({i+1}/{tickets}, 예: A3): ").upper()

    if len(seat) < 2:
        print("  잘못된 좌석")
        continue

    row_label = seat[0]
    col_label = seat[1:]

    if row_label not in rows or not col_label.isdigit():
        print("  잘못된 좌석")
        continue

    col_num = int(col_label)
    if col_num not in cols:
        print("  잘못된 좌석")
        continue

    row_idx = rows.index(row_label)
    col_idx = cols.index(col_num)

    if seats[row_idx][col_idx] == "X":
        print(f"  {seat}: 이미 예매된 좌석")
    else:
        seats[row_idx][col_idx] = "X"
        booked.append(seat)
        print(f"  {seat}: 예매 완료")

total_seats  = len(rows) * len(cols)
booked_count = len(booked)
remain_count = total_seats - booked_count

print(f"\n{'='*30}")
print(f"    1 2 3 4 5 6 7 8")
for i, row in enumerate(rows):
    print(f"  {row} ", end="")
    for seat in seats[i]:
        print(f"{seat} ", end="")
    print()
print(f"{'─'*30}")
print(f"  남은 좌석: {remain_count}석 / 예매율: {booked_count/total_seats*100:.1f}%")
print(f"{'='*30}")
