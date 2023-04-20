# 函数：米转换成里程

def metre_to_mileage(Mpoint):      # Mpoint 是里程转成米为单位的数 如：1024.256
    kilo = int(Mpoint / 1000)
    metre = Mpoint % 1000
    Kpoint = f"K{kilo}+{metre}"
    return Kpoint