/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    if (n < 0) {
        x = 1 / x;
        n *= -1;
    }
    if (n < 1) return 1;
    if (n % 2 === 0) {
        let half = myPow(x, n / 2);
        return half * half;
    }
    return x * myPow(x, n - 1);
};