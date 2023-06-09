package me.joohyuk.chapter11;

public abstract class StringUtils {

  private StringUtils() {}

  public boolean isDirectoryPath(String path) {
    return path.endsWith("/");
  }

}

