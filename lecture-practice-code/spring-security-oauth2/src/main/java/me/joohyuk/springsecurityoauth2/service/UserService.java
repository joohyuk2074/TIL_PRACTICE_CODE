package me.joohyuk.springsecurityoauth2.service;

import lombok.RequiredArgsConstructor;
import me.joohyuk.springsecurityoauth2.model.ProviderUser;
import me.joohyuk.springsecurityoauth2.model.User;
import me.joohyuk.springsecurityoauth2.repository.UserRepository;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;

    public void register(String registrationId, ProviderUser providerUser) {
        User user = User.builder()
            .registrationId(registrationId)
            .id(providerUser.getId())
            .username(providerUser.getUsername())
            .password(providerUser.getPassword())
            .email(providerUser.getEmail())
            .authorities(providerUser.getAuthorities())
            .provider(providerUser.getProvider())
            .build();

        userRepository.register(user);
    }
}
