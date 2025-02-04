import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int minReorder(int n, int[][] connections) {

        Map<Integer, List<int[]>> graph = new HashMap<>();
        for (int [] edge : connections) {
            int A = edge[0];
            int B = edge[1];
            graph.putIfAbsent(A, new ArrayList<>());
            graph.putIfAbsent(B, new ArrayList<>());
            // original direction
            graph.get(A).add(new int[]{B, 1}); // A -> B
            // reverse direction
            graph.get(B).add(new int[]{A, 0}); // B -> A

        }
        return dfs(0, -1, graph);
    }
    
    private int dfs(int node, int parent, Map<Integer, List<int[]>> graph) {
        int count = 0;
        for (int[] neighbor : graph.get(node)) {
            int nextNode = neighbor[0];
            int direction = neighbor[1];
            if (nextNode == parent) continue;
            count += direction;
            count += dfs(nextNode, node, graph);
        }
        return count;
    }


}