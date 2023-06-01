package me.joohyuk.springsecurityoauth2;

import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.Customizer;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityCustomizer;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@RequiredArgsConstructor
public class OAuth2ClientConfig {
//
//    private final CustomOAuth2UserService customOAuth2UserService;
//
//    private final CustomOidcUserService customOidcUserService;

    @Bean
    public WebSecurityCustomizer webSecurityCustomizer() {
        return (web) -> web.ignoring().requestMatchers
            ("/static/js/**", "/static/images/**", "/static/css/**", "/static/scss/**");
    }

    @Bean
    public SecurityFilterChain oauth2SecurityFilterChain(HttpSecurity http) throws Exception {
        http.authorizeHttpRequests(authRequest -> authRequest
            .requestMatchers("/").permitAll()
            .anyRequest().authenticated());

        http
            .oauth2Login(Customizer.withDefaults());

        http
            .logout().logoutSuccessUrl("/");
//        http.authorizeHttpRequests((requests) -> requests
//            .requestMatchers("/api/user")
//            .hasAnyRole("SCOPE_profile", "SCOPE_email")
//            .requestMatchers("/api/oidc")
//            .hasRole("SCOPE_openid")
//            .requestMatchers("/")
//            .permitAll()
//            .anyRequest().authenticated());
//
//        http
//            .oauth2Login(oauth2 -> oauth2
//                .userInfoEndpoint(userInfoEndpointConfig ->
//                    userInfoEndpointConfig.userService(customOAuth2UserService)
//                        .oidcUserService(customOidcUserService)
//                ));

        http.logout().logoutSuccessUrl("/");

        return http.build();
    }
//
//    @Bean
//    public GrantedAuthoritiesMapper customAuthorityMapper() {
//        return new CustomAuthorityMapper();
//    }
}
