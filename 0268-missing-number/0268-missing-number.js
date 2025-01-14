/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    nums.sort((a,b) => a - b);
    
    let number = 0;
    for (num of nums) {
        if (num === number) number++;
        else {
            return number;
        }
    }
    return nums.length;
};