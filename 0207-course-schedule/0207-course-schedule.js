/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
const canFinish = function(numCourses, prerequisites) {
    const graph = new Map();

    for (let [u, v] of prerequisites) {
        if (!graph.has(v)) graph.set(v, []);
        graph.get(v).push(u);
    }

    for (let key of [...graph.keys()]) {
        if (hasCycle(key, key, graph)) return false;
    }
    return true;

};

const hasCycle = (start, curr, graph) => {
    if (graph.has(curr)) {
        for ( let node of graph.get(curr)) {
            if (start === node) return true;
            if (hasCycle(start, node, graph)) return true;
        }
    }
    
    return false;
}