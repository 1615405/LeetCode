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


bool is_blue(int x) {/* ... */}  # 红蓝染色法

# 区间[l, r]被划分成[l, mid]和[mid + 1, r]时使用：
int bsearch_1(int l, int r)
{
    while (l < r)
    {
        int mid = l + r >> 1;
        if (is_blue(mid)) r = mid;    # mid 属于蓝色, right = mid
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
        if (is_red(mid)) l = mid; # mid 属于红色, l = mid
        else r = mid - 1;
    }
    return l;
}





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