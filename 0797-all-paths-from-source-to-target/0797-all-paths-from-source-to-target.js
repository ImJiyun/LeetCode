/**
 * @param {number[][]} graph
 * @return {number[][]}
 */
const allPathsSourceTarget = function(graph) {
    
    const list = new Map();

    for (let i = 0; i < graph.length; i++) {
        list.set(i, graph[i]);
    }

    const allPaths = [];

    const visited = new Set();
    findPath(0, list, visited, allPaths);

    return allPaths;
};

const findPath = (curr, list, visited, track) => {
    if (curr === list.size - 1) {
        track.push([...visited, curr]);
    }

    visited.add(curr);

    for (let node of list.get(curr)) {
        if (visited.has(node)) continue;
        findPath(node, list, visited, track);
        visited.delete(node);
    }
}