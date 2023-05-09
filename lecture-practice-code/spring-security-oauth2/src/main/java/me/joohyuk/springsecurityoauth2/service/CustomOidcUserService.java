package me.joohyuk.springsecurityoauth2.service;

import me.joohyuk.springsecurityoauth2.model.ProviderUser;
import me.joohyuk.springsecurityoauth2.repository.UserRepository;
import org.springframework.security.oauth2.client.oidc.userinfo.OidcUserRequest;
import org.springframework.security.oauth2.client.oidc.userinfo.OidcUserService;
import org.springframework.security.oauth2.client.registration.ClientRegistration;
import org.springframework.security.oauth2.client.userinfo.OAuth2UserService;
import org.springframework.security.oauth2.core.OAuth2AuthenticationException;
import org.springframework.security.oauth2.core.oidc.user.OidcUser;
import org.springframework.security.oauth2.core.user.OAuth2User;
import org.springframework.stereotype.Service;

@Service
public class CustomOidcUserService extends AbstractOAuth2UserService implements OAuth2UserService<OidcUserRequest, OidcUser> {

    public CustomOidcUserService(UserService userService, UserRepository userRepository) {
        super(userService, userRepository);
    }

    @Override
    public OidcUser loadUser(OidcUserRequest userRequest) throws OAuth2AuthenticationException {
        ClientRegistration clientRegistration = userRequest.getClientRegistration();
        OAuth2UserService<OidcUserRequest, OidcUser> oidcUserService = new OidcUserService();
        OAuth2User oAuth2User = oidcUserService.loadUser(userRequest);

        ProviderUser providerUser = super.providerUser(clientRegistration, oAuth2User);

        // 회원가입
        super.register(providerUser, userRequest);

        return null;
    }
}
