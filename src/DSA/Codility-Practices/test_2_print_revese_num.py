def solution(N):

    # error is at "% 10", rightmost digit when is 1, then prints.
    # did a "pass" at If statement as the code makes little sense. Hence the dicision to complete avoid the 
    # If condition, as the question does not state there should be a condition whether or not to print.

    N = int(str(N)[::-1].lstrip('0')[::-1]) # reverse string lstrip 0 and reverse again to original form
    enable_print = N % 10
    while N > 0:
        if enable_print == 0 and N % 10 != 0:
            enable_print = 1
        elif enable_print == 1:
            pass
        
        print(N % 10, end="")
        N = N // 10

# solution(1)
# solution(54321)
solution(11200)
# solution(1)
# solution(54321)
# solution(10011)