class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        Set<Integer> visitedRooms = new HashSet<>();
        Stack<Integer> keyStack = new Stack<>();

        keyStack.push(0);

        while (!keyStack.isEmpty()) {
            int currentRoom = keyStack.pop();
            if (!visitedRooms.contains(currentRoom)) {
                visitedRooms.add(currentRoom);
                for (int key: rooms.get(currentRoom)) {
                    if (!visitedRooms.contains(key)){
                        keyStack.push(key);
                    }
                }
            }
        }

        return visitedRooms.size() == rooms.size();
    }
}
