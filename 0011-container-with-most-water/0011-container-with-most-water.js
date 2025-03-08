/**
 * @param {number[]} height
 * @return {number}
 */
const maxArea = function(height) {
    let left = 0, right = height.length - 1;
    let largest = 0;

    while (left < right) {
        let h = Math.min(height[left], height[right]);
        largest = Math.max(largest, h * (right - left));

        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }

    return largest;
};