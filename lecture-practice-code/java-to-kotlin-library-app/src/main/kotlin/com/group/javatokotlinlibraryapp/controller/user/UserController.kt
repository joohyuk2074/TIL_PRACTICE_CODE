package com.group.javatokotlinlibraryapp.controller.user

import com.group.javatokotlinlibraryapp.dto.user.request.UserCreateRequest
import com.group.javatokotlinlibraryapp.dto.user.request.UserUpdateRequest
import com.group.javatokotlinlibraryapp.dto.user.response.UserResponse
import com.group.javatokotlinlibraryapp.service.user.UserService
import org.springframework.web.bind.annotation.*

@RestController
class UserController(
    private val userService: UserService,
) {

    @PostMapping("/user")
    fun saveUser(@RequestBody request: UserCreateRequest) {
        userService.saveUser(request)
    }

    @GetMapping("/user")
    fun getUsers(): List<UserResponse> {
        return userService.getUsers();
    }

    @PutMapping("/user")
    fun updateUserName(@RequestBody request: UserUpdateRequest) {
        userService.updateUserName(request)
    }

    @DeleteMapping("/user")
    fun deleteUser(@RequestParam name: String) {
        userService.deleteUser(name)
    }
}