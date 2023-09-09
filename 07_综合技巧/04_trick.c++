const int MAX_EDGES = 100010;
vector<int> ver[MAX_EDGES], edge[MAX_EDGES];

// 保存从 x 到 y 权值为 z 的有向边
void add(int x, int y, int z) {
    ver[x].push_back(y);
    edge[x].push_back(z);
}

// 遍历从 x 出发的所有边
for (int i = 0; i < ver[x].size(); i++) {
    int y = ver[x][i], z = edge[x][i];
    // 有向边 (x, y, z)
}