package me.joohyuk.springsecurityoauth2client.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.security.oauth2.client.OAuth2AuthorizedClient;
import org.springframework.security.oauth2.client.OAuth2AuthorizedClientService;
import org.springframework.security.oauth2.client.authentication.OAuth2AuthenticationToken;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@RequiredArgsConstructor
@Controller
public class HomeController {

    private final OAuth2AuthorizedClientService oAuth2AuthorizedClientService;

    @GetMapping("/home")
    public String home(Model model, OAuth2AuthenticationToken oAuth2AuthenticationToken) {

        OAuth2AuthorizedClient authorizedClient = oAuth2AuthorizedClientService.loadAuthorizedClient("keycloak", oAuth2AuthenticationToken.getName());
        model.addAttribute("oAuth2AuthenticationToken", oAuth2AuthenticationToken);
        model.addAttribute("AccessToken", authorizedClient.getAccessToken().getTokenValue());
        model.addAttribute("RefreshToken", authorizedClient.getRefreshToken().getTokenValue());

        return "home";
    }
}
