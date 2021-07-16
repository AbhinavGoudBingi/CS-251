import java.util.*;
 	class search {
	public static void main(String[] args){
		Vector vec = new Vector();
		int n = Integer.parseInt(String.valueOf(args[0]));
		for (int i=0; i < n; i++){
			vec.add(Integer.parseInt(String.valueOf(args[i+1])));
		}
	int x = Integer.parseInt(String.valueOf(args[n+1]));
	if (vec.contains(x))
		System.out.println(1);
	else
		System.out.println(0);
}}
	