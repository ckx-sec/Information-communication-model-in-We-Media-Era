package edu.neu.social.controller;


import com.alibaba.fastjson.JSONObject;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import edu.neu.social.dao.NewsContentMapper;
import edu.neu.social.dao.NewsSortMapper;
import edu.neu.social.entity.po.NewsContent;
import edu.neu.social.entity.po.NewsSort;
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
 * 新闻 前端控制器
 * </p>
 *
 * @author halozhy
 */
@Slf4j
@RestController
@RequestMapping("/api/news_content")
public class NewsContentController {

    @Autowired
    UserService userService;

    @Autowired
    NewsSortMapper newsSortMapper;

    @Autowired
    NewsContentMapper newsContentMapper;

    @PostMapping("/list")
    public List<NewsContent> list(@RequestBody String CONTENT){
        JSONObject jsonObject = JSONObject.parseObject(CONTENT);
        List<String> notEmptyNameList = Arrays.asList("sort_id");
        if (!Utils.checkEmpty(jsonObject, notEmptyNameList)) {
            return null; // 存在空字段
        } else {
            int sort_id = jsonObject.getInteger("sort_id");
            QueryWrapper<NewsContent> queryWrapper = new QueryWrapper<>();
            queryWrapper.eq("sort_id", sort_id);
            return newsContentMapper.selectList(queryWrapper);
        }
    }
}

