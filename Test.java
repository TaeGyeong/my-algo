import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
 
public class Test {    
        static BufferedReader br;
        static BufferedWriter bw;
        static StringTokenizer st;
        static int n;
        static int m;
        static boolean[][] connect;
        static int[] matchA;
        static int[] matchB;
        
    public static void main(String[] args) throws IOException {
        br=new BufferedReader(new InputStreamReader(System.in));
        bw=new BufferedWriter(new OutputStreamWriter(System.out));
        String str=br.readLine();
        st=new StringTokenizer(str);
        n=Integer.parseInt(st.nextToken());
        m=Integer.parseInt(st.nextToken());
        connect=new boolean[n+1][m+1];
        matchA=new int[n+1];
        matchB=new int[m+1];
        for(int i=1;i<=n;i++) {
            str=br.readLine();
            st=new StringTokenizer(str);
            int numB=Integer.parseInt(st.nextToken());
            for(int j=0;j<numB;j++) {
                int atob=Integer.parseInt(st.nextToken());
                connect[i][atob]=true;
            }
        }
        int result=go();
        bw.write(""+result);
        bw.flush();
        br.close();
        bw.close();
    }
    public static int go() {
        int so=0;
        boolean[] visit;
        for(int a=1;a<=n;a++) {
            visit=new boolean[n+1];
            if(dfs(a,visit)) so++;
        }
        
        return so;
    }
    public static boolean dfs(int a, boolean[] visit) {
        if(visit[a]) return false;
        visit[a]=true;
        for(int b=1;b<=m;b++) {
            if(connect[a][b]) {
                if(matchB[b]==0||dfs(matchB[b],visit)) {
                    matchA[a]=b;
                    matchB[b]=a;
                    return true;
                }
            }
        }
        return false;
    }
}
