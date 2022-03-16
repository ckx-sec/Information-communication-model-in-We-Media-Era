package edu.neu.social.controller;


import com.alibaba.fastjson.JSONObject;
import edu.neu.social.entity.po.User;
import edu.neu.social.service.UserService;
import edu.neu.social.utils.Utils;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.Arrays;
import java.util.List;

/**
 * <p>
 * 用户 前端控制器
 * </p>
 *
 * @author halozhy
 * @since 2021-07-15
 */
@Slf4j
@RestController
@RequestMapping("/api/user")
public class UserController {

    @Autowired
    UserService userService;

    /**
     * 添加用户 或 注册
     *
     * @param CONTENT
     * @return 0 成功 -1 username重复 -2 存在空字段
     */
    @PostMapping("/add")
    public int add(@RequestBody String CONTENT) {
        JSONObject jsonObject = JSONObject.parseObject(CONTENT);
        List<String> notEmptyNameList = Arrays.asList("username", "password", "name", "contact", "type");
        if (!Utils.checkEmpty(jsonObject, notEmptyNameList)) {
            return -2; // 存在空字段
        } else {
            User user = new User();
            user.setUUsername(jsonObject.getString("username"));
            user.setUPassword(jsonObject.getString("password"));
            user.setUName(jsonObject.getString("name"));
            user.setUContact(jsonObject.getString("contact"));
            return userService.addUser(user);
        }
    }

    /**
     * 登录
     *
     * @param CONTENT
     * @return 0 成功 -1 用户名或密码错误 -2 存在空字段
     */
    @PostMapping("/login")
    public JSONObject login(@RequestBody String CONTENT) {
        JSONObject jsonObject = JSONObject.parseObject(CONTENT);
        JSONObject result = new JSONObject();
        if (Utils.checkEmpty(jsonObject, Arrays.asList("username", "password"))) {

            User user = userService.login(jsonObject.getString("username"), jsonObject.getString("password"));
            if (user == null) {
                result.put("data", -1);
                return result;
            }
            result.put("data", 0);
            result.put("userId", user.getUId());
            result.put("username", user.getUUsername());
            return result;
        }
        result.put("data", -2);
        return result;
    }

    /**
     * 多字段 分页 查询用户
     * @param CONTENT
     * @return
     */
    @PostMapping("/list")
    public JSONObject list(@RequestBody String CONTENT) {
//        log.info(CONTENT);
        JSONObject j = JSONObject.parseObject(CONTENT);

//        JSONObject result = new JSONObject();
        return userService.listUser(
                j.getInteger("page"),
                j.getInteger("limit"),
                j.getString("id"),
                j.getString("username"),
                j.getString("name"));
//        return result;
    }

    @GetMapping("/count")
    public int count() {
        return userService.count();
    }

    /**
     * 删除用户
     *
     * @param uId
     * @return 0 ok -1 此用户下仍有未完成的订单 -2 无此用户
     */
    @GetMapping("/delete")
    public int delete(int uId) {
        return userService.deleteById(uId);
    }

    /**
     * 更新
     * 只能更改密码，联系方式，真实姓名
     * 对于云工厂管理员，可以更改工厂的相关信息
     * @param CONTENT
     * @return 0 ok -2 存在空字段 -1 无此用户
     */
    @PostMapping("/update")
    public int update(@RequestBody String CONTENT) {
        JSONObject jsonObject = JSONObject.parseObject(CONTENT);
        List<String> notEmptyNameList = Arrays.asList("id", "username", "password", "name", "contact");
        if (!Utils.checkEmpty(jsonObject, notEmptyNameList)) {
            return -2; // 存在空字段
        } else {
            User u = userService.getById(jsonObject.getInteger("id"));
            if (u == null) {
                return -1;
            }
            u.setUPassword(jsonObject.getString("password"));
            u.setUContact(jsonObject.getString("contact"));
            u.setUName(jsonObject.getString("name"));
            userService.updateById(u);
            return 0;
        }
    }
}

