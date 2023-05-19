package me.joohyuk.springsecurityoauth2client.config;

import jakarta.annotation.PostConstruct;
import lombok.RequiredArgsConstructor;
import me.joohyuk.springsecurityoauth2client.filter.CustomOAuth2AuthenticationFilter;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.Customizer;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.oauth2.client.registration.ClientRegistrationRepository;
import org.springframework.security.oauth2.client.web.DefaultOAuth2AuthorizedClientManager;
import org.springframework.security.oauth2.client.web.OAuth2AuthorizedClientRepository;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

@RequiredArgsConstructor
@Configuration
@EnableWebSecurity
public class OAuth2ClientConfig {


    private final ClientRegistrationRepository clientRegistrationRepository;

    private final OAuth2AuthorizedClientRepository oAuth2AuthorizedClientRepository;

    private DefaultOAuth2AuthorizedClientManager auth2AuthorizedClientManager;

    @PostConstruct
    public void init() {
        auth2AuthorizedClientManager = new DefaultOAuth2AuthorizedClientManager(clientRegistrationRepository, oAuth2AuthorizedClientRepository);
    }

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(
                authRequest -> authRequest.requestMatchers("/", "/oauth2Login", "/client").permitAll()
                    .anyRequest().authenticated());

        http
            .oauth2Client(Customizer.withDefaults());

        http
            .addFilterBefore(customOAuth2AuthenticationFilter(), UsernamePasswordAuthenticationFilter.class);

        return http.build();
    }

    private CustomOAuth2AuthenticationFilter customOAuth2AuthenticationFilter() {
        CustomOAuth2AuthenticationFilter auth2AuthenticationFilter = new CustomOAuth2AuthenticationFilter(auth2AuthorizedClientManager, oAuth2AuthorizedClientRepository);
        auth2AuthenticationFilter.setAuthenticationSuccessHandler((request, response, authentication) -> response.sendRedirect("/home"));
        return auth2AuthenticationFilter;
    }
}
