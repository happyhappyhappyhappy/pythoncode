using namespace std;

struct Edge {
    int source, destination, weight;
};

void BellmanFord(vector<Edge>& edges, int numVertices, int source) {
    vector<int> distance(numVertices, INT_MAX);
    distance[source] = 0;

    // ベルマンフォードアルゴリズムの反復 -> N-1回しか行わない
    for (int i = 1; i < numVertices; i++) {
        for (const Edge& edge : edges) {
            int u = edge.source;
            int v = edge.destination;
            int w = edge.weight;

            if (distance[u] != INT_MAX && distance[u] + w < distance[v]) {
                distance[v] = distance[u] + w;
            }
        }
    }

    // 負の重みサイクルのチェック->さらに改善の余地があると分かった時点で負の経路があるとみて終わる
    for (const Edge& edge : edges) {
        int u = edge.source;
        int v = edge.destination;
        int w = edge.weight;

        if (distance[u] != INT_MAX && distance[u] + w < distance[v]) {
            cout << "負の重みサイクルが存在します" << endl;
            return;
        }
    }

    // 最短距離を出力
    for (int i = 0; i < numVertices; i++) {
        cout << "頂点 " << i << " への最短距離: " << distance[i] << endl;
    }
}

int main() {
    int numVertices = 5;
    vector<Edge> edges = {
        {0, 1, -1},
        {0, 2, 4},
        {1, 2, 3},
        {1, 3, 2},
        {1, 4, 2},
        {3, 2, 5},
        {3, 1, 1},
        {4, 3, -3}
    };
    int source = 0;

    BellmanFord(edges, numVertices, source);

    return 0;
}
