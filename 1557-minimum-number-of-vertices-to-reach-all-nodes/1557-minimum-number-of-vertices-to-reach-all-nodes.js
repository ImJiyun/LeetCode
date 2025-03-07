/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
const findSmallestSetOfVertices = function(n, edges) {
    const nodes = new Set();

    for (let edge of edges) {
        nodes.add(edge[1]);
    }

    const from = [];

    for (let i = 0; i < n; i++) {
        if (!nodes.has(i)) from.push(i);
    }

    return from;
};