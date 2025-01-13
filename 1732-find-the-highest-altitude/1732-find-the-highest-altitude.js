/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
    const arr = [0];
    let idx = 0;
    for (item of gain) {
        arr.push(arr[idx++] + item);
    }
    arr.sort((a, b) => a - b);
    return arr[arr.length - 1];
};