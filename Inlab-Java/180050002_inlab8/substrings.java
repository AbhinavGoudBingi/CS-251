import java.util.*; 
class substrings {
	public static List<String> sibn(String s, int size){
		List<String> ans = new ArrayList<String>((s.length() + size - 1) / size );
		for (int i=0; i< s.length(); i+=1){
			ans.add(s.substring(i, Math.min(s.length(), i + size)));
		}
		return ans;
	}
	public static void main(String[] args){
	String string = args[0];
	int size = Integer.parseInt(String.valueOf(args[1]));
	List<String> res = sibn(string, size);
	for (int i=0; i < res.size(); i++){
		if(res.get(i).length() == size)
			System.out.println(res.get(i));
	}
	}
}