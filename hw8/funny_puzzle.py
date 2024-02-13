import heapq

def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: implement this function. This function will not be tested directly by the grader. 

    INPUT: 
        Two states (if second state is omitted then it is assumed that it is the goal state)

    RETURNS:
        A scalar that is the sum of Manhattan distances for all tiles.
    """
    dis = ([0,0], [1,0], [2,0], [0,1], [1,1], [2,1], [0,2], [1,2], [2,2])
    distance = 0
    num = 0

    for i in from_state:
        if i == 0:
            distance += 0
            num += 1
            
        else:
            distance += (abs(dis[i-1][0]-dis[num][0]) + abs(dis[i-1][1]-dis[num][1]))
            num += 1

    return distance

def print_succ(state):
    """
    TODO: This is based on get_succ function below, so should implement that function.

    INPUT: 
        A state (list of length 9)

    WHAT IT DOES:
        Prints the list of all the valid successors in the puzzle. 
    """
    succ_states = get_succ(state)

    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))


def get_succ(state):
    """
    TODO: implement this function.

    INPUT: 
        A state (list of length 9)

    RETURNS:
        A list of all the valid successors in the puzzle (don't forget to sort the result as done below). 
    """
    succ_states = []
    for i in range(len(state)):
        if state[i] == 0:
            if i == 0:
                if state[1] != 0:
                    copyS = state[:]
                    copyS[0] = state[1]
                    copyS[1] = 0
                    succ_states.append(copyS)
                if state[3] != 0:
                    copyS = state[:]
                    copyS[0] = state[3]
                    copyS[3] = 0
                    succ_states.append(copyS)
            if i == 1:
                if state[0] != 0:
                    copyS = state[:]
                    copyS[1] = state[0]
                    copyS[0] = 0
                    succ_states.append(copyS)
                if state[2] != 0:
                    copyS = state[:]
                    copyS[1] = state[2]
                    copyS[2] = 0
                    succ_states.append(copyS)
                if state[4] != 0:
                    copyS = state[:]
                    copyS[1] = state[4]
                    copyS[4] = 0
                    succ_states.append(copyS)
            if i == 2:
                if state[1] != 0:
                    copyS = state[:]
                    copyS[2] = state[1]
                    copyS[1] = 0
                    succ_states.append(copyS)
                if state[5] != 0:
                    copyS = state[:]
                    copyS[2] = state[5]
                    copyS[5] = 0
                    succ_states.append(copyS)
            if i == 3:
                if state[0] != 0:
                    copyS = state[:]
                    copyS[3] = state[0]
                    copyS[0] = 0
                    succ_states.append(copyS)
                if state[4] != 0:
                    copyS = state[:]
                    copyS[3] = state[4]
                    copyS[4] = 0
                    succ_states.append(copyS)
                if state[6] != 0:
                    copyS = state[:]
                    copyS[3] = state[6]
                    copyS[6] = 0
                    succ_states.append(copyS)
            if i == 4:
                if state[1] != 0:
                    copyS = state[:]
                    copyS[4] = state[1]
                    copyS[1] = 0
                    succ_states.append(copyS)
                if state[3] != 0:
                    copyS = state[:]
                    copyS[4] = state[3]
                    copyS[3] = 0
                    succ_states.append(copyS)
                if state[5] != 0:
                    copyS = state[:]
                    copyS[4] = state[5]
                    copyS[5] = 0
                    succ_states.append(copyS)
                if state[7] != 0:
                    copyS = state[:]
                    copyS[4] = state[7]
                    copyS[7] = 0
                    succ_states.append(copyS)
            if i == 5:
                if state[2] != 0:
                    copyS = state[:]
                    copyS[5] = state[2]
                    copyS[2] = 0
                    succ_states.append(copyS)
                if state[4] != 0:
                    copyS = state[:]
                    copyS[5] = state[4]
                    copyS[4] = 0
                    succ_states.append(copyS)
                if state[8] != 0:
                    copyS = state[:]
                    copyS[5] = state[8]
                    copyS[8] = 0
                    succ_states.append(copyS)
            if i == 6:
                if state[3] != 0:
                    copyS = state[:]
                    copyS[6] = state[3]
                    copyS[3] = 0
                    succ_states.append(copyS)
                if state[7] != 0:
                    copyS = state[:]
                    copyS[6] = state[7]
                    copyS[7] = 0
                    succ_states.append(copyS)
            if i == 7:
                if state[4] != 0:
                    copyS = state[:]
                    copyS[7] = state[4]
                    copyS[4] = 0
                    succ_states.append(copyS)
                if state[6] != 0:
                    copyS = state[:]
                    copyS[7] = state[6]
                    copyS[6] = 0
                    succ_states.append(copyS)
                if state[8] != 0:
                    copyS = state[:]
                    copyS[7] = state[8]
                    copyS[8] = 0
                    succ_states.append(copyS)
            if i == 8:
                if state[5] != 0:
                    copyS = state[:]
                    copyS[8] = state[5]
                    copyS[5] = 0
                    succ_states.append(copyS)
                if state[7] != 0:
                    copyS = state[:]
                    copyS[8] = state[7]
                    copyS[7] = 0
                    succ_states.append(copyS)



    return sorted(succ_states)

def check_exist(find_list, s):  
    r = False         
    for find in find_list:
        if find[1] == s:
            r = True
    return r         

def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: Implement the A* algorithm here.

    INPUT: 
        An initial state (list of length 9)

    WHAT IT SHOULD DO:
        Prints a path of configurations from initial state to goal state along  h values, number of moves, and max queue number in the format specified in the pdf.
    """
    state_info_list = []
    max_length = 0

    start_list = []
    find_list = []
    current_index = 0
    m = 0

    #make the starting state
    heapq.heappush(start_list,(get_manhattan_distance(state, goal_state), state, (0,get_manhattan_distance(state, goal_state),current_index, -1)))
    # heapq.heappush(state_info_list,(start_list[1],start_list[2][1],m))

    while len(start_list) > 0:
        #first move the start point to find list
        first = heapq.heappop(start_list)
        heapq.heappush(find_list, first)

        if first[1] == goal_state:
            break
        
        succ = get_succ(first[1])
        for s in succ:
            if check_exist(find_list, s) == False:
                g = first[2][0] + 1
                h = get_manhattan_distance(s, goal_state)
                cost = g + h
                current_index += 1
                pre_index = first[2][2]
                new = (cost, s, (g,h,current_index, pre_index))
                heapq.heappush(start_list, new)

    #Traceback from the last to the first
    traceback = []
    trace = 0
    traceback.append(find_list[-1])
    while traceback[-1][2][2] != 0:
        for i in find_list:
            if traceback[-1] == state:
                break
            if i[2][2] == traceback[trace][2][3]:
                trace += 1
                traceback.append(i)
    traceback.reverse()

    for t in traceback:
        state_info_list.append((t[1],t[2][1],t[2][0]))
    max_length = len(start_list) + 1


    # This is a format helper.
    # build "state_info_list", for each "state_info" in the list, it contains "current_state", "h" and "move".
    # define and compute max length
    # it can help to avoid any potential format issue.
    for state_info in state_info_list:
        current_state = state_info[0]
        h = state_info[1]
        move = state_info[2]
        print(current_state, "h={}".format(h), "moves: {}".format(move))
    print("Max queue length: {}".format(max_length))

if __name__ == "__main__":
    """
    Feel free to write your own test code here to exaime the correctness of your functions. 
    Note that this part will not be graded.
    """
    print_succ([2,5,1,4,0,6,7,0,3])
    print()

    print(get_manhattan_distance([2,5,1,4,0,6,7,0,3], [1, 2, 3, 4, 5, 6, 7, 0, 0]))
    print()

    solve([2,5,1,4,0,6,7,0,3])
    print()
