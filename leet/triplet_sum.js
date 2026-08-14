// Approach one

// sum == 0
/* 
Pehle array ko sort karo
Ek number ko fix karo (nums[i])
Duplicate fixed numbers ko skip karo
left pointer ko fixed number ke baad rakho
right pointer ko array ke end par rakho
Teen numbers ka sum nikalo
Agar sum 0 hai:
Triplet ko result mein add karo
left++ aur right-- karo
Duplicate left values skip karo
Duplicate right values skip karo
Agar sum 0 se chhota hai:
left++ karo (bada sum chahiye)
Agar sum 0 se bada hai:
right-- karo (chhota sum chahiye)
Jab tak left < right hai, process repeat karo
Sab fixed elements check hone ke baad result return karo */
var threeSum = function (nums) {
    nums.sort((a, b) => a - b);

    let result = [];

    for (let i = 0; i < nums.length - 2; i++) {

        // Duplicate first element skip karo
        if (i > 0 && nums[i] === nums[i - 1]) {
            continue;
        }

        let left = i + 1;
        let right = nums.length - 1;

        while (left < right) {

            let sum = nums[i] + nums[left] + nums[right];

            if (sum === 0) {
                result.push([nums[i], nums[left], nums[right]]);

                left++;
                right--;

                // Duplicate left values skip karo
                while (left < right && nums[left] === nums[left - 1]) {
                    left++;
                }

                // Duplicate right values skip karo
                while (left < right && nums[right] === nums[right + 1]) {
                    right--;
                }

            } else if (sum < 0) {
                left++;

            } else {
                right--;
            }
        }
    }

    return result;
};