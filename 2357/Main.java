import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static long[] arr;
    static StringBuilder sb;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new long[N + 1];
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i] = Long.parseLong(st.nextToken());
        }
        sb = new StringBuilder();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            find(start, end);
        }

        System.out.println(sb);
    }

    static void find(int s, int e) {
        long maxVal = Long.MIN_VALUE;
        long minVal = Long.MAX_VALUE;
        for (int i = s; i <= e; i++) {
            maxVal = Math.max(arr[i], maxVal);
            minVal = Math.min(arr[i], minVal);
        }
        sb.append(minVal + " " + maxVal + "\n");
    }
}