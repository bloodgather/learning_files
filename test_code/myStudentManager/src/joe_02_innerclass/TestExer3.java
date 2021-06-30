package joe_02_innerclass;

import org.junit.jupiter.api.DynamicTest;
import org.junit.jupiter.api.Test;

public class TestExer3 {
    @Test
    public static void main(String[] args) {
        Father f = new Father(){
            public void method() {
                System.out.println("hello");
            }
        };
        f.method();
    }
}

abstract class Father{
    public abstract void method();
}