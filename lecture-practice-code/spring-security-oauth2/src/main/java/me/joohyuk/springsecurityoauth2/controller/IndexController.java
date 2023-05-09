package me.joohyuk.springsecurityoauth2.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class IndexController {
//
//    private final ClientRegistrationRepository clientRegistrationRepository;
//
//    public IndexController(ClientRegistrationRepository clientRegistrationRepository) {
//        this.clientRegistrationRepository = clientRegistrationRepository;
//    }

    @GetMapping("/")
    public String index() {
        return "index";
    }
//
//    @GetMapping("/user")
//    public OAuth2User user(String accessToken) {
//        ClientRegistration clientRegistration = clientRegistrationRepository.findByRegistrationId("keycloak");
//        OAuth2AccessToken oAuth2AccessToken = new OAuth2AccessToken(OAuth2AccessToken.TokenType.BEARER, accessToken, Instant.now(), Instant.MAX);
//
//        OAuth2UserRequest oAuth2UserRequest = new OAuth2UserRequest(clientRegistration, oAuth2AccessToken);
//        DefaultOAuth2UserService defaultOAuth2UserService = new DefaultOAuth2UserService();
//
//        return defaultOAuth2UserService.loadUser(oAuth2UserRequest);
//    }
//
//    @GetMapping("/oidc")
//    public OAuth2User oidc(String accessToken, String idToken) {
//        ClientRegistration clientRegistration = clientRegistrationRepository.findByRegistrationId("keycloak");
//        OAuth2AccessToken oAuth2AccessToken = new OAuth2AccessToken(OAuth2AccessToken.TokenType.BEARER, accessToken, Instant.now(), Instant.MAX);
//
//        Map<String, Object> idTokenClaims = new HashMap<>();
//        idTokenClaims.put(IdTokenClaimNames.ISS, "http://localhost:8080/realms/oauth2");
//        idTokenClaims.put(IdTokenClaimNames.SUB, "OIDC0");
//        idTokenClaims.put("preferred_username", "user");
//
//        OidcIdToken oidcIdToken = new OidcIdToken(idToken, Instant.now(), Instant.MAX, idTokenClaims);
//
//        OidcUserRequest oidcUserService = new OidcUserRequest(clientRegistration, oAuth2AccessToken, oidcIdToken);
//        OidcUserService defaultOAuth2UserService = new OidcUserService();
//
//        return defaultOAuth2UserService.loadUser(oidcUserService);
//    }
}
