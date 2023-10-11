import matplotlib.pyplot as plt
def resh(N=100):
    #достижение точки
    dp = [0] * (N+1)
    dp[0] = dp[1] = 1
    dp[2] = 2
    # стоимость
    c = [0] * (N+1)
    c[1] = 1
    c[2] = 2
    c[3] = 4
    # арифметическая прогрессия
    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-3]
        c[i] = i * (i+1) // 2

    return dp, c
# значения входа
way_counts, c = resh(100)
#визуализация кол-во способов
plt.figure(figsize=(15, 9))
plt.subplot(121)
plt.plot(range(101), way_counts, marker="o", color="green")
plt.title('кол-во способов')
plt.xlabel('точки')
plt.ylabel('кол-во способов')


#визуализация цены
plt.subplot(122)
plt.plot(range(101), c, marker="o", color="orange")
plt.title('стоимость')
plt.xlabel('точки')
plt.ylabel('стоимость')

plt.tight_layout()
plt.show()