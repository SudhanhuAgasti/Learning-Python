/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function (nums) {
    // Arrays for negative and positive numbers
    let a = [];
    let b = [];

    // Separate negative and positive numbers
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] >= 0) {
            b.push(nums[i]);// positive 
        } else {
            a.push(nums[i]);// negetive
        }
    }

    // Square negative numbers
    for (let i = 0; i < a.length; i++) {
        a[i] = a[i] * a[i];
    }

    // Reverse negative squares
    // Example: [49, 9, 1] -> [1, 9, 49]
    a.reverse();

    // Square positive numbers
    for (let i = 0; i < b.length; i++) {
        b[i] = b[i] * b[i];
    }

    // Merge the two sorted arrays
    let i = 0;
    let j = 0;
    let id = 0;

    let n = a.length;
    let m = b.length;

    let res = new Array(n + m);

    // Compare and merge
    while (i < n && j < m) {
        if (a[i] <= b[j]) {
            res[id] = a[i];
            i++;
        } else {
            res[id] = b[j];
            j++;
        }

        id++;
    }

    // Add remaining elements from a
    while (i < n) {
        res[id] = a[i];
        i++;
        id++;
    }

    // Add remaining elements from b
    while (j < m) {
        res[id] = b[j];
        j++;
        id++;
    }

    return res;
};