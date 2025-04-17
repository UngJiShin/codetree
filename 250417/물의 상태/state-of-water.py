
def water_state(celsius):
    if celsius <= 0:
        return "ice"
    elif celsius < 100:
        return "water"
    else:
        return "vapor"

# 사용자 입력
temp = int(input())
state = water_state(temp)
print(state)
"""
def water_state(celcius):
    if celcius <= 0:
        print('ice')
    elif celcius < 100:
        print('water')
    else:
        print('vapor')

temp = int(input())
state = water_state(temp)
print(state)
