import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;


public class Main {

    static int N, M;
    static BufferedReader br;
    static BufferedWriter bw;
    static StringTokenizer st;

    static int[] person;
    static int[] task;
    static boolean[][] connect;

    public static void main(String[] args) throws Exception {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        connect = new boolean[N + 1][M + 1];
        person = new int[N + 1];
        task = new int[M + 1];

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            int tmp = Integer.parseInt(st.nextToken());
            for (int j = 0; j < tmp; j++) {
                int tmp2 = Integer.parseInt(st.nextToken());
                connect[i][tmp2] = true;
            }
        }
        int result = go();
        bw.write("" + result);
        bw.flush();
        br.close();
        bw.close();
    }

    public static int go() {
        int taskNum = 0;
        boolean[] doList;
        for(int a=1;a<=N;a++) {
            doList=new boolean[N+1];
            if(dfs(a,doList)) taskNum++;
        }
        return taskNum;
    }

    public static boolean dfs(int a, boolean[] list) {
        if (list[a]) return false;
        list[a] = true;
        for (int b = 1; b <= M; b++) {
            if (connect[a][b]) {
                if (task[b] == 0 || dfs(task[b], list)) {
                    person[a] = b;
                    task[b] = a;
                    return true;
                }
            }
        }
        return false;
    }

}