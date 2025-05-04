/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
const findOrder = function(numCourses, prerequisites) {
    const adj = new Map();
    const inDegree = Array(numCourses).fill(0);

    for (let i = 0; i < numCourses; i++) {
        adj.set(i, []);
    }

    for (let [to, from] of prerequisites) {
        adj.get(from).push(to);
        inDegree[to]++;
    }

    const queue = [];

    for (let i = 0; i < inDegree.length; i++) {
        if (inDegree[i] === 0) queue.push(i);
    }

    const result = [];

    while (queue.length > 0) {
        const curr = queue.shift();
        result.push(curr);

        for (let neighbor of adj.get(curr)) {
            inDegree[neighbor]--;
            if (inDegree[neighbor] === 0) queue.push(neighbor);
        }
    }
    
    return result.length === numCourses ? result : [];
};