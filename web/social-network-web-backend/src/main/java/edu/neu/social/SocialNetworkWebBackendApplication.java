package edu.neu.social;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.servlet.ServletComponentScan;

@SpringBootApplication
@MapperScan("edu.neu.social.dao")
@ServletComponentScan
public class SocialNetworkWebBackendApplication {

	public static void main(String[] args) {
		SpringApplication.run(SocialNetworkWebBackendApplication.class, args);
	}

}
