# TASK 1: Word Wrap using Dynamic Programming
def word_wrap(words, width):
    n=len(words)
    dp=[float("inf")]*(n+1); nxt=[-1]*(n+1)
    dp[n]=0
    for i in range(n-1,-1,-1):
        used=0
        for j in range(i,n):
            used += len(words[j]) + (1 if j>i else 0)
            if used>width: break
            unused=width-used
            penalty=0 if j==n-1 else unused**2
            if penalty+dp[j+1] < dp[i]:
                dp[i]=penalty+dp[j+1]; nxt[i]=j+1
    if nxt[0] == -1: raise ValueError("A word is wider than the line width.")
    lines=[]; i=0
    while i<n:
        j=nxt[i]; line_words=words[i:j]
        used=sum(map(len,line_words))+len(line_words)-1
        unused=width-used
        penalty=0 if j==n else unused**2
        lines.append((line_words,unused,penalty))
        i=j
    print(f"\\nWIDTH={width}; MINIMUM PENALTY={dp[0]}")
    for k,(ws,u,p) in enumerate(lines,1):
        print(f"Line {k}: {' '.join(ws)} | unused={u} | penalty={p}")
    print("DP states (minimum cost from word i to end):")
    for i,v in enumerate(dp[:-1]): print(f"dp[{i}] ({words[i]}): {v}; next index={nxt[i]}")
    return dp[0],lines

if __name__=="__main__":
    text="Dynamic programming finds an optimal arrangement of words in a document layout engine".split()
    for w in (18,22,26): word_wrap(text,w)
    print("\\nBoundary test: width smaller than longest word")
    try: word_wrap(["short","extraordinary","word"],8)
    except ValueError as e: print("Correctly handled:",e)
