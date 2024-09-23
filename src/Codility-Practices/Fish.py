# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# using stack to store downstream fish
def solution(A, B):

    
    upstream_fish_survived = 0
    downstream_fishes= []   # stack

    AB = zip(A, B)

    for size, direction in AB:

        # collect downstream fishes
        if direction == 1:
            downstream_fishes.append(size)

        # upstream fish
        else:

            while downstream_fishes:
                dsfSize = downstream_fishes.pop()
                if dsfSize > size:
                    # put back downstream fish in stack cozits larger than upstream fish
                    downstream_fishes.append(dsfSize)
                    break
            # else:
            #     upstream_fish_survived += 1
            
            # same as while else, just testing. Using "While Else" is more elegant
            if not downstream_fishes:
                upstream_fish_survived += 1
                    

    result = upstream_fish_survived + len(downstream_fishes)

    return result


A = [4,3,2,1,5] #2
B = [0,1,0,0,0]

A = [4,3,2,1,5] #2
B = [0,1,0,1,0]

# # A = [4,5] #2
# # B = [1,1]

# # A = [1] #2
# # B = [0]

# # A = [4,3,2,1,5] #2
# # B = [0,1,0,0,0]
print(solution(A, B))

