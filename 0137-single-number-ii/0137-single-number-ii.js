/**
 * @param {number[]} nums
 * @return {number}
 */
const singleNumber = function(nums) {
    const map = new Map();

    for (let num of nums) {
        if (!map.has(num)) map.set(num, 0);
        map.set(num, map.get(num) + 1);
    }

    for (let [key, value] of map.entries()) {
        if (value === 1) return key;
    }
};