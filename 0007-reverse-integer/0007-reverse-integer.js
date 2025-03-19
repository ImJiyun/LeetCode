/**
 * @param {number} x
 * @return {number}
 */
const reverse = function(x) {
    const isNegative = x < 0;
    let reversed = Number(Math.abs(x).toString().split("").reverse().join(""));
    if (isNegative) reversed *= -1;

    if (reversed < -(2**31) || reversed > (2**31 - 1)) {
        return 0;
    }
    return reversed;
};