import java.time.LocalDate;
import java.util.ArrayList;
public class Task {
    private int number;
    private int counter=0;
    public ArrayList<String> field_to_down=new ArrayList<>();
    public ArrayList<String> sub_to_down=new ArrayList<>();
    public ArrayList<String> date_to_down=new ArrayList<>();
    boolean [] do_check=new boolean[number];
    boolean [] time_check=new boolean [number];
    Task(int number)
    {
        this.number=number;
    }
    void get_number(int number) {this.number=number;}
    void add_task(String field,String sub ,String date)
    {
        counter++;
        field_to_down.add(field);
        sub_to_down.add(sub);
        date_to_down.add(date);
    }
    boolean check_deadline(int count)
    {
        LocalDate task_time=LocalDate.parse(date_to_down.get(count));
        LocalDate now=LocalDate.now();
        if(task_time.isBefore(now))
        {
            time_check[count]=false;
            return false;
        }
        return true;
    }
    void do_check(String s,int num)
    {
        do_check[num]= s.equals("accepted");
    }
    String answer(String a,int number_of_task)
    {
        if(check_deadline(number_of_task))
        {
            return "failed to send\ntime is over...";
        }
        String result=field_to_down.get(number_of_task)+" "+sub_to_down.get(number_of_task)+"answer is\n"+a; // class pedar
        return result;
    }
    void printTasks()
    {
        for (int i=0;i<field_to_down.size();i++)
        {
            if (!check_deadline(i))
            {
                System.out.println(i+1+')');
                System.out.println(field_to_down.get(i));
                System.out.println(sub_to_down.get(i));
                System.out.println(date_to_down.get(i));
                System.out.println("----------------------------------------------");
            }
        }
    }
}