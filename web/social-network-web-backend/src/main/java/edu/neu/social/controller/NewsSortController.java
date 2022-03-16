package edu.neu.social.controller;


import com.alibaba.fastjson.JSONObject;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import edu.neu.social.dao.NewsSortMapper;
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
 * 新闻类别 前端控制器
 * </p>
 *
 * @author halozhy
 */
@Slf4j
@RestController
@RequestMapping("/api/news_sort")
public class NewsSortController {

    @Autowired
    UserService userService;

    @Autowired
    NewsSortMapper newsSortMapper;


    /**
     * 多字段 分页 查询新闻分类
     * @param
     * @return
     */
    @PostMapping("/list")
    public List<NewsSort> list() {
        QueryWrapper<NewsSort> queryWrapper = new QueryWrapper<>();
        return newsSortMapper.selectList(queryWrapper);
    }

}

