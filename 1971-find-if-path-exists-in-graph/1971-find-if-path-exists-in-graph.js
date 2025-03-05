/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} source
 * @param {number} destination
 * @return {boolean}
 */
const validPath = function(n, edges, source, destination) {
    if (source === destination) return true; 

    const graph = new Map();

    for (let [u, v] of edges) {
        if (!graph.has(u)) graph.set(u, []);
        if (!graph.has(v)) graph.set(v, []);
        graph.get(u).push(v);
        graph.get(v).push(u);
    }

    const queue = [source];
    const visited = new Set();
    visited.add(source);

    while (queue.length > 0) {
        const curr = queue.shift();

        if (curr === destination) return true;

        for (let node of graph.get(curr)) {
            if (!visited.has(node)) {
                visited.add(node);
                queue.push(node);
            }
        }
    }
    return false;
};