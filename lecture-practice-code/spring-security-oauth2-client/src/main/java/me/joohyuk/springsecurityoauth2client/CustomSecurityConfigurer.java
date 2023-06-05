//package me.joohyuk.springsecurityoauth2client;
//
//import lombok.extern.slf4j.Slf4j;
//import org.springframework.security.config.annotation.web.builders.HttpSecurity;
//import org.springframework.security.config.annotation.web.configurers.AbstractHttpConfigurer;
//
//@Slf4j
//public class CustomSecurityConfigurer extends AbstractHttpConfigurer<CustomSecurityConfigurer, HttpSecurity> {
//
//    private boolean isSecure;
//
//    @Override
//    public void init(HttpSecurity builder) throws Exception {
//        super.init(builder);
//        log.info("init method started..");
//    }
//
//    @Override
//    public void configure(HttpSecurity builder) throws Exception {
//        super.configure(builder);
//        log.info("configure method started..");
//        if (isSecure) {
//            log.info("https is required");
//        } else {
//            log.info("http is optional");
//        }
//    }
//
//    public CustomSecurityConfigurer setFlag(boolean isSecure) {
//        this.isSecure = isSecure;
//        return this;
//    }
//}
