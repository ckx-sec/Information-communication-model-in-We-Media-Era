package edu.neu.social;

import edu.neu.social.dao.UserMapper;
import edu.neu.social.entity.po.User;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
@Slf4j
public class Runner implements ApplicationRunner {
    @Autowired
    UserMapper userMapper;

    public void run(ApplicationArguments args) throws Exception {
        log.info("test plus");
        List<User> userList = userMapper.selectList(null);
        userList.forEach(user -> {
            System.out.println(user.getUId());
        });
    }
}
