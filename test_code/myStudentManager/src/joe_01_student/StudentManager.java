package joe_01_student;

import java.util.ArrayList;
import java.util.Scanner;

public class StudentManager {
    public static void main(String[] args) {
        ArrayList<Student> array = new ArrayList<Student>();
        while (true) {
            System.out.println("-----欢迎来到学生管理系统------");
            System.out.println("1 添加学生");
            System.out.println("2 删除学生");
            System.out.println("3 修改学生");
            System.out.println("4 查看所有学生");
            System.out.println("5 退出");
            System.out.println("请输入你的选择：");

            Scanner sc = new Scanner(System.in);
            String line = sc.nextLine();

            switch (line) {
                case "1" -> addStudent(array);
                case "2" -> deleteStudent(array);
                case "3" -> updateStudent(array);
                case "4" -> findAllStudent(array);
                case "5" -> {
                    System.out.println("谢谢使用");
                    System.exit(0);
                }
            }
        }
    }

    public static void addStudent(ArrayList<Student> array) {
        Scanner sc = new Scanner(System.in);
        String sid;
        while (true) {
            System.out.println("请输入学生学号：");
            sid = sc.nextLine();

            boolean flag = isUsed(array, sid);
            if (flag) {
                System.out.println("你输入的学号已经被使用，请重新输入");
            }else {
                break;
            }
        }
        System.out.println("请输入学生姓名：");
        String name = sc.nextLine();
        System.out.println("请输入学生年龄：");
        String age = sc.nextLine();
        System.out.println("请输入学生居住地：");
        String address = sc.nextLine();




        Student s = new Student();
        s.setSid(sid);
        s.setName(name);
        s.setAge(age);
        s.setAddress(address);

        array.add(s);
        System.out.println("添加成功");

    }

    public static void findAllStudent(ArrayList<Student> array) {
        if (array.size() == 0) {
            System.out.println("无信息");
            return;
        }
        System.out.println("学号\t\t\t姓名\t\t年龄\t\t居住地");
        for (int i = 0; i < array.size(); i++) {
            Student s = new Student();
            System.out.println((s.getSid() + "\t" +
                    s.getName() + "\t" + s.getAge() + "岁\t\t" + s.getAddress()));
        }
    }

    public static void deleteStudent(ArrayList<Student> array) {
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入需要删除学生的学号");
        String sid = sc.nextLine();

        for (int i = 0; i < array.size(); i++) {
            Student s = array.get(i);
            if (s.getSid().equals(sid)) {
                array.remove(i);
                break;
            }
        }
        System.out.println("删除成功");
    }

    public static void updateStudent(ArrayList<Student> array) {
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入要修改的学生编号");
        String sid = sc.nextLine();

        System.out.println("请输入学生新姓名");
        String name = sc.nextLine();
        System.out.println("请输入学生新年龄");
        String age = sc.nextLine();
        System.out.println("请输入学生地址");
        String address = sc.nextLine();

        Student s = new Student();
        s.setName(name);
        s.setAge(age);
        s.setAddress(address);

        for (int i = 0; i < array.size(); i++) {
            Student student = array.get(i);
            if (student.getSid().equals(sid)) {
//              数组列表需要创建新对象替换
                array.set(i, s);
                break;
            }
        }
        System.out.println("修改成功");
    }

    public static boolean isUsed(ArrayList<Student> array, String sid) {
        boolean flag = false;
        for (Student s : array) {
            if (s.getSid().equals(sid)) {
                flag = true;
                break;
            }
        }
        return flag;
    }
}


