# 제품의 개수 n, 1~m까지의 정수를 포함
n, m = map(int, input().split())
# 모든 조건을 만족하는지 아닌지 판별하는 변수
flag = "No"
products = []

for _ in range(n):
    products.append(list(map(int, input().split())))

# Sample Input 1번의 예를 들어,
# 1번째 제품의 가격은 10000원이고, 2개의 기능을 가지고 있음. 1 기능과 3 기능
# 2번째 제품의 가격은 15000원이고, 3개의 기능을 가지고 있음. 1, 2, 4 기능
# 3번째 제품의 가격은 30000원이고, 3개의 기능을 가지고 있음. 1, 3, 5 기능
# 4번째 제품의 가격은 35000원이고, 2개의 기능을 가지고 있음. 1, 5 기능
# 5번째 제품의 가격은 100000원이고, 6개의 기능을 가지고 있음. 1, 2, 3, 4, 5, 6 기능
# i번째 제품의 가격이 더 높고, j번째 제품이 i번째 제품의 모든 기능을 가지고 있으면서,
# i번째 제품의 가격이 j번째 제품의 가격보다 높거나 j번째 제품이 i번째 제품이 가지고 있지 않은 하나 이상의 기능을 가지고 있으면 Yes
# 즉, 예제 1번에서는 (i, j) = (4, 3)일 때 조건을 만족할 수 있으므로 Yes를 출력한다.

for i in range(n):
    for j in range(n):
        if i != j:
            # i번째 제품의 가격이 더 높고, j번째 제품이 i번째 제품의 모든 기능을 가지고 있는지 검사
            print(products[i][2:] == products[j][2:])
            if products[i][0] >= products[j][0]:
                # 두 제품의 교집합을 구한다. j번째 제품이 i번째 제품의 모든 기능을 가지고 있는지 검사
                if (set(products[i][2:]) & set(products[j][2:])) == set(products[j][2:]):
                    flag = "Yes"
                    break

print(flag)
