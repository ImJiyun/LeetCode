/**
 * @param {number[]} nums
 * @return {number}
 */
var arraySign = function(nums) {
    const product = nums.reduce((acc, num) => {
        return acc * num;
    })
    if (product > 0) return 1;
    else if (product < 0) return -1;
    else return 0;
};