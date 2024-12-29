/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let zeroCnt = 0;
    let index = 0;

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== 0) {
            nums[index++] = nums[i];
        } else {
            zeroCnt++;
        }
    }

    while (zeroCnt > 0) {
        nums[index++] = 0;
        zeroCnt--;
    }
};