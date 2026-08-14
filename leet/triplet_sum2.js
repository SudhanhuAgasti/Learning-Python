// approach 2
var threeSum = function (nums) {
    let ans = []
    nums.sort((a, b) => a - b);
    for (let i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i - 1] == nums[i]) continue;
        if (nums[i] > 0) break;
        let j = i + 1, k = nums.length - 1;
        while (j < k) { 
            if (nums[j] + nums[k] + nums[i] == 0) {
                ans.push([nums[i], nums[j], nums[k]]);
                j++;
                while (j < nums.length && nums[j - 1] == nums[j]) j++;
                k--;
                while (k > j && nums[k + 1] == nums[k])
                    k--;
            } else if (nums[j] + nums[k] + nums[i] > 0) {
                k--;
            } else {
                j++;
            }
        }

    }

    return ans;
};