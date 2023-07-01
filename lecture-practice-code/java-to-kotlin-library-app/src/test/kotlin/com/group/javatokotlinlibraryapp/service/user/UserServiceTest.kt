package com.group.javatokotlinlibraryapp.service.user

import com.group.javatokotlinlibraryapp.domain.user.UserRepository
import com.group.javatokotlinlibraryapp.dto.user.request.UserCreateRequest
import org.assertj.core.api.AssertionsForInterfaceTypes.assertThat
import org.junit.jupiter.api.Test
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.context.SpringBootTest

@SpringBootTest
class UserServiceTest @Autowired constructor(
    private val userRepository: UserRepository,
    private val userService: UserService
) {

    @Test
    fun saveUserTest() {
        // given
        val request = UserCreateRequest("김주혁", null)

        // when
        userService.saveUser(request)

        // then
        val results = userRepository.findAll();
        assertThat(results).hasSize(1)
        assertThat(results[0].name).isEqualTo("김주혁")
        assertThat(results[0].age).isNull()
    }
}