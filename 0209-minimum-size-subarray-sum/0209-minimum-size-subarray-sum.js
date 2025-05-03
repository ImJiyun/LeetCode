/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
const minSubArrayLen = function(target, nums) {
    let leftIdx = 0;
    let minLen = Infinity;
    let sum = 0;
    
    for (let rightIdx = 0; rightIdx < nums.length; rightIdx++) {
        sum += nums[rightIdx];

        while (sum >= target) {
            minLen = Math.min(minLen, rightIdx - leftIdx + 1);
            sum -= nums[leftIdx];
            leftIdx++;
        }
    }

    return minLen === Infinity ? 0 : minLen;
};