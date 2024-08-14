def find_min_arrow_shots(points):
    sorted_points = sorted(points, key= lambda x: x[0])
    print(sorted_points)
    x_end = float('-inf')
    count = 0
    for point in sorted_points:
        if point[0] > x_end:
            count += 1
            x_end = point[1]
            
    return count

points = [[8,9],[7,14],[10,16],[17,20]]
print(find_min_arrow_shots(points))