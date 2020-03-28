def floydWarshall(graph): 
	dist = map(lambda i : map(lambda j : j , i) , graph) 
	for k in range(V): 
		 for i in range(V): 
			for j in range(V): 
				 dist[i][j] = min(dist[i][j] , 
                                  dist[i][k]+ dist[k][j] 
                                ) 
	print "Following matrix shows the shortest distances\ 
 	between every pair of vertices" 
    	for i in range(V): 
        	for j in range(V): 
            	if(dist[i][j] == INF): 
                	print "%7s" %("INF"), 
            	else: 
                	print "%7d\t" %(dist[i][j]), 
            	if j == V-1: 
                print "" 