bool check(int x) {/* ... */}  # 检查 x 是否满足某种性质

# 区间[l, r]被划分成[l, mid]和[mid + 1, r]时使用：
int bsearch_1(int l, int r)
{
    while (l < r)
    {
        int mid = l + r >> 1;
        if (check(mid)) r = mid;    # check()判断 mid 是否满足性质
        else l = mid + 1;
    }
    return l;
}

# 区间[l, r]被划分成[l, mid - 1]和[mid, r]时使用：
int bsearch_2(int l, int r)
{
    while (l < r)
    {
        int mid = l + r + 1 >> 1;
        if (check(mid)) l = mid;
        else r = mid - 1;
    }
    return l;
}




'''
整数集合上的二分
lower_bound 返回最小的满足 nums[i] >= target 的 i
如果数组为空，或者所有数都 < target, 则返回 len(nums)
要求 nums 是非递减的，即 nums[i] <= nums[i + 1]

有序数组中二分查找的四种类型
    1. 第一个大于等于x的下标: low_bound(x)
    2. 第一个大于x的下标: 可以转换为第一个大于等于 x+1 的下标, low_bound(x+1)
    3. 最后一个一个小于x的下标: 可以转换为第一个大于等于 x 的下标的左边位置, low_bound(x) - 1;
    4. 最后一个小于等于x的下标: 可以转换为第一个大于等于 x+1 的下标的左边位置, low_bound(x+1) - 1;
'''

# 闭区间写法
def lower_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1  # 闭区间 [left, right]
    while left <= right:  # 区间不为空
        # 循环不变量：
        # nums[left-1] < target
        # nums[right+1] >= target
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # 范围缩小到 [mid+1, right]
        else:
            right = mid - 1  # 范围缩小到 [left, mid-1]
    return left  # 或者 right+1


# 左闭右开区间写法
def lower_bound2(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)  # 左闭右开区间 [left, right)
    while left < right:  # 区间不为空
        # 循环不变量：
        # nums[left-1] < target
        # nums[right] >= target
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # 范围缩小到 [mid+1, right)
        else:
            right = mid  # 范围缩小到 [left, mid)
    return left  # 或者 right


# 开区间写法
def lower_bound3(nums: List[int], target: int) -> int:
    left, right = -1, len(nums)  # 开区间 (left, right)
    while left + 1 < right:  # 区间不为空
        mid = (left + right) // 2
        # 循环不变量：
        # nums[left] < target
        # nums[right] >= target
        if nums[mid] < target:
            left = mid  # 范围缩小到 (mid, right)
        else:
            right = mid  # 范围缩小到 (left, mid)
    return right  # 或者 left+1





'''
在实数域上二分较为简单, 确定好所需的精度eps, 以 l+eps < r 为循环条件, 每次
根据在mid上的判定选择 r=mid 或 l=mid 分支之一即可。一般需要保留 k 位小数时,
则取 eps = pow(10, -(k+2))
'''

while (l + eps < r) {
    double mid = (l + r) / 2;
    if (calc(mid)) {
        r = mid;
    } else {
        l = mid;
    }
}

for (int i = 0; i < times; i++) {
    double mid = (l + r) / 2;
    if (calc(mid)) {
        r = mid;
    } else {
        l = mid;
    }
}