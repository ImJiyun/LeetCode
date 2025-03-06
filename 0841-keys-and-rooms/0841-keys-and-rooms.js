/**
 * @param {number[][]} rooms
 * @return {boolean}
 */
const canVisitAllRooms = function(rooms) {
    const visited = new Set();
  
    dfs(rooms, 0, visited);

    return visited.size === rooms.length;
};

const dfs = (graph, node, visited) => {
    visited.add(node);

    for (let i = 0; i < graph[node].length; i++) {
        if (visited.has(graph[node][i])) continue;
        
        dfs(graph, graph[node][i], visited);
    }
}
