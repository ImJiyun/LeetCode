/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    const greatest = Math.max(...candies); 
    const result = [];
    
    for (const candy of candies) { 
        if (candy + extraCandies >= greatest) {
            result.push(true);
        } else {
            result.push(false);
        }
    }
    return result;
};
