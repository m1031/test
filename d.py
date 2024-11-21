from collections import defaultdict, deque
graph = defaultdict(list)
def add_edge(start, end, distance):
    graph[start].append((end, distance))
    graph[end].append((start, distance))
def build_graph(edges):
    for edge in edges:
        start, end, distance = map(str.strip, edge.split(','))
        add_edge(int(start), int(end), float(distance))
# 幅優先探索で最も長い片道切符の旅を求める
def longest_path(graph):
    max_distance = 0
    longest_path = []
    starta=len(graph)
    for start in range(starta):
        queue = deque([(start, 0, [start], False)])  # (現在の駅, 累積距離, 経路, 始発点に戻ったかどうか)
        while queue:
            current, dist, path, returned_to_start = queue.popleft()
            # 最長距離を更新（始発点に戻った場合か、まだ戻っていない途中の経路も評価）
            if dist > max_distance and (not returned_to_start or (returned_to_start and path[-1] == path[0])):
                max_distance = dist
                longest_path = path
            for neighbor, neighbor_dist in graph[current]:
                if neighbor not in path:
                    # 通常の駅を訪問する場合
                    queue.append((neighbor, dist + neighbor_dist, path + [neighbor], returned_to_start))
                elif neighbor == start and not returned_to_start and current != start:
                    # 始発点に戻る場合（経路の途中で1回のみ許可）
                    queue.append((neighbor, dist + neighbor_dist, path + [neighbor], True))
    return longest_path, max_distance
# 入力例
edges=[]
check=0
while check==0:
    edge=input()
    check=int(input())
    edges.append(edge)
# グラフを構築
build_graph(edges)
path, distance = longest_path(graph)
# 結果を出力
print("最も長い片道切符の旅の経路:", "->".join(map(str, path)))
print("距離:", distance)