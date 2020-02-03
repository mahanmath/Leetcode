class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        if(not endWord in wordList):
            return []
        wordList.append(beginWord)
    
        L = len(beginWord)
        
        all_combo_dict = {}
        for word in wordList:
            for i in range(L):
                gen_word = word[:i] + "*" + word[i+1:]
                if(gen_word in all_combo_dict):
                    all_combo_dict[gen_word].append(word)
                else:
                    all_combo_dict[gen_word] = [word]
        
        def edgeDetection(v_1, v_2, all_combo_dict, L):
            if(v_1 == v_2):
                return False
            for i in range(L):
                gen_word = v_1[:i] + "*" + v_1[i+1:]
                if v_2 in all_combo_dict[gen_word]:
                    return True
            return False
        
        visited = {word: False for word in wordList}
        visited[beginWord] = True
        
        parent = {word: [] for word in wordList}
        parent[beginWord] = beginWord
        
        distance = {word: L+1 for word in wordList}
        distance[beginWord] = 1
    
        Q = [beginWord]
        
        found = False
        
        while(Q and not found):
                vertex = Q.pop(0)
                for i in range(L):
                    generic_word = vertex[:i] + "*" + vertex[i+1:]
                    for word in all_combo_dict[generic_word]:
                        if(not visited[word]):
                            Q.append(word)
                            visited[word] = 1
                            distance[word] = distance[vertex] + 1
                            if(word == endWord):
                                found = True
                                break
        if(not found): return []
        
        BFS_distance = [[word for word in wordList if distance[word] == d]
                                for d in range(1, distance[endWord] + 1)]

        paths = [[endWord]]
        
        for d in reversed(range(1, distance[endWord])):
            new_paths = []
            for word in BFS_distance[d-1]:
                for path in paths:
                        if edgeDetection(word, path[0], all_combo_dict, L):
                            path_temp = path.copy()
                            path_temp.insert(0, word)
                            if (not path_temp in new_paths):
                                new_paths.append(path_temp)
            paths = new_paths
        
        return(paths)