from collections import defaultdict, deque

def parse_input(data):
    dependencies = defaultdict(list)
    lines = data.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if '->' in line:
            parts = line.split('->')
            package = parts[0].strip().strip('"')
            dependency = parts[1].split()[0].strip().strip('"')
            dependencies[dependency].append(package)  # Обратное отношение зависимости
            
            # Ensure every package is in the dependencies dictionary
            if package not in dependencies:
                dependencies[package] = []
            
    return dependencies

def topological_sort(dependencies):
    indegree = {pkg: 0 for pkg in dependencies}
    for deps in dependencies.values():
        for dep in deps:
            indegree[dep] += 1
    
    zero_indegree_queue = deque([pkg for pkg in indegree if indegree[pkg] == 0])
    sorted_packages = []
    
    while zero_indegree_queue:
        pkg = zero_indegree_queue.popleft()
        sorted_packages.append(pkg)
        
        for dep in dependencies[pkg]:
            indegree[dep] -= 1
            if indegree[dep] == 0:
                zero_indegree_queue.append(dep)
                
    if len(sorted_packages) != len(indegree):
        raise ValueError("Graph has a cycle, which should not be the case per problem statement.")
    
    return sorted_packages

# Чтение данных
import sys
data = sys.stdin.read()

# Парсинг и обработка
dependencies = parse_input(data)
sorted_packages = topological_sort(dependencies)

# Вывод результатов
for package in sorted_packages:
    print(package)
