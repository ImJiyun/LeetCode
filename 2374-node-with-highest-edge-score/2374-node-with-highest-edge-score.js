/**
 * @param {number[]} edges
 * @return {number}
 */
const edgeScore = function(edges) {
    const nodes = new Map();

    for (let i = 0; i < edges.length; i++) {
        if (!nodes.has(edges[i])) nodes.set(edges[i], 0);
        nodes.set(edges[i], nodes.get(edges[i]) + i);   
    }

    const noDuplicates = new Set(edges);

    let highest = -1;
    let index = 0;
    for (let idx of noDuplicates) {
        if (nodes.get(idx) > highest) {
            highest = nodes.get(idx);
            index = idx;
        } else if (nodes.get(idx) === highest) {
            index >= idx ? index = idx : index = index;
        }
    }
    return index;
};