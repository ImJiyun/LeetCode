/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let counts = {}; 
    for (let num of nums) {
        if (counts[num] == null) counts[num] = 1; 
        else counts[num]++;
    }

    for (let count in counts) {
        if (counts[count] === 1) return +count; 
    }
};
