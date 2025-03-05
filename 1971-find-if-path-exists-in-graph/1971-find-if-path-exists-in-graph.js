/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} source
 * @param {number} destination
 * @return {boolean}
 */
const validPath = function(n, edges, source, destination) {
    const graph = {};

    for (let [u, v] of edges) {
        (graph[u] ??= []).push(v);
        (graph[v] ??= []).push(u);
    }

    const queue = [source];
    const visited = new Set();
    visited.add(source);

    while (queue.length > 0) {
        const curr = queue.shift();

        if (curr === destination) return true;

        for (let node of graph[curr]) {
            if (!visited.has(node)) {
                visited.add(node);
                queue.push(node);
            }
        }
    }
    return false;
};