import math
import mileage_to_metre
import metre_to_mileage

pi = math.pi

# 所有单位统一为米(m)
Alpha = float(input("请输入Alpha的角度:"))
L = float(input("请输入缓和曲线的长度："))
R = float(input("请输入圆曲线半径："))
KJD = input("请输入交点里程：")
Alpha = Alpha * math.pi / 180
KJD = mileage_to_metre.mileage_to_metre(KJD)     # JD里程转成米

# 缓和曲线常数计算
# Beta0切线角 m切垂距 P圆曲线内移量
Beta0 = (L/(2*R))       # 弧度值
m = L/2 - (L*L*L) / (240*R*R)
P = (L*L) / (24*R)
print(f"\n切线角Beta0 = {Beta0}, 切垂距m = {m}, 圆曲线内移量P = {P}")

"""Alpha = 60
Beta0 = Beta0*180/pi """

# 曲线综合要素计算
# TH切线长 圆曲线Lc LH曲线长 EH外矢距 q切曲差
TH = m + (R+P) * math.tan(Alpha/2)
Lc = R * (Alpha-2*Beta0)
LH = R * (Alpha-2*Beta0) + 2*L
EH = (R+P) * (1/math.cos(Alpha/2)) - R
q = 2*TH - LH
print(f"切线长TH为{TH}\n圆曲线长Lc为{Lc}\n曲线长LH为{LH}\n外矢距EH为{EH}\n切曲差q为{q}")
#print(math.tan(Alpha/2))

# 曲线主点里程的计算
KZH = KJD - TH
KHY = KZH + L
KQZ = KZH + LH/2
KYH = KHY + Lc
KHZ = KYH + L
print("\n直缓点、缓圆点、曲中点、圆缓点、缓直点里程分别如下：")
for everyPmileage in [KZH, KHY, KQZ, KYH, KHZ]:
    A = metre_to_mileage.metre_to_mileage(everyPmileage)
    print(A)



# 1.以ZH为原点，ZH-JD为x轴建立的独立坐标系

# 计算每隔5m的坐标点
segment_length = 5  # 每隔5m取一个坐标点
start_mileage = math.ceil(KZH / 5) * 5  # 向上取整，得到第一个坐标点的里程

print("\n1.以ZH为原点，ZH-JD为x轴建立的独立坐标系：")
print("缓和曲线坐标：")
for mileage in range(start_mileage, math.ceil(KHZ / 5) * 5 + 1, segment_length):
    distance = mileage - KZH
    if distance <= L:
        # 使用课本上缓和曲线独立坐标的简化计算公式
        x_real = distance - math.pow(distance, 5)/(40*R*R*L*L)
        y_real = math.pow(distance, 3)/(6*R*L)

        # 输出独立坐标系下的坐标
        real_mileage = metre_to_mileage.metre_to_mileage(distance + KZH)
        print(f"里程:{real_mileage} X坐标:{x_real} Y坐标:{y_real}")

print("圆曲线坐标：")
for mileage in range(start_mileage, math.ceil(KHZ / 5) * 5 + 1, segment_length):
    distance = mileage - KZH
    if distance >L and distance <= LH / 2:
        # 计算
        Karma = Beta0 + (distance - L) / R  # Karma是对应的圆心角
        x_real = m + R * math.sin(Karma)
        y_real = P + R * (1 - math.cos(Karma))

        # 输出独立坐标系下的坐标
        real_mileage = metre_to_mileage.metre_to_mileage(distance + KZH)
        print(f"里程:{real_mileage} X坐标:{x_real} Y坐标:{y_real}")


# 2.以HZ为原点，HZ-JD为x轴建立的独立坐标系

# 计算每隔5m的坐标点
segment_length = 5  # 每隔5m取一个坐标点
start_mileage = math.ceil(KQZ / 5) * 5  # 向上取整，得到第一个坐标点的里程

print("\n2.以HZ为原点，HZ-JD为x轴建立的独立坐标系：")
print("缓和曲线坐标：")
for mileage in range(start_mileage, math.ceil(KHZ / 5) * 5 + 1, segment_length):
    distance = KHZ - mileage
    if distance <= LH:
        # 使用课本上缓和曲线独立坐标的简化计算公式
        x_real = distance - math.pow(distance, 5)/(40*R*R*L*L)
        y_real = math.pow(distance, 3)/(6*R*L)

        # 输出独立坐标系下的坐标
        real_mileage = metre_to_mileage.metre_to_mileage(distance + KZH)
        print(f"里程:{real_mileage} X坐标:{x_real} Y坐标:{y_real}")

print("圆曲线坐标：")
for mileage in range(start_mileage, math.ceil(KHZ / 5) * 5 + 1, segment_length):
    distance = KHZ - mileage
    if distance >L and distance <= LH / 2:
        # 计算
        Karma = Beta0 + (distance - L) / R  # Karma是对应的圆心角
        x_real = m + R * math.sin(Karma)
        y_real = P + R * (1 - math.cos(Karma))

        # 输出独立坐标系下的坐标
        real_mileage = metre_to_mileage.metre_to_mileage(distance + KZH)
        print(f"里程:{real_mileage} X坐标:{x_real} Y坐标:{y_real}")























