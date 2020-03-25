import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
 
public class Main {
    static int N, K, Min, sum, partsum;
    static int [] peo;
    static int [][] link;
    static boolean [] check;
    static int [] temp;
    static boolean [] visited;

    
 
    public static void main(String[] args) throws NumberFormatException, IOException {
        // TODO Auto-generated method stub
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        peo = new int [N+1];
        link = new int [N+1][N+1];
        String s = br.readLine();
        StringTokenizer st = new StringTokenizer(s);
 
        for(int i = 1; i<N+1; i++) {  
            peo[i] = Integer.parseInt(st.nextToken());
        }
        
        
        for(int x = 1; x<N+1; x++) { 
            s = br.readLine();
            st = new StringTokenizer(s);
            int each = Integer.parseInt(st.nextToken());
            for(int y = 0; y<each; y++) {
                int spot = Integer.parseInt(st.nextToken());
                link[x][spot] = 1;  
            }
        }
                
        Min = Integer.MAX_VALUE;
        
        for(int i = 0; i<(N/2)+1; i++) { 
            K = i;
            check = new boolean[N+1];
            pick(1,0);
        }
        
        if(Min == Integer.MAX_VALUE) {  
            System.out.println(-1);
        }
        else {
            System.out.println(Min);
        }
    }
    
    public static void pick(int start, int cnt) {
        if(cnt == K) {
            sum = Integer.MAX_VALUE;
            temp = new int[N+1];
            for(int i = 1; i<N+1; i++) {
                if(check[i] == true) {
                    temp[i] = 1;
                }
                else {
                    temp[i] = 0;
                }
            }
            confirm();
            Min = Math.min(Min, sum);
            return;
        }
        for(int i = start; i<N+1; i++) {
            check[i]=true;
            pick(i+1,cnt+1);
            check[i]=false;
        }
    }
    
    public static void confirm() {
        visited = new boolean[N+1];
        int people1 = 0;
        int people2 = 0;
        for(int i = 1; i<N+1; i++) {
            if(temp[i] == 1 && !visited[i]) {  
                partsum = 0;
                gary(i);
                people1 = partsum;
                break;
            }
        }
        
        for(int i = 1; i<N+1; i++) {
            if(temp[i] == 0 && !visited[i]) {  
                partsum = 0;
                gary(i);
                people2 = partsum;
                break;
            }
        }
        
        for(int i = 1; i<N+1; i++) {
            if(!visited[i]) {
                return;
            }
        }
        sum = Math.abs(people2-people1);
    }
    
    public static void gary(int x) {
        visited[x] = true;
        partsum = partsum + peo[x];
        for(int i = 1; i<N+1; i++) {
            if(!visited[i] && temp[i] == temp[x] && link[i][x] == 1) {
                gary(i);
            }
        }
    }
 
}