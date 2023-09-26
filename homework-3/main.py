from src.channel import Channel

if __name__ == '__main__':
    # Создаем два экземпляра класса
    moscow_python = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    high_load = Channel('UCwHL6WHUarjGfUM_586me8w')

    # Используем различные магические методы
    print(moscow_python)  # 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'
    print(moscow_python + high_load)  # 100100
    print(moscow_python - high_load)  # -48300
    print(high_load - moscow_python)  # 48300
    print(moscow_python > high_load)  # False
    print(moscow_python >= high_load)  # False
    print(moscow_python < high_load)  # True
    print(moscow_python <= high_load)  # True
    print(moscow_python == high_load)  # False
