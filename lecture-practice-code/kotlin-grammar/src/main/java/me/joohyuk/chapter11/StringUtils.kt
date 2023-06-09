package me.joohyuk.chapter11

fun isDirectoryPath(path: String): Boolean {
    return path.endsWith("/")
}