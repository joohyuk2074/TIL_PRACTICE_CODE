package com.group.javatokotlinlibraryapp.dto.book.request;

public class BookRequest {

    private String name;

    public BookRequest(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

}
