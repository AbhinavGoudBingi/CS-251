import java.time.LocalTime;
import java.util.Date;

class Clock implements Runnable{
    private String threadId;
    private Thread thr;
    Clock(String d){
      threadId = d;//time for which thread sleeps
    }
    public void run(){
       
        try{
            while(true){
                Date dt=new Date();
                String[] now=dt.toString().split("\\s+");
                System.out.println(now[3]);
                Thread.sleep(1000);
            }
        }
        catch(InterruptedException e){}

    }

public void start(){
    if (thr==null){
        thr = new Thread(this,threadId);
        thr.start();
    }
}
}

class clock{
    public static void main(String[] args){
     
       Clock ti = new Clock("clock");
       ti.start();
    }
}