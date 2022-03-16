package edu.neu.social.service;

import com.alibaba.fastjson.JSONObject;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.service.IService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import edu.neu.social.dao.UserMapper;
import edu.neu.social.entity.po.User;
import edu.neu.social.entity.vo.UserVo;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * <p>
 * 用户 服务实现类
 * </p>
 *
 * @author halozhy
 */
@Slf4j
@Service
public class UserService extends ServiceImpl<UserMapper, User> implements IService<User> {
    @Autowired
    UserMapper userMapper;

    public int addUser(User user) {
        if (userMapper.selectByName(user.getUUsername()) == null) {
            userMapper.insert(user);
            return 0;
        } else {
            return -1; // username 重复
        }
    }

    public User login(String username, String password) {
        Map<String, Object> colMap = new HashMap<>();
        colMap.put("u_username", username);
        colMap.put("u_password", password);
        List<User> userList = userMapper.selectByMap(colMap);
        if (userList.size() != 1) {
            return null;
        } else {
            return userList.get(0);
        }
    }

    public int deleteById(int uId) {
        User u = userMapper.selectById(uId);
        if (u == null) {
            return -2; // 无此用户
        } else {
            userMapper.deleteById(uId);
            return 0;
        }

    }


    public JSONObject listUser(int page, int limit, String id, String username, String name) {
        // 分页查询，多字段查询
//        log.info("{}, {}, {}",id, username, name);
        QueryWrapper<User> queryWrapper = new QueryWrapper<>();
        if (id != null && !id.isEmpty()) {
            queryWrapper.like("u_id", id);
        }
        if (username != null && !username.isEmpty()) {
            queryWrapper.like("u_username", username);
        }
        if (name != null && !name.isEmpty()) {
            queryWrapper.like("u_name", name);
        }

        List<User> userList = userMapper.listPage((page - 1) * limit, limit, queryWrapper);
        List<UserVo> userVoList = new ArrayList<>();
        userList.forEach(user -> {
            UserVo userVo = new UserVo();
            userVo.setId(user.getUId());
            userVo.setUsername(user.getUUsername());
            userVo.setPassword(user.getUPassword());
            userVo.setName(user.getUName());
            userVo.setContact(user.getUContact());
            userVoList.add(userVo);
        });
        JSONObject result = new JSONObject();
        result.put("data", userVoList);
        result.put("count", userMapper.selectCount(queryWrapper));
        return result;
    }
}


