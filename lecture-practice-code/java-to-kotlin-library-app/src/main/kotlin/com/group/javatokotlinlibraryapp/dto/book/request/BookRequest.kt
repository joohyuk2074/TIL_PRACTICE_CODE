package com.group.javatokotlinlibraryapp.dto.book.request

import com.group.javatokotlinlibraryapp.domain.book.BookType

data class BookRequest(
    val name: String,
    val type: BookType
)
