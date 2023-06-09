package me.joohyuk.springsecurityoauth2.controller;

import org.springframework.security.core.Authentication;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.oauth2.client.authentication.OAuth2AuthenticationToken;
import org.springframework.security.oauth2.core.oidc.user.OidcUser;
import org.springframework.security.oauth2.core.user.OAuth2User;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.Map;

@Controller
public class IndexController {

    @GetMapping("/")
    public String index(Model model, Authentication authentication, @AuthenticationPrincipal OAuth2User oAuth2User) {
        OAuth2AuthenticationToken oAuth2AuthenticationToken = (OAuth2AuthenticationToken) authentication;
        if (oAuth2AuthenticationToken != null) {
            Map<String, Object> attributes = oAuth2User.getAttributes();
            String userName = (String) attributes.get("name");

            if (oAuth2AuthenticationToken.getAuthorizedClientRegistrationId().equals("naver")) {
                Map<String, Object> response = (Map<String, Object>) attributes.get("response");
                userName = (String) response.get("name");
            }

            model.addAttribute("user", userName);
        }
        return "index";
    }

    @GetMapping("/user")
    public OAuth2User user(Authentication authentication) {
        OAuth2AuthenticationToken authentication2 = (OAuth2AuthenticationToken) authentication;
        return authentication2.getPrincipal();
    }

    @GetMapping("/oauth2User")
    public OAuth2User user(@AuthenticationPrincipal OAuth2User oAuth2User) {
        System.out.println("oAuth2User = " + oAuth2User);
        return oAuth2User;
    }

    @GetMapping("/oidcUser")
    public OidcUser user(@AuthenticationPrincipal OidcUser oidcUser) {
        System.out.println("oidcUser = " + oidcUser);
        return oidcUser;
    }
}
