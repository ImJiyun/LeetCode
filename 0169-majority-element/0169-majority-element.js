/**
 * @param {number[]} nums
 * @return {number}
 */
const majorityElement = function(nums) {
    const count = {};

    for (let num of nums) {
        if (!count[num]) count[num] = 1;
        else count[num]++;
    }

    let cnt = 0;
    let val = 0;

    for (let num in count) {
        if (count[num] > cnt) {
            cnt = count[num];
            val = Number(num);
        }
    }
    return val;
};