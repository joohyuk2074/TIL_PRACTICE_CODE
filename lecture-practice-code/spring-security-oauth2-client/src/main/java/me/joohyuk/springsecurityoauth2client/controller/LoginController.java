package me.joohyuk.springsecurityoauth2client.controller;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.RequiredArgsConstructor;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.oauth2.client.OAuth2AuthorizeRequest;
import org.springframework.security.oauth2.client.OAuth2AuthorizedClient;
import org.springframework.security.oauth2.client.web.DefaultOAuth2AuthorizedClientManager;
import org.springframework.security.oauth2.client.web.OAuth2AuthorizedClientRepository;
import org.springframework.security.web.authentication.logout.SecurityContextLogoutHandler;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@RequiredArgsConstructor
@Controller
public class LoginController {
//
//    private final DefaultOAuth2AuthorizedClientManager oAuth2AuthorizedClientManager;
//
//    private final OAuth2AuthorizedClientRepository oAuth2AuthorizedClientRepository;
//
//    @GetMapping("/oauth2Login")
//    public String oauth2Login(Model model, HttpServletRequest request, HttpServletResponse response) {
//
//        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
//
//        OAuth2AuthorizeRequest authorizeRequest = OAuth2AuthorizeRequest
//            .withClientRegistrationId("keycloak")
//            .principal(authentication)
//            .attribute(HttpServletRequest.class.getName(), request)
//            .attribute(HttpServletRequest.class.getName(), response)
//            .build();
//
//        OAuth2AuthorizedClient authorizedClient = oAuth2AuthorizedClientManager.authorize(authorizeRequest);
//
//        if (authorizedClient != null) {
//
//        }
//
//        return "redirect:/";
//    }
//
//    @GetMapping("/logout")
//    public String logout(Authentication authentication, HttpServletRequest request, HttpServletResponse response) {
//        SecurityContextLogoutHandler logoutHandler = new SecurityContextLogoutHandler();
//        logoutHandler.logout(request, response, authentication);
//
//        return "redirect:/";
//    }
}
