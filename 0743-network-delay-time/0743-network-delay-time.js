/**
 * @param {number[][]} times
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
const networkDelayTime = function(times, n, k) {
    const adj = new Map();

    for (let i = 1; i <= n; i++) adj.set(i, []);
    for (let [u, v, w] of times) {
        adj.get(u).push([v, w]);
    }

    const dist = Array(n+1).fill(Infinity);
    dist[k] = 0;

    const pq = [[0, k]];

    while (pq.length > 0) {
        pq.sort((a, b) => a[0] - b[0]);
        const [currTime, node] = pq.shift();

        if (currTime > dist[node]) continue;

        for (const [neighbor,time] of adj.get(node)) {
            const newTime = currTime + time;
            if (newTime < dist[neighbor]) {
                dist[neighbor] = newTime;
                pq.push([newTime, neighbor]);
            }
        }
    }
    const maxTime = Math.max(...dist.slice(1));
    return maxTime === Infinity ? -1 : maxTime;
};