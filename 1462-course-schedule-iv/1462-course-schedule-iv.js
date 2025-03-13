/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @param {number[][]} queries
 * @return {boolean[]}
 */
const checkIfPrerequisite = function(numCourses, prerequisites, queries) {
    const map = new Map();
    const answer = [];

    function putList(prerequisites) {
        if (prerequisites.length === 0) return;

        for (let [prev, dst] of prerequisites) {
            if (!map.has(prev)) map.set(prev, []);
            map.get(prev).push(dst);
        }
    }

    putList(prerequisites);

    function dfs(src, dst, visited) {
        if (src === dst) return true;
        if (visited.has(src)) return false;

        visited.add(src);

        if (map.has(src)) {
            for (let next of map.get(src)) {
                if (dfs(next, dst, visited)) return true;
            }
        }
        return false;
    }

    for (let [prev, dst] of queries) {
        answer.push(dfs(prev, dst, new Set()));
    }

    return answer;
};