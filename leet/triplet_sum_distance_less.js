// TRIPLET SUM LESS DISTANCE \\
/*
Pehle array ko sort karo
Ek number ko fix karo (nums[i])
maxDiff = Infinity aur resultSum initialize karo
left pointer ko fixed number ke baad rakho (i + 1)
right pointer ko array ke end par rakho
Teen numbers ka sum nikalo
Target aur sum ke beech ka difference nikalo (Math.abs(sum - target))
Agar current difference ab tak ke smallest difference se chhota hai:
maxDiff update karo
resultSum mein current sum store karo
Agar sum target ke barabar hai:
Sum ko turant return kar do (exact answer mil gaya)
Agar sum target se chhota hai:
left++ karo (bada sum chahiye)
Agar sum target se bada hai:
right-- karo (chhota sum chahiye)
Jab tak left < right hai, process repeat karo
Sab fixed elements check hone ke baad resultSum return karo ✅
*/
var threeSumClosest = function(nums, target) {
    nums.sort((a, b) => a - b);

    let maxDiff = Infinity;
    let resultSum;

    for (let i = 0; i < nums.length - 2; i++) {
        let left = i + 1;
        let right = nums.length - 1;

        while (left < right) {
            let sum = nums[i] + nums[left] + nums[right];
            let diff = Math.abs(sum - target);

            if (diff < maxDiff) {
                maxDiff = diff;
                resultSum = sum;
            }

            if (sum < target) {
                left++;
            } else if (sum > target) {
                right--;
            } else {
                return sum; // exact match
            }
        }
    }

    return resultSum;
};