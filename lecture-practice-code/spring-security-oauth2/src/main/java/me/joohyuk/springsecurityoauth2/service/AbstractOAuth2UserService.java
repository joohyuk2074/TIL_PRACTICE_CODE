package me.joohyuk.springsecurityoauth2.service;

import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import me.joohyuk.springsecurityoauth2.model.*;
import me.joohyuk.springsecurityoauth2.repository.UserRepository;
import org.springframework.security.oauth2.client.registration.ClientRegistration;
import org.springframework.security.oauth2.client.userinfo.OAuth2UserRequest;
import org.springframework.security.oauth2.core.user.OAuth2User;

@Slf4j
@Getter
@RequiredArgsConstructor
public abstract class AbstractOAuth2UserService {

    private final UserService userService;

    private final UserRepository userRepository;

    protected void register(ProviderUser providerUser, OAuth2UserRequest userRequest) {
        User user = userRepository.findByUsername(providerUser.getUsername());

        if (user == null) {
            ClientRegistration clientRegistration = userRequest.getClientRegistration();
            userService.register(clientRegistration.getRegistrationId(), providerUser);
        } else {
            log.info("user: {}", user);
        }
    }

    protected ProviderUser providerUser(ClientRegistration clientRegistration, OAuth2User oAuth2User) {
        String registrationId = clientRegistration.getRegistrationId();
        return switch (registrationId) {
            case "keycloak" -> new KeycloakUser(oAuth2User, clientRegistration);
            case "google" -> new GoogleUser(oAuth2User, clientRegistration);
            case "naver" -> new NaverUser(oAuth2User, clientRegistration);
            default -> null;
        };

    }
}
