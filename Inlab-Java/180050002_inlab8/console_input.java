import java.lang.*; 
import java.io.*; 
import java.util.*; 
class console_input{

	public static void main(String[] args){
		System.out.print("Enter first name: ");
		String fname = System.console().readLine();
		String fname1=fname.toLowerCase();
		StringBuilder fname2 = new StringBuilder();
		fname2.append(fname1); 
  
        // reverse StringBuilder input1 
        fname2 = fname2.reverse();
        String fname3=fname2.toString();  
		System.out.print("Enter last name: ");
		String lname = System.console().readLine();
		String lname1=lname.toLowerCase();
		StringBuilder lname2 = new StringBuilder();
		lname2.append(lname1); 
  
        // reverse StringBuilder input1 
        lname2 = lname2.reverse();
        String lname3=lname2.toString();
		if(fname1.equals(fname3)){System.out.println(fname+" "+"is a palindrome");}
		//else{System.out.println(fname+" "+"is a palindrome");}
		if(lname1.equals(lname3)){System.out.println(lname+" "+"is a palindrome");}
		//else{System.out.println(lname+" "+"is a palindrome");}
	}
}