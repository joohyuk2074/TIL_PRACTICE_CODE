package com.group.javatokotlinlibraryapp.domain.user.loanhistory

import com.group.javatokotlinlibraryapp.domain.user.User
import javax.persistence.*

@Entity
class UserLoanHistory(
    @ManyToOne
    val user: User,

    val bookName: String,

    var isReturn: Boolean,

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    val id: Long? = null,
) {
    fun doReturn() {
        this.isReturn = true
    }
}