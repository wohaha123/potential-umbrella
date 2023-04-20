# 函数: 里程转换成米

def mileage_to_metre(Kpoint):      # Kpoint 是里程 如：K1+024.256
    kilo = float((Kpoint.split("+")[0]).split("K")[1])
    metre = float(Kpoint.split("+")[1])
    Mpoint = kilo * 1000 + metre
    return Mpoint