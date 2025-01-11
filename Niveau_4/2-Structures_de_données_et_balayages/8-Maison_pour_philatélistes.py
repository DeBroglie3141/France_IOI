def trouver_distance_minimale(N, positions):
    positions.sort()
    
    distance_minimale = float('inf')
    
    for i in range(1, N):
        distance = abs(positions[i] - positions[i-1])
        if distance < distance_minimale:
            distance_minimale = distance
    
    return distance_minimale

N = int(input())
positions = list(map(int, input().split()))

print(trouver_distance_minimale(N, positions))