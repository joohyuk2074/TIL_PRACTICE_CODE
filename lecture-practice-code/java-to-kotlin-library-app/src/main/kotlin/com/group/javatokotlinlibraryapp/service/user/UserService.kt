package com.group.javatokotlinlibraryapp.service.user

import com.group.javatokotlinlibraryapp.domain.user.User
import com.group.javatokotlinlibraryapp.domain.user.UserRepository
import com.group.javatokotlinlibraryapp.dto.user.request.UserCreateRequest
import com.group.javatokotlinlibraryapp.dto.user.request.UserUpdateRequest
import com.group.javatokotlinlibraryapp.dto.user.response.UserResponse
import org.springframework.stereotype.Service
import org.springframework.transaction.annotation.Transactional

@Service
class UserService(
    private val userRepository: UserRepository,
) {

    @Transactional
    fun saveUser(request: UserCreateRequest) {
        val newUser = User(request.name, request.age)
        userRepository.save(newUser)
    }

    @Transactional(readOnly = true)
    fun getUsers(): List<UserResponse> {
        return userRepository.findAll()
            .map { user -> UserResponse(user) }
    }

    @Transactional
    fun updateUserName(request: UserUpdateRequest) {
        val user = userRepository.findById(request.id).orElseThrow(::IllegalArgumentException)
        user.updateName(request.name)
    }

    @Transactional
    fun deleteUser(name: String) {
        val user = userRepository.findByName(name).orElseThrow(::IllegalArgumentException)
        userRepository.delete(user)
    }
}