/**
 * @param {number[][]} edges
 * @return {number}
 */
var findCenter = function(edges) {
    const graph = {};
    for (let edge of edges) {
        const firstNode = edge[0];
        const secondNode = edge[1];
        if (!graph[firstNode]) graph[firstNode] = [secondNode];
        else graph[firstNode].push(secondNode);
        if (!graph[secondNode]) graph[secondNode] = [firstNode];
        else graph[secondNode].push(firstNode);
    }

    for (let item in graph) {
        if (graph[item].length === edges.length) return Number(item);
;    }
};