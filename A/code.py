def find_peak_time(n, sessions):
    events = []
    
    for s, f in sessions:
        events.append((s, 'start'))
        events.append((f, 'end'))
    
    # Сортируем события: по времени, затем 'end' идут после 'start'
    events.sort(key=lambda x: (x[0], x[1] == 'end'))
    
    max_count = 0
    current_count = 0
    best_time = 0
    
    for time, event in events:
        if event == 'start':
            current_count += 1
            if current_count > max_count:
                max_count = current_count
                best_time = time
        else:
            current_count -= 1
    
    return best_time

# Чтение ввода
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
sessions = [(int(data[i*2+1]), int(data[i*2+2])) for i in range(n)]

# Нахождение искомого времени
result = find_peak_time(n, sessions)
print(result)
