/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const searchRange = function(nums, target) {
    let first = nums.findIndex(num => num === target);
    let last = nums.findLastIndex(num => num === target);

    if (!first || !last) return [-1, -1];
    return [first, last];
};