import java.io.*;
import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        long[] data = new long[n];
        for(int i = 0; i < n; i++) {
            data[i] = Long.parseLong(bf.readLine());
        }
        long[] tree = new long[4*n];
        sum(data, tree, 1, 0, n-1);
        m += k;
        while(m-- > 0) {
            st = new StringTokenizer(bf.readLine());
            int a = Integer.parseInt(st.nextToken());
            if(a == 1) {
                int b = Integer.parseInt(st.nextToken());
                long c = Long.parseLong(st.nextToken());
                b -= 1;
                long diff = c - data[b];
                data[b] = c;
                update(tree, 1, 0, n-1, b, diff);
            }
            else if(a == 2) {
                int b = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                System.out.println(changedSum(tree, 1, 0, n-1, b-1, c-1));
            }
        }
    }
    private static long sum(long[] input, long[] tree, int node, int start, int end) {
        if(start == end) {
            return tree[node] = input[start];
        }
        int mid = (start + end) / 2;
        return tree[node] = sum(input, tree, node * 2, start, mid) + sum(input, tree, node * 2 + 1, mid + 1, end);
    }
    private static void update(long[] tree, int node, int start, int end, int index, long diff) {
        if(index < start || index > end) {
            return;
        }
        tree[node] += diff;
        if(start != end) {
            int mid = (start + end) / 2;
            update(tree, node * 2, start, mid, index, diff);
            update(tree, node * 2 + 1, mid + 1, end, index, diff);
        }
    }
    private static long changedSum(long[] tree, int node, int start, int end, int left, int right) {
        if(left > end || right < start) {
            return 0;
        }
        if(left <= start && end <= right) {
            return tree[node];
        }
        int mid = (start + end) / 2;
        return changedSum(tree, node * 2, start, mid, left, right) + changedSum(tree, node * 2 + 1, mid + 1, end, left, right);
    }
}