package me.joohyuk.springsecurityoauth2;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.Customizer;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityCustomizer;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
public class OAuth2ClientConfig {
//
//    @Bean
//    public ClientRegistrationRepository clientRegistrationRepository() {
//        return new InMemoryClientRegistrationRepository(keycloakClientRegistration());
//    }
//
//    private ClientRegistration keycloakClientRegistration() {
//        return ClientRegistrations.fromIssuerLocation("http://localhost:8080/realms/oauth2")
//            .registrationId("keycloak")
//            .clientId("oauth2-client-app")
//            .clientSecret("lygPKsTF849lHc0PA0uV3HVdGmneGaMU")
//            .redirectUri("http://localhost:8081/login/oauth2/code/keycloak")
//            .build();
//    }
//
//    @Bean
//    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
//        http.authorizeHttpRequests(authRequest -> authRequest
////            .requestMatchers("/loginPage").permitAll()
//            .anyRequest().permitAll());
////        http.oauth2Login(oauth2 -> oauth2.loginPage("/loginPage"));
//        http.oauth2Login(Customizer.withDefaults());
//
//        return http.build();
//    }


    @Bean
    public WebSecurityCustomizer webSecurityCustomizer() {
        return (web) -> web.ignoring().requestMatchers("/static/js/**", "/static/images/**", "/static/css/**", "/static/scss/**");
    }

    @Bean
    public SecurityFilterChain oauth2SecurityFilterChain(HttpSecurity http) throws Exception {
        http.authorizeHttpRequests((requests) -> requests
            .requestMatchers("/")
            .permitAll()
            .anyRequest().authenticated());

        http
            .oauth2Login(Customizer.withDefaults());

        http.logout().logoutSuccessUrl("/");

        return http.build();
    }
}
