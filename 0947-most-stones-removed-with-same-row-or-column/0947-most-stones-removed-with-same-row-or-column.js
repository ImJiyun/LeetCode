/**
 * @param {number[][]} stones
 * @return {number}
 */
const removeStones = function(stones) {
    let largest = 0;
    const visited = new Set();

    for (let [r, c] of stones) {
        if (visited.has(key(r, c))) continue;
        let count = dfs(r, c, stones, visited) - 1;
        largest = Math.max(largest, count);
    }
    return largest;
};

const dfs = (r, c, stones, visited) => {
    visited.add(key(r, c));
    let count = 1;

    for (let [nr, nc] of stones) {
        if (!visited.has(key(nr, nc)) && (r === nr || c === nc)) {
            count += dfs(nr, nc, stones, visited);
        }
    }
    return count;
}

const key = (x, y) => `${x},${y}`;