package com.group.javatokotlinlibraryapp.service.book

import com.group.javatokotlinlibraryapp.domain.book.Book
import com.group.javatokotlinlibraryapp.domain.book.BookRepository
import com.group.javatokotlinlibraryapp.domain.user.UserRepository
import com.group.javatokotlinlibraryapp.domain.user.loanhistory.UserLoanHistoryRepository
import com.group.javatokotlinlibraryapp.domain.user.loanhistory.UserLoanStatus
import com.group.javatokotlinlibraryapp.dto.book.request.BookLoanRequest
import com.group.javatokotlinlibraryapp.dto.book.request.BookRequest
import com.group.javatokotlinlibraryapp.dto.book.request.BookReturnRequest
import com.group.javatokotlinlibraryapp.util.fail
import org.springframework.stereotype.Service
import org.springframework.transaction.annotation.Transactional

@Service
class BookService(
    private val bookRepository: BookRepository,
    private val userRepository: UserRepository,
    private val userLoanHistoryRepository: UserLoanHistoryRepository,
) {

    @Transactional
    fun saveBook(request: BookRequest) {
        val book = Book(request.name, request.type)
        bookRepository.save(book)
    }

    @Transactional
    fun loanBook(request: BookLoanRequest) {
        val book = bookRepository.findByName(request.bookName) ?: fail()
        if (userLoanHistoryRepository.findByBookNameAndStatus(request.bookName, UserLoanStatus.LOANED) != null) {
            throw IllegalArgumentException("진작 대출되어 있는 책입니다")
        }

        val user = userRepository.findByName(request.userName) ?: fail()
        user.loanBook(book)
    }

    @Transactional
    fun returnBook(request: BookReturnRequest) {
        val user = userRepository.findByName(request.userName) ?: fail()
        user.returnBook(request.bookName)
    }
}