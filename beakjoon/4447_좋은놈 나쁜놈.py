n = int(input())

for _ in range(n):
    hero = input()

    s = hero.lower()
    good = s.count('g')
    bad = s.count('b')

    if good == bad:
        print(hero, "is NEUTRAL")
    elif good < bad:
        print(hero, "is A BADDY")
    elif good > bad:
        print(hero, "is GOOD")