/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function(nums) {
    let maximum = -Infinity
    let secondMaximum = -Infinity
    let thirdMaximum = -Infinity

    for (let num of nums){
        if (num === maximum || num === secondMaximum || num === thirdMaximum) {
            continue
        }
        if (num > maximum) {
            thirdMaximum = secondMaximum
            secondMaximum = maximum
            maximum = num
        }
        else if (num > secondMaximum) {
            thirdMaximum = secondMaximum
            secondMaximum = num
        }
        else if (num > thirdMaximum) {
            thirdMaximum = num
        }

    }
    return thirdMaximum === -Infinity ? maximum : thirdMaximum
};