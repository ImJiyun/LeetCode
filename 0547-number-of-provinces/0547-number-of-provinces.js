/**
 * @param {number[][]} isConnected
 * @return {number}
 */
const findCircleNum = function(isConnected) {
    const visited = new Set();
    let count = 0;

    for (let r = 0; r < isConnected.length; r++) {
        if (!visited.has(r)) {
            count++;
            dfs(isConnected, r, visited);
        }
    }
    return count;
};

const dfs = (graph, r, visited) => {
    for (let c = 0; c < graph[r].length; c++) {
        if (r === c) continue;
        if (visited.has(c)) continue;
        if (graph[r][c] === 0) continue;
        visited.add(c);
        dfs(graph, c, visited);
    }
}