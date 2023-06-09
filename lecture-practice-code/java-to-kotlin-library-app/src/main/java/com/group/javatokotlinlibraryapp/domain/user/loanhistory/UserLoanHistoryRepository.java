package com.group.javatokotlinlibraryapp.domain.user.loanhistory;

import org.springframework.data.jpa.repository.JpaRepository;

public interface UserLoanHistoryRepository extends JpaRepository<UserLoanHistory, Long> {

    UserLoanHistory findByBookNameAndIsReturn(String bookName, boolean isReturn);

}
