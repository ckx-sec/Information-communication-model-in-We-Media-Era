package edu.neu.social.service;

import com.alibaba.fastjson.JSONObject;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.service.IService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import edu.neu.social.dao.NewsSortMapper;
import edu.neu.social.dao.UserMapper;
import edu.neu.social.entity.po.NewsSort;
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
 * 新闻类别 服务实现类
 * </p>
 *
 * @author halozhy
 */
@Slf4j
@Service
public class NewsSortService extends ServiceImpl<NewsSortMapper, NewsSort> implements IService<NewsSort> {
    @Autowired
    NewsSortMapper newsSortMapper;

}


