class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_set<int> uset;
        vector<int> ans;
        for (int i = 0; i < nums.size(); ++i) {
            if (uset.find(target - nums[i]) != uset.end()) {
                ans.push_back(i);
                for (int j = 0; j < nums.size(); ++j) {
                    if (nums[j] == target - nums[i]) {
                        ans.push_back(j);
                        break;
                    }
                }
                break;
            }
            uset.insert(nums[i]);
        }
        return ans;
    }
};