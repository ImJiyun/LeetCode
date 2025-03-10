/**
 * @param {number[]} nums
 * @return {number}
 */
const maximumGap = function(nums) {
    if (nums.length < 2) return 0;
    nums.sort((a,b) => a - b);

    let max = 0;

    for (let i = 0; i < nums.length - 1; i++) {
        let diff = nums[i+1] - nums[i];
        max = Math.max(max, diff);
    }
    return max;
};