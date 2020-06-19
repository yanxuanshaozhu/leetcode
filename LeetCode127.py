from collections import defaultdict


def ladderLength(beginWord: str, endWord: str, wordList: list) -> int:
    words = defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            key = word[:i] + "@" + word[i + 1:]
            words[key].append(word)
    result = [(beginWord, 1)]
    visited = {beginWord: True}
    while result:
        curword, curdidst = result.pop(0)
        for i in range(len(curword)):  # Find all connected words of curword
            temp = curword[:i] + "@" + curword[i + 1:]
            for word in words[temp]:
                if word not in visited:
                    visited[word] = True
                    if word == endWord:
                        return curdidst + 1
                    result.append((word, curdidst + 1))

    return 0  # When the result has already been an empty queue, yet not curdist + 1 is returned, this means
    # the endWord is not in the connected words of startWord


if __name__ == "__main__":
    begin = "hot"
    end = "dog"
    ls = ["hot", "dog"]
    print(ladderLength(begin, end, ls))
