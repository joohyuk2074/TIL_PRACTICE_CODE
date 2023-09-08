package java.me.joohyuk.graph;

import java.util.HashMap;
import java.util.Map;

public class DijikstraAlgorithm {

    public static Map<String, Integer> run(
        final HashMap<String, Node> nodes,
        final String from,  // 시작 노드명
        final HashMap<String, String> prevs
    ) {

        Map<String, Integer> minDists = new HashMap<>();
//
//        // distance를 INF값으로 초기화
//        final int INF = Integer.MAX_VALUE;
//        for (var entry : nodes.entrySet()) {
//            String name = entry.getKey();
//            minDists.put(name, INF);
//        }
//
//        minDists.put(from, 0);  // 시작노드의 거리를 0으로 설정
//        prevs.put(from, null);
//
//        Queue<Candidate> open = new PriorityQueue<>();
//
//        Node s = nodes.get(from);
//        Candidate candidate = new Candidate(s, 0);
//
//        open.add(candidate);
//
//        while (!open.isEmpty()) {
//            candidate = open.poll();
//
//            Node n = candidate.getNode();
//            String nodeName = n.getName();
//
//            int minDist = minDists.get(nodeName);
//            int dist = candidate.getDistance();
//
//            if (minDist < dist) {
//                continue;
//            }
//
//            Map<Node, Integer> roads = n.getRoads();
//            for (var e : roads.entrySet()) {
//                Node next = e.getKey();
//
//                int weight = e.getValue();
//                int newDist = minDist + weight;
//
//                String nextName = next.getName();
//                int nextMinDist = minDists.get(nextName);
//
//                if (newDist >= nextMinDist) {
//                    continue;
//                }
//
//                minDists.put(nextName, newDist);
//            }
//        }
        return minDists;
    }

    public static final class Node {
        private final String name;
        private final HashMap<Node, Integer> roads = new HashMap<>();

        public Node(final String name) {
            this.name = name;
        }

        public Map<Node, Integer> getRoads() {
            return this.roads;
        }

        public void addRoad(final Node to, final int dist) {
            this.roads.put(to, dist);
        }

        public int getDistance(final Node to) {
            return this.roads.get(to);
        }

    }

    public static class Candidate {

        private Node node;

        private int distance;

        public Candidate(Node node, int distance) {
            this.node = node;
            this.distance = distance;
        }

        public Node getNode() {
            return node;
        }

        public int getDistance() {
            return distance;
        }
    }
}
