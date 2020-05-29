import java.util.*;

class PlatformAllocation{

	public static void main(String[] args) {


        Scanner sc =new Scanner(System.in);
		int n= sc.nextInt();
		Vector<String> trainName = new Vector<String>(), arrivalTime = new Vector<String>(), departureTime = new Vector<String>(), timeTakenToDepart = new Vector<String>();
		Vector<Integer> trainNumber = new Vector<Integer>();
		for(int i=0;i<n;i++)
		{
			trainName.add(sc.next());
			trainNumber.add(sc.nextInt());
			arrivalTime.add(sc.next());
			departureTime.add(sc.next());
			timeTakenToDepart.add(sc.next());
		}
		Solution so = new Solution();
		Pair p=so.platformAllocation(trainName,trainNumber,arrivalTime,departureTime,timeTakenToDepart);
		System.out.println(p.first);
		for(int i=0;i<n;i++)
		{
			System.out.println(trainName.get(i)+" "+trainNumber.get(i)+" "+(p.second).get(i));
		}
	}
}
