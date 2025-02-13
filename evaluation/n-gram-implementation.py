def main():
    ref = "It will be a sort of bridge"
    hyp = "It will sort of be a bridge"
    
    ref_split = ref.split()
    hyp_split = hyp.split()
    
    # Build distance matrix
    distance_matrix = [[float("inf") for i in range(len(hyp_split) + 2)] for j in range(len(ref_split) + 2)]
    
    # Set initial position to infinity    
    set_initial_distances(distance_matrix, len(ref_split) + 2, len(hyp_split) + 2)
    # Traverse Matrix
    traverse_matrix(distance_matrix, len(ref_split) + 2, len(hyp_split) + 2)
    
    

    print_matrix(distance_matrix)
    
def set_initial_distances(distance_matrix, row, column):
    for i in range(row):
        distance_matrix[0][i] = i
        distance_matrix[i][0] = i

def traverse_matrix(distance_matrix, row, column):
    pass
        
def print_matrix(m):
    for i in m:
        print(i)

if __name__ == "__main__":
    main()