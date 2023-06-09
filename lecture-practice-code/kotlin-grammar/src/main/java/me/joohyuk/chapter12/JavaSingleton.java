package me.joohyuk.chapter12;

public class JavaSingleton {

  private static final JavaSingleton INSTANCE = new JavaSingleton();

  private JavaSingleton() { }

  public static JavaSingleton getInstance() {
    return INSTANCE;
  }

}
