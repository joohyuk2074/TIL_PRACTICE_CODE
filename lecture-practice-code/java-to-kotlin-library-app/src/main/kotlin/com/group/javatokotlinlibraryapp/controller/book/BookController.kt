package com.group.javatokotlinlibraryapp.controller.book

import com.group.javatokotlinlibraryapp.dto.book.request.BookLoanRequest
import com.group.javatokotlinlibraryapp.dto.book.request.BookRequest
import com.group.javatokotlinlibraryapp.dto.book.request.BookReturnRequest
import com.group.javatokotlinlibraryapp.service.book.BookService
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.PutMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RestController

@RestController
class BookController(
    private val bookService: BookService,
) {

    @PostMapping("/book")
    fun saveBook(@RequestBody request: BookRequest) {
        bookService.saveBook(request)
    }

    @PostMapping("/book/loan")
    fun loanBook(@RequestBody request: BookLoanRequest) {
        bookService.loanBook(request)
    }

    @PutMapping("/book/return")
    fun returnBook(@RequestBody request: BookReturnRequest) {
        bookService.returnBook(request)
    }
}