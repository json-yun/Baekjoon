import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main
{
    public static int hi() {
        return 6;
    }
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] NS = br.readLine().split(" ");
		int N = Integer.parseInt(NS[0]);
		int S = Integer.parseInt(NS[1]);
		
		int[] A = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		
		int a = 0, b = 0;
		int total = A[0];
		int shortest = N+1;
		
		while (b < N) {
		    if (total >= S) {
		        if (b-a+1 < shortest) {
		            shortest = b-a+1;
		        }
		        total -= A[a];
		        a += 1;
		    } else if (b < N-1) {
		        b += 1;
		        total += A[b];
		    } else {
		        break;
		    }
		}
		
		if (shortest < N+1) {
    		System.out.println(shortest);
		} else {
		    System.out.println(0);
		}
	}
}
