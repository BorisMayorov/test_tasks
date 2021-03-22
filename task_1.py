# Реализованый мной алгоритм по сути является алгоритмом бинарного поиска скорость которого O(log n).
# Данную задачу можно решить используя встроенную функцию Python array.find('0'), но я посчитал что это было бы слишком просто.

def task(array):
    start = 0
    end = len(array)-1
    while end-start > 1:
        point = (start+end)//2
        if array[point] == '0':
            end = point
        else:
            start = point
    return end


print(task("1111111111111111111111111000000000"))
