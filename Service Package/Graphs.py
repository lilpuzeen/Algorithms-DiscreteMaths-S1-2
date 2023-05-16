import itertools


def Dijkstra(G, s):
	# Initialize
	Q = set(G.keys())
	dist = {}
	prev = {}
	for v in Q:
		dist[v] = float('inf')
		prev[v] = None
	dist[s] = 0
	# Main loop
	while Q:
		u = min(Q, key=dist.get)
		Q.remove(u)
		for v in G[u]:
			alt = dist[u] + G[u][v]
			if alt < dist[v]:
				dist[v] = alt
				prev[v] = u
	return dist, prev


def FloydWarshall(G):
	# Initialize
	dist = {}
	for u in G:
		dist[u] = {}
		for v in G:
			dist[u][v] = float('inf')
		dist[u][u] = 0
		for v in G[u]:
			dist[u][v] = G[u][v]
	# Main loop
	for k in G:
		for i in G:
			for j in G:
				dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
	return dist


def BellmanFord(G, s):
	# Initialize
	dist = {}
	prev = {}
	for v in G:
		dist[v] = float('inf')
		prev[v] = None
	dist[s] = 0
	# Main loop
	for i in range(len(G) - 1):
		for u in G:
			for v in G[u]:
				alt = dist[u] + G[u][v]
				if alt < dist[v]:
					dist[v] = alt
					prev[v] = u
	# Check for negative cycles
	for u in G:
		for v in G[u]:
			assert dist[v] <= dist[u] + G[u][v]
	return dist, prev


def Johnson(G):
	# Initialize
	H = {}
	for u in G:
		H[u] = {}
		for v in G[u]:
			H[u][v] = G[u][v]
	for v in G:
		H[v][v] = 0
	# Main loop
	dist = BellmanFord(H, v)[0]
	for u in G:
		for v in G[u]:
			G[u][v] += dist[u] - dist[v]
	dist = {}
	for u in G:
		dist[u] = Dijkstra(G, u)[0]
		for v in dist[u]:
			dist[u][v] += dist[v][u] - dist[u][u]
	return dist


def Prim(G):
	# Initialize
	Q = set(G.keys())
	dist = {}
	prev = {}
	for v in Q:
		dist[v] = float('inf')
		prev[v] = None
	dist[list(Q)[0]] = 0
	# Main loop
	while Q:
		u = min(Q, key=dist.get)
		Q.remove(u)
		for v in G[u]:
			if v in Q and G[u][v] < dist[v]:
				dist[v] = G[u][v]
				prev[v] = u
	return dist, prev


def Kruskal(G):
	# Initialize
	Q = set(G.keys())
	dist = {}
	prev = {}
	for v in Q:
		dist[v] = float('inf')
		prev[v] = None
	dist[list(Q)[0]] = 0
	# Main loop
	while Q:
		u = min(Q, key=dist.get)
		Q.remove(u)
		for v in G[u]:
			if v in Q and G[u][v] < dist[v]:
				dist[v] = G[u][v]
				prev[v] = u
	return dist, prev


def FordFulkerson(G, s, t):
	# Initialize
	flow = {}
	for u in G:
		flow[u] = {}
		for v in G[u]:
			flow[u][v] = 0
	# Main loop
	while True:
		# Find an augmenting path
		Q = set(G.keys())
		dist = {}
		prev = {}
		for v in Q:
			dist[v] = float('inf')
			prev[v] = None
		dist[s] = 0
		while Q:
			u = min(Q, key=dist.get)
			Q.remove(u)
			for v in G[u]:
				if dist[v] == float('inf') and G[u][v] > flow[u][v]:
					dist[v] = dist[u] + 1
					prev[v] = u
		if dist[t] == float('inf'):
			break
		# Augment flow along the path
		delta = float('inf')
		v = t
		while v != s:
			u = prev[v]
			delta = min(delta, G[u][v] - flow[u][v])
			v = u
		v = t
		while v != s:
			u = prev[v]
			flow[u][v] += delta
			flow[v][u] -= delta
			v = u
	# Compute value of the flow
	value = 0
	for v in G[s]:
		value += flow[s][v]
	return value, flow


def traveling_salesman(G, s):
	# Initialize
	n = len(G)
	A = {}
	for m in range(1, n):
		A[(frozenset([s]), s)] = (0, None)
	# Main loop
	for m in range(1, n):
		B = {}
		for S in [frozenset(C) | {j} for C in itertools.combinations(G.keys(), m) for j in G.keys() if j not in C]:
			for j in S:
				B[(S, j)] = min((A[(S-{j}, k)][0] + G[k][j], k) for k in S if k != j)
		A = B
	res = min((A[d][0] + G[d[1]][s], d[1]) for d in iter(A))
	# Reconstruct the path
	path = []
	while res[1] is not None:
		path.append(res[1])
		res = A[(frozenset(path), res[1])]
	return res[0], path[::-1] + [s]


def dfs(G, s):
	visited = set()
	stack = [s]
	while stack:
		u = stack.pop()
		if u not in visited:
			visited.add(u)
			stack.extend(G[u] - visited)
	return visited


def bfs(G, s):
	visited = set()
	queue = [s]
	while queue:
		u = queue.pop(0)
		if u not in visited:
			visited.add(u)
			queue.extend(G[u] - visited)
	return visited


def graph_paint(G, k):
	# Initialize
	color = {}
	for v in G:
		color[v] = None
	# Main loop
	for v in G:
		if color[v] is None:
			color[v] = 0
			queue = [v]
			while queue:
				u = queue.pop(0)
				for w in G[u]:
					if color[w] is None:
						color[w] = (color[u] + 1) % k
						queue.append(w)
					elif color[w] == color[u]:
						return False
	return True


G = {
	'a': {'b', 'c'},
	'b': {'a', 'c', 'd'},
	'c': {'a', 'b', 'd', 'e'},
	'd': {'b', 'c', 'e', 'f'},
	'e': {'c', 'd'},
	'f': {'d'}
}
# print('Dijkstra')
# print(Dijkstra(G, 'a'))
# print('BellmanFord')
# print(BellmanFord(G, 'a'))
# print('FloydWarshall')
# print(FloydWarshall(G))
# print('Prim')
# print(Prim(G))
# print('Kruskal')
# print(Kruskal(G))
# print('FordFulkerson')
# print(FordFulkerson(G, 'a', 'c'))
# print('traveling_salesman')
# print(traveling_salesman(G, 'a'))
# print('dfs')
# print(dfs(G, 'a'))
# print('bfs')
# print(bfs(G, 'a'))
print('graph_paint')
print(graph_paint(G, 2))