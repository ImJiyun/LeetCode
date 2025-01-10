/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    const counts = {};
    for (let i = 0; i < nums.length; i++) {
        let num = nums[i];
        if (counts[num] == null) counts[num] = 1;
        else counts[num]++;
    }

    let maxCount = 0;
    let maxNum = 0;

    for (num in counts) {
        if (+counts[num] > maxCount) {
            maxCount = +counts[num];
            maxNum = +num;
        }
    }
    return maxNum;
};