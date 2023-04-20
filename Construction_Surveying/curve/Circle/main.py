import math
import mileage_to_metre
import metre_to_mileage

# 所有单位统一为米(m)
Alpha = float(input("请输入Alpha的角度:"))
R = float(input("请输入圆曲线半径："))
KJD = input("请输入交点里程：")
Alpha = Alpha * math.pi / 180
KJD = mileage_to_metre.mileage_to_metre(KJD)     # JD里程转成米
# calculation of elements
T = R * math.tan(Alpha/2)
L = R * Alpha
E = R * (1/math.cos(Alpha/2) - 1)
q = 2 * T - L
print(f"切线长:{T}\n曲线长:{L}\n外矢距:{E}\n切曲差:{q}")
# calculation of mileage
KZY = KJD - T
KQZ = KZY + L/2
KYZ = KZY + L
print("\n直圆点、曲中点、圆直点里程分别如下：")
for everyPmileage in [KZY, KQZ, KYZ]:
    A = metre_to_mileage.metre_to_mileage(everyPmileage)
    print(A)

# 计算每隔5m的坐标点
segment_length = 5  # 每隔5m取一个坐标点
start_mileage = math.ceil(KZY / 5) * 5  # 向上取整，得到第一个坐标点的里程

for mileage in range(start_mileage, math.ceil(KYZ / 5) * 5 + 1, segment_length):
    distance = mileage - KZY

    if distance <= T:
        # 计算圆弧段的横坐标和纵坐标
        x = math.sqrt(R ** 2 - (R - distance) ** 2)
        y = R - math.sqrt(R ** 2 - (R - distance) ** 2)

        # 旋转坐标系得到实际坐标值
        X = x * math.cos(Alpha / 2) + E * math.sin(Alpha / 2)
        Y = y * math.cos(Alpha / 2) - E * math.sin(Alpha / 2)

        # 通过里程算出弧长，然后通过弧长算出点所对应的圆心角
        arc_length = distance
        angle = arc_length / R

        # 通过圆心角和坐标轴正方向的夹角计算独立坐标系下的坐标
        if angle <= math.pi / 2:
            x_real = R * math.sin(angle)
            y_real = R - R * math.cos(angle)
        elif angle <= math.pi:
            x_real = R * math.cos(angle - math.pi / 2)
            y_real = R * math.sin(angle - math.pi / 2)
        elif angle <= 3 * math.pi / 2:
            x_real = -(R * math.sin(angle - math.pi))
            y_real = -(R - R * math.cos(angle - math.pi))
        else:
            x_real = -(R * math.cos(angle - 3 * math.pi / 2))
            y_real = R * math.sin(angle - 3 * math.pi / 2)

        # 输出独立坐标系下的坐标
        real_mileage = metre_to_mileage.metre_to_mileage(distance + KZY)
        print(f"里程:{real_mileage} X坐标:{x_real} Y坐标:{y_real}")















'''
# 计算每隔5m的整数里程坐标点
segment_length = 5 # 每隔5m取一个坐标点
start_mileage = math.ceil(KZY / 5) * 5 # 向上取整，得到第一个坐标点的里程
for mileage in range(start_mileage, math.ceil(KYZ / 5) * 5 + 1, segment_length):
    distance = mileage - KZY
    if distance <= T:
        x = math.sqrt(R ** 2 - (R - distance) ** 2) # 圆弧段的横坐标
        y = R - math.sqrt(R ** 2 - (R - distance) ** 2) # 圆弧段的纵坐标
        X = x * math.cos(Alpha/2) + E * math.sin(Alpha/2) # 旋转坐标系得到实际坐标值
        Y = y * math.cos(Alpha/2) - E * math.sin(Alpha/2)
        real_mileage = metre_to_mileage.metre_to_mileage(distance + KZY)
    print(f"里程:{real_mileage} X坐标:{X} Y坐标:{Y}")
'''