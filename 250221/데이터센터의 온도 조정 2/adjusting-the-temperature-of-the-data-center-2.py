N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

def max_workload(N, C, G, H, temperature_ranges):
    min_temp = min(t[0] for t in temperature_ranges)
    max_temp = max(t[1] for t in temperature_ranges)
    
    max_work = 0
    
    for temp in range(min_temp, max_temp + 1):
        total_work = 0
        for T_a, T_b in temperature_ranges:
            if temp < T_a:
                total_work += C
            elif T_a <= temp <= T_b:
                total_work += G
            else:
                total_work += H
        
        max_work = max(max_work, total_work)
    
    return max_work

print(max_workload(N, C, G, H, ranges))