/**
 * @param {number} n
 * @return {number}
 */
const climbStairs = function(n) {
    const dp = [1, 1];
    for (let i = 2; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    return dp[n];
};