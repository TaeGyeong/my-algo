import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {
    static int N, M , start;
	static List[] list;
    static boolean[] visit;
    
	public static void bfs(int num) {
		Queue<Integer> queue = new LinkedList<>();
		
		queue.add(num);
		visit[num] = true;
		System.out.print(num + " ");
		while(!queue.isEmpty()) {
			int temp = queue.poll();
			for(int i = 0; i < list[temp].size(); i++) {
				if(!visit[(int) list[temp].get(i)]) {
					visit[(int) list[temp].get(i)] = true;
					System.out.print(list[temp].get(i) + " ");
					queue.add((Integer) list[temp].get(i));
				}
			}
		}
	}
	public static void dfs(int num) {
		
		visit[num] = true;
		System.out.print(num + " ");
		for(int i = 0; i < list[num].size(); i++) {
			if(!visit[(int) list[num].get(i)]) {
				dfs((int) list[num].get(i));
			}
		}
	}
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer str = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(str.nextToken()); 
		M = Integer.parseInt(str.nextToken()); 
	
		start = Integer.parseInt(str.nextToken()); 
		list = new ArrayList[N + 1];
		
		for(int i = 1; i <= N; i++) {
			list[i] = new ArrayList<>();
		}
		visit = new boolean[N + 1]; 
		
		for(int i = 0; i < M; i++) {
			
			StringTokenizer temp = new StringTokenizer(br.readLine());
			
			int x = Integer.parseInt(temp.nextToken());
			int y = Integer.parseInt(temp.nextToken());
			
			list[x].add(y);
			list[y].add(x);
		}
		for(int i = 1; i <= N; i++) {
			Collections.sort(list[i]);
		}
		dfs(start);
		System.out.println();
		visit = new boolean[N + 1];
		bfs(start);
	}
}